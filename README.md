# JobIndex job searcher
Searches JobIndex for IT jobs in a inputted radius. 
Uses my address for now, but change query for your own.

## Features
- Fetches JobIndex.
- Breaks down jobs in title, description, URL and distance.
- Saves it to a csv.

## Output
jobs.csv

## How to Run
1. Have pandas, requests, beautifulsoup and argparse installed.`
4. Run: `python script.py` and enter a radius e.g. python3 script.py 100

## Files
- `script.py`: Main code.
- `jobs.csv`: Raw job data.
