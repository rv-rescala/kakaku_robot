from __future__ import print_function

import argparse
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark import SparkContext
from kakakucom.model.item import RankedItemTable
from catscore.db.mysql import MySQLConf

def main():
    conf = SparkConf()
    conf.setAppName('kakaku_robot')
    sc: SparkContext = SparkContext(conf=conf)
    spark:SparkSession = SparkSession(sc)

    parser = argparse.ArgumentParser(description='pyspark app args')
    parser.add_argument('-ip', '--input_path', type=str, required=True, help='input folder path')
    parser.add_argument('-db', '--db_conf', type=str, required=True, help='input db conf path')
    args = parser.parse_args()
    print("todb_job: start")
    print(f"args: {args}")
    mysql_conf = MySQLConf.from_json(args.db_conf)
    print(f"mysql_conf {mysql_conf}")
    df = RankedItemTable.from_local_as_df(spark, args.input_path)
    RankedItemTable.overwrite_table(spark=spark, df=df, mysql_conf=mysql_conf)


if __name__ == '__main__':
    main()