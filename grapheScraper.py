import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pprint import pprint
from bs4 import BeautifulSoup
import platform
import time


chromeOptions = Options()

#chromeOptions.add_argument("--profile-directory=Profile 6")
#chromeOptions.add_argument('--disable-extensions')
if platform.system().lower() == "linux":
	chromeOptions.add_argument("--user-data-dir=/home/rohan/Desktop/projects/google_cookies")
	driver = webdriver.Chrome('chromedriver111.0.5563.64' , options=chromeOptions)
elif platform.system().lower() == "windows":
	chromeOptions.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 5")
	driver = webdriver.Chrome('chromedriver.exe' , options=chromeOptions)







def Scroll_to_end():
	All_Content_links=[]
	screenHeightCount = 1
	
	driver.get('https://www.instagram.com/thegraphe/' )
	countDown(10)
	
	#Getting the initial screen height after loading the page and printing It
	screen_height = driver.execute_script("return window.screen.height;")
	print(f"the current screen height is {screen_height}")
	


	
##################################################################################################
	#the loop to scroll to the end of the page
	while True:
		driver.execute_script(f"window.scrollTo(0 , {screen_height}*{screenHeightCount});")
		print(f" ======================== Scroll Execution {screenHeightCount} ==========================")
		countDown(4)

		
		#######################################################################
		#Scrpaping the data from the new loaded page with each iteration
		page_source_code = driver.page_source
		soup = BeautifulSoup(page_source_code , 'lxml')
		all_the_links_in_the_page = soup.find_all('a')

		
		for link in all_the_links_in_the_page:
			if '/p/' in link.get('href'):
				print(link.get('href'))
				All_Content_links.append(f"https://www.instagram.com{link.get('href')}\n")

		
		#######################################################################
		screenHeightCount+=1
		scroll_height = driver.execute_script("return document.body.scrollHeight;")

		if (screen_height * screenHeightCount) > scroll_height:
			print('End of the page reached Fam ---- !')
			print(driver.execute_script('return document.body.scrollHeight;'))
			break
	
	countDown(5)
	
	print(f'Total content data scraped is {len(All_Content_links)} ------------- ')
	writeDataToFile(All_Content_links)
	print("DONE BRO -------------------------------------------")



def countDown(time_to_count):
	counter = time_to_count
	for i in range(time_to_count):
		print(f'Remainig ------ {counter-i}')
		sleep(1)
	print('Time Over')




def writeDataToFile(Data_list):
	
	if len(Data_list) == len(set(Data_list)):
		print("---------- > No Duplicated in the data set detected +-+-+-+-+-+-+-+-+-+-+-+-+-")
	else:
		print("theres duplicate shit in the list ----- Removal on progress")
		Data_list = list(set(Data_list))

	with open('GrapheInstaContentLinks.txt' , 'w') as file:
		file.writelines(Data_list)
		print(f'Total number of data added to the file is {len(Data_list)} ------------- ')
	print('Saving Successful :')



if __name__ == '__main__':
	Scroll_to_end()




	
'''
	Content_links = driver.find_elements(By.XPATH , "//div[@class='_aabd _aa8k  _al3k']//a")
	for content in Content_links:
		link = content.get_attribute("href")
		All_Content_links.append(f'{link}')
		print()
		pprint(f"the link {link} has been added to the list bruv ------ !")
	print()
	print(f'< ----------- Total Number of Content scraped is {len(All_Content_links)} ---------- >')
	writeDataToFile(All_Content_links)
'''
