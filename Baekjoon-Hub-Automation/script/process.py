import time
import GUI
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def set_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return driver
#####

def start_setting_BJ(id, pw, i, driver):

    if i!=True:
        url = 'https://www.acmicpc.net/login'
        driver.get(url)
        selector = "#submit_button"
        time.sleep(1)
        driver.find_element(By.NAME, 'login_user_id').send_keys(id)
        driver.find_element(By.NAME, 'login_password').send_keys(pw)
        elem = driver.find_element(By.CSS_SELECTOR, selector)
        elem.click()
        time.sleep(2)
    login_check= driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/ul/li[3]/a") # 로그인 여부 확인용 "로그인" 텍스트 인식
    if login_check.text=="로그인":
        return -1

    else:
        driver.get('https://www.acmicpc.net/user/' + id)
        Peoblem_list = '/html/body/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div'
        time.sleep(1)
        elem = driver.find_element(By.XPATH, Peoblem_list)
        all = elem.text.split()
        return all





def start_BJ(id,elem,driver,t):

    for j in elem:
        driver.get("https://www.acmicpc.net/status?from_mine=1&problem_id=%s&user_id=%s"%(j,id))
        time.sleep(t)



def start_nat_BJ(driver):
    driver.get('https://www.acmicpc.net/login')


def start_EP(driver):
    driver.get('https://chrome.google.com/webstore/detail/%EB%B0%B1%EC%A4%80%ED%97%88%EB%B8%8Cbaekjoonhub/ccammcjdkpgjmcpijpahlehmapgmphmk?hl=ko')







