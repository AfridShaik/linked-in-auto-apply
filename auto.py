from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

# Set up the Chrome webdriver
driver = webdriver.Chrome()

# Open the LinkedIn website
driver.get('https://www.linkedin.com')

# Log in to your account
wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.ID, 'session_key')))
username.send_keys('afridali102@gmail.com')
password = wait.until(EC.presence_of_element_located((By.ID, 'session_password')))
password.send_keys('Sharina8$')
password.send_keys(Keys.RETURN)


# Navigate to the job search page
driver.get('https://www.linkedin.com/jobs')

# Search for the desired job role
# Search for the desired job role
search_bar = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'jobs-search-box__text-input')))
search_bar.send_keys('java full stack webdeveloper intership')
search_bar.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Find and apply to a job
# Note: This will apply to the first job in the list. You might want to add more logic to select the right job.
# Traceback (most recent call last):
#   File "C:\Users\afrid\Documents\Python\auto.py", line 46, in <module>
#     apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'artdeco-button__icon')))        
#                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        
#   File "C:\Python312\Lib\site-packages\selenium\webdriver\support\wait.py", line 101, in until
#     raise TimeoutException(message, screen, stacktrace)
# selenium.common.exceptions.TimeoutException: Message:
job_link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'job-card-container__link')))
job_link.click()

# Wait for the apply button to be clickable
apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'jobs-apply-button artdeco-button artdeco-button--icon-right artdeco-button--3 artdeco-button--primary ember-view')))
apply_button.click()

# Fill out the application form
# You'll need to inspect the elements on the application form and use the appropriate methods to fill them out

# Submit the application
submit_button = driver.find_element_by_class_name('submit-button')
submit_button.click()

# Close the browser
time.sleep(5)  # Wait for 5 seconds before closing the browser
driver.quit()