# Wikipedia Scraper (Python/Scrapy)
Scrape random wikipedia articles and export data in CSV.

## Getting Started
1. Download or clone project.
2. Create and activate virtual environment.
```
   python3 -m venv virtual_environment_name
   source virtual_environment_name/bin/activate
```
3. Install required packages.
```
   pip install -r requirements.txt
```
4. Start scraping.
```
   scrapy crawl wikipedia
```
If you want to export data in CSV:
```
   scrapy crawl wikipedia -o file.csv -t csv
```
