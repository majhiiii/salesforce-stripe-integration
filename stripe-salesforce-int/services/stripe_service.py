import stripe
from datetime import datetime
from config.settings import STRIPE_SECRET_KEY
from datetime import datetime, timedelta

stripe.api_key = STRIPE_SECRET_KEY

def get_card_status(customer_id):
    try:
        # Use payment_methods instead of legacy sources
        methods = stripe.PaymentMethod.list(
            customer=customer_id,
            type="card"
        )

        if not methods['data']:
            return "Invalid"

        card = methods['data'][0]['card']  # Assume default card
        exp_month = int(card['exp_month'])
        exp_year = int(card['exp_year'])

        # Card expires end of the month
        expiry_date = datetime(exp_year, exp_month, 1)
        next_month = expiry_date.month % 12 + 1
        next_year = expiry_date.year + (expiry_date.month // 12)
        expiry_end = datetime(next_year, next_month, 1) - timedelta(days=1)

        today = datetime.today()

        if expiry_end < today:
            return "Expired"
        elif (expiry_end - today).days <= 30:
            return "Expires Soon"
        else:
            return "Active"

    except Exception as e:
        print("Error fetching card:", str(e))
        return "Invalid"
