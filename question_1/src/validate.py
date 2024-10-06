from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count, avg, sum as spark_sum


def count_records(df: DataFrame) -> int:
    """
    Count the total number of records in the DataFrame.

    Args:
        df (DataFrame): The input DataFrame.

    Returns:
        int: Total record count.
    """
    return df.count()


def total_sales_by_region(df: DataFrame) -> DataFrame:
    """
    Calculate the total sales amount by region.

    Args:
        df (DataFrame): The input DataFrame.

    Returns:
        DataFrame: Total sales by region.
    """
    return df.groupBy("region").agg(spark_sum("net_sale").alias("total_sales"))


def avg_sales_per_transaction(df: DataFrame) -> float:
    """
    Calculate the average sales amount per transaction.

    Args:
        df (DataFrame): The input DataFrame.

    Returns:
        float: Average sales per transaction.
    """
    return df.agg(avg("net_sale")).first()[0]


def check_duplicates(df: DataFrame) -> bool:
    """
    Check for duplicate OrderIds in the DataFrame.

    Args:
        df (DataFrame): The input DataFrame.

    Returns:
        bool: True if no duplicates, False otherwise.
    """
    return df.select("OrderId").distinct().count() == df.count()

