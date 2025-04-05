# workation-api

REST API for the Workation app 

It receives a natural language query and returns (fake) listings from Airbnb related to that query.

## Running the Project

1. Install dependencies:

    ```
    pip install -r requirements.txt
    ```


2. Create a `.env` file in the root directory with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   REDIS_HOST=your_redis_host
   REDIS_PORT=your_redis_port
   REDIS_USERNAME=your_redis_username
   REDIS_PASSWORD=your_redis_password
   MONGODB_URI=your_mongodb_connection_string
   ```

3. Run the API server:
   ```bash
   uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://localhost:8000`.

