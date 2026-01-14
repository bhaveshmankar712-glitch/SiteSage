from app.core.config import settings
from app.services.ai.mock_client import MockClient
from app.services.ai.letta_client import LettaClient


def get_ai_client():
    if settings.AI_MODE == "letta":
        return LettaClient(
            apiKey=settings.LETTA_API_KEY.get_secret_value(),
            environment=settings.LETTA_ENVIRONMENT,
            agentName=settings.LETTA_AGENT_NAME,
            model=(
                settings.LETTA_MODEL_CLOUD
                if settings.LETTA_ENVIRONMENT == "cloud"
                else settings.LETTA_MODEL_LOCAL
            ),
        )

    # default = mock
    return MockClient()
