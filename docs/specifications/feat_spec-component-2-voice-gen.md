
# Feature Spec - Voice Generation (Component 2)**
Developed in Gemini [Chat Session] (https://gemini.google.com/gem/291fcca1fd00/bdba9e3d7bc0beb1)

### **Next Core Component: Voice Generation (Component 2)**

This component is crucial as it takes the structured data from the Script Parser and transforms it into a single, complete audio track containing all character dialogues.

#### **1. Overview & Goals**

  * **Goal**: Generate a **single, complete multi-character dialogue track (.wav file)** from the structured JSON output of Step 1 (Script Parser).
  * **Input**: JSON timeline from the Script Parser (now using `tests/reference/episode_007.md` as the primary test case), which contains dialogue text, character attribution, and voice directions.
  * **Output**: A single `.wav` audio file per episode, representing the complete talk track of two people. This file will be stored in `output/voices/`.
  * **Value Proposition**: This step delivers a unified voice track, ready for direct integration with music and SFX in Component 3.
  * **Primary Validation**: The combined talk track must sound authentic, with distinct voices for Thorak and Zara, and all intonations and emotional cues (e.g., "breathless") accurately interpreted by ElevenLabs.
  * **Simplicity Goal**: It should operate with a single command, such as `python voice_gen.py episode_007.json`.

#### **2. Technical Approach (`src/voice_gen.py`)**

The `src/voice_gen.py` script will be updated to leverage ElevenLabs' text-to-dialogue capabilities.

  * **ElevenLabs Text-to-Dialogue Integration**:
      * The script will utilize the ElevenLabs `text-to-dialogue` API endpoint to process the entire dialogue script in a single call. This is a change from potentially generating individual voice files.
      * Dialogue entries (text, character, direction) from the Script Parser's JSON will be prepared as a list of inputs for the ElevenLabs API request. Each input object will specify the `text` and `voice_id` for the respective character.
      * **Intonation and Instructions**: All intonations and emotional cues (e.g., "(Breathless with excitement)", "(Gravelly, analytical)") will be passed directly within the dialogue text to ElevenLabs. The Eleven v3 model (or other suitable multi-speaker models) can interpret these textual cues to influence speech emotion and delivery.
  * **Character Voice Mapping**: The existing mapping of "THORAK" and "ZARA" to their respective ElevenLabs `voice_id`s will be used within the API call's inputs.
  * **Input Processing**: It will load the JSON output from the Script Parser. The primary test file for this phase will be `output/json/episode_007.json`, derived from `tests/reference/episode_007.md`.
  * **Output Management**: The generated complete dialogue track will be saved as a single `.wav` file in `output/voices/{episode_name}/`.
  * **Model Selection**: Prioritize the Eleven v3 model if access is available, as it is designed for Text to Dialogue. Otherwise, use the recommended `eleven_multilingual_v2` model which offers high quality and is stable for long-form generations.

#### **3. Component 3 (Audio Assembly) Capabilities in Mind**

  * **Simplified Handoff**: By generating a single, complete dialogue track in Component 2, the task for Component 3 (Audio Assembly) becomes simpler and more focused: mixing this talk track with background music and sound effects. This eliminates the need for Component 3 to handle complex individual dialogue timing and sequencing.
  * **Optimized for Mixing**: The output `.wav` file will be a clean, ready-to-mix talk track, ideal for layering additional audio elements without requiring extensive post-processing by Component 3.

#### **4. Key Design Considerations**

  * **API Key Management**: The ElevenLabs API key must be securely loaded from a `.env` file.
  * **Error Recovery**: The component should handle API rate limits and network failures gracefully, logging warnings and aiming to produce partial results where possible.
  * **Cost Optimization**: **As per your instruction, cost optimization is explicitly deferred to a much later stage.** The current focus is on getting the core functionality to work reliably.
  * **Progress Reporting**: The script should provide clear progress updates, following the 5-step status display pattern established by the Script Parser.

#### **5. Validation & Quality Gates**

  * **Primary Test File**: `tests/reference/episode_007.md` will be the definitive source for parsing and voice generation validation.
  * **Functional**: The process must generate a single `.wav` file for the entire episode's dialogue, including all assigned characters and their respective lines from `episode_007.md`.
  * **Quality**: Manual review of the generated `.wav` file will confirm that Thorak and Zara's voices are authentic and distinct, and that all emotional cues (e.g., "(Breathless)") have been interpreted accurately by ElevenLabs. The overall dialogue flow and timing within the single file should sound natural.
  * **Performance**: The generation of the complete dialogue track for `episode_007.md` should be efficient, with a target processing time that allows for the overall pipeline goals.
  * **Reliability**: The process should complete without manual intervention and produce a usable audio file ready for Component 3.

This refined specification streamlines the Voice Generation component by leveraging ElevenLabs' advanced dialogue capabilities, directly facilitating the subsequent Audio Assembly step.

### Sources

  * [Text to Speech | ElevenLabs Documentation](https://elevenlabs.io/docs/capabilities/text-to-speech)
  * [Text to Dialogue | ElevenLabs Documentation](https://elevenlabs.io/docs/capabilities/text-to-dialogue)
  * [Mastering Multi-Voice Conversations with ElevenLabs: A Guide to Realistic AI Dialogue](https://ragaboutit.com/mastering-multi-voice-conversations-with-elevenlabs-a-guide-to-realistic-ai-dialogue/)
  * [The narrative integrity of dialog with multiple voices : r/ElevenLabs - Reddit](https://www.reddit.com/r/ElevenLabs/comments/1aqo9y2/the_narrative_integrity_of_dialog_with_multiple/)
  * [Text to Dialogue quickstart | ElevenLabs Documentation](https://elevenlabs.io/docs/cookbooks/text-to-dialogue)
  * [versusMonster Video Pipeline - PRD vo](https://www.google.com/search?q=uploaded:PRD-v0.pdf)
  * [CLAUDE.md](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a6d3525cd4023283dcb65e4772f8daf0b0b983de/CLAUDE.md)
  * [Product Requirements Document: Voice Generation (Step 2 of 8-Component Pipeline)](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a6d3525cd4023283dcb65e4772f8daf0b0b983de/archive/prd-voice-generation.md)
  * [Development Environment Setup](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a6d3525cd4023283dcb65e4772f8daf0b0b983de/docs/setup/development_setup.md)
  * [config.json](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a6d3525cd4023283dcb65e4772f8daf0b0b983de/config/config.json)
  * [feat\_spec-component-2-voice-gen.md](https://www.google.com/search?q=uploaded:feat_spec-component-2-voice-gen.md)
  * [tests/reference/episode\_2\_ex\_final.md](https://www.google.com/search?q=uploaded:episode_007.md)