const axios = require('axios');

// Process a payment using the BudPay API
const processPayment = async () => {
  try {
    const apiBaseUrl = 'https://api.budpay.com/api/v2'; // Replace with the actual API base URL
    const apiKey = 'YOUR_API_KEY'; // Replace with your BudPay API key

    const paymentData = {
      amount: 100.00,
      currency: 'USD',
      cardNumber: '4111111111111111',
      cardExpiryMonth: '12',
      cardExpiryYear: '2024',
      cardCvv: '123'
    };

    // Make a POST request to the payment endpoint
    const response = await axios.post(`${apiBaseUrl}/payment`, paymentData, {
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      }
    });

    console.log('Payment successful:', response.data);
  } catch (error) {
    console.error('Payment failed:', error.response.data);
  }
};

// Call the function to process the payment
processPayment();