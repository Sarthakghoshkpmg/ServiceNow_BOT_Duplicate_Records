import pandas as pd
import random

# Generate synthetic data
data = {
    "ID": [i for i in range(1, 21)],  # 20 unique IDs
    "Name": ["Person_" + str(i) for i in range(1, 21)],
    "Age": [random.randint(18, 60) for _ in range(20)],
    "Email": [f"user{i}@example.com" for i in range(1, 21)]
}

# Introduce duplicates
duplicate_rows = [
    {"ID": 5, "Name": "Person_5", "Age": 30, "Email": "user5@example.com"},
    {"ID": 10, "Name": "Person_10", "Age": 45, "Email": "user10@example.com"}
]
data["ID"].extend([row["ID"] for row in duplicate_rows])
data["Name"].extend([row["Name"] for row in duplicate_rows])
data["Age"].extend([row["Age"] for row in duplicate_rows])
data["Email"].extend([row["Email"] for row in duplicate_rows])

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("synthetic_dataset.csv", index=False)

print("Synthetic dataset generated: synthetic_dataset.csv")
