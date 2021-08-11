from selenium import webdriver
import time

driver_path = "C:\\Users\\abc\\Desktop\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

driver.get("https://seller.indiamart.com/")

signin = driver.find_element_by_id('lshead')

signin.click()

mobileNumEntry = driver.find_element_by_id('mobile')
mobileNumEntry.send_keys('7774004912')

sbmBtn = driver.find_element_by_id('logintoidentify')
sbmBtn.click()

time.sleep(5)

leadManager = driver.find_element_by_id('lead_manager')
leadManager.click()

time.sleep(5)

# reqOtpMobBtn = driver.find_element_by_id('reqOtpMobBtn')
enterPassword = driver.find_element_by_id('passwordbtn1')
enterPassword.click()

otpEmail = driver.find_element_by_id('otp_login_em')
otpEmail.click()

print('-'*50)
print("TYPE OTP OF THE FORM....")
print('-'*50)
input('Press any button when Done!!')

time.sleep(5)

unreadMsg = driver.find_element_by_id('cb-unrd-div')
unreadMsg.click()

time.sleep(10)

count = 0
while count < 100:
    time.sleep(2)
    chat = driver.find_element_by_id(f'{count}')
    chat.click()
    time.sleep(2)
    sendBtn = driver.find_element_by_id('send-reply-span')
    quickText = driver.find_elements_by_class_name('tooltip.slr-chatSgtnBlk.usr-def-temp')
    try:
        for i in quickText:
            print(i.text())
        # print(quickText[4].text())
        # if "hello" in str(quickText[4].text()):
        #     quickText[4].click()
        #     count += 1
    except:
        count += 1
        pass
    # count += 1
    # time.sleep(2)
    # sendBtn.click()
    # cnt = 0
    # while cnt < 3:
    #     attachment = driver.find_element_by_id('attachment_icon')
    #     attachment.click()
    #     cls = driver.find_elements_by_class_name('drive_flname')
    #     cls[cnt].click()
    #     drvBtn = driver.find_element_by_id('drive_insert')
    #     drvBtn.click()
    #     cnt += 1
    count += 1
