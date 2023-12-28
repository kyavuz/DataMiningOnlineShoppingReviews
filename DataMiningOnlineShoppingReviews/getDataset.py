from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--headless")

service = Service('E:/Kağan/Heçkırlık/PYTHON/selenium/chromeDriver119/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chromeOptions)

driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://www.amazon.com/Samsung-Chromebook-Celeron-Processor-Gigabit/product-reviews/B07XQQTVS3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")
driver.implicitly_wait(10)

commentCount = range(int(120))

xPATH = f'//*[@id="cm_cr-review_list"]'  # amazon review list
comment = driver.find_element(By.XPATH, xPATH).text

start_text = "Reviewed in the "
end_text = "Helpful"

comment_list = []
try:
    for number in commentCount:
        indx = number + 1

        start_index = comment.find(start_text)
        end_index = comment.find(end_text)+7

        if start_index != -1 and end_index != -1:
            result = comment[start_index + len(start_text):end_index].strip()
            #print('-----------------------------------------------------------------------------')
            #print(result)
            comment_list.append(result)
            #print('-----------------------------------------------------------------------------')
            comment = comment[end_index:]
        else:
            #print("There is no text in this page")
            # Click the "Next Page" button
            try:
                next_button = driver.find_element(By.XPATH, '//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
                next_button.click()
                # Wait for the next page to load
                driver.implicitly_wait(5)
                xPATH = f'//*[@id="cm_cr-review_list"]'  # amazon review list
                comment = driver.find_element(By.XPATH, xPATH).text
            except Exception as e:
                # Code to handle other exceptions
                #print(f"An error occurred: {e}")
                pass

        #print(comment)
        #comment = comment[end_index:]
        # print(XPATH)
except:
    print('Something went wrong')

import io
with io.open('user_reviews.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(comment_list))


