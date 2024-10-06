from pyspark.sql import DataFrame
from question_1.config.db_config import DB_CONNECTION


def load_to_db(df: DataFrame) -> None:
    """
    Load the transformed DataFrame into a database.

    Args:
        df (DataFrame): Transformed DataFrame.
    """
    df.write \
        .format("jdbc") \
        .option("url", DB_CONNECTION["url"]) \
        .option("dbtable", DB_CONNECTION["table"]) \
        .option("user", DB_CONNECTION["user"]) \
        .option("password", DB_CONNECTION["password"]) \
        .mode("append") \
        .save()
