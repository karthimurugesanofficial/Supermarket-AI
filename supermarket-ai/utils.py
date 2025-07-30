import pandas as pd

def load_product_data(csv_path="Supermarket - Sheet1.csv"):
    df = pd.read_csv(csv_path).fillna("")
    return df

def row_to_text(row):
    return f"Product: {row['product_name']}, Brand: {row['brand']}, Quantity: {row['quantity']}, Price: ₹{row['price']}, Category: {row['category']}, Availability: {row['availability']}"
