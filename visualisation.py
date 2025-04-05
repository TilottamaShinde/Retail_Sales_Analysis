import pandas as pd
import matplotlib.pyplot as plt
import load_data

def plot_sales_trend(df):
    df['YearMonth'] = df['Order Date'].dt.to_period('M')
    monthly_sales = df.groupby('YearMonth')['Sales'].sum()
    plt.figure(figsize=(10,5))
    monthly_sales.plot(kind = 'line', marker = 'o', color = 'b')
    plt.title('Monthly Sales Trends ')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid()
    plt.show()
if __name__ == "__main__":
    df = load_data.load_data("/Users/apple/Documents/Retail_Sales_Analysis/Online_Retail_Sales.csv", encoding="ISO-8859-1")
    if df is not None:
        print("Data loaded successfully")
        plot_sales_trend(df)
    else:
        print("Data loading failed. Exiting Script")