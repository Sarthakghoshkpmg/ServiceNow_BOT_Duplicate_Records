import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import gradio as gr

# Step 1: Generate Synthetic Dataset
def generate_dataset():
    data = {
        "Customer_ID": [i for i in range(1, 21)],  # 20 unique customers
        "Name": [f"Customer_{i}" for i in range(1, 21)],
        "Age": [random.randint(18, 65) for _ in range(20)],
        "Purchase_Amount": [random.randint(100, 10000) for _ in range(20)],
        "Email": [f"user{i}@example.com" for i in range(1, 21)]
    }

    # Introducing duplicate records
    duplicate_entries = [
        {"Customer_ID": 5, "Name": "Customer_5", "Age": 28, "Purchase_Amount": 5000, "Email": "user5@example.com"},
        {"Customer_ID": 10, "Name": "Customer_10", "Age": 34, "Purchase_Amount": 7500, "Email": "user10@example.com"}
    ]
    for row in duplicate_entries:
        for key in data.keys():
            data[key].append(row[key])

    # Convert to DataFrame and Save as CSV
    df = pd.DataFrame(data)
    df.to_csv("synthetic_dataset.csv", index=False, encoding="utf-8")

    return df

# Step 2: Analyze Dataset
def analyze_dataset(df):
    total_records = len(df)
    unique_customers = df["Customer_ID"].nunique()
    duplicate_count = df.duplicated().sum()

    summary = f"""
    📊 Dataset Analysis:
    -------------------
    - Total Records: {total_records}
    - Unique Customers: {unique_customers}
    - Duplicate Entries Found: {duplicate_count}
    - Age Range: {df['Age'].min()} - {df['Age'].max()}
    - Average Purchase Amount: ${df['Purchase_Amount'].mean():.2f}
    """

    return summary, duplicate_count

# Step 3: Graphical Visualization
def visualize_data(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Age"], bins=10, kde=True, color='blue')
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.title("Age Distribution of Customers")
    plt.savefig("age_distribution.png")

    plt.figure(figsize=(8, 5))
    sns.boxplot(df["Purchase_Amount"], color='red')
    plt.xlabel("Purchase Amount")
    plt.title("Purchase Amount Distribution")
    plt.savefig("purchase_distribution.png")

    return "age_distribution.png", "purchase_distribution.png"

# Step 4: Gradio Interface
def process_file(file):
    df = pd.read_csv(file)
    summary, duplicate_count = analyze_dataset(df)
    age_plot, purchase_plot = visualize_data(df)
    
    duplicates = df[df.duplicated(keep=False)]
    duplicate_message = "✅ No duplicate records found!" if duplicates.empty else f"⚠️ {duplicate_count} Duplicate Records Detected!"
    
    return summary, duplicate_message, age_plot, purchase_plot

# Launch Gradio App
interface = gr.Interface(
    fn=process_file,
    inputs="file",
    outputs=["text", "text", "image", "image"],
    title="Duplicate Checker & Data Analysis Portal",
    description="Upload your dataset to analyze duplicates and visualize trends."
)

interface.launch()
