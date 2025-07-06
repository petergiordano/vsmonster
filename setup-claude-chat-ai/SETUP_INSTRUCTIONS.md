# Claude Project Setup Instructions

## Creating the Chat Assistant - Strategist Claude Project

### 1. **Create New Claude Project**
1. Go to Claude.ai
2. Click "Create Project" 
3. Name: "AI-Assisted Development - Chat Assistant (Strategist)"
4. Description: "Strategic AI collaborator for structured, context-rich software development workflow"

### 2. **Add Project Instructions & Knowledge**

**Project Instructions (Main System Prompt):**
- Copy the entire contents of `PROJECT_INSTRUCTIONS.md` and paste as Project Instructions
- This defines the Chat AI's role, behavior, and response patterns

**Project Knowledge (Reference Documents):**
- Upload `../AI_CONTEXT.md` - Master briefing template structure
- Upload `../_project-scaffolding/.ai-rules/01_create-prd.md` - PRD creation rules
- Upload `../_project-scaffolding/.ai-rules/02_generate-tasks.md` - Task generation rules
- Upload `../WORKFLOW_GUIDE.md` - Complete workflow documentation
- **Add GitHub Repository** - Connect your current coding project repository for live project context

**Optional Project Knowledge (For Advanced Context):**
- Upload `../_project-scaffolding/.project-docs/Roadmap.md` - Project planning template
- Upload `../_project-scaffolding/.project-docs/VibeTesting.md` - UX planning template

### 3. **Project Configuration**
- **Knowledge Limit:** This project requires substantial context, so monitor knowledge usage
- **Update Strategy:** Update project knowledge as the template evolves
- **Context Engineering:** The project is designed to accumulate and transfer context effectively

### 4. **Testing the Enhanced Project**

**Test Conversation 1: Session Start**
```
User: "Working on my-awesome-app"

Expected Response: 
- Loads context from GitHub repository
- Shows project status from AI_CONTEXT.md
- Confirms current workflow stage and active features
- Asks what to work on in this session
```

**Test Conversation 2: Strategic Work**
```
User: "I need to build a user authentication system. Help me think through the requirements."

Expected Response: 
- References current project context from repository
- Strategic analysis with architectural considerations
- Comprehensive CLI AI prompt preparation
```

**Test Conversation 3: Session Bridging**
```
User: "I'm running out of context window. Please provide a summary to continue in a new session."

Expected Response:
- SESSION BRIDGE SUMMARY with all key elements
- Clear instructions for next session startup
- Status of AI_CONTEXT.md and any needed updates
```

### 5. **Enhanced Usage Instructions**

**For Project Users:**

**Starting a New Session:**
1. **Simple Project ID:** Say "Working on [PROJECT_NAME]"
2. **Automatic Context Loading:** Chat Assistant reads current state from GitHub repository
3. **Validation & Planning:** Receive project status and choose session focus
4. **Strategic Work:** Full context-aware strategic analysis and CLI AI prompt preparation

**During Sessions:**
1. **Rich Context Awareness:** Chat Assistant understands current project state automatically
2. **Strategic Planning:** Get architectural guidance and implementation strategies
3. **CLI AI Preparation:** Receive comprehensive prompts for CLI AI execution
4. **Context Evolution:** Get recommendations for AI_CONTEXT.md updates

**Ending Sessions:**
1. **Session Bridge Request:** Say "I'm running out of context" or "Provide session summary"
2. **Comprehensive Summary:** Receive SESSION BRIDGE SUMMARY with all key information
3. **Next Session Setup:** Clear instructions for continuing work
4. **Context Continuity:** Seamless transition to new chat session

**For Template Maintainers:**
1. **Static Knowledge Management:** Update project knowledge when template files change
2. **Repository Integration:** Ensure GitHub repository access provides live project context
3. **Session Pattern Monitoring:** Track effectiveness of session bridging patterns
4. **Context Engineering Refinement:** Improve context accumulation and transfer approaches

---

## Project Benefits

### For Individual Users
- **🎯 Perfect Context Transfer:** CLI AI receives comprehensive context for flawless execution
- **⚡ Faster Development:** Strategic thinking separated from tactical implementation
- **🔄 Learning Accumulation:** Project knowledge builds systematically over time
- **🛡️ Quality Assurance:** Built-in validation and architectural guidance

### For the Template Ecosystem
- **📈 User Success:** Higher success rates with structured AI collaboration
- **🔧 Workflow Optimization:** Clear role boundaries and smooth handoffs
- **🧠 Context Engineering:** Advanced context accumulation and transfer patterns
- **📊 Scalable Development:** Framework that grows with project complexity

## Maintenance Notes

- **Knowledge Updates:** Sync with template changes quarterly or when major enhancements are made
- **Context Pattern Refinement:** Monitor and improve context engineering approaches
- **Role Boundary Optimization:** Refine the balance between strategic and tactical AI roles
- **Success Metric Tracking:** Monitor user outcomes and template effectiveness
