import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    aws_region: str = os.getenv("AWS_REGION", "us-east-1")
    bedrock_model_id: str | None = os.getenv("BEDROCK_MODEL_ID")
    vertex_ai_project: str | None = os.getenv("VERTEX_AI_PROJECT")
    neo4j_uri: str | None = os.getenv("NEO4J_URI")
    neo4j_username: str | None = os.getenv("NEO4J_USERNAME")
    neo4j_password: str | None = os.getenv("NEO4J_PASSWORD")
    pinecone_api_key: str | None = os.getenv("PINECONE_API_KEY")
    pinecone_index_name: str | None = os.getenv("PINECONE_INDEX_NAME")


settings = Settings()
