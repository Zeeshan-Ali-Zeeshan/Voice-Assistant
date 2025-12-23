from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def send_message(contact_name, message):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:/whatsapp-session")  # Persist session
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    service = Service("C:/chromedriver/chromedriver.exe")  # Adjust path as needed
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://web.whatsapp.com")
    driver.minimize_window()
    
    print("🔄 Waiting for WhatsApp Web to load...")
    time.sleep(10)  # Allow time for QR scan or auto-login

    try:
        wait = WebDriverWait(driver, 20)

        # Search and select contact
        search_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@role="textbox" and @contenteditable="true"]')
        ))
        search_box.click()
        time.sleep(1)
        search_box.clear()
        search_box.send_keys(contact_name)
        time.sleep(2)

        contact = wait.until(EC.presence_of_element_located(
            (By.XPATH, f'//span[@title="{contact_name}"]')
        ))
        contact.click()
        time.sleep(2)

        # Send the message
        message_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@role="textbox" and @contenteditable="true" and not(ancestor::div[@data-testid="chat-list-search"]) and not(ancestor::div[@data-testid="search-input"]) and not(@data-tab="3")]')
        ))
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        print(f"✅ Message sent to {contact_name}!")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        time.sleep(5)
        driver.quit()

# === Input from user ===
if __name__ == "__main__":
    contact_name = input("Enter contact name: ")
    message = input("Enter your message: ")
    send_message(contact_name, message)
