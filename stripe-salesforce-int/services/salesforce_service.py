import requests
from config.settings import SF_CLIENT_ID, SF_CLIENT_SECRET, SF_TOKEN_URL, SF_API_VERSION

def get_salesforce_token():
    response = requests.post(SF_TOKEN_URL, data={
        'grant_type': 'client_credentials',
        'client_id': SF_CLIENT_ID,
        'client_secret': SF_CLIENT_SECRET
    })
    response.raise_for_status()
    data = response.json()
    return data['access_token'], data['instance_url']

def get_contacts_with_stripe_id(instance_url, access_token):
    url = f"{instance_url}/services/data/{SF_API_VERSION}/query"
    query = "SELECT Id, Stripe_Customer_Id__c FROM Contact WHERE Stripe_Customer_Id__c != NULL"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers, params={'q': query})
    response.raise_for_status()
    return response.json().get("records", [])

def update_card_status(instance_url, access_token, contact_id, status):
    url = f"{instance_url}/services/data/{SF_API_VERSION}/sobjects/Contact/{contact_id}"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    body = {"Card_Status__c": status}
    response = requests.patch(url, headers=headers, json=body)
    return response.status_code
