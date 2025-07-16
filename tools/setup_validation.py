#!/usr/bin/env python3
"""
versusMonster Environment Validation Script

This script validates that the development environment is properly configured
for the versusMonster Automated Video Podcast System (AVPS).

Usage:
    python setup_validation.py
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Try to import required packages
REQUIRED_PACKAGES = [
    'elevenlabs',
    'pydub', 
    'ffmpeg',
    'moviepy',
    'requests',
    'dotenv',
    'cv2',
    'PIL',
    'imageio'
]

class ValidationResult:
    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0
        self.warnings = []
        self.errors = []
        self.info = []

    def add_pass(self, message: str):
        self.tests_passed += 1
        self.info.append(f"✅ {message}")
        print(f"✅ {message}")

    def add_fail(self, message: str):
        self.tests_failed += 1
        self.errors.append(f"❌ {message}")
        print(f"❌ {message}")

    def add_warning(self, message: str):
        self.warnings.append(f"⚠️ {message}")
        print(f"⚠️ {message}")

    def add_info(self, message: str):
        self.info.append(f"ℹ️ {message}")
        print(f"ℹ️ {message}")

def check_python_version(result: ValidationResult) -> bool:
    """Check if Python version is 3.9 or higher."""
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    if version.major == 3 and version.minor >= 9:
        result.add_pass(f"Python {version_str} meets requirements (≥3.9)")
        return True
    else:
        result.add_fail(f"Python {version_str} is too old (need ≥3.9)")
        return False

def check_ffmpeg_installation(result: ValidationResult) -> bool:
    """Check FFmpeg installation and capabilities."""
    try:
        # Check FFmpeg version
        ffmpeg_result = subprocess.run(
            ['ffmpeg', '-version'], 
            capture_output=True, 
            text=True, 
            timeout=10
        )
        
        if ffmpeg_result.returncode != 0:
            result.add_fail("FFmpeg not found or not working")
            return False
            
        # Parse version
        version_line = ffmpeg_result.stdout.split('\n')[0]
        result.add_pass(f"FFmpeg found: {version_line}")
        
        # Check for VideoToolbox support (macOS hardware acceleration)
        encoders_result = subprocess.run(
            ['ffmpeg', '-encoders'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if 'h264_videotoolbox' in encoders_result.stdout:
            result.add_pass("VideoToolbox hardware acceleration available")
        else:
            result.add_warning("VideoToolbox not available - using software encoding")
            
        return True
        
    except subprocess.TimeoutExpired:
        result.add_fail("FFmpeg command timed out")
        return False
    except FileNotFoundError:
        result.add_fail("FFmpeg not found in PATH")
        result.add_info("Install with: brew install ffmpeg")
        return False
    except Exception as e:
        result.add_fail(f"FFmpeg check failed: {e}")
        return False

def test_ffmpeg_basic_operation(result: ValidationResult) -> bool:
    """Test basic FFmpeg video/audio operations."""
    try:
        # Create a simple test video
        test_output = Path("test_output.mp4")
        
        # Clean up any existing test file
        if test_output.exists():
            test_output.unlink()
            
        # Generate 2-second test video
        cmd = [
            'ffmpeg',
            '-f', 'lavfi',
            '-i', 'testsrc=duration=2:size=320x240:rate=30',
            '-f', 'lavfi', 
            '-i', 'sine=frequency=1000:duration=2',
            '-c:v', 'h264',
            '-c:a', 'aac',
            '-y',  # Overwrite output
            str(test_output)
        ]
        
        test_result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if test_result.returncode == 0 and test_output.exists():
            result.add_pass("FFmpeg basic video/audio generation works")
            # Clean up
            test_output.unlink()
            return True
        else:
            result.add_fail("FFmpeg basic operation failed")
            result.add_info(f"Error: {test_result.stderr[:200]}")
            return False
            
    except subprocess.TimeoutExpired:
        result.add_fail("FFmpeg test operation timed out")
        return False
    except Exception as e:
        result.add_fail(f"FFmpeg test failed: {e}")
        return False

def check_required_packages(result: ValidationResult) -> bool:
    """Check if all required Python packages are installed."""
    all_packages_ok = True
    
    for package in REQUIRED_PACKAGES:
        try:
            if package == 'ffmpeg':
                import ffmpeg
            elif package == 'dotenv':
                from dotenv import load_dotenv
            elif package == 'cv2':
                import cv2
            elif package == 'PIL':
                from PIL import Image
            else:
                __import__(package)
            result.add_pass(f"Package {package} is installed")
        except ImportError:
            result.add_fail(f"Package {package} is missing")
            all_packages_ok = False
    
    return all_packages_ok

def check_project_structure(result: ValidationResult) -> bool:
    """Check if required project directories exist."""
    required_dirs = [
        'output',
        'output/json',
        'output/voices', 
        'output/audio',
        'output/videos',
        'assets',
        'assets/images',
        'assets/sfx',
        'assets/music',
        'reference',
        'src'
    ]
    
    all_dirs_ok = True
    project_root = Path.cwd()
    
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if full_path.exists():
            result.add_pass(f"Directory {dir_path}/ exists")
        else:
            result.add_fail(f"Directory {dir_path}/ missing")
            result.add_info(f"Create with: mkdir -p {dir_path}")
            all_dirs_ok = False
    
    return all_dirs_ok

def check_env_file(result: ValidationResult) -> bool:
    """Check if .env file exists and has required keys."""
    env_path = Path('.env')
    
    if not env_path.exists():
        result.add_fail(".env file not found")
        result.add_info("Create .env file and add ELEVENLABS_API_KEY=your-key-here")
        return False
    
    result.add_pass(".env file exists")
    
    # Try to load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('ELEVENLABS_API_KEY')
        if api_key:
            # Check if it's not the placeholder value
            if api_key.startswith('your-') or api_key == 'your-key-here':
                result.add_warning("ELEVENLABS_API_KEY looks like placeholder value")
            else:
                result.add_pass("ELEVENLABS_API_KEY is configured")
        else:
            result.add_fail("ELEVENLABS_API_KEY not found in .env")
            return False
            
    except Exception as e:
        result.add_fail(f"Error loading .env file: {e}")
        return False
    
    return True

def test_elevenlabs_api(result: ValidationResult) -> bool:
    """Test basic ElevenLabs API connectivity (if API key is available)."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('ELEVENLABS_API_KEY')
        if not api_key or api_key.startswith('your-'):
            result.add_warning("Skipping ElevenLabs API test - no valid API key")
            return True
            
        # Try to import and initialize ElevenLabs client
        from elevenlabs import ElevenLabs
        
        client = ElevenLabs(api_key=api_key)
        
        # Test API connection by getting voices
        voices = client.voices.get_all()
        
        if voices.voices:
            result.add_pass(f"ElevenLabs API working - {len(voices.voices)} voices available")
            return True
        else:
            result.add_warning("ElevenLabs API connected but no voices found")
            return True
            
    except ImportError:
        result.add_fail("elevenlabs package not installed")
        return False
    except Exception as e:
        result.add_fail(f"ElevenLabs API test failed: {e}")
        return False

def check_episode_7_reference(result: ValidationResult) -> bool:
    """Check if Episode 7 reference file exists."""
    episode_path = Path('tests/reference/episode_2_ex_final.md')
    
    if episode_path.exists():
        # Check file size to ensure it's not empty
        size = episode_path.stat().st_size
        if size > 1000:  # Should be several KB for a full episode
            result.add_pass(f"Episode 7 reference file exists ({size} bytes)")
            return True
        else:
            result.add_warning(f"Episode 7 file exists but seems small ({size} bytes)")
            return True
    else:
        result.add_fail("Episode 7 reference file not found")
        result.add_info("Should be at: tests/reference/episode_2_ex_final.md")
        return False

def check_gitignore(result: ValidationResult) -> bool:
    """Check if .gitignore includes .env file."""
    gitignore_path = Path('.gitignore')
    
    if not gitignore_path.exists():
        result.add_warning(".gitignore not found")
        return False
        
    try:
        with open(gitignore_path, 'r') as f:
            content = f.read()
            
        if '.env' in content:
            result.add_pass(".env is in .gitignore")
            return True
        else:
            result.add_fail(".env is NOT in .gitignore - SECURITY RISK!")
            result.add_info("Add to .gitignore: echo '.env' >> .gitignore")
            return False
            
    except Exception as e:
        result.add_warning(f"Could not read .gitignore: {e}")
        return False

def generate_report(result: ValidationResult):
    """Generate and save validation report."""
    total_tests = result.tests_passed + result.tests_failed
    success_rate = (result.tests_passed / total_tests * 100) if total_tests > 0 else 0
    
    report = {
        'timestamp': subprocess.run(['date'], capture_output=True, text=True).stdout.strip(),
        'summary': {
            'total_tests': total_tests,
            'passed': result.tests_passed,
            'failed': result.tests_failed,
            'warnings': len(result.warnings),
            'success_rate': f"{success_rate:.1f}%"
        },
        'results': {
            'info': result.info,
            'warnings': result.warnings,
            'errors': result.errors
        }
    }
    
    # Save report
    with open('validation_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n{'='*50}")
    print("VALIDATION SUMMARY")
    print('='*50)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {result.tests_passed}")
    print(f"Failed: {result.tests_failed}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Success Rate: {success_rate:.1f}%")
    
    if result.tests_failed == 0:
        print("\n🎉 Environment setup is complete and ready for development!")
        print("Next step: Run '/start-coding' in Claude Code to begin development")
    else:
        print(f"\n⚠️ Environment setup has {result.tests_failed} issues that need attention")
        print("Please fix the failed tests before proceeding")
    
    print(f"\nDetailed report saved to: validation_report.json")

def main():
    """Main validation function."""
    print("versusMonster Environment Validation")
    print("="*40)
    
    result = ValidationResult()
    
    # Run all validation checks
    print("\n1. Checking Python version...")
    check_python_version(result)
    
    print("\n2. Checking FFmpeg installation...")
    check_ffmpeg_installation(result)
    
    print("\n3. Testing FFmpeg basic operations...")
    test_ffmpeg_basic_operation(result)
    
    print("\n4. Checking Python packages...")
    check_required_packages(result)
    
    print("\n5. Checking project structure...")
    check_project_structure(result)
    
    print("\n6. Checking environment configuration...")
    check_env_file(result)
    
    print("\n7. Checking .gitignore security...")
    check_gitignore(result)
    
    print("\n8. Testing ElevenLabs API...")
    test_elevenlabs_api(result)
    
    print("\n9. Checking Episode 7 reference...")
    check_episode_7_reference(result)
    
    # Generate final report
    generate_report(result)
    
    # Exit with appropriate code
    sys.exit(0 if result.tests_failed == 0 else 1)

if __name__ == "__main__":
    main()