import sys
import shutil
import logging

from operator import add
from pyspark import SparkContext


if __name__ == "__main__":
    
    sc = SparkContext(appName="Spark")
    
    # Datasource looks like
    # Athlete,Country,Year,Sport,Gold,Silver,Bronze,Total
    # Yang Yilin,China,2008,Gymnastics,1,0,2,3

    olympic_data = sc.textFile("hdfs:///tmp/olympic.csv")

    def country_medal_map(line):
        country = ""
        medals = 0
        try:
            country = line.split(',')[1]
            medals = int(line.split(',')[7])
        except:
            pass
        return (country, medals)
    

    country_medals = olympic_data.map(country_medal_map)
    
    # TODO

    country_medals.saveAsTextFile("hdfs:///tmp/output")

    sc.stop()
