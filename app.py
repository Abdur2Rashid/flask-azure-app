import os
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    # Example of reading a secret/key from environment variables
    api_key = os.getenv("MY_API_KEY", "not-set")
    return f"Hello from Azure! MY_API_KEY is {'set' if api_key != 'not-set' else 'NOT set'}"

if __name__ == "__main__":
    app.run()
