from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


def run(code):
    # Directly specify the path to your downloaded ChromeDriver
    driver_path = "C:/Users/arthu/Desktop/Code/chromedriver-win64/chromedriver.exe"  # Replace this with the actual path
    service = Service(executable_path=driver_path)

    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-data-dir=C:/Users/arthu/AppData/Local/Google/Chrome/User Data"
    )
    options.add_argument("profile-directory=Default")  # Use the correct profile
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(
        "--disable-software-rasterizer"
    )  # Optional: to avoid GPU errors

    # Initialize the WebDriver with options
    driver = webdriver.Chrome(service=service, options=options)

    # Open the Binance cryptobox URL directly, assuming you are already logged in
    driver.get("https://www.binance.com/en/my/wallet/account/payment/cryptobox")

    # Find the code input box and submit button under it
    code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'input[placeholder="Enter red packet code"]')
        )
    )
    claim_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Claim"]'))
    )

    # Enter the code and click the submit button
    code_input.send_keys(code)
    claim_button.click()
    try:
        invalid_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[contains(text(),"Invalid Red Packet code")]')
            )
        )
        if invalid_message:
            print("Invalid Red Packet Code detected. Closing the driver.")
            driver.quit()

    except:
        print("No 'Invalid Red Packet Code' message detected.")

        # Wait for the "Claim" button in the popup and click it
        try:
            open_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//button[contains(text(),"Open")]')
                )
            )
            open_button.click()

            print("Clicked the 'Open' button in the popup!")
        except Exception as e:
            # Print the page source for debugging
            print(driver.page_source)
            print(f"Failed to click the 'Open' button. Error: {e}")

    # Close the WebDriver
    driver.quit()
