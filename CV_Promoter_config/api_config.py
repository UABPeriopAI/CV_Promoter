from pathlib import Path

from langchain.chat_models import ChatOpenAI
from langchain_openai import AzureChatOpenAI

NAME = "cv"


# END points
AZURE_END_POINT = "https://nlp-ai-svc.openai.azure.com"
OPENAI_END_POINT = "https://api.openai.com/v1/engines"

REVIEW_TABLE_NAME = "review_drafter"
NARRATIVE_TABLE_NAME = "narrative_drafter"
LETTER_TABLE_NAME = "letter_drafter"

AZURE_CHAT_CONFIG = AzureChatOpenAI(
    azure_endpoint=AZURE_END_POINT,
    openai_api_version="2024-02-01",
    deployment_name="ChatGPT4",
    openai_api_type="azure",
    temperature=0.5,
    model_name="gpt-4",
)

OPENAI_CHAT_CONFIG = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo", request_timeout=300)
