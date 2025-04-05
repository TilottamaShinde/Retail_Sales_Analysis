import pandas as pd
import load_data

def top_selling_products(df):
    #find top 10 best selling products
    top_products = df.groupby("Product Name")['Sales'].sum().nlargest(10)
    return top_products

def top_profitable_categories(df):
    top_categories = df.groupby('Category')['Profit'].sum().sort_values(ascending = False)
    return top_categories

if __name__ == '__main__':
        df = load_data.load_data("/Users/apple/Documents/Retail_Sales_Analysis/Online_Retail_Sales.csv", encoding="ISO-8859-1")
        print("Top Selling Products : \n", top_selling_products(df))
        print("Most Profitable Categories : \n", top_profitable_categories(df))