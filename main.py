from crawler import WebCrawler
import validators
import argparse
import asyncio


def get_valid_url():
    """Prompt the user to enter a valid URL in a loop until a valid URL is provided."""
    while True:
        url = input("Please enter a valid URL: ")
        if validators.url(url):
            return url
        else:
            print("The URL provided is not valid. Please try again.")

def main():
    """
    Entry point for the web crawler script.
    Parses command-line arguments to get the starting URL and download directory.
    Initializes and runs the web crawler.
    """
    parser = argparse.ArgumentParser(description="Web Crawler")
    parser.add_argument("url", nargs='?', help="The starting URL for the web crawler")
    parser.add_argument("--directory", "-d", default="downloaded_pages", help="The directory to save the downloaded pages")
    args = parser.parse_args()

    start_url = args.url
    download_folder = args.directory

    if not start_url or not validators.url(start_url):          # validate the URL
        print("The URL provided is not valid.")
        start_url = get_valid_url()

    crawler = WebCrawler(start_url, download_folder)
    asyncio.run(crawler.run())

if __name__ == '__main__':
    main()
