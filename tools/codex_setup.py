#!/usr/bin/env python3
"""
Codex Environment Setup Script for versusMonster AVPS

This script prepares the Codex environment for implementing core pipeline components.
It ensures all dependencies, directories, configurations, and task templates are ready.

Based on OpenAI Codex documentation for task-based development with proper project
context loading and execution environment setup.

Usage:
    python tools/codex_setup.py

Environment Requirements:
    - Python 3.11+
    - Git
    - FFmpeg (for audio processing)
    - Valid ELEVENLABS_API_KEY in .env file
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Optional

class CodexSetup:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.errors = []
        self.warnings = []
        self.success_messages = []
        
    def run(self):
        """Main setup orchestration"""
        print("🚀 Codex Environment Setup for versusMonster AVPS")
        print("=" * 60)
        
        # Run all setup steps
        self.check_python_version()
        self.install_dependencies()
        self.create_directory_structure()
        self.validate_configuration_files()
        self.check_environment_variables()
        self.validate_reference_files()
        self.validate_ffmpeg_installation()
        self.setup_git_environment()
        
        # Report results
        self.print_summary()
        
        # Exit with appropriate code
        sys.exit(0 if not self.errors else 1)
    
    def check_python_version(self):
        """Ensure Python 3.11+ is being used"""
        version = sys.version_info
        if version.major == 3 and version.minor >= 11:
            self.success_messages.append(f"Python {version.major}.{version.minor}.{version.micro} ✓")
        else:
            self.errors.append(f"Python 3.11+ required, found {version.major}.{version.minor}")
    
    def install_dependencies(self):
        """Install all required Python packages"""
        print("\n📦 Installing dependencies...")
        requirements_path = self.project_root / "requirements.txt"
        
        if not requirements_path.exists():
            self.errors.append("requirements.txt not found")
            return
            
        try:
            # Upgrade pip first
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                         check=True, capture_output=True, text=True)
            
            # Install requirements
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "-r", str(requirements_path)],
                capture_output=True, text=True
            )
            
            if result.returncode == 0:
                self.success_messages.append("All Python dependencies installed ✓")
            else:
                self.errors.append(f"Failed to install dependencies: {result.stderr}")
        except Exception as e:
            self.errors.append(f"Error installing dependencies: {str(e)}")
    
    def create_directory_structure(self):
        """Create all required output directories"""
        print("\n📁 Creating directory structure...")
        
        directories = [
            "output/json",
            "output/voices",
            "output/audio", 
            "output/videos",
            "archive/codex_task_logs",
            "logs",
            ".taskmaster/docs",
            ".taskmaster/tasks"
        ]
        
        for dir_path in directories:
            full_path = self.project_root / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            
        self.success_messages.append(f"Created {len(directories)} directories ✓")
    
    def validate_configuration_files(self):
        """Check that all required config files exist"""
        print("\n⚙️  Validating configuration files...")
        
        config_files = {
            "config/config.json": "Central pipeline configuration",
            "config/notion-database-schema.json": "Notion database schema",
            ".gitignore": "Git ignore configuration",
            "pyproject.toml": "Python project configuration"
        }
        
        for file_path, description in config_files.items():
            full_path = self.project_root / file_path
            if full_path.exists():
                self.success_messages.append(f"{file_path} exists ✓")
            else:
                self.warnings.append(f"Missing {file_path} ({description})")
                
        # Validate config.json structure
        config_path = self.project_root / "config/config.json"
        if config_path.exists():
            try:
                with open(config_path) as f:
                    config = json.load(f)
                    
                # Check for required sections
                required_sections = ["voice_generation", "script_parser"]
                for section in required_sections:
                    if section not in config:
                        self.warnings.append(f"config.json missing '{section}' section")
                        
            except json.JSONDecodeError:
                self.errors.append("config/config.json is not valid JSON")
    
    def check_environment_variables(self):
        """Check for required environment variables"""
        print("\n🔐 Checking environment variables...")
        
        # Check for .env file
        env_path = self.project_root / ".env"
        if not env_path.exists():
            self.warnings.append(".env file not found - creating template")
            with open(env_path, 'w') as f:
                f.write("# ElevenLabs API Configuration\n")
                f.write("ELEVENLABS_API_KEY=your-api-key-here\n\n")
                f.write("# Future API Keys\n")
                f.write("# OPENAI_API_KEY=your-openai-key-here\n")
                f.write("# ANTHROPIC_API_KEY=your-anthropic-key-here\n")
        
        # Check if ELEVENLABS_API_KEY is set
        from dotenv import load_dotenv
        load_dotenv()
        
        if os.getenv("ELEVENLABS_API_KEY") and os.getenv("ELEVENLABS_API_KEY") != "your-api-key-here":
            self.success_messages.append("ELEVENLABS_API_KEY is configured ✓")
        else:
            self.warnings.append("ELEVENLABS_API_KEY not configured in .env file")
    
    def validate_reference_files(self):
        """Ensure critical reference files exist"""
        print("\n📄 Validating reference files...")
        
        reference_files = {
            "tests/reference/episode_2_ex_final.md": "Gold standard test episode",
            "docs/specifications/feat_spec-component-2-voice-gen.md": "Component 2 specification",
            "archive/codex_task_logs/TASK_LOG_TEMPLATE.md": "Task log template",
            "docs/specifications/workflow-log.md": "Workflow dashboard"
        }
        
        for file_path, description in reference_files.items():
            full_path = self.project_root / file_path
            if full_path.exists():
                self.success_messages.append(f"{description} found ✓")
            else:
                self.errors.append(f"Missing {file_path} ({description})")
    
    def validate_ffmpeg_installation(self):
        """Check if FFmpeg is installed and accessible"""
        print("\n🎥 Checking FFmpeg installation...")
        
        try:
            result = subprocess.run(
                ["ffmpeg", "-version"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                self.success_messages.append(f"FFmpeg installed: {version_line} ✓")
            else:
                self.errors.append("FFmpeg not found - required for audio processing")
        except FileNotFoundError:
            self.errors.append("FFmpeg not installed - install with 'brew install ffmpeg' (macOS)")
    
    def setup_git_environment(self):
        """Ensure git is configured properly"""
        print("\n🔀 Checking Git configuration...")
        
        try:
            # Check git installation
            result = subprocess.run(["git", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                self.success_messages.append(f"Git installed: {result.stdout.strip()} ✓")
            
            # Check if we're in a git repository
            result = subprocess.run(
                ["git", "rev-parse", "--git-dir"], 
                cwd=self.project_root,
                capture_output=True, text=True
            )
            if result.returncode == 0:
                self.success_messages.append("Git repository detected ✓")
                
                # Check current branch
                result = subprocess.run(
                    ["git", "branch", "--show-current"],
                    cwd=self.project_root,
                    capture_output=True, text=True
                )
                if result.returncode == 0:
                    branch = result.stdout.strip()
                    self.success_messages.append(f"Current branch: {branch}")
                    
        except FileNotFoundError:
            self.errors.append("Git not installed")
    
    def print_summary(self):
        """Print setup summary"""
        print("\n" + "=" * 60)
        print("📊 SETUP SUMMARY")
        print("=" * 60)
        
        if self.success_messages:
            print("\n✅ Successes:")
            for msg in self.success_messages:
                print(f"  {msg}")
        
        if self.warnings:
            print("\n⚠️  Warnings:")
            for msg in self.warnings:
                print(f"  {msg}")
        
        if self.errors:
            print("\n❌ Errors:")
            for msg in self.errors:
                print(f"  {msg}")
            print("\n🚨 Setup failed! Please fix the errors above.")
        else:
            print("\n🎉 Setup completed successfully!")
            print("\n📝 Next steps:")
            print("  1. Add your ELEVENLABS_API_KEY to the .env file")
            print("  2. Review docs/specifications/feat_spec-component-2-voice-gen.md")
            print("  3. Check workflow-log.md for implementation tracking")
            print("  4. Review and refine Codex-generated tasks before starting")
            
        print("\n" + "=" * 60)

if __name__ == "__main__":
    setup = CodexSetup()
    setup.run()