from db.db_connection import execute_query, insert_query
from openai_api import generate_embeddings
from fastapi import HTTPException


def get_matches(sentence, limit):
    embeddings = generate_embeddings([sentence])
    query_embedding_str = "[" + ",".join(map(str, embeddings)) + "]"
    # Convert the embedding list to a string representation that PostgreSQL can use
    # Query to find similar embeddings using cosine similarity
    query = """
        SELECT sentence, embedding <-> %s AS distance
        FROM sentences_new
        ORDER BY distance
        LIMIT %s;
    """
    results = execute_query(query, (query_embedding_str, limit))

    return results if results else []


def insert_all_sentences(sentences):
    # Generate embeddings for the sentences
    embeddings = generate_embeddings(sentences)
    # Insert sentences and their embeddings into the PostgreSQL database

    """
    Insert multiple sentences and their embeddings into the database.
    :param sentences: List of sentences.
    :param embeddings: List of embedding vectors.
    """
    query = "INSERT INTO sentences_new (sentence, embedding) VALUES (%s, %s);"
    for sentence, embedding in zip(sentences, embeddings):
        embedding_str = '[' + ','.join(map(str, embedding)) + ']'
        success = insert_query(query, (sentence, embedding_str))
        if not success:
            return False
    return True


def insert_pdf_data_into_db(text_pages, embeddings):
    """
    Insert extracted text and embeddings into the database.
    :param text_pages: List of text chunks.
    :param embeddings: List of corresponding embeddings.
    """
    query = "INSERT INTO sentences_new (sentence, embedding) VALUES (%s, %s);"
    for text, embedding in zip(text_pages, embeddings):
        # Convert embedding to PostgreSQL-compatible format
        embedding_str = f"[{','.join(map(str, embedding))}]"
        success = insert_query(query, (text, embedding_str))
        if not success:
            raise HTTPException(
                status_code=500, detail=f"Failed to insert text: {text}")

    msg = "PDF data inserted successfully!"
    print(msg)
    return msg
