# versusMonster Pipeline Tag Specification

## Overview
This document defines the standardized tag system that enables automated pipeline processing from script generation through final video production. All tags must be consistently formatted to ensure reliable parsing and service integration.

## Core Tag Categories

### **1. SCENE MARKERS**
**Purpose**: Define episode structure and transitions
**Format**: `## **[SCENE: SCENE_NAME]**`

**Examples**:
```markdown
## **[SCENE: COLD OPEN]**
## **[SCENE: INTRO & HOST BANTER]**
## **[SCENE: BATTLE SETUP]**
## **[SCENE: BATTLE COMMENTARY]**
## **[SCENE: ADVERTISEMENT BREAK 1]**
## **[SCENE: AFTERMATH ANALYSIS]**
## **[SCENE: OUTRO & NEXT EPISODE TEASE]**
```

**Pipeline Usage**:
- **Script Parser**: Scene boundary detection, timing calculation
- **Video Generation**: Scene transition timing, chapter markers
- **Asset Library**: Scene-specific asset selection

---

### **2. DIALOGUE TAGS**
**Purpose**: Character voice generation with ElevenLabs
**Format**: `CHARACTER_NAME: (Voice direction) "Dialogue text"`

**Supported Characters**:
```markdown
THORAK: (Voice direction) "Dialogue content"
ZARA: (Voice direction) "Dialogue content"
```

**Voice Direction Examples**:
- `(Gravelly, impressed)`
- `(Breathless)`
- `(Excited, dramatic)`
- `(Thoughtful, analytical)`

**Pipeline Usage**:
- **Script Parser**: Extract dialogue with character attribution and voice direction
- **Voice Generation**: Send to ElevenLabs with character-specific voice settings
- **Audio Assembly**: Character voice timing and mixing

**ElevenLabs Integration**:
- **Thorak Settings**: Stability 0.75, Similarity 0.85, Deep Scottish voice
- **Zara Settings**: Stability 0.45, Similarity 0.75, Energetic voice with "honey/sweetie" mannerisms

---

### **3. IMAGE GENERATION TAGS**
**Purpose**: AI image generation for visual content
**Format**: `[IMG: image_id] PROMPT: "Detailed image generation prompt"`

**Examples**:
```markdown
[IMG: cold_open_leap] PROMPT: "Massive armored bulette erupting from forest ground in mid-leap, jaws agape, targeting a green dragon hovering just above, dramatic lighting with earth and stone spraying, cinematic fantasy art style"

[IMG: hosts_broadcast] PROMPT: "Thorak (dwarf cleric with gray beard, robes) and Zara (tiefling with red skin, small horns, dark clothing) in ancient stone chamber with glowing scrying stones, warm magical lighting, fantasy broadcast studio"

[IMG: thornwall_grove] PROMPT: "Ancient forest clearing with massive oak trees, rocky outcroppings providing elevation, dappled sunlight through canopy, tactical stone platforms and fallen logs, atmospheric depth with mist in background"
```

**Prompt Standards**:
- **Style Consistency**: "cinematic fantasy art style", "atmospheric depth", "dramatic lighting"
- **Character Consistency**: 
  - Thorak: "dwarf cleric with gray beard, robes"
  - Zara: "tiefling with red skin, small horns, dark clothing"
- **Scene Context**: Include relevant environmental details and mood
- **Technical Quality**: "high resolution", "professional quality", "detailed"

**Pipeline Usage**:
- **Script Parser**: Extract image_id and prompt text
- **Image Generation**: Send prompt to AI image service
- **Asset Library**: Store generated images with metadata
- **Video Generation**: Insert images at scene timing markers

---

### **4. SOUND EFFECTS TAGS**
**Purpose**: Audio enhancement and atmosphere
**Format**: `[SFX: effect_name]`

**Categories and Examples**:

**Combat/Action**:
```markdown
[SFX: dice_rolling]
[SFX: sword_clash]
[SFX: armor_clinking]
[SFX: spell_casting]
```

**Environmental**:
```markdown
[SFX: earth_rumbling_deep]
[SFX: forest_settling_quiet]
[SFX: wind_through_trees]
[SFX: water_flowing]
```

**Interface/Transition**:
```markdown
[SFX: scrying_stone_powerdown]
[SFX: magical_whoosh]
[SFX: page_turning]
```

**Pipeline Usage**:
- **Script Parser**: Extract SFX cues with timing context
- **Asset Library**: Match to existing SFX or note for generation
- **Audio Assembly**: Layer SFX over dialogue and music
- **Cost Estimation**: Track SFX generation/licensing costs

---

### **5. MUSIC TAGS**
**Purpose**: Background music and musical transitions
**Format**: `[MUSIC: music_id]`

**Music Categories**:

**Themes**:
```markdown
[MUSIC: main_theme_intro]
[MUSIC: main_theme_outro]
[MUSIC: character_theme_thorak]
[MUSIC: character_theme_zara]
```

**Mood/Atmosphere**:
```markdown
[MUSIC: tavern_festive]
[MUSIC: battle_tension]
[MUSIC: elegant_orchestral]
[MUSIC: mysterious_ambient]
```

**Transitions**:
```markdown
[MUSIC: transition_whoosh]
[MUSIC: scene_change_sting]
[MUSIC: commercial_break]
```

**Pipeline Usage**:
- **Script Parser**: Extract music cues with scene context
- **Asset Library**: Match to existing music library or commission new
- **Audio Assembly**: Background music mixing with proper ducking for dialogue
- **Cost Estimation**: Track music licensing/generation costs

---

### **6. AMBIENT AUDIO TAGS**
**Purpose**: Environmental soundscapes
**Format**: `[AMBIENT: environment_name]`

**Examples**:
```markdown
[AMBIENT: forest_wind_eerie]
[AMBIENT: forest_battle_tension]
[AMBIENT: forest_peaceful_aftermath]
[AMBIENT: tavern_background]
[AMBIENT: castle_great_hall]
```

**Pipeline Usage**:
- **Script Parser**: Extract ambient cues for scene atmosphere
- **Asset Library**: Environmental audio loops and soundscapes
- **Audio Assembly**: Subtle background atmosphere mixing

---

### **7. TRANSITION TAGS**
**Purpose**: Scene transitions and special effects
**Format**: `[TRANSITION: transition_description]`

**Examples**:
```markdown
[TRANSITION: Magical whoosh effect leading to intro music]
[TRANSITION: Battle atmosphere returns]
[TRANSITION: Return to aftermath atmosphere]
[TRANSITION: Fade to black with mysterious music]
```

**Pipeline Usage**:
- **Script Parser**: Mark transition points and effects
- **Audio Assembly**: Special transition audio effects
- **Video Generation**: Visual transition effects between scenes

---

## Pipeline Integration Standards

### **Script Generator → Script Parser**
**Requirements**:
- All tags must use exact format specifications
- Image prompts must include style consistency markers
- Character dialogue must include voice direction parentheticals
- Scene markers must follow episode structure pattern

**Quality Validation**:
- Minimum 7 image prompts per episode
- Balanced dialogue between Thorak and Zara
- Appropriate SFX density (1-2 per scene minimum)
- Music cues at scene transitions

### **Script Parser → Service APIs**
**Data Structure**:
```json
{
  "episode_metadata": {
    "title": "Episode Title",
    "number": "S1-Sesh007",
    "runtime_estimate": "18 minutes"
  },
  "scenes": [
    {
      "scene_id": "cold_open",
      "scene_name": "COLD OPEN",
      "dialogue": [
        {
          "character": "ZARA",
          "voice_direction": "Breathless",
          "text": "OH MY GODS! That landshark just launched itself thirty feet straight up at a DRAGON!",
          "timestamp": 5.2
        }
      ],
      "images": [
        {
          "image_id": "cold_open_leap",
          "prompt": "Massive armored bulette erupting from forest ground...",
          "timestamp": 2.0
        }
      ],
      "sfx": [
        {
          "effect": "earth_rumbling_deep",
          "timestamp": 0.0
        }
      ],
      "music": [],
      "ambient": [],
      "transitions": []
    }
  ]
}
```

### **Service Integration Specifications**

#### **ElevenLabs Voice Generation**
- **Input**: Character name, voice direction, dialogue text
- **Output**: WAV file with specific naming: `{episode_id}_{character}_{line_number}.wav`
- **Quality**: 44.1kHz, 16-bit, mono
- **Cost Tracking**: Character count, API calls

#### **Image Generation (TBD Service)**
- **Input**: Image prompt with style consistency
- **Output**: High-resolution image (1920x1080 minimum)
- **Format**: PNG for transparency support, JPG for backgrounds
- **Cost Tracking**: Prompt complexity, resolution, style requirements

#### **Music/SFX Services**
- **Asset Library**: Prioritize reusable assets
- **Generation**: When new assets needed
- **Licensing**: Track usage rights and costs
- **Format**: WAV for SFX, MP3 for music

## Quality Assurance

### **Script Generator Feedback Loop**
**Automated Validation**:
- [ ] All required scene types present
- [ ] Minimum image count met (7+ per episode)
- [ ] Character dialogue balance maintained
- [ ] SFX density appropriate for content
- [ ] Music cues present at transitions

**Quality Scoring**:
- **Parsing Success Rate**: % of tags successfully extracted
- **Prompt Quality**: Consistency with style guidelines
- **Content Balance**: Dialogue/SFX/Music ratio analysis
- **Cost Efficiency**: Asset reuse vs. new generation ratio

### **Human Review Points**
- **Generated Images**: Quality and consistency check
- **Voice Output**: Character authenticity verification
- **Final Video**: Overall production quality assessment

## Cost Management

### **Bill of Materials Tracking**
**Per Episode**:
- **ElevenLabs**: Character count × rate
- **Image Generation**: Number of prompts × complexity factor
- **Music Licensing**: Track count × licensing fee
- **SFX Generation**: New effects × generation cost
- **Processing Time**: Local compute costs

**Budget Controls**:
- **Daily/Weekly Limits**: API usage caps
- **Asset Reuse Prioritization**: Favor existing library content
- **Quality vs. Cost Tradeoffs**: Configurable quality presets

---

## Evolution and Versioning

**Tag Format Version**: 1.0
**Last Updated**: 2025-01-07

**Future Considerations**:
- Advanced character emotion tags
- 3D environment specifications
- Interactive element markers
- Multi-language support
- Real-time generation capabilities

This specification ensures consistent, automated pipeline processing while maintaining creative quality and cost efficiency.