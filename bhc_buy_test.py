#%%
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(30)
    
    driver.get('https://101financial.app/auth/login')
    AccInput = driver.find_element(By.ID, 'account')
    pwd_input = driver.find_element(By.ID, 'password')
    
    login_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[3]/div/form/div[5]/button')
    
    AccInput.send_keys('aurora08')
    pwd_input.send_keys('123456Aa')
    
    login_button.click()
    
    man_icon_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[1]/button[6]'))
    )
    
    driver.get('https://101financial.app/m/markets/crypto?pg=3_hot')
    # MetaBuy_button = driver.find_element(By.XPATH, '//*[@id="cell-91"]/div/div/button[1]')
    # MetaBuy_button.click()
    BCH_tab = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div[2]/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div[3]')
    BCH_tab.click() 
    
    BCHBuy_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/button[1]'))
        )
    BCHBuy_button.click()
    
    
    
    BuyLimit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div[3]/form/div[1]/div/div/div[1]/div/button[2]'))
        )
    # TypeShare_button = driver.find_element(
    #     By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div/button[1]'
    #     )
    # ShareAdd_button = driver.find_element(
    #     By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div/div/div[3]/div/button[2]'
    #     )
    # ShareMinus_button = driver.find_element(
    #     By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div/div/div[3]/div/button[1]'
    #     )
    
    QuantMinus_button = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/form/div[1]/div/div/div[2]/div/button[1]'
        )
    PriceAdd_button = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/form/div[1]/div/div/div[3]/div/button[2]'
        )
    PriceMinus_button = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/form/div[1]/div/div/div[3]/div/button[1]'
        )
    Leverage5X_button = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[3]/form/div[1]/div/div/div[5]/div/button[4]'
        )
    
    PlaceOrder_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/form/div[3]/button[1]'))
    )
    
    BuyLimit_button.click()
    QuantMinus_button.click()
    
    #TypeShare_button.click()
    #QuantInput.clear()
    #QuantInput.send_keys('0.02')
    #ShareAdd_button.click()
    PriceMinus_button.click()
    Leverage5X_button.click()
    PlaceOrder_button.click()
    
    
    Postion_tab = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/nav/div/a[4]')
    Postion_tab.click()
    
    function_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/header/div/div[2]/button[2]')
    notify_button = driver.find_element(By.XPATH, '/html/body/div[2]/aside/div[2]/nav/ol[7]/div[2]')
    markRead_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/header/div/div[2]/button')
    
    
    
    
    
    
