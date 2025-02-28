import os
from dotenv import load_dotenv

load_dotenv()

class Development():
    MONGO_URI = "mongodb://localhost:27017/todos"
class Build():
    MONGO_URI=os.getenv("MONGO_URI")
    