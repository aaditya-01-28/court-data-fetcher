# Court-Data Fetcher & Mini-Dashboard

This web application is designed to fetch case metadata and judicial orders from the Delhi High Court website. A user can input a case type, number, and year, and the backend attempts to programmatically scrape the public information for display. This project was built to fulfill the requirements of Task 1 of the internship assignment.

## Features

* **Simple Web UI:** A clean interface built with Flask allows users to input case details.
* **Automated Backend:** Uses `undetected-chromedriver` to navigate the court website and handle form submissions.
* **Query Logging:** Every search attempt and its raw HTML response is logged to a local SQLite database for auditing and debugging.
* **Data Display:** Renders successfully fetched details, including party names, dates, and order links, in a user-friendly format.

## Technology Stack

* **Backend:** Python, Flask
* **Scraping:** Selenium, undetected-chromedriver
* **Database:** SQLAlchemy, SQLite
* **Frontend:** HTML, CSS

## Setup and Installation

1.  **Clone the Repository**
    ```bash
    git clone <your-repo-url>
    cd court-data-fetcher
    ```

2.  **Create and Activate Virtual Environment**
    * On Windows (PowerShell):
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate.ps1
        ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    python run.py
    ```
    Navigate to `http://127.0.0.1:5001` in your web browser.

## Blocker: Advanced Anti-Scraping Measures

A significant challenge in this project is the highly effective anti-bot system on the target website.

The server actively detects browser automation and returns a `404 Not Found` error to block the scraper, even when the correct URL is requested. This happens before the CAPTCHA screen is even loaded. A series of advanced techniques were employed to bypass this block, including:

1.  Masking the browser's user-agent.
2.  Using `selenium-stealth` to patch the standard driver.
3.  Switching to `undetected-chromedriver`, a specialized library designed to evade bot detection.

Despite these efforts, the website's protection remains effective. As per the internship guidelines to **"document blockers in the README rather than ghosting,"** this issue is documented as the project's primary impediment.