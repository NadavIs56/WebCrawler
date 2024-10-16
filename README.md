#  <p align ="center" height="40px" width="40px"> WebCrawler 🕸️ </p>

### <p align ="center"> Implemented using: </p>
<p align ="center">
<a href="https://beautiful-soup-4.readthedocs.io/en/latest/#" target="_blank" rel="noreferrer">   <img src="https://db0dce98.rocketcdn.me/en/files/2024/01/beautiful-soup.png" width="80" height="48" /></a>
<a href="https://docs.aiohttp.org/en/stable/" target="_blank" rel="noreferrer">   <img src="https://kinsta.com/wp-content/uploads/2023/04/aiohttp.png" width="80" height="48" /></a>
<a href="https://www.python.org/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" width="48" height="48" /></a>
<a href="https://docs.python.org/3/library/asyncio.html" target="_blank" rel="noreferrer">   <img src="https://miro.medium.com/v2/resize:fit:750/1*6R6elwexUmNnLc1EJJ-t9g.jpeg" width="80" height="48" /></a>
<a href="https://docs.pytest.org/en/8.2.x/" target="_blank" rel="noreferrer">   <img src="https://media.licdn.com/dms/image/v2/D5612AQGJX_fKnD8pdg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1695384787213?e=1734566400&v=beta&t=T44X1c_meqgUcU7LapFFjB7xdBJ3eVAiAw6QDtTLv5Q" width="80" height="48" /></a>
</p>

<br>

##     <p align = "left"> 🌟 Introduction </p>
This project is designed to build a web crawler that, given an entry point for a website (e.g., https://example.com), downloads all pages of the website into a designated local folder. The crawler ensures that each page is downloaded only once.

<br>

##     <p align = "left"> 📂 Repository Structure </p>
The repository contains the following files and directories:
```bash
WebCrawler_Arato.ai/
│
├── crawler/
│ ├── init.py
│ └── crawler.py
│
├── downloaded_pages/ # This directory will be created when running the script, not included initially
│
├── tests/
│ ├── init.py
│ ├── test_crawler.py
│ └── test_downloaded_pages/ # This is the directory created during tests, not included initially
│
├── main.py
├── README.md
└── requirements.txt
```
- main.py - The entry point of the script, which handles command-line arguments and starts the web crawler.
- crawler.py - Contains the WebCrawler class, which implements the core functionality of the web crawler.
- test_crawler.py - Contains tests to verify the functionality of the web crawler.
- README.md - This file, which provides an overview of the project and instructions on how to use it.
- requirements.txt - Lists the Python dependencies required to run the project.

<br>
 
##     <p align = "left"> 💻 Installation </p>
To set up and run the web crawler, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/NadavIs56/WebCrawler_Arato.ai.git
cd WebCrawler_Arato.ai
```
2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```

<br>

##     <p align = "left"> 📘 Usage </p>

You can run the web crawler by executing the main.py script. The script accepts a URL and an optional directory argument to specify where the pages should be saved (Set to "downloaded_pages" by default).<br>If the URL is not provided or is invalid, the script will prompt you to enter a valid URL.<br><br>
**Example command:**
```bash
python main.py https://example.com --directory custom_folder
```

<br>

##     <p align = "left"> 🛠️ System Design </p>
The web crawler is designed with modularity and efficiency in mind, leveraging asynchronous I/O operations for handling multiple network requests concurrently. The core components of the system include:
1. **URL Fetching:** Asynchronously fetches the HTML content of web pages.
2. **HTML Parsing:** Uses BeautifulSoup to parse HTML content and extract links.
3. **URL Management:** Keeps track of visited URLs and those yet to be visited, ensuring each URL is processed only once.
4. **Content Storage:** Saves the HTML content of each page to a designated local folder, with filenames derived from the sanitized URLs.


### System Components and Their Responsibilities
**1. main.py:**
- Entry point for the script.
- Parses command-line arguments.
- Validates the provided URL.
- Initializes and starts the WebCrawler.

**2. crawler.py:**
- Contains the WebCrawler class.
- Implements methods for fetching, downloading, parsing, and managing URLs.
- Ensures that each page is downloaded only once and stored with a unique filename.

**3. test_crawler.py:**
- Contains tests for verifying the functionality of the web crawler using the pytest framework.
- Tests include checking for non-HTML content, correct downloading, domain restriction, and content hashing.

<br>

##     <p align = "left"> ⚠️ Potential Bottlenecks and Mitigations </p>
In the context of this web crawler, potential bottlenecks refer to points in the system where performance issues or inefficiencies may occur. Identifying these bottlenecks is crucial for ensuring the crawler runs efficiently and scales well. Mitigations are strategies or solutions to address these bottlenecks and improve the system's overall performance and reliability.
### 1. Network Latency and I/O Operations:
**Mitigation:** Use asynchronous I/O to handle multiple requests concurrently, reducing idle wait times.
### 2. CPU Utilization:
**Mitigation:** Offload CPU-intensive tasks like hashing to separate workers or use parallel processing.
### 3. Memory Usage:
**Mitigation:** Limit the number of URLs (Maximum 10) processed concurrently and use efficient data structures (Sets) to manage URLs.

<br>

##     <p align = "left"> 📊 Efficient Data Structures </p>
- **Sets:** Used for visited_urls and visited_hashes to ensure O(1) average-time complexity for membership checks.
- **Queue:** A deque or a priority queue can be used for managing URLs to be visited, ensuring efficient append and pop operations.

<br>

##     <p align = "left"> 📝 Conclusion </p>
This project demonstrates the implementation of a web crawler with robust error handling, efficient data structures, and clear logging. The code is organized, well-documented, and tested, providing a solid foundation for further development and scalability.

<br>

<div align="center">
  Made with ❤️ by <a href="https://github.com/NadavIs56">Nadav Ishai</a>
</div>
