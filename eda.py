#Exploratory Data Analysis

import pandas as pd
import load_data

def perform_eda(df):
    print("Inside perform_eda()")
    print("Data Overview : \n",df.head())
    print("\nMissing Values : ", df.isnull().sum())
    print("\nSummery Statistics : \n", df.describe())

if __name__ == "__main__":
    print("Running EDA")
    df = load_data.load_data("/Users/apple/Documents/Retail_Sales_Analysis/Online_Retail_Sales.csv", encoding="ISO-8859-1")
    if df is not None:
        perform_eda(df)
    else:
        print("Data loading failed")
