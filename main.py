
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
#          RAINFALL DATA ANALYZER
# ==========================================

def load_data():
    try:
        data = pd.read_csv("rain.csv")

        # Check required columns
        if "Month" not in data.columns or "Rainfall" not in data.columns:
            print("Error: Required columns are missing.")
            return None

        # Convert rainfall values into numbers
        data["Rainfall"] = pd.to_numeric(
            data["Rainfall"], errors="coerce"
        )

        # Remove invalid and negative values
        data = data.dropna(subset=["Month", "Rainfall"])
        data = data[data["Rainfall"] >= 0]

        if data.empty:
            print("No valid rainfall records found.")
            return None

        print("\nData loaded successfully!")
        print(data.to_string(index=False))

        return data

    except FileNotFoundError:
        print("Error: rain.csv not found.")
        return None

    except Exception as error:
        print("Error:", error)
        return None


# Calculate rainfall statistics
def show_statistics(data):
    rainfall = data["Rainfall"]

    total = np.sum(rainfall)
    average = np.mean(rainfall)
    maximum = np.max(rainfall)
    minimum = np.min(rainfall)
    deviation = np.std(rainfall)

    print("\n========== RAINFALL STATISTICS ==========")
    print("Total Rainfall:", round(total, 2), "mm")
    print("Average Rainfall:", round(average, 2), "mm")
    print("Maximum Rainfall:", maximum, "mm")
    print("Minimum Rainfall:", minimum, "mm")
    print("Standard Deviation:", round(deviation, 2), "mm")


# Find wettest and driest months
def show_monthly_comparison(data):
    wettest = data.loc[data["Rainfall"].idxmax()]
    driest = data.loc[data["Rainfall"].idxmin()]

    print("\n========== MONTHLY COMPARISON ==========")
    print("Wettest Month:", wettest["Month"])
    print("Highest Rainfall:", wettest["Rainfall"], "mm")

    print("Driest Month:", driest["Month"])
    print("Lowest Rainfall:", driest["Rainfall"], "mm")


# Identify heavy rainfall months
def show_heavy_rainfall(data):
    heavy = data[data["Rainfall"] > 200]

    print("\n========== HEAVY RAINFALL ==========")

    if heavy.empty:
        print("No months with rainfall above 200 mm.")
    else:
        print(heavy[["Month", "Rainfall"]].to_string(index=False))


# Compare rainfall with average
def compare_average(data):
    average = data["Rainfall"].mean()

    above = data[data["Rainfall"] > average]
    below = data[data["Rainfall"] < average]
    equal = data[data["Rainfall"] == average]

    print("\n========== ABOVE AVERAGE ==========")

    if above.empty:
        print("No months above average.")
    else:
        print(above[["Month", "Rainfall"]].to_string(index=False))

    print("\n========== BELOW AVERAGE ==========")

    if below.empty:
        print("No months below average.")
    else:
        print(below[["Month", "Rainfall"]].to_string(index=False))

    if not equal.empty:
        print("\nMonths equal to average:")
        print(equal[["Month", "Rainfall"]].to_string(index=False))


# Display bar chart
def show_bar_chart(data):
    plt.figure(figsize=(10, 5))

    plt.bar(data["Month"], data["Rainfall"])

    plt.title("Monthly Rainfall Analysis")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# Display line chart
def show_line_chart(data):
    plt.figure(figsize=(10, 5))

    plt.plot(
        data["Month"],
        data["Rainfall"],
        marker="o"
    )

    plt.title("Monthly Rainfall Trend")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")
    plt.xticks(rotation=45)
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# Display all analysis results
def show_all_results(data):
    show_statistics(data)
    show_monthly_comparison(data)
    show_heavy_rainfall(data)
    compare_average(data)


# Main program
def main():

    print("=" * 45)
    print("          RAINFALL DATA ANALYZER")
    print("=" * 45)

    data = load_data()

    if data is None:
        return

    while True:

        print("\n============== MAIN MENU ==============")
        print("1. Rainfall Statistics")
        print("2. Wettest and Driest Months")
        print("3. Heavy Rainfall Months")
        print("4. Compare Rainfall with Average")
        print("5. Bar Chart")
        print("6. Line Chart")
        print("7. Display All Results")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            show_statistics(data)

        elif choice == "2":
            show_monthly_comparison(data)

        elif choice == "3":
            show_heavy_rainfall(data)

        elif choice == "4":
            compare_average(data)

        elif choice == "5":
            show_bar_chart(data)

        elif choice == "6":
            show_line_chart(data)

        elif choice == "7":
            show_all_results(data)

        elif choice == "8":
            print("\nThank you for using Rainfall Data Analyzer!")
            break

        else:
            print("\nInvalid choice. Please enter 1 to 8.")


if __name__ == "__main__":
    main()
