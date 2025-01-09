import os
from dotenv import load_dotenv

load_dotenv()


if os.getenv('TEST_ENV_API_KEY') is None:
    print("no env variables found.")
else:
    print(f"ENV variable = {os.getenv('TEST_ENV_API_KEY')}")