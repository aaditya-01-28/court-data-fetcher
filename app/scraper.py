import time
import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_case_data(case_type, case_no, case_year):
    """
    Fetches case data from Delhi High Court website using undetected-chromedriver.
    """
    # *** USE undetected_chromedriver INSTEAD OF THE STANDARD DRIVER ***
    driver = uc.Chrome(headless=False, use_subprocess=True)

    try:
        driver.get("https://delhihighcourt.nic.in/dhc_case_status_list_new.asp")
        
        wait = WebDriverWait(driver, 15) # Increased wait time slightly
        case_type_dropdown = wait.until(EC.presence_of_element_located((By.ID, "ccasetype")))
        
        # ... The rest of the code is the same ...
        Select(case_type_dropdown).select_by_value(case_type)
        driver.find_element(By.ID, "cno").send_keys(case_no)
        driver.find_element(By.ID, "cyear").send_keys(case_year)
        
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!! Please solve the CAPTCHA in the browser window.  !!!")
        print("!!! After solving, press Enter in this console.      !!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        input("Press Enter to continue...")
        driver.find_element(By.NAME, "Submit").click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "history-div")))

        if "Record not Found" in driver.page_source or "Invalid details" in driver.page_source:
            return {"error": "Invalid case number or details. Record not found."}, driver.page_source
        
        parties_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(., 'Petitioner(s)')]/following-sibling::td")))
        parties = parties_element.text
        
        filing_date_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(., 'Date of Filing')]/following-sibling::td")))
        filing_date = filing_date_element.text

        try:
            next_hearing_date_element = driver.find_element(By.XPATH, "//td[contains(., 'Next Date of Hearing')]/following-sibling::td/font")
            next_hearing_date = next_hearing_date_element.text
        except:
            next_hearing_date = "Not specified"

        order_links = []
        links = driver.find_elements(By.XPATH, "//div[@class='history-div']//a[contains(@href, 'Uploaded_File')]")
        for link in links:
            order_links.append({
                "text": link.text.strip(),
                "url": link.get_attribute("href")
            })

        raw_html = driver.page_source

        return {
            "parties": parties,
            "filing_date": filing_date,
            "next_hearing_date": next_hearing_date,
            "orders": order_links[:5]
        }, raw_html

    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": f"An unexpected error occurred. Please check the console. Details: {e}"}, driver.page_source
    finally:
        time.sleep(2) 
        driver.quit()