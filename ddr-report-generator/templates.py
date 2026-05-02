SYSTEM_PROMPT = """You are an expert civil engineer creating professional Detailed Diagnostic Reports (DDR).
- Only use information present in the documents.
- Write "Not Available" if information is missing.
- Use simple, client-friendly language."""

JSON_SCHEMA = """Return only valid JSON with this structure:
{
  "property_issue_summary": "One paragraph summary",
  "area_wise_observations": [
    {
      "area": "Hall / Bedroom etc",
      "observation": "description",
      "thermal_findings": "thermal correlation",
      "severity": "High/Medium/Low"
    }
  ],
  "probable_root_cause": "string",
  "severity_assessment": {"level": "High/Medium/Low", "reasoning": "string"},
  "recommended_actions": ["action1", "action2"],
  "additional_notes": "string",
  "missing_information": ["item1", "item2"]
}"""