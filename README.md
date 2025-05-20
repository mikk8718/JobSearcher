#TODO 
rewrite to js

# Job Scraper Automator
Scrapes IT jobs near Aalborg from Jobindex.dk.

## Features
- Fetches job title, URL, distance, and description with Python/BeautifulSoup.
- Filters by radius (CLI arg, e.g., `python script.py 10` for 10 km).
- Sorts by distance, saves to `jobs.csv`.

## Setup
1. `pip install requests beautifulsoup4 pandas`
2. Run: `python3 scraper.py <radius>`

## Files
- `script.py`: The scraper.
- `jobs.csv`: Sample output (ignored in git).
