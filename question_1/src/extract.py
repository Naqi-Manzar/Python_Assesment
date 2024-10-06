from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame


def create_spark_session(app_name: str = "Sales Data Processing") -> SparkSession:
    """
    Create a Spark session.

    Args:
        app_name (str): Name of the Spark application.

    Returns:
        SparkSession: A Spark session.
    """
    return SparkSession.builder.appName(app_name).getOrCreate()


def read_data(spark: SparkSession, file_path: str) -> DataFrame:
    """
    Read data from CSV files into a PySpark DataFrame.

    Args:
        spark (SparkSession): Spark session.
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Spark DataFrame containing the read data.
    """
    return spark.read.option("header", "true").csv(file_path)

