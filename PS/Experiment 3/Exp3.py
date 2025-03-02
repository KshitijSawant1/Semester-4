# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Read CSV File
file_path = "Experiment 3/Data.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Step 3: Display First 5 Rows
print("First 5 Rows of Data:\n", df.head())

# Step 4: Display Information About Data
print("\nDataset Information:")
print(df.info())

# Step 5: Display Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Step 6: Mathematical Operations (Column 'Sales')
df["Sales_After_Tax"] = df["Sales"] * 1.10  # Adding 10% tax
df["Discounted_Sales"] = df["Sales"] - (df["Sales"] * 0.15)  # Subtracting 15% discount

# Step 7: Aggregate Functions
print("\nAggregate Functions on 'Sales' Column:")
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Maximum Sales:", df["Sales"].max())
print("Minimum Sales:", df["Sales"].min())
print("Count of Sales Entries:", df["Sales"].count())

# Step 8: Display Updated Data
print("\nUpdated Data with Mathematical Operations:\n", df.head())

# Step 9: Ask User if they want Visualization
visualize = input("\nWould you like an additional visualization using graphs for better analysis? 😊 (yes/no): ").strip().lower()

if visualize == "yes":
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Bar Chart for Original and Discounted Sales
    axes[0].bar(df.index, df["Sales"], label="Original Sales", color="blue", alpha=0.6)
    axes[0].bar(df.index, df["Discounted_Sales"], label="Discounted Sales", color="green", alpha=0.6)
    axes[0].set_title("Original vs Discounted Sales")
    axes[0].set_xlabel("Index")
    axes[0].set_ylabel("Sales Amount")
    axes[0].legend()

    # Line Chart for Sales Trends (Before and After Tax)
    axes[1].plot(df.index, df["Sales"], marker="o", linestyle="--", label="Sales", color="blue")
    axes[1].plot(df.index, df["Sales_After_Tax"], marker="o", linestyle="--", label="Sales After Tax", color="red")
    axes[1].set_title("Sales Trends Before and After Tax")
    axes[1].set_xlabel("Index")
    axes[1].set_ylabel("Sales Value")
    axes[1].legend()

    # Pie Chart for Sales Distribution
    total_sales = df["Sales"].sum()
    total_sales_after_tax = df["Sales_After_Tax"].sum()
    total_discounted_sales = df["Discounted_Sales"].sum()

    sales_values = [total_sales, total_sales_after_tax, total_discounted_sales]
    labels = ["Original Sales", "Sales After Tax", "Discounted Sales"]
    colors = ["blue", "red", "green"]

    axes[2].pie(sales_values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90, shadow=True)
    axes[2].set_title("Sales Distribution")

    # Display the graphs
    plt.tight_layout()
    plt.show()

print("\nAnalysis Completed!")
