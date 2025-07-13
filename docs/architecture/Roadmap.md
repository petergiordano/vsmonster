# Project Roadmap: versusMonster AVPS

## Vision
An automated Python-based system that transforms markdown podcast scripts into complete multimedia YouTube episodes, enabling 2 episodes per week production with minimal manual intervention.

## Goals & Objectives
*Specific, measurable outcomes that define success for this project.*

- **Goal 1**: Reduce episode production time to under 1 hour per week
- **Goal 2**: Enable batch pre-production of 10-20 episodes per month
- **Goal 3**: Achieve professional broadcast quality indistinguishable from manual production
- **Goal 4**: Build scalable foundation for multi-genre "faceless YouTube business"
- **Goal 5**: Create potentially marketable AVPS system for other creators

## Desired User Experience & Vibe
*How should users feel when using the application? What emotional response are you aiming for?*

- **Target Vibe**: Simple, reliable, excitement-generating
- **Key Emotions**: 
  - Starting batch: Excitement about generative content variety
  - During processing: Confidence in system reliability with clear status updates
  - Reviewing output: Curiosity, excitement, anticipation for audience feedback
- **Experience Principles**: 
  - "System never breaks unexpectedly - fault tolerant with resume capability"
  - "Clear, understandable status updates throughout processing"
  - "Fail fast with clear error messages"

## Architecture Overview
*High-level description of the technical approach and system components.*

- **Core Language**: Python 3.11+ with virtual environment
- **Media Processing**: FFmpeg with VideoToolbox hardware acceleration (macOS)
- **Voice Generation**: ElevenLabs API with streaming capabilities
- **Asset Management**: Simple folder-based library (images/, sfx/, music/)
- **Interface**: Command-line first, ASCII progress indicators
- **Pipeline**: 8-component iterative build strategy

## User Stories & Features

### Phase 1A: Script Parser + Feedback (Weeks 1-2)
- [ ] **US1**: As a content creator, I want to parse Episode 7 markdown into structured JSON, so that all components can access dialogue and multimedia cues reliably
  - Feature 1.1: Extract Thorak/Zara dialogue with proper attribution
  - Feature 1.2: Parse [SFX:], [MUSIC:], [IMG:] tags with context
  - Feature 1.3: Handle scene transitions and timing markers
  - Feature 1.4: Create feedback mechanism to script generator for parsing issues

### Phase 1B: Asset Library Foundation (Week 3)
- [ ] **US2**: As a content creator, I want simple asset management, so that I can reuse images/SFX/music efficiently
  - Feature 2.1: Folder-based asset discovery and organization
  - Feature 2.2: Basic metadata tracking for reuse optimization
  - Feature 2.3: Simple asset addition via folder drop

### Phase 2: Voice Generation Integration (Weeks 4-5)
- [ ] **US3**: As a content creator, I want automated voice generation, so that Thorak and Zara sound authentic and distinct
  - Feature 3.1: ElevenLabs integration with character-specific settings
  - Feature 3.2: Timing synchronization with parsed dialogue
  - Feature 3.3: Quality validation and regeneration capability

### Phase 3: Complete Pipeline (Weeks 6-8)
- [ ] **US4**: As a content creator, I want end-to-end episode production, so that I can generate complete YouTube-ready videos
- [ ] **US5**: As a content creator, I want cost estimation and tracking, so that I can manage production budgets effectively

### Future: Scaling & Business Development
- [ ] **US6**: As a business owner, I want multi-genre podcast support, so that I can expand content variety
- [ ] **US7**: As a potential product owner, I want user-friendly deployment, so that I can sell AVPS to other creators

## Known Challenges & Constraints
*Identified risks, limitations, and how they'll be addressed.*

- **Challenge 1**: API Cost Management (ElevenLabs, potentially others)
  - Mitigation: Build cost estimation utility, track BOM per episode

- **Challenge 2**: Script Parser Reliability
  - Mitigation: Establish feedback loop to script generator, comprehensive Episode 7 testing

- **Challenge 3**: Processing Fault Tolerance
  - Mitigation: Resume capability, component-level error isolation, clear status reporting

- **Challenge 4**: Asset Library Growth Management
  - Mitigation: Simple folder structure with metadata, avoid premature optimization

---

## Roadmap Changelog
*Track significant changes to the roadmap itself.*

- **2025-01-07**: Initial roadmap created from foundation interview
- **2025-01-07**: Established 8-component pipeline strategy and feedback loop requirements
---