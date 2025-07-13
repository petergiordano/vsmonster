# Simple, Lovable, Complete (SLC) Session Notes: versusMonster AVPS

## Session Overview
*Planning notes for the first development sprint focusing on Script Parser + Asset Library foundation.*

**Session Date**: 2025-01-07  
**Sprint Goal**: Establish reliable Script Parser with Episode 7 validation and basic Asset Library  
**Success Metric**: Parse Episode 7 perfectly + create reusable asset foundation

## Simple: Core Feature Definition

### **What's the Single Most Important Feature?**
**Script Parser** - Transform Episode 7 markdown into structured JSON that all other components can reliably consume.

**Core Value Proposition**: 
"Every other component depends on clean, structured data from the script parser. If this fails, everything fails."

### **Must-Have vs Nice-to-Have**

#### ✅ **Must-Have (Week 1-2)**
- **CRITICAL**: Implement complete Pipeline Tag Specification (`docs/pipeline_tag_specification.md`)
- Parse Episode 7 markdown structure (`[SCENE:`, `THORAK:`, `ZARA:`, etc.)
- Extract all dialogue with character attribution AND voice direction parentheticals
- Capture multimedia tags (`[SFX:]`, `[MUSIC:]`, `[IMG:]`, `[AMBIENT:]`, `[TRANSITION:]`) with full context
- Parse image generation prompts with style consistency requirements for AI services
- Generate structured JSON that maps directly to service APIs (ElevenLabs, image gen, etc.)
- Handle scene transitions and timing markers
- Create feedback mechanism to script generator for tag format compliance

#### 🎯 **Nice-to-Have (Future Sprints)**
- Support multiple episode formats simultaneously
- Advanced timing calculations
- Automatic script quality scoring
- Real-time parsing validation during script creation

### **Simplicity Focus: How to Keep This Feature Simple**
1. **Single Input Format**: Focus only on Episode 7 markdown format initially
2. **Clear JSON Schema**: Simple, predictable output structure
3. **One Episode at a Time**: No batch processing complexity initially
4. **Direct File I/O**: No database, just files in/out
5. **Command-Line Only**: No GUI or web interface

## Lovable: Delightful Touch

### **What Makes This Feature Delightful?**

#### **🎯 Primary Delight Factor**
**"Perfect Handoff Confidence"** - When the parser runs, the user should feel complete confidence that downstream components will work flawlessly because the data structure is so clean and reliable.

#### **🌟 Delightful Moments**
1. **Clear Progress Feedback**: 
   ```
   ✓ Found 142 dialogue lines
   ✓ Extracted 8 image prompts  
   ✓ Parsed 12 SFX cues
   ✓ Validated scene structure
   📄 Generated: output/json/episode_007.json
   ```

2. **Intelligent Validation**:
   ```
   ⚠️ Warning: Missing [IMG:] tag in SCENE: BATTLE COMMENTARY
   💡 Suggestion: Add image prompt for visual engagement
   ```

3. **Script Generator Feedback**:
   ```
   📨 Feedback sent to script generator:
   ✓ All required tags present
   ✓ Character dialogue well-formatted
   ⚠️ Consider more SFX cues in battle scenes
   ```

### **User Experience Touches**
- **Anticipation**: "I wonder what images the AI suggested this time?"
- **Confidence**: "The parser caught every detail - voice generation will be perfect"
- **Learning**: "The system is helping improve future scripts automatically"

## Complete: Definition of Done

### **How to Know Script Parser is "Truly Complete"**

#### **Functional Completeness**
- [ ] Successfully parses Episode 7 with 100% accuracy
- [ ] Extracts all Thorak dialogue (verified against manual count)
- [ ] Extracts all Zara dialogue (verified against manual count)  
- [ ] Captures all SFX tags with proper context
- [ ] Captures all image prompts with scene association
- [ ] Captures all music cues with timing information
- [ ] Handles scene transitions correctly
- [ ] Generates valid JSON that validates against schema

#### **Quality Completeness**
- [ ] Processing time under 10 seconds for Episode 7
- [ ] Clear error messages for any parsing failures
- [ ] Robust handling of markdown formatting variations
- [ ] Validation against Episode 7 reference implementation
- [ ] JSON output is human-readable and debuggable

#### **Integration Completeness**
- [ ] JSON output successfully consumed by mock voice generator
- [ ] All required fields present for downstream components
- [ ] No manual cleanup needed after parsing
- [ ] Feedback mechanism functional with script generator
- [ ] Asset references properly linked to library structure

#### **User Experience Completeness**
- [ ] Command runs with single, obvious command
- [ ] Progress indication shows meaningful steps
- [ ] Success/failure states are crystal clear
- [ ] Error recovery guidance provided when needed
- [ ] Output location is obvious and accessible

### **User Acceptance Criteria**
*"When a user runs the script parser, they should feel..."*

1. **Confident**: "This definitely worked correctly"
2. **Informed**: "I understand exactly what happened"
3. **Ready**: "Voice generation will work perfectly with this output"
4. **Excited**: "I can see the high-quality data structure this created"

## Asset Library Foundation (Week 3)

### **Simple Asset Management**
**Core Need**: Easy way to store, discover, and reuse images/SFX/music across episodes.

#### **Must-Have Features**
- Folder-based organization (`assets/images/`, `assets/sfx/`, `assets/music/`)
- Auto-discovery of new assets dropped into folders
- Basic metadata tracking (filename, size, usage count)
- Simple asset referencing in output JSON

#### **Delightful Touch**
- **Smart Recommendations**: "Based on battle scenes, suggesting: sword_clash_01.wav"
- **Usage Analytics**: "tavern_ambient.mp3 used in 3 episodes - very effective!"
- **Easy Addition**: "Just drop files in the folder - we'll handle the rest"

### **Success Definition**
- [ ] Assets organized in logical folder structure
- [ ] New assets automatically discovered and cataloged
- [ ] Episode 7 processing references existing assets when appropriate
- [ ] Asset usage tracked for future optimization

## Development Strategy

### **Phase 1A: Core Parser (Week 1)**
1. **Day 1-2**: Episode 7 markdown analysis and JSON schema design
2. **Day 3-4**: Core parsing logic with dialogue extraction
3. **Day 5-7**: Multimedia tag parsing and validation

### **Phase 1B: Polish & Integration (Week 2)**
1. **Day 8-9**: Error handling and user experience polish
2. **Day 10-11**: Script generator feedback mechanism
3. **Day 12-14**: Integration testing and Episode 7 validation

### **Phase 1C: Asset Foundation (Week 3)**
1. **Day 15-16**: Asset folder structure and discovery
2. **Day 17-18**: Metadata tracking and usage analytics
3. **Day 19-21**: Integration with parser output and testing

## Risk Mitigation

### **Primary Risks**
1. **Script Format Variations**: Episode 7 might have unique formatting
   - **Mitigation**: Start with exact Episode 7 format, add flexibility iteratively

2. **Parsing Complexity**: Markdown parsing more complex than expected
   - **Mitigation**: Use proven markdown libraries, focus on specific tags

3. **JSON Schema Evolution**: Downstream components need different data structure
   - **Mitigation**: Design flexible schema with versioning capability

### **Quality Gates**
- **Gate 1**: Parse Episode 7 without errors
- **Gate 2**: Extract all dialogue with character attribution
- **Gate 3**: Validate JSON structure with sample voice generator
- **Gate 4**: Complete end-to-end test with Episode 7

---

## Session Success Metrics

**Technical Success**:
- Episode 7 parsed with 100% accuracy
- JSON validates against schema
- Processing time under 10 seconds
- Zero manual cleanup required

**User Experience Success**:
- Single command operation
- Clear progress feedback
- Obvious success/failure states
- Ready for voice generation

**Strategic Success**:
- Foundation for all 8 pipeline components
- Reliable handoff to voice generation
- Asset library ready for scaling
- Feedback loop established with script generation

---

*SLC Session Notes Version: 1.0*  
*Last Updated: 2025-01-07*