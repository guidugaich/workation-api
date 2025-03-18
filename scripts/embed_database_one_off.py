import pymongo
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Set up MongoDB client
mongo_client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
db = mongo_client["sample_airbnb"]
collection = db["listingsAndReviews"]

# Set up OpenAI client
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
embedding_model_id="text-embedding-3-small"

def get_big_field(listing_document):
    summary = listing_document.get("summary", "")
    space = listing_document.get("space", "")
    description = listing_document.get("description", "")
    price = listing_document.get("price", "")
    neighborhood_overview = listing_document.get("neighborhood_overview", "")
    city = listing_document.get("address", {}).get("street", "")

    return f'the summary is: {summary}; about the space: {space}; the description is: {description}; the neighborhood overview is: {neighborhood_overview};the location is: {city} and the price is {price}'

def generate_embeddings(texts):
    response = openai.embeddings.create(
        input=texts,
        model=embedding_model_id,
        encoding_format="float"
    )
    embeddings = [item.embedding for item in response.data]
    print(f"Embedded {len(texts)} texts into vectors")
    return embeddings

def process_documents(documents):
    texts = [get_big_field(doc) for doc in documents]
    embeddings = generate_embeddings(texts)
    
    bulk_operations = []
    for doc, embedding, text in zip(documents, embeddings, texts):
        bulk_operations.append(
            pymongo.UpdateOne(
                {"_id": doc["_id"]},
                {"$set": 
                    {
                        f"embedding_{embedding_model_id}": embedding,
                        "big_field": text
                    }
                }
            )
        )
    
    if bulk_operations:
        collection.bulk_write(bulk_operations)
        print(f"Updated {len(bulk_operations)} documents with embeddings.")

def main():
    print("Starting...")
    documents = list(collection.find(
        { "amenities": { "$all": ["Wifi", "Laptop friendly workspace"] } }
    ).limit(20))
    
    process_documents(documents)

if __name__ == "__main__":
    main()