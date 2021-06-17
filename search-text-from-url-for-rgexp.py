#!/usr/bin/env python
''' Crossword Solve
Scrape text from URL, search for regex.
This was originally designed to find a pattern matching "************ ********" for a CTF hosted
on Hack The Box which included a hint showing the number of characters expected in the answer.

## Example URL used for testing
https://en.wikipedia.org/wiki/Bash_(Unix_shell)
https://en.wikipedia.org/wiki/Command-line_interface

'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

###################################################################
url = input("Enter URL to search: ")

###################################################################
## This section is from: https://realpython.com/python-web-scraping-practical-introduction/

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
text_from_url = soup.get_text()

###################################################################
## This section is new, look for regex in text from URL
# Note: '- matches a "dash"

print("")
print("Strings matching 12-9 character pattern: ")

text_from_url = text_from_url.lower()
result = (set(re.findall(r"\b[a-zA-Z'-]{12}\b\s\b[a-zA-Z'-]{9}\b", text_from_url)))

for each_word in result:
    print("\t", each_word)