import os
from dotenv import load_dotenv
load_dotenv()

# Salesforce credentials
SF_CLIENT_ID = os.getenv("SF_CLIENT_ID")
SF_CLIENT_SECRET = os.getenv("SF_CLIENT_SECRET")
SF_TOKEN_URL = "enter your token url"
SF_API_VERSION = "v63.0"  # Adjust if needed

# Stripe
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
