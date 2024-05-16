from urllib.parse import urlparse
from crawler import WebCrawler
import pytest
import os

@pytest.mark.asyncio
async def test_webcrawler_non_html_content():
    """
    Test that the web crawler skips non-HTML content.
    Ensures no HTML files are downloaded from a non-HTML URL.
    """
    start_url = 'https://httpbin.org/image'
    download_folder = 'test_downloaded_pages'
    crawler = WebCrawler(start_url, download_folder)
    await crawler.run()
    # Ensure no HTML files are downloaded since it's a non-HTML content
    downloaded_files = [f for f in os.listdir(download_folder) if f.endswith('.html')]
    assert len(downloaded_files) == 0


@pytest.mark.asyncio
async def test_webcrawler_correct_downloading():
    """
    Test that the web crawler correctly downloads HTML content.
    Ensures that the visited_urls set is not empty and at least one HTML file is downloaded.
    """
    start_url = 'https://httpbin.org'
    download_folder = 'test_downloaded_pages'
    crawler = WebCrawler(start_url, download_folder)
    await crawler.run()
    assert len(crawler.visited_urls) > 0
    assert os.path.exists(download_folder)
    downloaded_files = [f for f in os.listdir(download_folder) if f.endswith('.html')]
    assert len(downloaded_files) > 0

@pytest.mark.asyncio
async def test_webcrawler_domain_restriction():
    """
    Test that the web crawler only visits URLs within the same domain.
    Ensures that all visited URLs have the same network location as the start URL.
    """
    start_url = 'https://httpbin.org'
    download_folder = 'test_downloaded_pages'
    crawler = WebCrawler(start_url, download_folder)
    await crawler.run()
    for url in crawler.visited_urls:
        assert urlparse(url).netloc == 'httpbin.org'

@pytest.mark.asyncio
async def test_webcrawler_page_content_hashing():
    """
    Test that the web crawler hashes the content of visited pages.
    Ensures that the visited_hashes set contains hashes of downloaded content.
    """
    start_url = 'https://httpbin.org'
    download_folder = 'test_downloaded_pages'
    crawler = WebCrawler(start_url, download_folder)
    await crawler.run()
    # Check that the visited_hashes set contains hashes of downloaded content
    assert len(crawler.visited_hashes) > 0

if __name__ == '__main__':
    pytest.main()
