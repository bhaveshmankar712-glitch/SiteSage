from letta_client import Letta
from typing import Dict

import json

PERSONA = """
You are an expert on-page SEO analyst.

You specialize in:
- Title tags and meta descriptions
- Heading structure (H1, H2)
- Image alt text and accessibility
- Page speed and basic performance signals
- Web accessibility best practices

Your response rules:
1. Write a clear 2–3 paragraph SEO quality summary
2. Provide 3–5 actionable improvements
3. Prioritize fixes by SEO impact and ease of implementation
4. Keep recommendations practical and measurable
"""


PROMPT = """Analyze the following on-page SEO audit data.

Your task:

1. **SEO Quality Summary** (2–3 paragraphs):
   - Overall SEO health
   - Strengths and weaknesses
   - Impact on search visibility and user experience

2. **3–5 Actionable Improvements**:
   For each improvement include:
   - What to fix
   - Why it matters for SEO
   - Expected impact (High / Medium / Low)

"""


client = Letta(
    api_key="YOUR_API_KEY",
    environment="cloud",
)

agent = client.agents.create(
    name="test-agent-sitesage",
    model="openai/gpt-4o-mini",
    memory_blocks=[
        {
            "label": "persona",
            "value": PERSONA,
        }
    ],
)
audit_data = {
    "url": "https://example.com",
    "seo_score": 82,
    "issues": ["Missing meta description", "2 images missing alt attributes"],
    "metrics": {
        "title": "Example Domain",
        "h1_count": 1,
        "h2_count": 0,
        "images_missing_alt": 2,
    },
}


def analyze_audit(audit_data: Dict) -> str:
    """
    Send SEO audit data to Letta agent and return AI-generated analysis
    """

    prompt = f"""
            {PROMPT}

            Audit Data (JSON):
            ```json
            {json.dumps(audit_data, indent=2)}
            ```
            Focus only on issues supported by the data.
            Avoid generic SEO advice.
        """

    response = client.agents.messages.create(
        agent_id=agent.id, messages=[{"role": "user", "content": prompt}]
    )
    outputs = []

    for message in response.messages:
        if message.message_type == "assistant_message":
            outputs.append(message.content)

    return "\n\n".join(outputs).strip()


result = analyze_audit(audit_data)
