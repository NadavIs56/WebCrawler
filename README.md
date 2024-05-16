#  <p align ="center" height="40px" width="40px"> WebCrawler </p>

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

##     <p align = "left"> 📝 Conclusion </p>
This project demonstrates the implementation of a web crawler with robust error handling, efficient data structures, and clear logging. The code is organized, well-documented, and tested, providing a solid foundation for further development and scalability.

