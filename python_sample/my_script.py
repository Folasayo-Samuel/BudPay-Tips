import requests

# Process a payment using the BudPay API
def process_payment():
    try:
        api_base_url = 'https://api.budpay.com/api/v2'  # Replace with the actual API base URL
        api_key = 'YOUR_API_KEY'  # Replace with your BudPay API key

        payment_data = {
            'amount': 100.00,
            'currency': 'USD',
            'cardNumber': '4111111111111111',
            'cardExpiryMonth': '12',
            'cardExpiryYear': '2024',
            'cardCvv': '123'
        }

        # Make a POST request to the payment endpoint
        response = requests.post(f"{api_base_url}/payment", json=payment_data, headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })

        response_data = response.json()
        if response.status_code == 200:
            print('Payment successful:', response_data)
        else:
            print('Payment failed:', response_data)
    except Exception as e:
        print('Payment failed:', str(e))

# Call the function to process the payment
process_payment()