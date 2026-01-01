import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

merchants = ["Amazon", "Walmart", "Apple", "Target", "BestBuy", "Gas Station"]
locations = ["New York", "Texas", "California", "Florida", "Illinois", "London"]
channels = ["Online", "In-store"]

rows = []

start_date = datetime.now() - timedelta(days=30)

for i in range(100):
    is_fraud = 1 if random.random() < 0.15 else 0

    amount = (
        random.randint(1500, 4000) if is_fraud
        else random.randint(10, 300)
    )

    transaction_time = start_date + timedelta(
        days=random.randint(0, 30),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )

    location = "London" if is_fraud and random.random() < 0.5 else random.choice(locations)
    channel = "Online" if is_fraud else random.choice(channels)

    rows.append({
        "TransactionID": f"T{i+1:03}",
        "DateTime": transaction_time,
        "Amount": amount,
        "Merchant": random.choice(merchants),
        "Location": location,
        "Channel": channel,
        "IsFraud": is_fraud
    })

df = pd.DataFrame(rows)
df.to_csv("data/transactions.csv", index=False)

print("✅ Dataset created: data/transactions.csv")
