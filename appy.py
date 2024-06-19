import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

file_path = 'OnlineRetail.csv'
retail_df = pd.read_csv(file_path, encoding='ISO-8859-1')
retail_df = retail_df.dropna(subset=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
       'UnitPrice', 'CustomerID', 'Country'])
retail_df = retail_df[retail_df['Quantity'] > 0]
grouped_df = retail_df.groupby(['Country','Description']).agg({'Quantity':'sum'}).reset_index()
top_selling_per_country = grouped_df.loc[grouped_df.groupby("Country")["Quantity"].idxmax()]
print(retail_df['Country'].unique())

def returnData(c):
    country_data = grouped_df[(grouped_df['Country']).str.lower() == c.lower()]
    return country_data.to_dict(orient='records')
