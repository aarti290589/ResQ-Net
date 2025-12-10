def get_mission_plan(summary):
    try:
        # ATTEMPT 1: REAL AI (Nemotron)
        llm = ChatNVIDIA(
            base_url="http://localhost:8000/v1", 
            model="nvidia/nemotron-nano-9b-v2", 
            api_key="dummy", 
            temperature=0.1,
            timeout=5
        )
        # We tell it to be strict
        msg = f"Situation: {summary}. Return ONLY a JSON object with fields 'priority', 'assets', 'note'. Do not add conversational text."
        response = llm.invoke([HumanMessage(content=msg)])
        
        content = response.content
        
        # CLEANUP: Find the JSON part inside the text
        if "{" in content and "}" in content:
            start = content.find("{")
            end = content.rfind("}") + 1
            clean_json = content[start:end]
            return clean_json, "⚡ Nemotron-9B (Real)"
            
        return content, "⚡ Nemotron-9B (Real)"
        
    except Exception as e:
        # FAILSAFE
        priority = "CRITICAL" if "injured" in summary else "Medium"
        asset = "Rescue Boat" if "survivor" in summary else "Drone Scout"
        
        fallback_json = json.dumps({
            "priority": priority,
            "assets": [asset],
            "note": f"Automated Response: {summary}"
        }, indent=2)
        return fallback_json, "⚠️ Emergency Protocol (Backup)"
