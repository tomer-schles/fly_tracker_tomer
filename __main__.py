import argparse
from Scraper import PriceScraper
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument('--src')
parser.add_argument('--dest')
parser.add_argument('--price')
parser.add_argument('--date')

args = parser.parse_args()

def main():
    scraper = PriceScraper(args.src,args.dest,args.price,args.date)
    page = scraper.get_page()
    parsed_page = scraper.parser(scraper.soupify(page))
    df = scraper.create_df(parsed_page)
    timestamp = datetime.now()
    df.to_csv(f'Results_{timestamp}.csv')

if __name__ == "__main__":
    main()
        