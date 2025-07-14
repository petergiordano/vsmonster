# CHRONICLES OF KHRONEXIA: STANDARDIZED EPISODE TEMPLATE

⚠️ **CRITICAL INSTRUCTION FOR AI MODELS (Claude, GPT, etc.)**: 
**DO NOT REMOVE BACKSLASHES FROM TAGS!** All `\[TAG:]` formats are intentional and required. The backslash before square brackets is NOT a formatting error - it's essential for parser compatibility. When generating episodes, preserve ALL backslashes exactly as shown in this template.

**Document Title:** standard_episode_template  TECHNICAL VALIDATION CHECKLIST

**Version:** 2.0  

**Last Updated:** July 11, 2025  

**Purpose:** Complete 8-section structure and formatting specifications for episode generation with parser-compliant multimedia tags  

**Authority:** Supporting Document - Reports to instruct_who_would_win

**System Role:** Provides structure and format specifications for Step 4 of episode generation workflow  

**Dependencies:** None (self-contained template)  

**Referenced By:** instruct_who_would_win (Step 4: Episode Structure Building)  

**Integration Reference:** See document_reference_map for complete system architecture

**Change Log - Version 2.0:** January 12, 2025
- Updated all multimedia tag formats to use escaped brackets (\[TAG:\]) for parser compatibility
- Fixed scene header format to use double ## for all scenes including EPISODE METADATA
- Aligned format specifications with tag-fixes.md requirements for automated validation

**Change Log - Version 2.1:** January 12, 2025
- Corrected all example sections to properly show escaped brackets format
- Fixed format in Section 1-8 templates to match parser requirements
- All multimedia tags now properly display as \[TAG:\] in template examples

## AUTOMATION COMPLIANCE TEMPLATE

**CRITICAL**: This template MUST be followed exactly for successful automation. No deviations permitted.

**FORMATTING PRESERVATION RULES FOR AI GENERATION:**
1. **NEVER REMOVE BACKSLASHES** - All multimedia tags MUST retain the backslash escape character: `\[TAG: id\]`
2. **DO NOT SIMPLIFY** - Keep the exact format `\[IMG: id\] PROMPT:` even if it seems redundant
3. **PRESERVE ESCAPING** - The backslash before square brackets is REQUIRED for parser compatibility
4. **EXACT REPLICATION** - Copy the tag format character-for-character: `\[SFX: effect_name\]`
5. **NO MARKDOWN OPTIMIZATION** - Do not let markdown rendering remove the escape characters

**CORRECT FORMAT EXAMPLES:**
- ✅ `\[IMG: cold_open_moment\] PROMPT: "description"`
- ✅ `\[SFX: battle_clash\]`
- ✅ `\[MUSIC: main_theme\]`
- ✅ `\[AMBIENT: forest_sounds\]`
- ✅ `\[TRANSITION: magical_whoosh\]`

**INCORRECT FORMATS (NEVER USE):**
- ❌ `[IMG: cold_open_moment] PROMPT: "description"`
- ❌ `[SFX: battle_clash]`
- ❌ `![image description](prompt)`
- ❌ `<IMG id="cold_open">`

---

## **[SCENE: EPISODE METADATA]**

EPISODE METADATA

- Episode Title: [Monster A] vs. [Monster B]: [Creative subtitle referencing stakes/location]

- Episode Number: [Sequential number in format: 008]

- Rules Version: D&D 2024 (or D&D 5E if needed)

- Battle Location: [Specific Khronexia location with geographic details]

- Featured Monsters: [Monster A Name] (CR [X]) vs. [Monster B Name] (CR [Y])

- Key Sponsors: [2 businesses from Fantasy Business Directory]

- Runtime Estimate: [15-20] minutes

- Content Warnings: [None/Mild fantasy violence/etc.]

---

---

## ENHANCED ASSET TAG EXAMPLES

### **Image Prompt Format Standards**

****Required Format****: `\[IMG: unique_id\] PROMPT: "Detailed description"`

**CRITICAL FOR AI MODELS**: The backslash before the brackets is MANDATORY. Do NOT remove it thinking it's a formatting error.

****Examples****:

\[IMG: cold_open_moment\] PROMPT: "Most dramatic battle moment showing [specific details], cinematic lighting, fantasy art style"

\[IMG: environment_wide\] PROMPT: "Wide establishing shot of [location] with tactical features, atmospheric depth, detailed background"

\[IMG: monster_a_portrait\] PROMPT: "[Monster A] individual showcase in environment, highlighting unique features, menacing presence"

\[IMG: monster_b_portrait\] PROMPT: "[Monster B] individual showcase in environment, contrasting features to Monster A"

\[IMG: battle_key_moment\] PROMPT: "Critical combat moment - [specific action], dynamic poses, magical effects"

\[IMG: battle_climax\] PROMPT: "Most dramatic moment - decisive blow or critical hit, epic composition"

\[IMG: aftermath_scene\] PROMPT: "Battle conclusion showing victor and environmental impact, sense of resolution"

### **Audio Cue Format Standards**

**SFX Format**: `\[SFX: effect_name\]` (lowercase, underscores)

**REMINDER**: The backslash `\` before `[SFX:` is REQUIRED - it's not a typo or markdown artifact.

**Examples**:

\[SFX: battle_start_tension\] \[SFX: weapon_clash_metal\] \[SFX: spell_cast_whoosh\] \[SFX: creature_roar_deep\] \[SFX: footsteps_heavy\] \[SFX: ambient_wind_eerie\] \[SFX: impact_crushing\] \[SFX: creature_death_cry\]

**Music Format**: `\[MUSIC: cue_name\]` (lowercase, underscores)

**Examples**:

\[MUSIC: main_theme_intro\] \[MUSIC: battle_tension_build\] \[MUSIC: dramatic_climax\] \[MUSIC: resolution_peaceful\] \[MUSIC: suspense_ominous\]

### **Thumbnail Format Standard**

**Required Format**: `\[THUMBNAIL\] PROMPT: "Complete description"`

**Example**:

\[THUMBNAIL\] PROMPT: "Epic fantasy battle scene showing [Monster A] vs [Monster B] on left side of image, [environment] background, dramatic lighting, space reserved on right side for text overlay, golden lightning bolt separator, high contrast concept art style suitable for YouTube thumbnail"

**Critical**: Only ONE thumbnail tag per episode, placed at the very end.

### **Asset ID Naming Conventions**

**Best Practices**:

- **Descriptive**: `gorgon_intro` not `monster1`

- **Consistent**: Use same pattern throughout episode

- **Unique**: Never repeat an ID within the same episode

- **Short**: 3-25 characters maximum

- **Format**: lowercase_letters_with_underscores_only

**Good Examples**:

- `cold_open_petrification`

- `environment_badlands_wide`

- `gorgon_charging_attack`

- `wight_life_drain_moment`

- `victory_aftermath_scene`

**Bad Examples**:

- `Image1` (not descriptive)

- `GORGON_INTRO` (capitals not allowed)

- `monster fighting scene` (spaces not allowed)

- `super_long_descriptive_name_that_exceeds_character_limits` (too long)

---

---

## SECTION 1: COLD OPEN (30 seconds)

**PURPOSE**: Hook audience with most dramatic battle moment

```

## **[SCENE: COLD OPEN]**

\[SFX: [Specific dramatic sound from climactic moment]\]

\[IMG: [unique_id]\] PROMPT: "[Detailed description of most dramatic visual moment from battle - critical hit, decisive blow, or dramatic reversal]"

ZARA: [Excited reaction to dramatic moment] "[Direct quote from battle climax showcasing excitement]"

THORAK: [Analytical response] "[Tactical or lore-based observation about the moment]"

[Brief pause for dramatic effect]

ZARA: "I'm Zara Emberclaw—"

THORAK: "—and I'm Thorak Ironquill, and you're listening to Chronicles of Khronexia: Battle Witnessed!"

\[TRANSITION: Magical whoosh effect leading to intro music\]

```

**REQUIREMENTS**:

- Use MOST dramatic moment from upcoming battle

- Avoid spoiling ultimate victor

- Create immediate emotional investment

- Exact host identification format required

---

## SECTION 2: INTRO & HOST BANTER (90 seconds)

**PURPOSE**: Welcome audience and establish episode context

```

## **[SCENE: INTRO & HOST BANTER]**

\[MUSIC: Upbeat fantasy theme music fading to background\]

\[IMG: hosts_intro\] PROMPT: "Thorak (dwarf cleric with beard, robes) and Zara (tiefling with horns, dark clothing) in [current broadcasting location] with scrying stones visible"

THORAK: "Welcome back to Chronicles of Khronexia: Battle Witnessed! I'm Thorak Ironquill, your humble chronicler and battle analyst."

ZARA: "And I'm Zara Emberclaw, bringing you all the excitement, drama, and delicious chaos! This is episode [number], and honey, do we have a treat for you today!"

THORAK: "[Brief personal update or world news relevant to battle location/monsters - 2-3 sentences]"

ZARA: "[Energetic response with street smart perspective - reference to patron whispers or past cons - 2-3 sentences]"

THORAK: "Today, our Scrying Stones take us to [specific location in Khronexia with geographic and tactical details]."

ZARA: "Where we'll witness an epic showdown between [Monster A description] and [Monster B description]! [Excited prediction or observation]"

THORAK: "Indeed. Let's set the stage for what promises to be a most educational encounter."

```

**REQUIREMENTS**:

- Exact welcome phrase

- Episode number reference

- Current location description

- Brief personal updates maintaining character voices

- Battle participant tease without spoiling outcome

---

## SECTION 3: BATTLE SETUP (3 minutes)

**PURPOSE**: Set stage and build tension before combat

```

## **[SCENE: BATTLE SETUP]**

\[AMBIENT: [Environment-specific sounds - wind, forest, cave echoes, etc.]\]

\[IMG: environment_wide\] PROMPT: "Wide establishing shot of [battle location] showing tactical features, lighting, and atmospheric details"

THORAK: "[Detailed environment description with tactical implications - 4-5 sentences covering terrain, weather, obstacles, advantages]"

ZARA: "[Enthusiastic reaction to environment with street-smart observations - 2-3 sentences]"

\[IMG: monster_a_showcase\] PROMPT: "Individual showcase of [Monster A] in environment, highlighting unique features and menacing presence"

THORAK: "Our first combatant: [Full monster name and earned title]. [Physical description highlighting unique features - 3-4 sentences]"

ZARA: "[Colorful commentary on Monster A's appearance and attitude - 2-3 sentences with personality flair]"

THORAK: "[Monster A background - brief but compelling personal history, current motivation for this battle - 3-4 sentences]"

\[IMG: monster_b_showcase\] PROMPT: "Individual showcase of [Monster B] in environment, emphasizing contrasting features to Monster A"

THORAK: "And facing this [Monster A descriptor]: [Full Monster B name and earned title]. [Physical description highlighting unique features - 3-4 sentences]"

ZARA: "[Dramatic commentary on Monster B's presence and demeanor - 2-3 sentences]"

THORAK: "[Monster B background - personal history, stakes for this battle - 3-4 sentences]"

ZARA: "So what do you think, Thorak? [Prediction with reasoning - 2-3 sentences]"

THORAK: "[Counter-analysis with tactical reasoning - 3-4 sentences] My prediction: [clear stance with reasoning]"

ZARA: "Well, let's see who's right! Time to roll initiative!"

\[SFX: dice_rolling\]

Initiative Order:

- [Monster A]: d20 ([roll]) + [modifier] \= [total]

- [Monster B]: d20 ([roll]) + [modifier] \= [total]

THORAK: "[Winner] strikes first. Let the battle begin!"

```

**REQUIREMENTS**:

- Detailed environment with tactical implications

- Full monster introductions with names, titles, descriptions

- Brief but compelling backstories

- Host predictions with clear reasoning

- Initiative roll with proper formatting

- Smooth transition to combat

---

## SECTION 4: ADVERTISEMENT BREAK 1 (30 seconds)

**PURPOSE**: Monetization while maintaining immersion

```

## **[SCENE: ADVERTISEMENT BREAK 1]**

\[MUSIC: light_whimsical_theme\]

\[IMG: sponsor_showcase\] PROMPT: "Product showcase for [Sponsor Business] with fantasy marketplace setting"

\[SPONSOR: Must use business from Fantasy Business Directory Tiers 1-3\]

THORAK: "This epic battle is brought to you by [Sponsor Business Name]!"

ZARA: "[Enthusiastic endorsement with character voice - 2-3 sentences using 'honey/sweetie' and street smart appeal]"

THORAK: "[Product details with MANDATORY PRICING in fantasy currency - MUST include at least 2 specific prices in gold/silver/copper pieces - 2-3 sentences with scholarly tone]"

ZARA: "[Humorous disclaimer or magical side effect - MANDATORY - 1-2 sentences]"

BOTH: "[Business slogan]!"

\[TRANSITION: Brief musical flourish back to battle atmosphere\]

```

**REQUIREMENTS**:

- Use only approved Fantasy Business Directory sponsors

- Maintain character voices throughout

- Include fantasy currency pricing

- Add humorous disclaimers

- 15-20 seconds when read aloud

---

## SECTION 5: BATTLE COMMENTARY (8-10 minutes)

**PURPOSE**: Main event - detailed combat with expert analysis

```

## **[SCENE: BATTLE COMMENTARY]**

\[AMBIENT: battle_environment_sounds\]

\[IMG: battle_opening\] PROMPT: "Both monsters in combat-ready positions, showing the moment before first attack"

THORAK: "The Scrying Stone focuses on the combatants. Let us chronicle this battle!"

**Combatants**: [Monster A] (HP: [max], AC: [X]) vs. [Monster B] (HP: [max], AC: [Y])

**ROUND 1**

**[First Monster]'s Turn (Initiative: [total])**:

ZARA: "[Dramatic description of monster's action/attitude - 2-3 sentences]"

THORAK: "[Tactical analysis of chosen action - 1-2 sentences]"

[Action Name]: [Description of ability/attack]

Attack Roll: d20 ([die result]) + [modifier] \= [total] [HIT/MISS]

[If HIT] Damage: [dice] ([individual results]) + [modifier] \= [total] [damage type] damage

[Target Monster]: HP reduced from [previous] to [new total]

ZARA: "[Reaction to result - excitement, concern, analysis - 1-2 sentences]"

THORAK: "[Technical commentary on mechanics or tactics - 1-2 sentences]"

**[Second Monster]'s Turn (Initiative: [total])**:

[Continue same format for each action]

\[IMG: key_moment\] PROMPT: "[Description of significant combat moment - critical hit, special ability use, tactical maneuver]"

**ROUND 2**

[Continue round structure...]

[Include 3-4 rounds minimum, with dramatic moments and tactical decisions]

\[IMG: battle_climax\] PROMPT: "[Most dramatic moment - usually the decisive blow or critical hit]"

THORAK: "[Final tactical analysis as battle concludes]"

ZARA: "[Emotional reaction to battle conclusion]"

**Battle Conclusion**:

[Winner]: [Final HP/condition]

[Loser]: [Final HP/defeated state]

\[SFX: battle_end_ambience\]

```

**REQUIREMENTS**:

- Round-by-round D&D 2024 mechanics

- All dice rolls with exact formatting: d20 (result) + modifier \= total

- HP tracking throughout

- Host commentary balancing analysis and excitement

- Multiple image prompts for key moments

- Clear victor declaration

---

## SECTION 6: ADVERTISEMENT BREAK 2 (30 seconds)

**PURPOSE**: Second monetization with battle integration

```

## **[SCENE: ADVERTISEMENT BREAK 2]**

\[MUSIC: elegant_sponsor_theme\]

\[IMG: second_sponsor_showcase\] PROMPT: "[Second sponsor] product showcase in fantasy setting"

\[SPONSOR: Different business from Fantasy Business Directory than first ad\]

THORAK: "[Reference to battle event], it reminds me of [Sponsor Business Name]!"

ZARA: "[Connection between battle and product with enthusiasm - 2-3 sentences]"

THORAK: "[Product benefits with scholarly endorsement - MUST include at least 2 specific prices in gold/silver/copper pieces - 2-3 sentences]"

ZARA: "[Playful warning or side effect - MANDATORY disclaimer - 1-2 sentences]"

BOTH: "[Business slogan]!"

\[TRANSITION: Return to aftermath atmosphere\]

```

**REQUIREMENTS**:

- Different sponsor from first break

- Reference current battle events

- Same format requirements as first ad

---

## SECTION 7: AFTERMATH ANALYSIS (2 minutes)

**PURPOSE**: Educational wrap-up and consequences

```

## **[SCENE: AFTERMATH ANALYSIS]**

\[AMBIENT: calm_reflective_music\]

\[IMG: aftermath_scene\] PROMPT: "Wide shot showing battle site with aftermath - victor's position, environmental damage, sense of conclusion"

THORAK: "[Clear victor declaration and final state of both combatants - 2-3 sentences]"

ZARA: "[Emotional reaction to outcome and respect for both combatants - 2-3 sentences]"

THORAK: "Let us analyze the key moments that decided this battle. [Tactical breakdown of 2-3 decisive moments with specific rounds/actions referenced]"

ZARA: "[What the loser could have done differently - 2-3 sentences with street-smart perspective]"

THORAK: "[Lessons for adventurers - 3-4 sentences about broader tactical principles demonstrated]"

ZARA: "[Consequences in Khronexia world - what happens to winner/loser, environmental impact - 2-3 sentences]"

THORAK: "[Connection to broader monster lore or world events - 2-3 sentences]"

ZARA: "Another incredible battle for the chronicles!"

```

**REQUIREMENTS**:

- Clear victor and final states

- Tactical analysis of key moments

- Educational value for D&D players

- World-building consequences

- Smooth transition to outro

---

## SECTION 8: OUTRO & NEXT EPISODE TEASE (60 seconds)

**PURPOSE**: Professional conclusion and audience retention

```

## **[SCENE: OUTRO & NEXT EPISODE TEASE]**

\[MUSIC: main_theme_outro\]

\[IMG: hosts_farewell\] PROMPT: "Thorak and Zara in broadcast location, waving goodbye with scrying stones glowing in background"

THORAK: "And so concludes another chronicle of legendary combat. Thank you to our sponsors, [Sponsor 1] and [Sponsor 2]."

ZARA: "And thank you to all our amazing listeners! Your support keeps the Scrying Stones glowing!"

THORAK: "Next time on Chronicles of Khronexia..."

ZARA: "[Brief, exciting description of next battle without spoiling outcome - featuring two different monsters with CR balance - 2-3 sentences building anticipation]"

THORAK: "Will [Monster A capability] prove stronger than [Monster B capability]?"

ZARA: "Find out next week as we witness another legendary battle!"

THORAK: "Until then, I'm Thorak Ironquill—"

ZARA: "—and I'm Zara Emberclaw!"

BOTH: "Stay safe, and watch the skies!"

\[MUSIC: theme_music_swell\]

\[SFX: scrying_stone_powerdown\]

```

**REQUIREMENTS**:

- Thank sponsors by name

- Next episode tease with new monsters (different from current episode)

- CR-balanced monster preview (1-3 level difference)

- Signature sign-off format

- No outcome spoilers in tease

---

## TECHNICAL VALIDATION CHECKLIST

**STRUCTURE COMPLIANCE**:

- [ ] All 8 sections present with exact headers

- [ ] Episode Metadata header included

- [ ] Timing estimates for each section

- [ ] Total runtime 15-20 minutes

**CONTENT COMPLIANCE**:

- [ ] Cold Open uses dramatic moment from battle

- [ ] Both monsters from official D&D 2024 Monster Manual

- [ ] CR difference 1-3 levels maximum

- [ ] All dice rolls in proper format: d20 (result) + modifier \= total

- [ ] No mathematical notation ($, $$, etc.)

- [ ] Sponsors from approved Fantasy Business Directory only

**PRODUCTION COMPLIANCE**:

- [ ] Minimum 7 IMG prompts with unique IDs using \[IMG: id\] PROMPT: format
  - **AI GENERATION NOTE**: Keep the backslash before brackets - it's required, not optional

- [ ] Minimum 15 audio cues \[SFX\], \[MUSIC\], \[AMBIENT\] using snake_case format
  - **AI GENERATION NOTE**: All audio tags must have backslash escaping: `\[SFX:]` not `[SFX:]`

- [ ] Single \[THUMBNAIL\] PROMPT: tag for episode thumbnail
  - **AI GENERATION NOTE**: Even thumbnail tags need escaping: `\[THUMBNAIL\]`

- [ ] Character voices consistent throughout

- [ ] Next episode tease includes new monster matchup

- [ ] Episode asset manifest present at end (YAML format)

**AUTOMATION COMPLIANCE**:

- [ ] Ready for voice synthesis (clear speaker attribution)

- [ ] Ready for image generation (all IMG tags have unique IDs)

- [ ] Ready for audio production (all SFX/MUSIC use snake_case)

- [ ] Ready for thumbnail generation (single THUMBNAIL tag present)

- [ ] Asset manifest matches all tags used in episode

- [ ] No human intervention required for content completion

---

## FAILURE CONDITIONS

**AUTOMATIC REGENERATION REQUIRED IF**:

- Missing any of 8 required sections

- Cold Open absent or malformed

- Non-existent monsters referenced

- CR violations (\>3 level difference)

- Unapproved sponsors used

- Mathematical notation in dice rolls

- Missing next episode tease

- Insufficient image prompts (\<7)

- Runtime outside 15-20 minute range

---

---

## MANDATORY: EPISODE ASSET MANIFEST

Every episode MUST conclude with this YAML block for automation:

```yaml

episode_assets:

  metadata:

    episode_number: "[NUMBER]"

    title: "[TITLE]"

    runtime_estimate: "[X] minutes"

    monsters: ["[MONSTER_A]", "[MONSTER_B]"]

    location: "[KHRONEXIA_LOCATION]"


  voices:

    - speaker: "THORAK"

      voice_id: "thorak_dwarf_cleric"

    - speaker: "ZARA"

      voice_id: "zara_tiefling_warlock"


  sfx_required: [List all unique SFX tags used]


  music_cues: [List all unique MUSIC tags used]


  image_prompts:

    - id: "[ID]"

      prompt: "[FULL_PROMPT_TEXT]"

    [Repeat for all IMG tags]


  thumbnail:

    prompt: "[COMPLETE_THUMBNAIL_PROMPT]"

CRITICAL REQUIREMENTS:

Asset manifest must accurately reflect all tags used in episode

All IMG IDs must be unique within the episode

SFX/MUSIC lists must include every tag used

Thumbnail prompt must match the single [THUMBNAIL] tag

YAML syntax must be valid for automated parsing

VALIDATION:

 Episode asset manifest present at end

 All referenced IDs match tags used in episode

 No duplicate asset IDs

 YAML syntax is valid

 All asset categories populated correctly

