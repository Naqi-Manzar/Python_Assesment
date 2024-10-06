# Sales Data Processing Pipeline

## Overview
This project processes sales data from two regions (A and B) by applying business transformations and loading it into a database.

## How to Run
1. Install the required dependencies:

2. Set up the database connection in `config/db_config.py`.

3. Run the pipeline:


## Database Setup
This pipeline uses a MySQL database. You can change the connection string in the `db_config.py` file.

## Assumptions
- PromotionDiscount is in a JSON format and the currency is always INR.
- Duplicates are removed based on `OrderId`.

-- Count total records
SELECT COUNT(*) FROM sales_data;

-- Total sales by region
SELECT region, SUM(net_sale) FROM sales_data GROUP BY region;

-- Average sales per transaction
SELECT AVG(net_sale) FROM sales_data;

-- Check for duplicate OrderIds
SELECT OrderId, COUNT(*) FROM sales_data GROUP BY OrderId HAVING COUNT(*) > 1;
