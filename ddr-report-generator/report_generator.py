from groq import Groq
import json
from templates import SYSTEM_PROMPT, JSON_SCHEMA

# ============== CHANGE HERE ==============
client = Groq(api_key="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")   # ← Paste your Groq key
# ========================================

def generate_ddr(insp_data, therm_data):
    inspection_text = insp_data.get("raw_text", "")
    thermal_text = therm_data.get("raw_text", "")

    prompt = f"""
Inspection Report:
{inspection_text[:14000]}

Thermal Report:
{thermal_text[:7000]}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        messages=[
            {"role": "system", "content": f"{SYSTEM_PROMPT}\n\n{JSON_SCHEMA}"},
            {"role": "user", "content": prompt}
        ]
    )
    
    try:
        return json.loads(response.choices[0].message.content)
    except:
        return None