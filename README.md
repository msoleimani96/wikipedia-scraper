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
   Note: Make sure you are in wikipedia directory that scrapy.cfg file located, then run the commands below.
```
   scrapy crawl wikipedia
```
If you want to export data in CSV:
```
   scrapy crawl wikipedia -o file.csv -t csv
```
