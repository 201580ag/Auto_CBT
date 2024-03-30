import json
import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

def decrypt_password(encrypted_password):
    # base64 디코딩을 통해 암호화된 비밀번호를 복호화합니다.
    decrypted_password = base64.b64decode(encrypted_password).decode()
    return decrypted_password

# JSON 파일에서 데이터 읽기
with open('./config/config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

encrypted_password = data['비밀번호']
cbt_id = data['아이디']
event = data['기능사 종목']
cbt_pass = decrypt_password(encrypted_password)

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 자동화 메시지 제거
chrome_options.add_argument("--force-dark-mode")# 브라우저 다크 모드 활성화
chrome_options.add_argument('--incognito')# 브라우저 시크릿 탭 모드
chrome_options.add_argument("--start-maximized") # 브라우저 창 최대화

driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://www.comcbt.com/xe/?mid=outlogin&cbt_server_name=www.comcbt.com&hack_number=0&javer=0')

driver.implicitly_wait(3)

input1 = driver.find_element(By.XPATH, '//*[@id="fo_login_widget"]/div/div/input[1]')
input1.send_keys(cbt_id)

input2 = driver.find_element(By.XPATH, '//*[@id="fo_login_widget"]/div/div/input[2]')
input2.send_keys(cbt_pass)
driver.implicitly_wait(3)

button = driver.find_element(By.XPATH, '//*[@id="fo_login_widget"]/div/input')
button.click()
driver.implicitly_wait(3)

button = driver.find_element(By.XPATH, '/html/body/center/table/tbody/tr/td/div/table/tbody/tr/td[1]/center/form[1]/input[8]')
button.click()
driver.implicitly_wait(3)

button = driver.find_element(By.XPATH, '/html/body/table[1]/tbody/tr[2]/td[1]/form/input[3]')
button.click()
driver.implicitly_wait(3)

option = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/form/p/select/option[5]')
option.click()
driver.implicitly_wait(3)

button = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/form/p/input[3]')
button.click()
driver.implicitly_wait(3)

select_element = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/form/p/select')
select = Select(select_element)
select.select_by_value(event)
driver.implicitly_wait(3)

button = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/form/p/input[3]')
button.click()
driver.implicitly_wait(3)

button = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/form/p/input[11]')
button.click()
driver.implicitly_wait(3)

button = driver.find_element(By.XPATH, '//*[@id="cjbutton"]')
button.click()
driver.implicitly_wait(3)

time.sleep(999999999) # 브라우저 종료 방지