import json
from typing import Dict

from letta_client import Letta

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

Respond in the EXACT format below:

SUMMARY:
(Write a clear 2–3 paragraph summary of overall SEO quality, strengths,
weaknesses, and impact on search visibility and user experience.)

RECOMMENDATIONS:
(List 3–5 actionable improvements as bullet points.
Each bullet should describe what to fix and why it matters.)


"""


class LettaClient:

    def __init__(self, apiKey, environment, agentName, model):
        self.client = Letta(api_key=apiKey, environment=environment)
        self.agent = self._create_seo_agent(agent_name=agentName, model=model)

    def _create_seo_agent(self, agent_name, model):
        """
        Create a Letta agent specialized in on-page SEO analysis
        """

        agent = self.client.agents.create(
            name=agent_name,
            model=model,
            memory_blocks=[
                {
                    "label": "persona",
                    "value": PERSONA,
                }
            ],
        )

        return agent

    def analyze_audit(self, audit_data: Dict) -> dict:
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

        response = self.client.agents.messages.create(
            agent_id=self.agent.id, messages=[{"role": "user", "content": prompt}]
        )
        summary, recommendations = self._extract_assistant_output(response)

        return {
            "summary": summary,
            "recommendations": recommendations,
        }

    @staticmethod
    def _extract_assistant_output(response) -> tuple[str, list[str]]:
        """
        Extract summary and recommendations from Letta response.
        """

        full_text = []

        for message in response.messages:
            if message.message_type == "assistant_message":
                full_text.append(message.content)

        text = "\n".join(full_text).strip()

        summary = ""
        recommendations: list[str] = []

        if "RECOMMENDATIONS:" in text:
            summary_part, rec_part = text.split("RECOMMENDATIONS:", 1)

            summary = summary_part.replace("SUMMARY:", "").strip()

            for line in rec_part.splitlines():
                line = line.strip()
                if line.startswith("-"):
                    recommendations.append(line.lstrip("- ").strip())
        else:
            # Fallback: everything is summary
            summary = text

        return summary, recommendations
