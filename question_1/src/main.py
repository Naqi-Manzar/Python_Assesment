from extract import create_spark_session, read_data
from transform import transform_data, combine_data
from load import load_to_db
from validate import count_records, total_sales_by_region, avg_sales_per_transaction, check_duplicates

def main():
    # Create Spark session
    spark = create_spark_session()

    # Read data from both regions
    df_region_a = read_data(spark, "data/order_region_a.csv")
    df_region_b = read_data(spark, "data/order_region_b.csv")

    # Apply transformations
    transformed_a = transform_data(df_region_a, "A")
    transformed_b = transform_data(df_region_b, "B")

    # Combine the transformed data
    combined_data = combine_data(transformed_a, transformed_b)

    # Load the data into the database
    load_to_db(combined_data)

    # Validation
    print(f"Total records: {count_records(combined_data)}")
    total_sales_by_region(combined_data).show()
    print(f"Average sales per transaction: {avg_sales_per_transaction(combined_data)}")
    print(f"No duplicates: {check_duplicates(combined_data)}")

if __name__ == "__main__":
    main()
