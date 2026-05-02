from openai import OpenAI
import json

client = OpenAI()

def analyze_with_gpt4o(inspection_text, thermal_text, inspection_images, thermal_images):
    # Caption key thermal images using vision
    thermal_captions = []
    for img in thermal_images[:8]:  # limit for cost
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this thermal image in context of building dampness/leakage. Note temperatures and anomalies."},
                    {"type": "image_url", "image_url": {"url": f"data:image/{img['ext']};base64,{base64.b64encode(img['bytes']).decode()}"}}
                ]
            }]
        )
        thermal_captions.append(response.choices[0].message.content)

    # Main structured generation
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.1,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT + "\n" + JSON_SCHEMA},
            {"role": "user", "content": f"Inspection Report:\n{inspection_text[:12000]}\n\nThermal Report:\n{thermal_text[:8000]}\n\nThermal Image Analysis:\n{thermal_captions}"}
        ]
    )
    try:
        return json.loads(response.choices[0].message.content)
    except:
        return {"error": "JSON parsing failed", "raw": response.choices[0].message.content}