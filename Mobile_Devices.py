from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Hello\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe")

driver.get("https://demoblaze.com/")
driver.maximize_window()
time.sleep(5)
Name=[]
Specifications=[]
s=driver.find_elements_by_xpath('//*[@id="tbodyid"]/div/div/div/h4/a')
for i in s:
    j=i.text
    Specifications.append(j)
    print(Specifications)
    x=j.split(" ")
    if x[0] not in Specifications:
        Name.append(x[0])
print(Name)
price=[]
p=driver.find_elements_by_xpath("//*[@id='tbodyid']/div[1]/div/div/h5")
for cs in p:
    print(cs.text)


print(Name[0],cs.text)

