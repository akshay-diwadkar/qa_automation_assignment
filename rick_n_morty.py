import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

timeout = 1

def open_demo_website():
    driver = webdriver.Chrome(executable_path="C:\\Users\\adiwad\\Downloads\\chromedriver.exe")
    # driver.get("http://10.100.171.218:3000/")
    driver.get("http://localhost:3000/")
    return driver

def login(driver, username, password):
    time.sleep(timeout)
    email_field = driver.find_element(By.XPATH, "(//input[@id='outlined-basic'])[1]")
    email_field.send_keys(username)
    time.sleep(timeout)
    password_field = driver.find_element(By.XPATH, "(//input[@id='outlined-basic'])[2]")
    password_field.send_keys(password)
    time.sleep(timeout)
    login_button = driver.find_element(By.XPATH,  "//button")
    login_button.click()
    time.sleep(timeout)
    print("User is logged in application")

def search(driver, search_term):
    search_field = driver.find_element(By.XPATH, "//input")
    search_field.send_keys(search_term)
    time.sleep(timeout)
    search_list = []
    action = ActionChains(driver)
    while True:
        # for_parent_of_last = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]/../../../div[@class="MuiDataGrid-row MuiDataGrid-row--lastVisible"]')
        for_parent_of_last = driver.find_elements(By.XPATH, "//div[@data-rowindex = '19']")
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        for i in res:
            if i.text not in search_list:
                search_list.append(i.text)
        action.scroll_to_element(res[-1]).perform()
        if for_parent_of_last:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "19"]/div[@data-field="name"]/div[text()]')
            search_list.append(res.text)
            break
        time.sleep(timeout)
    for each_name in search_list:
        if search_term not in each_name:
            print("Error: Wrong result present in search")
            return []
    print("Search results validated!")
    # print(f"Searched list: {search_list}, len={len(search_list)}")
    time.sleep(timeout)
    
    
def scroll_to_top(driver):
    action = ActionChains(driver)
    print("Scrolling to top")
    while True:
        for_parent_of_first = driver.find_elements(By.XPATH, "//div[@data-rowindex = '1']")
        res = driver.find_elements(By.XPATH, '//div[@data-field="name"]/div[text()]')
        action.scroll_to_element(res[0]).perform()
        if for_parent_of_first:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "1"]/div[@data-field="name"]/div[text()]')
            break
        time.sleep(timeout)


def sorting_a(driver):
    sort_list = []
    scroll_to_top(driver)
    sort_button = driver.find_element(By.XPATH, '//div/div[text()="Name"]/../../div/button[@title="Sort" and @type="button"]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    action = ActionChains(driver)

    while True:
        for_parent_of_last = driver.find_elements(By.XPATH, "//div[@data-rowindex = '19']")
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        for i in res:
            if i.text not in sort_list:
                sort_list.append(i.text)
        action.scroll_to_element(res[-1]).perform()
        if for_parent_of_last:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "19"]/div[@data-field="name"]/div[text()]')
            sort_list.append(res.text)
            break
        time.sleep(timeout)
    error_raised = False
    for i in range(len(sort_list)-1):
        if sort_list[i] > sort_list[i+1]:
            error_raised = True
    if not error_raised:
        print("Ascending Sort Validated!")
    else:
        print("Error: Ascending Sort Failed!")
    # print(f"sorted-list = {sort_list}")
    time.sleep(timeout)

def sorting_d(driver):
    sort_list = []
    scroll_to_top(driver)
    sort_button = driver.find_element(By.XPATH, '//div/div[text()="Name"]/../../div/button[@title="Sort" and @type="button"]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    action = ActionChains(driver)

    while True:
        for_parent_of_last = driver.find_elements(By.XPATH, "//div[@data-rowindex = '19']")
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        for i in res:
            if i.text not in sort_list:
                sort_list.append(i.text)
        action.scroll_to_element(res[-1]).perform()
        if for_parent_of_last:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "19"]/div[@data-field="name"]/div[text()]')
            sort_list.append(res.text)
            break
        time.sleep(timeout)
    error_raised = False
    for i in range(len(sort_list)-1):
        if sort_list[i] < sort_list[i+1]:
            error_raised = True
    if not error_raised:
        print("Descending Sort Validated!")
    else:
        print("Error: Descending Sort Failed!")
    # print(f"sorted-list = {sort_list}")
    time.sleep(timeout)

driver = open_demo_website()
username = "johndoe@gmail.com"
password = "123456789"

login(driver, username, password)

search(driver, "Rick")

sorting_a(driver)

sorting_d(driver)

driver.quit()