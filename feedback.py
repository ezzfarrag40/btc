import numpy as np
from predictor import make_predictions

# Get user feedback on the predicted price
predictions = make_predictions()
feedback = []
for i in range(24):
    price = predictions[i][0]
    feedback.append(input(f"What do you think the price of BTC will be in {i+1} hour(s)? (current price: ${price:.2f})\n"))

# Calculate the mean absolute error
error = np.mean(np.abs(predictions - np.array(feedback, dtype=float)))

# Print the error to the console
print(f"Mean absolute error: {error:.2f}")
