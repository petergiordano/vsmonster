# Rule: Project Initialization Wizard

## Goal

To guide an AI assistant in conducting a structured interview with the user to populate all four initial project context documents (`Roadmap.md`, `VibeTesting.md`, `ComponentLibrary.md`, and `SLC_Session_Notes.md`) plus generate a project-specific `AI_CONTEXT.md` file. This process transforms blank templates into comprehensive project foundations through systematic questioning.

## Process Overview

1. **Introduction:** Explain the initialization process to the user
2. **Plan Mode Setup (if using Claude Code CLI):** Enter Plan Mode for safe context gathering
3. **Structured Interview:** Ask questions in five phases, one for each document
4. **Generate Documents:** Create populated versions of all four template files plus AI_CONTEXT.md
5. **Review & Refinement:** Allow user to request adjustments

## Claude Code Plan Mode Integration

When using Claude Code CLI for project initialization, leverage Plan Mode for enhanced safety and analysis:

### **Recommended Plan Mode Workflow:**

1. **Enter Plan Mode:** Press Shift+Tab twice at the start of the initialization process
2. **Safe Context Gathering:** 
   - Read any existing project files or documentation
   - Examine directory structure and existing patterns
   - Review any configuration files or dependencies
3. **Conduct Interview:** Ask all five phases of questions while in Plan Mode
4. **Analysis Phase:** Use the gathered information to understand the project scope and requirements
5. **Exit Plan Mode:** After completing the interview, exit Plan Mode (Shift+Tab) to begin document generation
6. **Generate Documents:** Create all five populated documents

### **Benefits of Using Plan Mode for Initialization:**

- **No Accidental Changes:** Safely explore existing project structure without modifications
- **Comprehensive Analysis:** Take time to understand any existing codebase or project context
- **Better Questions:** More informed follow-up questions based on discovered project details
- **Informed Document Generation:** Documents that better reflect the actual project structure and needs

### **Plan Mode Best Practices for Initialization:**

- **Explore Existing Files:** Use Plan Mode to read any existing README, package.json, or configuration files
- **Understand Dependencies:** Review existing tech stack choices and constraints
- **Check Project Structure:** Understand how the project is organized before making recommendations
- **Research Standards:** Look up best practices for the chosen tech stack during the interview process

## Phase Structure

### **Phase A: Project Vision & Strategy (→ Roadmap.md)**
Ask these questions to understand the project's core purpose and technical approach:

1. **Project Name:** "What's your project name?"
2. **Vision Statement:** "Describe your project in 1-2 sentences. What does it do and for whom?"
3. **Problem & Goals:** "What specific problem are you solving? What are 3-5 measurable goals that would define success?"
4. **Target Users:** "Who is your primary user? What's their current situation and desired outcome?"
5. **Technical Approach:** "What's your preferred tech stack? (Frontend, backend, database, key libraries)"
6. **Constraints & Risks:** "What are your biggest constraints (time, budget, technical complexity)? What could derail this project?"
7. **User Stories:** "Can you give me 3-5 user stories in the format: 'As a [user], I want to [action] so that [benefit]'?"

### **Phase B: User Experience & Emotional Design (→ VibeTesting.md)**
Ask these questions to define the emotional journey and user experience:

1. **Core Vibe:** "In 1-2 sentences, describe the overall feeling your app should evoke. How should users feel when using it?"
2. **Emotional Journey:** "Walk me through a user's emotional journey from first impression to success. What should they feel at each key moment?"
3. **Vibe Killers:** "What would completely ruin the experience? What friction points or design choices would break the vibe you're aiming for?"
4. **Success Emotions:** "When a user successfully completes their main task, what specific emotion should they feel? (achievement, relief, delight, etc.)"
5. **Inspiration:** "Are there any apps, websites, or experiences that capture the vibe you're aiming for?"

### **Phase C: Design System & Visual Identity (→ ComponentLibrary.md)**
Ask these questions to establish the visual and design foundation:

1. **Design Philosophy:** "How would you describe your design approach? (minimal, playful, professional, bold, etc.)"
2. **Brand Colors:** "Do you have existing brand colors or color preferences? If not, what mood should your colors convey?"
3. **Typography Style:** "What style of typography fits your project? (modern sans-serif, classic serif, playful, technical, etc.)"
4. **Key Components:** "What UI components do you know you'll need? (buttons, forms, cards, navigation, etc.)"
5. **Visual References:** "Any design inspiration or existing sites/apps whose visual style you admire?"

### **Phase D: First Sprint Planning (→ SLC_Session_Notes.md)**
Ask these questions to plan the initial development sprint:

1. **Core Feature:** "What's the single most important feature to build first? What's the core value proposition?"
2. **Must-Have vs Nice-to-Have:** "For this first feature, what's absolutely essential vs what would be nice but not critical?"
3. **Simplicity Focus:** "How will you keep this feature simple? What's the minimum that would still be valuable?"
4. **Delightful Touch:** "What's one small detail that could make this feature delightful or memorable?"
5. **Completeness Definition:** "How will you know this feature is truly complete? What would make a user say 'this works exactly as I expected'?"

## Interview Guidelines

### **Questioning Approach:**
- **Start with Plan Mode (if using Claude Code CLI):** Begin in Plan Mode to safely explore existing project context
- Ask questions one phase at a time
- Wait for complete answers before moving to the next phase
- Ask follow-up questions if answers are too vague or brief
- Encourage specific, concrete responses over abstract concepts
- If a user seems stuck, provide 2-3 example options to help them think
- **Use existing project context:** If Plan Mode reveals existing files or patterns, reference them in your questions

### **Tone & Style:**
- Be conversational and encouraging
- Frame questions as collaborative exploration, not interrogation
- Acknowledge good insights and build on their ideas
- Help users think through implications of their choices

### **Phase E: Technical Foundation & AI Context (→ AI_CONTEXT.md)**
Ask these questions to establish the technical conventions and AI briefing context:

1. **Programming Language:** "What's your primary programming language and version? (e.g., Python 3.11, TypeScript)"
2. **Code Formatting:** "What formatting tools do you use? (e.g., black for Python, prettier for JS/TS)"
3. **Naming Conventions:** "What naming conventions do you follow? (e.g., snake_case, camelCase, PascalCase)"
4. **File Structure:** "How do you organize your code? (e.g., /src for source, /tests for tests, component organization)"
5. **Error Handling:** "What's your approach to error handling? (e.g., try/catch patterns, error logging)"
6. **Dependencies Policy:** "How do you handle new libraries/packages? (approval process, restrictions)"
7. **Testing Requirements:** "What testing approach do you use? (unit tests required, testing frameworks)"

## Document Generation

After completing all five phases, generate the populated documents using this approach:

### **For Each Document:**
1. **Use the original template structure** from the `.project-docs/` files and `AI_CONTEXT.md` template
2. **Replace all placeholder text** with user's specific answers
3. **Maintain the formatting and sections** of the original templates
4. **Add rich detail** beyond just the direct answers - interpret and expand thoughtfully
5. **For AI_CONTEXT.md specifically:** Populate the Plan Mode best practices with project-specific guidance based on the tech stack, complexity, and requirements gathered during the interview

### **Output Format:**
Present each completed document clearly:

```markdown
## Generated Document: Roadmap.md

[Full populated content here]

---

## Generated Document: VibeTesting.md

[Full populated content here]

---

## Generated Document: ComponentLibrary.md

[Full populated content here]

---

## Generated Document: SLC_Session_Notes.md

[Full populated content here]

---

## Generated Document: AI_CONTEXT.md

[Full populated content synthesizing information from all previous documents]

```

## Quality Assurance

Before presenting the final documents:

1. **Completeness Check:** Ensure no template sections are left unfilled
2. **Consistency Check:** Verify that details across documents align and support each other
3. **Specificity Check:** Confirm that vague placeholders have been replaced with concrete, actionable content
4. **User Voice Check:** Ensure the content reflects the user's actual vision, not generic startup language
5. **Plan Mode Integration Check:** Verify that AI_CONTEXT.md includes project-specific Plan Mode guidance that reflects the actual tech stack, complexity level, and critical areas identified during the interview

## Refinement Process

After presenting the generated documents:

1. **Ask for feedback:** "Which sections need adjustment or don't quite capture your vision?"
2. **Offer targeted updates:** Focus on specific sections rather than regenerating entire documents
3. **Confirm completion:** Once satisfied, remind user to save these documents in their `.project-docs/` directory

## Final Instructions

- **Use Plan Mode for safe exploration** when using Claude Code CLI
- Complete all five phases before generating any documents
- Don't rush through questions - depth is more valuable than speed
- If a user's project idea is unclear, help them clarify it before proceeding
- **Leverage existing project context** discovered in Plan Mode to ask more informed questions
- Remember: these documents become the foundation for all future AI interactions on this project