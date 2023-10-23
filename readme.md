# Python Proxy Scraper

This project contains a Python script that scrapes the website `https://www.sslproxies.org/` to obtain a list of proxies. The list is then written to a `.txt` file.

## Getting Started

### Prerequisites

To run this script, you'll need the following installed:

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4
```
After running the script, you'll find a file named `ips_list.txt` in your directory, which contains the scraped proxies, each on a new line.

## Structure

The project consists of a main scraper class named `Scrape` in the `scrape.py` file. This class is responsible for fetching and parsing the webpage to extract the required proxy data. 

## Contribution

Feel free to fork this repository and enhance the code. Pull requests with improvements are also welcomed!

## License

This project is open source and available under the [MIT License](LICENSE).
