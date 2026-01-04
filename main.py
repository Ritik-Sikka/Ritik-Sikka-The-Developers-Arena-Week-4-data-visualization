import pandas as pd
import matplotlib.pyplot as plt

try:
    # Load dataset
    data = pd.read_csv("data/sales_data.csv")

    # Data cleaning
    data.dropna(inplace=True)
    data["Total_Sales"] = pd.to_numeric(data["Total_Sales"])

    # Analysis
    total_sales = data["Total_Sales"].sum()
    sales_by_product = data.groupby("Product")["Total_Sales"].sum()
    sales_by_region = data.groupby("Region")["Total_Sales"].sum()
    sales_trend = data.groupby("Date")["Total_Sales"].sum()

    print("Total Sales:", total_sales)

    # Bar Chart - Sales by Product
    plt.figure()
    sales_by_product.plot(kind="bar")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales Amount")
    plt.tight_layout()
    plt.savefig("charts/sales_by_product.png")
    plt.show()

    # Line Chart - Sales Trend
    plt.figure()
    sales_trend.plot(kind="line")
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/sales_trend.png")
    plt.show()

    # Pie Chart - Sales by Region
    plt.figure()
    sales_by_region.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sales Distribution by Region")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("charts/sales_by_region.png")
    plt.show()

except Exception as e:
    print("Error occurred:", e)
