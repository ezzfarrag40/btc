import numpy as np
from predictor import make_predictions

# Set the risk threshold and investment amount
risk_threshold = 0.1
investment_amount = 10000

# Make predictions for the next 24 hours
predictions = make_predictions()

# Calculate the percentage change in price
price_change = np.diff(predictions, axis=0) / predictions[:-1] * 100

# Calculate the total profit or loss
total_return = np.sum(price_change) * investment_amount / 100

# Check if the risk threshold has been exceeded
if np.abs(price_change).max() > risk_threshold:
    print("Risk threshold exceeded!")
else:
    print(f"Total return: ${total_return:.2f}")
