from __future__ import print_function

import argparse

from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession


def main():
    conf = SparkConf()
    conf.setAppName('kakaku_robot')
    sc = SparkContext(conf=conf)
    spark = SparkSession(sc)

    parser = argparse.ArgumentParser(description='pyspark app args example')
    parser.add_argument('--message', type=str, required=True, help='show message')
    args = parser.parse_args()

    sql = 'SELECT "{msg}" AS message'.format(msg=args.message)
    df = spark.sql(sql)
    df.show()


if __name__ == '__main__':
    main()