Detection from Banking Transactions

## Project Objective
Identify suspicious or potentially fraudulent transactions using Python, EDA, and anomaly detection principles.

## Dataset
- Synthetic dataset (100 transactions)
- Columns: TransactionID, DateTime, Amount, Merchant, Location, Channel, IsFraud
- 15% of transactions are fraudulent to simulate real-world patterns.

## Exploratory Data Analysis Insights
- Fraud transactions have **higher average amounts**.
- Fraud tends to occur during **odd hours** (late night).
- Certain merchants show **higher fraud frequency**.
- Online transactions have a slightly **higher fraud occurrence** than in-store.

## Next Steps
- Implement **anomaly detection model** (Isolation Forest / LOF)
- Create **visual fraud dashboard**
- Scale dataset for more realistic simulations

## Tools Used
- Python (Pandas, Matplotlib, Seaborn)
- Jupyter Notebook