#rdd vs dataframe vs datasets

#rdd : unstructured, immutable ( resilent disturbuted dataset), it is for unstructured data, lowlevel api , data
#dataframe: structured,immutable( it is depended on pandas libraries using python.)
from pyspark import *
from pyspark.sql import SparkSession


spark= SparkSession.builder.appName("my first app").getOrCreate()
rdd= [1,2,3,4,5]
rdd1=spark.sparkContext.parallelize(rdd).collect()
print(rdd1)
spark.stop()