#!/usr/bin/env python3
"""
PRD Auto-Update Script

Syncs Notion task completion with PRD.md component status.
Called by @finalize-task and @update-prd commands.
"""

import json
import re
from datetime import datetime
from pathlib import Path


def get_component_progress(notion_tasks):
    """Calculate component completion from Notion tasks."""
    components = {
        1: {"range": (1, 6), "name": "Script Parser", "status": "COMPLETE"},
        2: {"range": (31, 39), "name": "Voice Generation", "status": "IN PROGRESS"},
        3: {"range": (40, 49), "name": "Audio Assembly", "status": "PLANNED"},
        4: {"range": (50, 59), "name": "Static Video", "status": "PLANNED"},
        5: {"range": (60, 79), "name": "Advanced Features", "status": "PLANNED"}
    }
    
    progress = {}
    for comp_id, comp_info in components.items():
        start, end = comp_info["range"]
        component_tasks = [t for t in notion_tasks 
                          if start <= t.get("task_id", 0) <= end]
        
        if component_tasks:
            completed = len([t for t in component_tasks if t.get("status") == "Done"])
            total = len(component_tasks)
            progress[comp_id] = {
                "name": comp_info["name"],
                "completed": completed,
                "total": total,
                "status": "COMPLETE" if completed == total else comp_info["status"]
            }
    
    return progress


def update_prd_status(progress, prd_path):
    """Update PRD.md component status section."""
    with open(prd_path, 'r') as f:
        content = f.read()
    
    # Generate new status section
    timestamp = datetime.now().strftime("%Y-%m-%d")
    status_lines = [f"### Component Status (Auto-Updated: {timestamp})"]
    
    for comp_id, comp_data in progress.items():
        if comp_data["status"] == "COMPLETE":
            emoji = "✅"
            desc = f"{comp_data['name']} validated"
        elif comp_data["status"] == "IN PROGRESS":
            emoji = "🚧" 
            desc = f"({comp_data['completed']}/{comp_data['total']} tasks) - {comp_data['name']}"
        else:
            emoji = "📝"
            desc = f"PLANNED - {comp_data['name']}"
            
        status_lines.append(f"- **Component {comp_id}**: {emoji} {desc}")
    
    new_status = "\n".join(status_lines)
    
    # Replace existing status section
    pattern = r"### Component Status \(Auto-Updated:.*?\n(?:- \*\*Component.*?\n)*"
    content = re.sub(pattern, new_status + "\n", content)
    
    with open(prd_path, 'w') as f:
        f.write(content)
    
    return f"Updated {len(progress)} components in PRD.md"


if __name__ == "__main__":
    # Example usage - would be called by Claude commands
    prd_path = Path("docs/specifications/PRD.md")
    
    # Mock Notion data - in real usage, this comes from Notion API
    mock_tasks = [
        {"task_id": 31, "status": "Critical"},
        {"task_id": 32, "status": "Done"},
        {"task_id": 33, "status": "New"}
    ]
    
    progress = get_component_progress(mock_tasks)
    result = update_prd_status(progress, prd_path)
    print(result)
