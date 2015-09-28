import sys
import shutil
import logging

from operator import add
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

if __name__ == "__main__":

    sc = SparkContext(appName="Spark")

    # Datasource looks like
    # City, Year, Sport, Name, Gold, Silver, Bronze, Total_Medals
    # Moscow,1980,Volleyball,SOLOVOVA Olga,1,0,0,1

    sqlContext = SQLContext(sc)
    olympic_data = sc.textFile("hdfs://localhost:9000/spark-input/")

    parts = olympic_data.map(lambda l: l.split(","))
    people = parts.map(lambda p: (p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7]))

    # The schema is encoded in a string.
    schemaString = "city year sport name gold silver bronze total_medals"

    fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
    schema = StructType(fields)

    # Apply the schema to the RDD.
    schemaPeople = sqlContext.createDataFrame(people, schema)

    # Register the DataFrame as a table.
    schemaPeople.registerTempTable("olympics")

    olympic_result = sqlContext.sql("Select city, sum(total_medals) AS total from olympics group by city order by sum(total_medals) desc limit 1").collect()

    print "\nSTARTING OUTPUT\n"

    for result in olympic_result:
        print result

    print "\nEND OF OUTPUT\n"

    # YOUR CODE HERE
    # Link might be helpful for listing RDD operations:
    # http://spark.apache.org/docs/latest/programming-guide.html#rdd-operations
    # https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html

    sc.stop()
