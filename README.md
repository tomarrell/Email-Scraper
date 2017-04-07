# Email Scraper
A program to scrape Google searches for websites, then attempts to match regex in the search results for email addresses and the same on their respective contact pages. If no emails are found, the program will take a guess using the current domain.

## Installation
The program requires installation of the following Python packages:
- requests
- beautifulsoup4
Use "pip install [PackageName]" in the command line to install the above dependencies.

## Usage
Navigate to the program's root directory in your command line and run the command:
python main.py ["Google", "Search Terms", "Here"]
Where each string in the argument array is a new Google Search term to scrape.

I highly recommend using a proxy with multiple IP addresses as email scraping is not quite legal in most parts of the world. Scraping Google Search results is also against their TOS. Please be aware the developer will not be held responsible for any legal action taken against any individual using this code or any of its output.

## Output
Emails will all be output on a new line in /data/emails.txt. These include duplicates, it is recommended you put these through an online tool to remove duplicates. It has been noticed image URL's will slip through the regular expression, these can be found by searching the file for "png" or "jpeg."

## Disclaimer
This program is provided as is for educational use only. By using this program you agree to waive the developer of any responsibilities that occur due to your use of the program or its output.

