import argparse
import logging
from kakaku_robot.site.ranking import Ranking

def main():
    #parser = argparse.ArgumentParser(description=PCConfig.app_name)

    # args params
    #parser.add_argument('-conf', '--config', help="[must] configuration file", required=True)
    #args = parser.parse_args()
    #print(args)
    
    binary_location="/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
    executable_path="/Users/rv/workspace/docker/finance_db/tools/chromedriver"
    headless=False
    
    ranking = Ranking(binary_location=binary_location, executable_path=executable_path, headless=headless)
    result = ranking.all_category_ranking(pandas=True)
    result.to_csv("/Users/rv/Desktop/kakau_rank.csv")
    
if __name__ == "__main__":
    main()