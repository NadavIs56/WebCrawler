from urllib.parse import urljoin, urlparse, quote
from bs4 import BeautifulSoup, SoupStrainer
import aiohttp
import asyncio
import logging
import hashlib
import os

logging.basicConfig(level=logging.INFO)

class WebCrawler:
    def __init__(self, start_url, download_folder):
        """
        Initializes the WebCrawler with a start URL and a download folder.
        :param start_url: The initial URL to start crawling from.
        :param download_folder: The directory to save downloaded HTML files.
        """
        self.start_url = start_url
        self.download_folder = download_folder
        self.visited_urls = set()
        self.visited_hashes = set()         # store the hashes of the content of visited pages
        self.to_visit = {start_url}
        self.start_netloc = urlparse(start_url).netloc
        logging.info(f"WebCrawler initialized with start URL: {start_url} and download folder: {download_folder}")

    async def fetch(self, session, url):
        """
        Fetches the content of the given URL using an asynchronous HTTP GET request.
        :param session: The HTTP session to use for making requests.
        :param url: The URL to fetch content from.
        :return: str or None: The HTML content of the page if successful, None otherwise.
        """
        try:
            async with session.get(url, timeout=10) as response:            # initiates an asynchronous HTTP GET request, allowing other tasks to run in the meantime
                response.raise_for_status()
                if 'text/html' in response.headers.get('Content-Type', ''):
                    return await response.text()                            # until the response content is fully read other tasks allowed to run
                else:
                    logging.info(f"Skipping non-HTML content at {url}")
                    return None
        except Exception as e:
            logging.error(f"Error fetching {url}: {e}")
            return None

    async def download_page(self, session, url):
        """
        Downloads the content of the given URL and saves it to the download folder.
        :param session: The HTTP session to use for making requests.
        :param url: The URL to download content from.
        :return: str or None: The HTML content of the page if successful, None otherwise.
        """
        content = await self.fetch(session, url)
        if content:
            sanitized_filename = self.sanitize_url(url)                                 # create a valid and unique filename
            file_path = os.path.join(self.download_folder, sanitized_filename)
            os.makedirs(self.download_folder, exist_ok=True)
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            except Exception as e:
                logging.error(f"Error writing to file {file_path}: {e}")
            return content
        return None

    def sanitize_url(self, url):
        """
        Sanitizes the URL to create a valid filename.
        :param url: The URL to be sanitized.
        :return: str: A valid filename derived from the URL.
        """
        parsed_url = urlparse(url)
        path = quote(parsed_url.path.strip('/'), safe='')  # Remove leading/trailing slashes and quote
        filename = f"{parsed_url.netloc}_{path}"
        return filename if filename.endswith('.html') else f"{filename}.html"

    def hash_content(self, content):
        """
        Computes the SHA-256 hash of the given content.
        :param content: The content to be hashed.
        :return: str: The hexadecimal SHA-256 hash of the content.
        """
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    async def crawl(self, session, url):
        """
        Crawls the given URL, downloads its content, and discovers new URLs to visit.
        :param session: The HTTP session to use for making requests.
        :param url: The URL to crawl.
        """
        content = await self.download_page(session, url)            # contains the entire HTML structure of the webpage as a text string
        if content:
            content_hash = self.hash_content(content)
            if content_hash in self.visited_hashes:                 # checks if we already visited this page
                # logging.info(f"Skipping already visited URL: {url}")
                return
            self.visited_hashes.add(content_hash)

            strainer = SoupStrainer('a', href=True)                 # use SoupStrainer to parse only <a> tags with href attributes
            soup = BeautifulSoup(content, 'html.parser', parse_only=strainer)           # a parsed representation of the HTML content

            for link in soup:
                absolute_url = urljoin(url, link['href'])
                absolute_netloc = urlparse(absolute_url).netloc
                if absolute_url not in self.visited_urls and absolute_url not in self.to_visit and absolute_netloc == self.start_netloc:
                    self.to_visit.add(absolute_url)

    async def run(self):
        """
        Manages the crawling process by visiting URLs in batches and processing them asynchronously.
        """
        logging.info("Starting the crawling process")
        async with aiohttp.ClientSession() as session:
            while self.to_visit:
                current_batch = list(self.to_visit)
                self.to_visit.clear()
                tasks = [self.crawl(session, url) for url in current_batch if url not in self.visited_urls]
                self.visited_urls.update(current_batch)
                if tasks:
                    await asyncio.gather(*tasks)                # runs all the tasks concurrently and waits for them to complete
        logging.info("Crawling process completed")