# Dynamic Pricing Adjustment

## Overview
This notebook demonstrates a dynamic pricing adjustment system for a product catalog based on inventory levels and sales data. The goal is to optimize pricing by applying specific rules to ensure profitability, manage stock levels, and respond to demand.

## Approach
1. **Data Loading**: 
    - The product catalog (`products_df`) and recent sales data (`sales_df`) are loaded from CSV files.
    - The data is inspected to ensure correctness.

2. **Data Merging**:
    - The `products_df` and `sales_df` are merged on the `sku` column to create a unified dataset (`merged_df`).

3. **Pricing Rules**:
    - A function `apply_pricing_rules` is defined to calculate the new price for each product based on the following rules:
      - **Low Stock, High Demand**: If stock is less than 20 and quantity sold is greater than 30, increase the price by 15%.
      - **Dead Stock**: If stock is greater than 200 and quantity sold is 0, decrease the price by 30%.
      - **Overstocked Inventory**: If stock is greater than 100 and quantity sold is less than 20, decrease the price by 10%.
      - **Minimum Profit Constraint**: Ensure the new price is at least 20% higher than the cost price.
    - The calculated prices are rounded to two decimal places for clarity.

4. **Output**:
    - The updated dataset (`merged_df`) includes the old price, new price, and other relevant details.
    - The results are saved to a CSV file (`updated_prices.csv`) for further use.

## Assumptions
- The `sku` column is unique and serves as the primary key for merging datasets.
- The `cost_price` column represents the minimum cost of the product, and the new price must always exceed this by at least 20%.
- The rules are applied in the order listed, and the final price reflects all applicable adjustments.
- The dataset is small enough to process in memory without performance concerns.

## Files
- `products.csv`: Contains product details such as SKU, name, current price, cost price, and stock levels.
- `sales.csv`: Contains sales data, including SKU and quantity sold.
- `updated_prices.csv`: The output file with updated prices after applying the rules.

## Future Enhancements
- Incorporate machine learning models to predict demand and optimize pricing dynamically.
- Add more complex rules based on seasonality, competitor pricing, and customer behavior.
- Implement a user interface for real-time price adjustments.
```
