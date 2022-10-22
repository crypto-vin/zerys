# created by Vincent Munyalo 
# Github profile: https://github.com/crypto-vin

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import africastalking
from random import randint
import time
from datetime import datetime,date
from selenium.webdriver.remote.remote_connection import LOGGER
import os
import sys

class Zerys:
    def __init__(self, email, password, phone, loop_duration):
        self.email = email
        self.password = password
        self.loop_duration = loop_duration
        self.phone = phone
        self.prev_msg = ''
        self.prev_msg_list = []
        self.task_found = False
        self.login_url = 'https://writer.zerys.com/#/login'
        self.running = False
        self.f = open('bin/logs.txt', 'w')
        service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_experimental_option('prefs', {'credentials_enable_service': False,
                                                         'profile': {'password_manager_enabled': False}})
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    #get access to zerys' login site
    def get_site(self):
        self.driver.get(self.login_url)
        try:
            WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, ".//input[@placeholder='Email']"))
            ).click()
        except Exception as e:
            print(e)
        self.running = True
    
    # login to access dashboard
    def zerys_login(self, email, password):
        email_textbox = self.driver.find_element("xpath", ".//input[@placeholder='Email']")
        password_textbox = self.driver.find_element("xpath", ".//input[@placeholder='Password']")
        login_button = self.driver.find_element("xpath", ".//input[@class='full-width main_button']")
        time.sleep(randint(2,5))
        email_textbox.send_keys(self.email)
        time.sleep(randint(2,5))
        password_textbox.send_keys(self.password)
        time.sleep(randint(2,5))
        login_button.click()
        time.sleep(5)

    # check tasks on New Clients Board
    def check_new_clients(self, a):
        try:
            self.new_task = WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.XPATH, ".//div[@class='djc_available_job_tab']"))
                )
        except Exception as err:
            pass
        else:
            tasks_available = self.new_task.find_element("xpath", ".//a[@class='jc_avj_open_writer_tab']")
            total_tasks = tasks_available.text[-2:-1]
            f = open('bin/logs.txt', 'a+')
            if total_tasks != '0':
                print(f'\n--- Fetched data at {self.now} ---')
                with f:
                    f.write(f'\n\n--- Fetched data at {self.now} ---')
                if total_tasks == '1':
                    msg = f'A task has been posted in the New Clients Job tab. Check it out!'
                else:
                    msg = f'{total_tasks} tasks have been posted in the New Clients Job tab. Check them out!'
                with f:
                    f.write(f'\n{msg}')
                if msg not in self.prev_msg_list:
                    self.send_sms(msg)
                    self.prev_msg_list.append(msg)
                    self.task_found = True
            else:
                if a % 50 == 2:
                    print(f'\n\n--- Fetched data at {self.now} ---')
                    print(f'    No tasks in New Clients Job Board')
                    with f:
                        f.write(f'\n\n--- Fetched data at {self.now} ---')
                        f.write(f'\n    No tasks in New Clients Job Board')
                    self.prev_msg_list.clear()
    
    # check tasks on My Client Assignments
    def check_client_assignments(self, a):
        try:
            fav_tab = WebDriverWait(self.new_task, 60).until(
                    EC.presence_of_element_located((By.XPATH, ".//a[@class='jc_avj_favorite_writer_tab']"))
                )
        except Exception as err:
            pass
        else:
            f = open('bin/logs.txt', 'a+')
            total_tasks = fav_tab.text[-2:-1]
            if total_tasks != '0':
                print(f'\n--- Fetched data at {self.now} ---')
                with f:
                    f.write(f'\n\n--- Fetched data at {self.now} ---')
                if total_tasks == '1':
                    msg = f'A task has been posted in My Client Assignments tab. Check it out!'
                else:
                    msg = f'{total_tasks} tasks have been posted in My Client Assignments tab. Check them out!'
                with f:
                    f.write(f'\n{msg}')
                #print(msg)
                if msg not in self.prev_msg_list:
                    self.send_sms(msg)
                    self.prev_msg_list.append(msg)
                    self.task_found = True
            else:
                if a % 50 == 2:
                    msg = f'    No tasks in My Client Assignments'
                    print(msg)
                    with f:
                        f.write(f'\n{msg}')
    
    # send text notification once a task is spotted
    def send_sms(self, message):
        recipients = [self.phone,]
        username = 'algobet254'
        api_key='ca3772ca14af112280ae148c3cd969f46efc91eac893b0f544f722613d077bda'
        africastalking.initialize(username, api_key)
        sms = africastalking.SMS
        try:
            sms.send(message, recipients, None)
        except Exception as e:
            print (f'    Couldn\'t send sms: {e}')
            with self.f:
                self.f.write(f'    Couldn\'t send sms: {e}')


    # scan the website for new tasks
    def get_job(self, loop_duration):
        a = 0
        while True:
            self.now = datetime.now().time().replace(microsecond=0).isoformat()
            self.check_new_clients(a)
            self.check_client_assignments(a)
            time.sleep(loop_duration)
            if self.task_found:
                break
            try:
                self.driver.refresh()
                a += 1
            except:
                #print(f'    Could not refresh site')
                pass
    
    # terminate the process
    def terminate(self):
        try:
            self.driver.quit()
            
        except Exception as e:
            print(e)
            self.driver.get(self.login_url)
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, ".//input[@placeholder='Email']"))
            )

        sys.exit()

    # sequencially run the program
    def run(self):
        self.get_site()
        self.zerys_login(self.email, self.password)
        self.get_job(self.loop_duration)

if __name__ == "__main__":
    zerys = Zerys(email='topfreelancer87@yahoo.com', password='@Martin1111', loop_duration=5, phone='+254712897106')
    zerys.run()
