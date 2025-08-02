# Court-Data Fetcher & Mini-Dashboard

This web application is designed to fetch case metadata and judicial orders from the Delhi High Court website. A user can input a case type, number, and year, and the backend attempts to programmatically scrape the public information for display. This project was built to fulfill the requirements of Task 1 of the internship assignment.

## Features

* **Simple Web UI:** A clean interface built with Flask allows users to input case details.
* **Automated Backend:** Uses `undetected-chromedriver` to navigate the court website and handle form submissions.
* **Query Logging:** Every search attempt and its raw HTML response is logged to a **PostgreSQL** database for auditing and debugging.
* **Data Display:** Renders successfully fetched details, including party names, dates, and order links, in a user-friendly format.

## Technology Stack

* **Backend:** Python, Flask
* **Scraping:** Selenium, undetected-chromedriver
* **Database:** **PostgreSQL**, SQLAlchemy
* **Frontend:** HTML, CSS

## Setup and Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/aaditya-01-28/court-data-fetcher](https://github.com/aaditya-01-28/court-data-fetcher)
    cd court-data-fetcher
    ```

2.  **Set Up PostgreSQL Database**
    * Make sure you have PostgreSQL installed and running.
    * Create a new database for this project by running `CREATE DATABASE court_app_db;` in `psql`.

3.  **Create and Activate Virtual Environment**
    * On Windows (PowerShell):
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate.ps1
        ```

4.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Database Connection**
    * Open the `app/database.py` file.
    * Update the `DATABASE_URL` string with your PostgreSQL username, password, and database name.
        ```python
        DATABASE_URL = "postgresql://your_user:your_password@localhost/court_app_db"
        ```

6.  **Run the Application**
    ```bash
    python run.py
    ```
    Navigate to `http://127.0.0.1:5001` in your web browser.

## Blocker: Advanced Anti-Scraping Measures & Website Unavailability

A significant challenge in this project is the highly effective anti-bot system on the target website.

The server actively detects browser automation and returns a `404 Not Found` error to block the scraper. A series of advanced techniques were employed to bypass this block, including:

1.  Masking the browser's user-agent.
2.  Using `selenium-stealth` to patch the standard driver.
3.  Switching to `undetected-chromedriver`, a specialized library designed to evade bot detection.

Despite these efforts, the protection remained effective. Ultimately, the website became completely unavailable, serving a "File not found." error even to regular browsers. As per the internship guidelines to **"document blockers in the README rather than ghosting,"** this issue is documented as the project's primary impediment.