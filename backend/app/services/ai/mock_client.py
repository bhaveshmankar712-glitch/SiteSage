class MockClient:
    """
    Mock AI client used when AI_MODE=mock.
    Returns deterministic, human-readable output.
    """

    def analyze_audit(self, audit_data: dict) -> dict:
        return {
            "summary": (
                "The website has a basic SEO structure but several on-page issues "
                "are limiting its search visibility."
            ),
            "recommendations": [
                "Add missing meta descriptions to improve click-through rates",
                "Fix image alt attributes to improve accessibility",
                "Review heading structure to ensure a single H1 tag",
            ],
        }
