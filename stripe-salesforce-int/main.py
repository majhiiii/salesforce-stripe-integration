from services.salesforce_service import (
    get_salesforce_token,
    get_contacts_with_stripe_id,
    update_card_status
)
from services.stripe_service import get_card_status

def main():
    print(" Starting Stripe → Salesforce sync...")

    try:
        access_token, instance_url = get_salesforce_token()
        contacts = get_contacts_with_stripe_id(instance_url, access_token)

        print(f" Found {len(contacts)} Salesforce Contacts with Stripe IDs.")

        for contact in contacts:
            contact_id = contact['Id']
            stripe_id = contact['Stripe_Customer_Id__c']
            print(f" Checking card for Stripe customer {stripe_id}...")

            status = get_card_status(stripe_id)
            print(f"→ Status: {status}")

            resp_code = update_card_status(instance_url, access_token, contact_id, status)

            if resp_code == 204:
                print(f" Updated Contact {contact_id} with status: {status}")
            else:
                print(f" Failed to update Contact {contact_id}. HTTP {resp_code}")

        print(" Sync complete.")
    except Exception as e:
        print(" Sync failed:", e)

if __name__ == "__main__":
    main()
