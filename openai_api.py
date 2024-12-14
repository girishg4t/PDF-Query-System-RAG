import openai
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

# Retrieve the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError(
        "OpenAI API key is not set. Please add it to the .env file.")


def generate_embeddings(texts):
    openai.api_key = openai_api_key
    response = openai.Embedding.create(
        model="text-embedding-ada-002",  # You can replace with another model if necessary
        input=texts
    )
    # Extract embeddings from the response
    embeddings = response['data'][0]['embedding']  # This is already flat
    return embeddings


def generate_embeddings_list(text_list):
    """
    Generate embeddings for a list of text chunks.
    :param text_list: List of strings to embed.
    :return: List of embeddings.
    """
    embeddings = []
    try:
        for text in text_list:
            response = openai.Embedding.create(
                input=text,
                model="text-embedding-ada-002"
            )
            embeddings.append(response["data"][0]["embedding"])
    except Exception as e:
        print(f"Error generating embeddings: {e}")
    return embeddings
