import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "genshin_character_builds.json"), "r", encoding="utf-8") as f:
    builds = json.load(f)

# Map character names to builds (case-insensitive)
build_dict = {b['name'].lower(): b for b in builds}

# Initialize main window
#root = tk.Tk()

def get_build_info(char_name):
    """Return a formatted build string for a character"""
    char_name_lower = char_name.lower()
    if char_name_lower in build_dict:
        data = build_dict[char_name_lower]
        weapons = ', '.join(data.get('weapons', [])) or 'N/A'
        artifacts = ', '.join(data.get('artifacts', [])) or 'N/A'
        talents = data.get('talents', {})
        talent_priority = ', '.join(talents.get('priority_order', [])) or 'N/A'

        response = (
            f"🧍 Name: {data.get('name','N/A')}\n"
            f"⚔️ Role: {data.get('role','N/A')}\n"
            f"🗡 Weapons: {weapons}\n"
            f"🛡 Artifacts: {artifacts}\n"
            f"📜 Talent Priority: {talent_priority}\n"
        )
        return response
    else:
        return "Sorry, I couldn't find that character. Please check the spelling."


