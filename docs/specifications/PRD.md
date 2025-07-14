# VersusMonster Automated Video Podcast System - Product Requirements Document

**Version**: 2.1 (Consolidated Master)  
**Last Updated**: 2025-07-14
**Development Philosophy**: Function Over Fashion - Build iteratively with compound value

## 1. Executive Summary

### 1.1. Vision
An automated Python-based system that transforms markdown scripts into complete multimedia podcast episodes suitable for YouTube. The system eliminates manual audio/video production work, enabling focus on creative content generation.

### 1.2. Business Goals & Objectives
*   **Primary Goal**: Generate **2 podcast episodes per week for a full year (104 episodes)** to build an audience and explore monetization through advertising and sponsorships.
*   **Secondary Goals**:
    *   Reduce episode production time to under 1 hour per week.
    *   Enable batch pre-production of 10-20 episodes per month.
    *   Achieve professional broadcast quality indistinguishable from manual production.
    *   Build a scalable foundation for a multi-genre "faceless YouTube business."
    *   Create a potentially marketable AVPS system for other creators.

### 1.3. Guiding Principles
*   **Function Over Fashion**: Build iteratively with compound value. No fancy UI/UX - purely command-line tools that deliver functional value immediately.
*   **Simple, Lovable, and Complete (SLC)**: Each component should be built with a focus on being simple, lovable, and complete. For a detailed breakdown of this philosophy, see the **[SLC Principles](../architecture/SLC_Principles.md)**.

## 2. System Architecture & Status

### 2.1. 8-Component Pipeline Overview & Status

*   **Component 1: Script Parser** - ✅ COMPLETE (2025-01-08)
*   **Component 2: Voice Generation** - 🚧 IN PROGRESS (1/9 tasks)
*   **Component 3: Audio Assembly** - 📝 PLANNED
*   **Component 4: Static Video** - 📝 PLANNED
*   **Component 5: Image Transitions** - 📝 PLANNED
*   **Component 6: Sound Effects** - 📝 PLANNED
*   **Component 7: Background Music** - 📝 PLANNED
*   **Component 8: Batch Processing** - 📝 PLANNED

### 2.2. Technical Stack
*   **Language**: Python 3.11+
*   **Audio**: ElevenLabs API, FFmpeg
*   **Video**: FFmpeg with VideoToolbox
*   **Deployment**: Command-line tools
*   **Storage**: Local filesystem

## 3. Component Specifications

### 3.1. Component 1: Script Parser ✅ COMPLETE
*   **Status**: Complete (2025-01-08)
*   **Performance**: 0.003s processing time (300x faster than requirement)
*   **Accuracy**: 100% successful parsing of Episode 7
*   **Implementation Details**: See `../../archive/COMPLETED_TASKS.md` for full development history.

### 3.2. Component 2: Voice Generation 🚧 IN PROGRESS
*   **Status**: In Development
*   **Target**: Generate authentic character voices via ElevenLabs API.
*   **Current Tasks**: See `TODO.md`.

...(Detailed specifications for all 8 components follow, as in the original PRD)...

## 4. Technical Requirements & Constraints

### 4.1. Dependencies
*   Python 3.11+
*   ElevenLabs Python SDK
*   FFmpeg 7.1 with VideoToolbox
*   python-dotenv

### 4.2. Known Challenges & Mitigations
*   **API Cost Management**: Build a cost estimation utility and track the bill of materials (BOM) per episode.
*   **Script Parser Reliability**: Establish a feedback loop to the script generator and conduct comprehensive testing using Episode 7.
*   **Processing Fault Tolerance**: Implement resume capability, component-level error isolation, and clear status reporting.
*   **Asset Library Growth**: Use a simple folder structure with metadata to avoid premature optimization.

## 5. Success Metrics & Validation

### 5.1. Overall Project Success
*   Produce 104 episodes in one year.
*   Achieve a processing time of <30 minutes per episode.
*   Keep costs under $10 per episode.
*   Generate YouTube-ready quality videos.
*   Require zero manual intervention.

### 5.2. Validation Standards
*   Episode 7 serves as the primary test case.
*   Each component is validated against Episode 7.
*   Integration testing is performed between adjacent components.
*   End-to-end testing is conducted after Component 4 is complete.

## 6. Project Management

### 6.1. Source of Truth
This document is the definitive source of truth for component specifications and progress tracking.

### 6.2. PRD Maintenance
*   **Never Change**: Core requirements, success criteria, component architecture.
*   **Always Update**: Status markers, completion dates, validation results, task progress (often facilitated by AI commands like `@update-prd`).

---

**Bottom Line**: Build the simplest possible version of each component first. Each step should deliver immediate, testable value that compounds with previous work. No fancy interfaces—just rock-solid functionality that gets you closer to automated episode production with every iteration.