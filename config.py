import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    config = {
        "GITHUB_API_TOKEN": os.getenv("GITHUB_API_TOKEN"),
        "REPO_OWNER": os.getenv("REPO_OWNER"),
        "REPO_NAME": os.getenv("REPO_NAME")
    }
    return config
