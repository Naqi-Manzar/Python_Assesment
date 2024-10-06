from pyspark.sql import DataFrame
from pyspark.sql.functions import col, expr, lit


def transform_data(df: DataFrame, region: str) -> DataFrame:
    """
    Apply business transformations to the input DataFrame.

    Args:
        df (DataFrame): The input DataFrame containing sales data.
        region (str): The region (A or B) to be added to the DataFrame.

    Returns:
        DataFrame: The transformed DataFrame with required columns.
    """
    # Convert PromotionDiscount from JSON string to float
    df = df.withColumn("PromotionDiscount", expr("cast(regexp_extract(PromotionDiscount, '[0-9.]+', 0) as float)"))

    # Calculate total_sales and net_sale
    df = df.withColumn("total_sales", col("QuantityOrdered") * col("ItemPrice")) \
        .withColumn("net_sale", col("total_sales") - col("PromotionDiscount"))

    # Add region column
    df = df.withColumn("region", lit(region))

    # Remove duplicate OrderIds
    df = df.dropDuplicates(["OrderId"])

    # Filter out rows where net_sale is less than or equal to zero
    df = df.filter(col("net_sale") > 0)

    return df


def combine_data(df_a: DataFrame, df_b: DataFrame) -> DataFrame:
    """
    Combine the data from two regions into a single DataFrame.

    Args:
        df_a (DataFrame): Transformed DataFrame for region A.
        df_b (DataFrame): Transformed DataFrame for region B.

    Returns:
        DataFrame: Combined DataFrame.
    """
    return df_a.unionByName(df_b)
