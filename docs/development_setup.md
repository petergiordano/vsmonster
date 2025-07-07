# versusMonster Development Environment Setup

This guide provides step-by-step instructions for setting up your development environment for the versusMonster Automated Video Podcast System (AVPS).

## Prerequisites

Before beginning setup, ensure you have:
- **macOS** (tested on macOS 12+ with Apple Silicon or Intel)
- **Python 3.9 or higher** (3.11 recommended)
- **Homebrew** package manager installed
- **Git** for version control
- **Active internet connection** for package downloads
- **ElevenLabs API key** (sign up at https://elevenlabs.io)

## Step 1: Verify Python Installation

```bash
# Check Python version
python3 --version

# Should output: Python 3.9.x or higher
# If not installed, use Homebrew:
brew install python@3.11
```

## Step 2: Install FFmpeg with Video Support

FFmpeg is critical for all video/audio processing operations.

```bash
# Install FFmpeg with all codecs
brew install ffmpeg

# Verify installation
ffmpeg -version

# Should show version 5.0 or higher for optimal Apple Silicon support
# Check for VideoToolbox support (hardware acceleration)
ffmpeg -encoders | grep videotoolbox
```

Expected output should include:
- `h264_videotoolbox`
- `hevc_videotoolbox`

## Step 3: Choose Environment Manager

### Option A: Conda (Recommended)

Conda provides better dependency management for scientific/media processing projects.

**Install Conda (if not already installed):**
```bash
# Install Miniconda (lightweight)
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
bash Miniconda3-latest-MacOSX-arm64.sh

# Or install via Homebrew
brew install --cask miniconda

# Initialize conda
conda init zsh  # or bash
# Restart terminal or source ~/.zshrc
```

**Create and activate conda environment:**
```bash
# Navigate to project root
cd /path/to/vsmonster

# Create environment from environment.yml
conda env create -f environment.yml

# Activate environment
conda activate versusmonster
```

### Option B: Virtual Environment (Alternative)

If you prefer pip or conda isn't available:

```bash
# Navigate to project root
cd /path/to/vsmonster

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip
```

## Step 4: Install Python Dependencies

**If using Conda (Option A):**
```bash
# Dependencies are automatically installed from environment.yml
# Verify installation
conda list
```

**If using pip (Option B):**
```bash
# Install all required packages
pip install -r requirements.txt
```

## Step 5: Configure Environment Variables

1. Create `.env` file in project root:
```bash
touch .env
```

2. Add your API keys to `.env`:
```env
# ElevenLabs API Configuration
ELEVENLABS_API_KEY=your-elevenlabs-api-key-here

# Optional: Future API keys
# OPENAI_API_KEY=your-openai-key-here
# AWS_ACCESS_KEY_ID=your-aws-key-here
```

3. **CRITICAL**: Ensure `.env` is in `.gitignore`:
```bash
echo ".env" >> .gitignore
```

## Step 6: Create Project Directory Structure

```bash
# Create required directories
mkdir -p scripts
mkdir -p output/json output/voices output/audio output/videos
mkdir -p assets/images assets/sfx assets/music
mkdir -p reference

# Verify structure
tree -d -L 2
```

Expected structure:
```
.
├── assets
│   ├── images
│   ├── music
│   └── sfx
├── docs
├── output
│   ├── audio
│   ├── json
│   ├── videos
│   └── voices
├── reference
├── scripts
└── src
```

## Step 7: Add Episode 7 Test File

The Episode 7 reference file should already be in place:
```bash
# Verify Episode 7 exists
ls reference/episode_7_example.md
```

If needed, copy your Episode 7 markdown to:
```bash
cp /path/to/episode_7.md reference/episode_7_example.md
```

## Step 8: Run Environment Validation

Execute the validation script to ensure everything is configured correctly:

```bash
python setup_validation.py
```

This script will:
- Verify Python version
- Check FFmpeg installation and codecs
- Validate directory structure
- Test API key configuration
- Perform basic FFmpeg operations
- Generate a validation report

## Troubleshooting Common Issues

### FFmpeg Not Found
```bash
# Add Homebrew to PATH (Apple Silicon)
echo 'export PATH=/opt/homebrew/bin:$PATH' >> ~/.zshrc
source ~/.zshrc

# Intel Macs
echo 'export PATH=/usr/local/bin:$PATH' >> ~/.zshrc
source ~/.zshrc

# For current session only (temporary fix)
export PATH="/opt/homebrew/bin:$PATH"
```

### Python Package Installation Failures

**opencv-python on Apple Silicon:**
```bash
# If opencv-python fails, try:
pip install opencv-python-headless
```

**pillow installation issues:**
```bash
# Install dependencies first
brew install libjpeg libpng libtiff
pip install --no-cache-dir pillow
```

### ElevenLabs API Errors

1. **Invalid API Key**: Verify key in ElevenLabs dashboard
2. **Rate Limits**: Free tier has 10,000 characters/month
3. **Network Issues**: Check firewall/proxy settings

### FFmpeg Hardware Acceleration Not Working

```bash
# Test VideoToolbox encoding
ffmpeg -f lavfi -i testsrc=duration=10:size=1920x1080:rate=30 \
       -c:v h264_videotoolbox test.mp4

# If this fails, FFmpeg may need reinstalling:
brew reinstall ffmpeg
```

### Virtual Environment Issues

```bash
# If venv activation fails
deactivate  # If another venv is active
rm -rf venv
python3 -m venv venv
source venv/bin/activate
```

## Performance Optimization Tips

### macOS-Specific Optimizations

1. **Use VideoToolbox for encoding** (reduces CPU usage by 80%):
   ```python
   # In your FFmpeg commands
   '-c:v', 'h264_videotoolbox'
   ```

2. **Optimize for Apple Silicon**:
   - Ensure you're using native ARM64 Python
   - Use native ARM64 FFmpeg build
   - Monitor Activity Monitor for efficiency

3. **Memory Management**:
   - Process audio in chunks for large files
   - Use streaming APIs when possible
   - Clear temporary files after processing

## Validation Checklist

Before proceeding to development:

- [ ] Python 3.9+ installed and active
- [ ] FFmpeg 5.0+ installed with VideoToolbox support
- [ ] All Python packages installed successfully
- [ ] .env file created with valid ELEVENLABS_API_KEY
- [ ] All project directories created
- [ ] Episode 7 reference file in place
- [ ] setup_validation.py runs without errors
- [ ] Test FFmpeg command produces valid output

## Version Control Setup

This project uses **GitHub Desktop** for version control operations:

1. **Commits**: Use GitHub Desktop to stage and commit changes
2. **Pushes**: Push to https://github.com/petergiordano/vsmonster.git via GitHub Desktop
3. **Security**: Never commit `.env` files (protected by `.gitignore`)
4. **Frequency**: Commit after major setup steps or feature completions

## Next Steps

Once setup is complete:

1. **Commit current progress** using GitHub Desktop
2. Run `/start-coding` in Claude Code to begin development
3. Start with Component 1: Script Parser
4. Use Episode 7 as your test case
5. Validate each component before moving to the next

## Additional Resources

- [ElevenLabs API Documentation](https://elevenlabs.io/docs/api-reference/text-to-speech)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [Python subprocess Module](https://docs.python.org/3/library/subprocess.html)
- [MoviePy Documentation](https://zulko.github.io/moviepy/)

## Support

If you encounter issues not covered here:
1. Check the project's GitHub Issues
2. Review FFmpeg logs for detailed error messages
3. Verify all API keys and credentials
4. Ensure sufficient disk space for media processing