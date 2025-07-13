# Component Library: versusMonster AVPS

## Design Philosophy
*Simple, Lovable, Complete (SLC) framework with command-line first approach.*

**Core Principles**:
- **Simple**: Clean CLI interfaces with ASCII progress indicators
- **Lovable**: Exciting generative content with reliable fault tolerance  
- **Complete**: Professional broadcast-quality output ready for YouTube

## System Architecture Components

### **Pipeline Components (8-Stage Process)**

#### **1. Script Parser**
- **Purpose**: Transform markdown scripts into structured JSON
- **Input**: Episode markdown (e.g., `episode_007.md`)
- **Output**: Structured JSON with dialogue, timing, and multimedia cues
- **Interface**: `python src/parser.py episode_007.md`
- **Status Display**: Component progress with validation checkpoints

#### **2. Voice Generation**
- **Purpose**: Generate character voices using ElevenLabs API
- **Input**: Parsed JSON with dialogue segments
- **Output**: Individual WAV files for each character line
- **Interface**: `python src/voice_gen.py episode_007.json`
- **Characters**: Thorak (deep Scottish), Zara (energetic, uses "honey/sweetie")

#### **3. Audio Assembly**
- **Purpose**: Combine voice files into complete audio track
- **Input**: Individual voice files + timing data
- **Output**: Single MP3 with proper dialogue timing
- **Interface**: `python src/audio_mix.py episode_007`

#### **4. Video Generation** 
- **Purpose**: Combine audio with visual elements
- **Input**: Audio track + background images
- **Output**: MP4 video file (1920x1080, 30fps)
- **Interface**: `python src/video_gen.py episode_007`

#### **5. Image Integration**
- **Purpose**: Add dynamic image transitions
- **Input**: Video + multiple episode images
- **Output**: Video with image changes at scene breaks

#### **6. Sound Effects**
- **Purpose**: Layer SFX over existing video
- **Input**: Video + SFX cues from script
- **Output**: Enhanced video with battle sounds, dice rolling, etc.

#### **7. Background Music**
- **Purpose**: Add music layer for complete audio mix
- **Input**: Enhanced video + music cues
- **Output**: Full production video with complete audio

#### **8. Batch Processing**
- **Purpose**: Process multiple episodes automatically
- **Input**: Multiple script files
- **Output**: Queue of complete videos

### **User Interface Components**

#### **Command-Line Interface**
```bash
# Primary Commands
avps parse episode_007.md          # Run script parser
avps generate episode_007.json     # Generate voices
avps assemble episode_007           # Mix audio
avps create episode_007             # Generate video
avps process episode_007.md         # Run complete pipeline

# Utility Commands
avps status                         # Show current processing status
avps validate episode_007           # Validate output quality
avps costs episode_007              # Estimate/show costs
avps library list                   # Show available assets
```

#### **Progress Indicators**
```
[████████████████████░░░░] 80% Script Parser
  ✓ Dialogue extracted (142 lines)
  ✓ SFX tags parsed (12 cues)  
  ✓ Image tags parsed (8 prompts)
  ⏳ Scene timing calculation...
  
Estimated completion: 2 minutes
```

#### **Status Display Components**
- **Real-time Progress**: ASCII progress bars for each component
- **Validation Checkpoints**: Green checkmarks for completed validations
- **Error Messages**: Clear, actionable failure descriptions
- **Time Estimates**: Realistic completion time predictions
- **Cost Tracking**: Real-time API usage and cost estimation

### **Asset Management Components**

#### **Library Structure**
```
assets/
├── images/
│   ├── backgrounds/     # Episode background images
│   ├── characters/      # Character portraits
│   └── scenes/         # Scene-specific images
├── sfx/
│   ├── combat/         # Battle and dice sounds
│   ├── ambient/        # Environment sounds
│   └── ui/             # Interface sounds
└── music/
    ├── themes/         # Main themes
    ├── ambient/        # Background music
    └── stings/         # Short musical cues
```

#### **Asset Discovery**
- **Auto-Detection**: System scans folders for new assets
- **Metadata Tracking**: Usage frequency, quality ratings
- **Smart Selection**: Genre/mood-based asset recommendations
- **Simple Addition**: Drag-and-drop or folder copy for new assets

### **Quality Control Components**

#### **Validation Gates**
1. **Script Validation**: Ensure all required tags are present
2. **Voice Quality**: Validate audio levels and character consistency
3. **Timing Sync**: Verify audio/video synchronization
4. **Output Standards**: Confirm broadcast quality (1920x1080, proper audio levels)

#### **Error Recovery**
- **Component Isolation**: Failures don't cascade to other components
- **Resume Capability**: Restart from last successful checkpoint
- **Clear Diagnostics**: Specific error messages with suggested fixes
- **Rollback Options**: Return to previous successful state

### **Cost Management Components**

#### **Bill of Materials (BOM) Tracking**
- **API Usage**: ElevenLabs character count and costs
- **Processing Time**: Local compute resource usage
- **Storage**: Generated file size tracking
- **External Services**: Music, SFX, image generation costs

#### **Cost Estimation**
```
Episode 007 Cost Estimate:
├── ElevenLabs (2,847 characters): $0.85
├── Image Generation (8 prompts): $0.40
├── Background Music (1 track): $0.25
└── Total Estimated Cost: $1.50
```

## Color & Style Guidelines

### **CLI Color Scheme**
- **Success**: Green (✓ checkmarks, completed progress)
- **Warning**: Yellow (⚠️ warnings, cost alerts)
- **Error**: Red (❌ failures, critical issues)
- **Info**: Blue (ℹ️ information, tips)
- **Progress**: Cyan (⏳ current operations)

### **Typography Patterns**
- **Commands**: `monospace code style`
- **File Names**: `episode_007.md`
- **Status**: **Bold for emphasis**
- **Progress**: █████░░░░░ ASCII blocks

### **Message Templates**
```
✓ SUCCESS: Component completed successfully
⚠️ WARNING: High API usage detected
❌ ERROR: Invalid script format - missing [SCENE] tags
ℹ️ INFO: 8 images found in assets/images/backgrounds/
⏳ PROCESSING: Generating voice for Thorak (line 47/142)
```

## Key UI Components

### **Episode Queue Management**
- **Current Episode**: Show active processing status
- **Completed Episodes**: List with file locations and costs
- **Failed Episodes**: Show error status and recovery options
- **Asset Library**: Available images, SFX, music with usage stats

### **Configuration Management**
- **Voice Settings**: Character-specific ElevenLabs parameters
- **Quality Presets**: Different output quality levels
- **Cost Limits**: Budget controls and alerts
- **Asset Preferences**: Default music/SFX styles

### **Output Organization**
```
output/
├── episode_007/
│   ├── episode_007.mp4           # Final video
│   ├── episode_007_audio.mp3     # Audio track
│   ├── voices/                   # Individual voice files
│   ├── assets_used.json          # Asset manifest
│   └── production_report.json    # Complete cost/timing report
```

## Visual References

### **Inspiration CLI Tools**
- **Modern Tools**: `fd`, `ripgrep`, `bat` - clean, fast, informative
- **Progress Bars**: `wget`, `rsync` - clear progress indication
- **Status Display**: `htop`, `git status` - organized information hierarchy
- **Error Handling**: `rust compiler` - helpful, actionable error messages

### **Quality Standards**
- **Broadcast Quality**: 1920x1080, 30fps, professional audio levels
- **Generative Surprise**: Unique content each run while maintaining quality
- **User Confidence**: Never break without clear recovery path
- **Processing Speed**: Optimized for local macOS with hardware acceleration

---

*Component Library Version: 1.0*  
*Last Updated: 2025-01-07*