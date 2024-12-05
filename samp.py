from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType
from pyspark.sql.functions import *

schema = StructType([
    StructField("Id", IntegerType(), True),
    StructField("FIRSTNAME", StringType(), True),
    StructField("LASTNAME", StringType(), True),
    StructField("URL", StringType(), True),
    StructField("CAMPAIGNS", ArrayType(StringType()), True)
])

data = [
    [1, "nikhil", None, "https://tinyurl.8687", ["facebook", "instagram"]],
    [2, "pavan", "kalyan", "https://tinyurl.8681", ["twitter", "fling"]],
    [3, "sai", "arjun", "https://tinyurl.8682", ["whatsapp", "snapchat"]]
]

if __name__ == "__main__":
    spark = SparkSession.builder.appName("sam").getOrCreate()
    df = spark.createDataFrame(data, schema=schema)
    df.show()
   #for row in df.collect():
       # print(f"ID: {row['Id']}, FIRSTNAME: {row['FIRSTNAME']}, LASTNAME: {row['LASTNAME']}")

    #df.select("LASTNAME").show()
    #df1= df.withColumn("Id",df.Id+12).show()
  #  df2= df.withColumn("full_name",concat(col("FIRSTNAME"),lit("_"),col("LASTNAME")))
