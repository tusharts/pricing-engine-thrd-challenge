
import pandas as pd
import os


products_df = pd.read_csv(r'File Location\Thrd Coding Challenge\products.csv')


sales_df = pd.read_csv(r'File Location\Thrd Coding Challenge\sales.csv')

print("Products DataFrame:")
print(products_df.head())

print("\nSales DataFrame:")
print(sales_df.head())

merged_df = products_df.merge(sales_df, on='sku')


def apply_pricing_rules(row):
    new_price = row['current_price']
    
   
    if row['stock'] < 20 and row['quantity_sold'] > 30:
        new_price *= 1.15
    
    elif row['stock'] > 200 and row['quantity_sold'] == 0:
        new_price *= 0.7
    
    elif row['stock'] > 100 and row['quantity_sold'] < 20:
        new_price *= 0.9
    
    
    min_price = row['cost_price'] * 1.2
    if new_price < min_price:
        new_price = min_price
    
    
    return round(new_price, 2)


merged_df['new_price'] = merged_df.apply(apply_pricing_rules, axis=1)
merged_df.rename(columns={'current_price': 'old_price'}, inplace=True)



print(merged_df[['sku', 'name', 'old_price', 'new_price']])
output_path = r'File Saving Location\updated_prices.csv'

merged_df[['sku', 'old_price', 'new_price']].to_csv(output_path, index=False)


print("File created at:", os.path.abspath("updated_prices.csv"))

