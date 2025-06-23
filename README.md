This integration syncs Stripe customers' card status (active, expiring soon, expired, invalid) to Salesforce. 
It also:
Automatically updates Salesforce Contact records.
Triggers internal notifications and emails to customers if their card is about to expire.

🧰 Technologies Used
Stripe (Test Mode)

Salesforce (Flow + REST API)

Python 3.9+ (for sync script)

Salesforce REST API (with Client Credentials OAuth 2.0 flow)

