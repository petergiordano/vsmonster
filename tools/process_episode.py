#!/usr/bin/env python3
r"""
Chronicles of Khronexia Episode Post-Processor

Standalone pipeline component to fix multimedia tag escaping in episode markdown files.
Transforms [TAG:] format to \[TAG:\] format for parser compatibility.

Usage:
    python process_episode.py episode_file.md
    python process_episode.py episode_file.md --dry-run
    python process_episode.py episode_file.md --verify
    python process_episode.py episode_file.md --silent --json

Author: versusMonster Pipeline System
Version: 1.0
"""

import re
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ProcessingStats:
    """Statistics for tag processing results"""
    img_fixed: int = 0
    img_already_escaped: int = 0
    sfx_fixed: int = 0
    sfx_already_escaped: int = 0
    music_fixed: int = 0
    music_already_escaped: int = 0
    ambient_fixed: int = 0
    ambient_already_escaped: int = 0
    transition_fixed: int = 0
    transition_already_escaped: int = 0
    thumbnail_fixed: int = 0
    thumbnail_already_escaped: int = 0
    scene_fixed: int = 0
    scene_already_escaped: int = 0
    
    @property
    def total_fixed(self) -> int:
        return (self.img_fixed + self.sfx_fixed + self.music_fixed + 
                self.ambient_fixed + self.transition_fixed + self.thumbnail_fixed + self.scene_fixed)
    
    @property
    def total_already_escaped(self) -> int:
        return (self.img_already_escaped + self.sfx_already_escaped + 
                self.music_already_escaped + self.ambient_already_escaped + 
                self.transition_already_escaped + self.thumbnail_already_escaped + self.scene_already_escaped)


class EpisodeTagProcessor:
    """Main processor for fixing multimedia tags in episode files"""
    
    # Tags that need escaping (including SCENE headers for parser compatibility)
    MULTIMEDIA_TAGS = ['IMG', 'SFX', 'MUSIC', 'AMBIENT', 'TRANSITION', 'THUMBNAIL', 'SCENE']
    
    def __init__(self, verbose: bool = True, json_output: bool = False):
        self.verbose = verbose
        self.json_output = json_output
        self.stats = ProcessingStats()
        self.sample_fixes: List[Tuple[str, str]] = []
        
        # Compile regex patterns for each tag type
        self._compile_patterns()
    
    def _compile_patterns(self):
        """Compile regex patterns for detecting multimedia tags"""
        self.patterns = {}
        
        # Pattern for IMG tags with optional PROMPT continuation
        # Matches: [IMG: id] PROMPT: "description" or just [IMG: id]
        self.patterns['IMG'] = re.compile(
            r'(?<!\\)\[IMG:\s*([^\]]+)\](\s*PROMPT:\s*"[^"]*")?',
            re.MULTILINE | re.DOTALL
        )
        
        # Pattern for other multimedia tags
        for tag in ['SFX', 'MUSIC', 'AMBIENT', 'TRANSITION']:
            self.patterns[tag] = re.compile(
                rf'(?<!\\)\[{tag}:\s*([^\]]+)\]',
                re.MULTILINE
            )
        
        # Special pattern for SCENE tags (need to escape both brackets for parser)
        self.patterns['SCENE'] = re.compile(
            r'(?<!\\)\[SCENE:\s*([^\]]+)\]',
            re.MULTILINE
        )
        
        # Special pattern for THUMBNAIL (no colon content)
        self.patterns['THUMBNAIL'] = re.compile(
            r'(?<!\\)\[THUMBNAIL\]',
            re.MULTILINE
        )
        
        
        # Pattern to detect already escaped tags
        self.escaped_pattern = re.compile(
            r'\\?\[(?:IMG|SFX|MUSIC|AMBIENT|TRANSITION|THUMBNAIL|SCENE)(?::\s*[^\]]+)?\]',
            re.MULTILINE
        )
    
    def _is_in_code_block(self, text: str, position: int) -> bool:
        """Check if position is within a markdown code block"""
        # Find all code block boundaries before this position
        text_before = text[:position]
        
        # Count triple backticks
        triple_backticks = text_before.count('```')
        
        # If odd number, we're inside a code block
        return triple_backticks % 2 == 1
    
    def _count_already_escaped(self, content: str, tag_type: str) -> int:
        """Count already escaped tags of a specific type"""
        if tag_type == 'THUMBNAIL':
            pattern = r'\\?\[THUMBNAIL\]'
        else:
            pattern = rf'\\?\[{tag_type}:\s*[^\]]+\]'
        
        # Find all matches
        matches = re.findall(pattern, content, re.MULTILINE)
        
        # Count those that start with backslash
        escaped_count = sum(1 for match in matches if match.startswith('\\'))
        return escaped_count
    
    def _process_tag_type(self, content: str, tag_type: str) -> Tuple[str, int, int]:
        """Process a specific tag type and return updated content with stats"""
        pattern = self.patterns[tag_type]
        fixed_count = 0
        
        # Count already escaped tags before processing
        already_escaped_count = self._count_already_escaped(content, tag_type)
        
        def replace_match(match):
            nonlocal fixed_count
            
            # Check if we're in a code block
            if self._is_in_code_block(content, match.start()):
                return match.group(0)  # Don't modify
            
            original = match.group(0)
            
            # Add escaping (regex already excludes escaped ones)
            if tag_type == 'SCENE':
                # SCENE tags need both brackets escaped for parser compatibility
                escaped = original.replace('[SCENE:', '\\[SCENE:').replace(']', '\\]')
            else:
                escaped = '\\' + original
            fixed_count += 1
            
            # Store sample for reporting
            if len(self.sample_fixes) < 5:  # Limit samples
                self.sample_fixes.append((original, escaped))
            
            return escaped
        
        processed_content = pattern.sub(replace_match, content)
        return processed_content, fixed_count, already_escaped_count
    
    def process_file_content(self, content: str) -> Tuple[str, ProcessingStats]:
        """Process file content and return modified content with statistics"""
        self.stats = ProcessingStats()
        self.sample_fixes = []
        
        processed_content = content
        
        # Process each tag type
        for tag_type in self.MULTIMEDIA_TAGS:
            processed_content, fixed, already_escaped = self._process_tag_type(
                processed_content, tag_type
            )
            
            # Update statistics
            setattr(self.stats, f'{tag_type.lower()}_fixed', fixed)
            setattr(self.stats, f'{tag_type.lower()}_already_escaped', already_escaped)
        
        return processed_content, self.stats
    
    def process_episode_file(self, input_path: Path, output_path: Optional[Path] = None, 
                           dry_run: bool = False) -> Dict:
        """Process an episode file and return results"""
        
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        # Determine output path
        if output_path is None:
            output_path = input_path.parent / f"{input_path.stem}_processed{input_path.suffix}"
        
        # Read input file
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except Exception as e:
            raise IOError(f"Error reading input file: {e}")
        
        # Process content
        processed_content, stats = self.process_file_content(original_content)
        
        # Results dictionary
        results = {
            'input_file': str(input_path),
            'output_file': str(output_path),
            'dry_run': dry_run,
            'stats': {
                'img_fixed': stats.img_fixed,
                'img_already_escaped': stats.img_already_escaped,
                'sfx_fixed': stats.sfx_fixed,
                'sfx_already_escaped': stats.sfx_already_escaped,
                'music_fixed': stats.music_fixed,
                'music_already_escaped': stats.music_already_escaped,
                'ambient_fixed': stats.ambient_fixed,
                'ambient_already_escaped': stats.ambient_already_escaped,
                'transition_fixed': stats.transition_fixed,
                'transition_already_escaped': stats.transition_already_escaped,
                'thumbnail_fixed': stats.thumbnail_fixed,
                'thumbnail_already_escaped': stats.thumbnail_already_escaped,
                'scene_fixed': stats.scene_fixed,
                'scene_already_escaped': stats.scene_already_escaped,
                'total_fixed': stats.total_fixed,
                'total_already_escaped': stats.total_already_escaped
            },
            'sample_fixes': self.sample_fixes,
            'needs_processing': stats.total_fixed > 0,
            'success': True
        }
        
        # Write output file if not dry run
        if not dry_run and stats.total_fixed > 0:
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
                
                if self.verbose:
                    print(f"✓ Processed file saved: {output_path}")
            except Exception as e:
                results['success'] = False
                results['error'] = f"Error writing output file: {e}"
                return results
        
        return results
    
    def print_report(self, results: Dict):
        """Print human-readable processing report"""
        if self.json_output:
            print(json.dumps(results, indent=2))
            return
        
        print(f"\nProcessing: {results['input_file']}")
        
        if results['dry_run']:
            print("🔍 DRY RUN MODE - No files modified")
        else:
            print(f"Output: {results['output_file']}")
        
        stats = results['stats']
        
        if not results['needs_processing']:
            print("\n✅ No tags need processing - file is already properly formatted!")
            if stats['total_already_escaped'] > 0:
                print(f"   Found {stats['total_already_escaped']} already-escaped tags")
            return
        
        print("\n📊 Tags Fixed:")
        
        tag_types = [
            ('IMG', stats['img_fixed'], stats['img_already_escaped']),
            ('SFX', stats['sfx_fixed'], stats['sfx_already_escaped']),
            ('MUSIC', stats['music_fixed'], stats['music_already_escaped']),
            ('AMBIENT', stats['ambient_fixed'], stats['ambient_already_escaped']),
            ('TRANSITION', stats['transition_fixed'], stats['transition_already_escaped']),
            ('THUMBNAIL', stats['thumbnail_fixed'], stats['thumbnail_already_escaped']),
            ('SCENE', stats['scene_fixed'], stats['scene_already_escaped'])
        ]
        
        for tag_name, fixed, already_escaped in tag_types:
            if fixed > 0 or already_escaped > 0:
                print(f"- {tag_name} tags: {fixed} fixed ({already_escaped} already escaped)")
        
        print(f"\n📈 Total: {stats['total_fixed']} tags fixed")
        
        # Show sample fixes
        if results['sample_fixes']:
            print("\n🔧 Sample fixes:")
            for original, fixed in results['sample_fixes'][:3]:  # Show first 3
                # Truncate long samples
                orig_display = original[:50] + "..." if len(original) > 50 else original
                fixed_display = fixed[:50] + "..." if len(fixed) > 50 else fixed
                print(f"   {orig_display} → {fixed_display}")
        
        if results['success']:
            print("\n✅ Processing complete!")
        else:
            print(f"\n❌ Processing failed: {results.get('error', 'Unknown error')}")


def create_test_content() -> str:
    """Create test content for validation"""
    return r"""# Test Episode

## **[SCENE: COLD OPEN]**

[SFX: battle_start]

[IMG: test_image] PROMPT: "Test description"

Already escaped: \[SFX: already_escaped\]

## **[SCENE: BATTLE SETUP]**

[MUSIC: theme_music]
[AMBIENT: forest_sounds]
[TRANSITION: magical_whoosh]

```markdown
[SFX: code_block_should_not_change]
```

[THUMBNAIL]
"""


def run_tests() -> bool:
    """Run built-in tests to verify processor functionality"""
    print("🧪 Running built-in tests...")
    
    processor = EpisodeTagProcessor(verbose=False)
    test_content = create_test_content()
    
    processed_content, stats = processor.process_file_content(test_content)
    
    # Test assertions
    tests_passed = 0
    total_tests = 0
    
    # Test 1: SFX tags fixed
    total_tests += 1
    if stats.sfx_fixed == 1 and stats.sfx_already_escaped == 1:
        tests_passed += 1
        print("✓ SFX tag processing")
    else:
        print(f"✗ SFX tag processing (fixed: {stats.sfx_fixed}, escaped: {stats.sfx_already_escaped})")
    
    # Test 2: IMG tags fixed
    total_tests += 1
    if stats.img_fixed == 1:
        tests_passed += 1
        print("✓ IMG tag processing")
    else:
        print(f"✗ IMG tag processing (fixed: {stats.img_fixed})")
    
    # Test 3: Other tags fixed
    total_tests += 1
    expected_total = 8  # SFX(1) + IMG(1) + MUSIC(1) + AMBIENT(1) + TRANSITION(1) + THUMBNAIL(1) + SCENE(2)
    if stats.total_fixed == expected_total:
        tests_passed += 1
        print("✓ All multimedia tags processed")
    else:
        print(f"✗ Total tags processed (got: {stats.total_fixed}, expected: {expected_total})")
        print(f"   SFX: {stats.sfx_fixed}, IMG: {stats.img_fixed}, MUSIC: {stats.music_fixed}")
        print(f"   AMBIENT: {stats.ambient_fixed}, TRANSITION: {stats.transition_fixed}, THUMBNAIL: {stats.thumbnail_fixed}, SCENE: {stats.scene_fixed}")
    
    # Test 4: SCENE tags escaped
    total_tests += 1
    if '**\\[SCENE: COLD OPEN\\]**' in processed_content and '**\\[SCENE: BATTLE SETUP\\]**' in processed_content:
        tests_passed += 1
        print("✓ SCENE tags escaped")
    else:
        print("✗ SCENE tags not properly escaped")
        escaped_count = processed_content.count('\\[SCENE:')
        unescaped_count = processed_content.count('[SCENE:')
        print(f"   Content contains: {unescaped_count} unescaped, {escaped_count} escaped")
        # Print lines with SCENE to debug
        lines_with_scene = [line for line in processed_content.split('\n') if 'SCENE:' in line]
        print(f"   Lines with SCENE: {lines_with_scene}")
    
    # Test 5: Code blocks preserved
    total_tests += 1
    if '[SFX: code_block_should_not_change]' in processed_content:
        tests_passed += 1
        print("✓ Code blocks preserved")
    else:
        print("✗ Code blocks not preserved")
    
    success = tests_passed == total_tests
    print(f"\n📊 Tests: {tests_passed}/{total_tests} passed")
    
    if success:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed!")
    
    return success


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Process Chronicles of Khronexia episode files to fix multimedia tag escaping",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python process_episode.py episode_007.md
  python process_episode.py episode_007.md --dry-run
  python process_episode.py episode_007.md --output fixed_episode.md
  python process_episode.py episode_007.md --verify
  python process_episode.py --test
        """
    )
    
    parser.add_argument('input_file', nargs='?', help='Input episode markdown file')
    parser.add_argument('--output', '-o', help='Output file path (default: input_processed.md)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing files')
    parser.add_argument('--verify', action='store_true', help='Check if file needs processing')
    parser.add_argument('--silent', action='store_true', help='Minimal output for automation')
    parser.add_argument('--json', action='store_true', help='Output results as JSON')
    parser.add_argument('--test', action='store_true', help='Run built-in tests')
    
    args = parser.parse_args()
    
    # Handle test mode
    if args.test:
        success = run_tests()
        sys.exit(0 if success else 1)
    
    # Validate arguments
    if not args.input_file:
        parser.print_help()
        sys.exit(1)
    
    input_path = Path(args.input_file)
    output_path = Path(args.output) if args.output else None
    
    # Create processor
    processor = EpisodeTagProcessor(
        verbose=not args.silent,
        json_output=args.json
    )
    
    try:
        # Process file
        results = processor.process_episode_file(
            input_path=input_path,
            output_path=output_path,
            dry_run=args.dry_run or args.verify
        )
        
        # Print report
        if not args.silent:
            processor.print_report(results)
        elif args.json:
            print(json.dumps(results))
        
        # Exit codes for automation
        if args.verify:
            # Exit code 0 if needs processing, 1 if already processed
            sys.exit(0 if results['needs_processing'] else 1)
        
        sys.exit(0 if results['success'] else 1)
        
    except Exception as e:
        if args.json:
            print(json.dumps({'success': False, 'error': str(e)}))
        else:
            print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
