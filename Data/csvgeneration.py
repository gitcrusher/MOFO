import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate synthetic data
def generate_fraud_detection_data(num_samples=1000):
    """
    Generate a synthetic dataset for fraud detection in financial transactions.
    """
    # Initialize lists for features
    transaction_ids = [f"T{i+1}" for i in range(num_samples)]
    transaction_amounts = []
    transaction_times = []
    locations = []
    device_types = []
    ip_addresses = []
    user_behavior_scores = []
    historical_transaction_counts = []
    average_transaction_amounts = []
    is_fraud = []

    # Generate synthetic data
    for i in range(num_samples):
        # Transaction Amount (fraudulent transactions tend to have higher amounts)
        if random.random() < 0.05:  # 5% fraud rate
            amount = round(random.uniform(5000, 10000), 2)  # High amounts for fraud
            fraud = 1
        else:
            amount = round(random.uniform(10, 500), 2)  # Normal amounts
            fraud = 0
        transaction_amounts.append(amount)

        # Transaction Time (fraudulent transactions often occur late at night)
        start_time = datetime(2023, 1, 1, 0, 0, 0)
        time_delta = timedelta(minutes=random.randint(0, 60 * 24 * 30))  # Random time in 30 days
        transaction_time = start_time + time_delta
        if fraud == 1 and random.random() < 0.8:  # 80% of fraud occurs late at night
            transaction_time = transaction_time.replace(hour=random.randint(0, 6))
        transaction_times.append(transaction_time.strftime('%Y-%m-%d %H:%M:%S'))

        # Location (randomly assign from a list of cities)
        city_list = ['New York', 'London', 'Paris', 'Tokyo', 'Berlin', 'Sydney', 'Mumbai', 'Singapore']
        location = random.choice(city_list)
        locations.append(location)

        # Device Type (fraudulent transactions more likely from desktops)
        device_type = 'Desktop' if fraud == 1 and random.random() < 0.7 else 'Mobile'
        device_types.append(device_type)

        # IP Address (randomly generate an IP address)
        ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        ip_addresses.append(ip_address)

        # User Behavior Score (higher scores indicate normal behavior)
        behavior_score = random.randint(10, 100) if fraud == 0 else random.randint(0, 20)
        user_behavior_scores.append(behavior_score)

        # Historical Transaction Count (fraudulent accounts often have fewer transactions)
        historical_count = random.randint(5, 30) if fraud == 0 else random.randint(0, 5)
        historical_transaction_counts.append(historical_count)

        # Average Transaction Amount (fraudulent transactions deviate from the norm)
        avg_amount = round(random.uniform(50, 300), 2) if fraud == 0 else round(random.uniform(1000, 5000), 2)
        average_transaction_amounts.append(avg_amount)

        # Is Fraud (binary label)
        is_fraud.append(fraud)

    # Create DataFrame
    data = {
        'Transaction_ID': transaction_ids,
        'Transaction_Amount': transaction_amounts,
        'Transaction_Time': transaction_times,
        'Location': locations,
        'Device_Type': device_types,
        'IP_Address': ip_addresses,
        'User_Behavior_Score': user_behavior_scores,
        'Historical_Transaction_Count': historical_transaction_counts,
        'Average_Transaction_Amount': average_transaction_amounts,
        'Is_Fraud': is_fraud
    }
    df = pd.DataFrame(data)

    return df

# Generate dataset
if __name__ == "__main__":
    # Generate 1000 samples
    synthetic_data = generate_fraud_detection_data(num_samples=1000)

    # Save to CSV
    synthetic_data.to_csv('fraud_detection_synthetic_data.csv', index=False)

    # Display first few rows
    print(synthetic_data.head())