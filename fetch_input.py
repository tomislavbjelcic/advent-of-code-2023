import requests
import argparse
import datetime
import os



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('session')
    parser.add_argument('dest')
    parser.add_argument('-y', '--year', type=int)
    parser.add_argument('-d', '--day', type=int)
    
    args = parser.parse_args()
    tdy = datetime.date.today()
    
    y, d = args.year, args.day
    if not y: y = tdy.year
    if not d: d = tdy.day
    
    if not os.path.exists(args.session):
        print('File with session cookie does not exist.')
        return
    
    sk = open(args.session).read()
    get(d, y, sk, args.dest)
    
    
def get(day, year, sk, dest):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    print(f'Accessing: {url}\n')
    res = requests.get(
        url,
        cookies={'session':sk}
    )
    if res.status_code != 200:
        print(res.text)
        return
    
    print(f'Success. Writing to {dest}...')
    open(dest, 'w').write(res.text)
    print('Done')
        
    


if __name__ == '__main__':
    main()