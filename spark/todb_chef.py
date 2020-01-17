from __future__ import print_function

import argparse

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark import SparkContext

def main():
    conf = SparkConf()
    conf.setAppName('kakaku_robot')
    sc: SparkContext = SparkContext(conf=conf)
    spark:SparkSession = SparkSession(sc)

    parser = argparse.ArgumentParser(description='pyspark app args')
    parser.add_argument('-ip', '--input_path', type=str, required=True, help='show message')
    args = parser.parse_args()
    print("todb_chef start")
    print(args)
    input_path = f"{args.input_path}/*.csv"
    print(f"input path: {input_path}")
    df = spark.read.option("header", "true").csv(f"{args.input_path}/*.csv")
    print(df.collect()[0])

if __name__ == '__main__':
    main()