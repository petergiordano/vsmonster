# Feature Spec - Voice Generation (Component 2 )

### **Next Core Component: Voice Generation (Component 2)**

This component is crucial as it takes the structured data from the Script Parser and transforms it into individual audio files for each character's dialogue.

#### **1. Overview & Goals**

  * **Goal**: Transform the structured JSON output from Step 1 (Script Parser) into individual voice files.
  * **Input**: JSON timeline from the Script Parser, which contains dialogue text, character attribution, and voice directions.
  * **Output**: Separate WAV audio files for each character line. These files will be stored in `output/voices/`.
  * **Value Proposition**: This step proves that the ElevenLabs API integration works effectively.
  * **Primary Validation**: Thorak and Zara's voices must sound authentic and distinct.
  * **Simplicity Goal**: It should operate with a single command, such as `python voice_gen.py episode_007.json`.

#### **2. Technical Approach (`src/voice_gen.py`)**

The `src/voice_gen.py` script will be the core of this component.

  * **ElevenLabs Integration**: The script will interface with the ElevenLabs API using the official Python SDK (`elevenlabs` package).
      * **Character Voice Mapping**: Specific ElevenLabs voice IDs will be mapped to "THORAK" and "ZARA". For example, THORAK is expected to have a scholarly, gravelly tone, while ZARA should have an energetic, emotional variation.
      * **Voice Direction Integration**: The script will parse voice directions (e.g., "(Breathless)", "(Gravelly, impressed)") from the markdown and apply adjustments to ElevenLabs parameters like voice stability and similarity.
  * **Input Processing**: It will load and validate the JSON output from the Script Parser (`output/json/episode_007.json`).
  * **File Output Management**: Voice files will be saved in WAV format (44.1kHz sample rate) to `output/voices/{episode_name}/`, following a naming convention like `{episode}_{scene_id}_{dialogue_index}_{character}.wav`.

#### **3. Key Design Considerations**

  * **API Key Management**: The ElevenLabs API key must be securely loaded from a `.env` file.
  * **Error Recovery**: The component should handle API rate limits and network failures gracefully, never failing completely, and aiming to produce partial results with clear error messages.
  * **Cost Tracking**: It must monitor real-time API usage (character count) and integrate with the existing cost estimation framework.
  * **Progress Reporting**: The script should provide clear progress updates, following the 5-step status display pattern established by the Script Parser.

#### **4. Validation & Quality Gates**

  * **Functional**: All dialogues (e.g., 69 dialogues for Episode 7) must be converted to voice files.
  * **Quality**: Thorak and Zara's voices should be distinct and character-appropriate.
  * **Performance**: Episode 7 processing should complete in under 5 minutes.
  * **Reliability**: The process should complete without manual intervention.

**Next Steps**: Focus on implementing the `voice_gen.py` script to meet these criteria, using Episode 7 as the primary test case.

### Sources

  * [versusMonster Video Pipeline - PRD vo](https://www.google.com/search?q=uploaded:PRD-v0.pdf)
  * [Product Requirements Document: Voice Generation (Step 2 of 8-Component Pipeline)](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a6d3525cd4023283dcb65e4772f8daf0b0b983de/archive/prd-voice-generation.md)
  * [CLAUDE.md](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a6d3525cd4023283dcb65e4772f8daf0b0b983de/CLAUDE.md)
  * [Development Environment Setup](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a6d3525cd4023283dcb65e4772f8daf0b0b983de/docs/setup/development_setup.md)
  * [config.json](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a6d3525cd4023283dcb65e4772f8daf0b0b983de/config/config.json)
  * [src/voice\_gen.py](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a6d3525cd4023283dcb65e4772f8daf0b0b983de/src/voice_gen.py)