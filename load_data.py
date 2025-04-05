from unittest.mock import inplace
import chardet

import pandas as pd
def load_data(file_path, encoding="ISO-8859-1"):       #load dataset and perform basic cleaning
    df = pd.read_csv(file_path, encoding=encoding)

    #convert date columns
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst = True, errors = 'coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst = True, errors = 'coerce')

    #Remove Duplicates
    df.drop_duplicates(inplace = True)

    return df
if __name__ == '__main__':
    df = load_data("/Users/apple/Documents/Retail_Sales_Analysis/Online_Retail_Sales.csv", encoding="ISO-8859-1")
    print(df.info())