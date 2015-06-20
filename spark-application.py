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

    olympic_data = sc.textFile("olympic/input")

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

    country_medal_count = country_medals.reduceByKey(add)

    medal_country = country_medal_count.map(lambda (k,v): (v,k)).sortByKey(False)


    top_scoring_country = sc.parallelize(medal_country.take(1))

    top_scoring_country.saveAsTextFile("olympic/output")

    sc.stop()
