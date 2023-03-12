import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By


def countDown(time_to_count):
	counter = time_to_count
	for i in range(time_to_count):
		print(f'Remainig ------ {counter-i}')
		sleep(1)
	print('Time Over')


def GetData():
	with open('GrapheInstaContentLinks.txt' , 'r') as file:
		links = file.readlines()
	clean_links = [link.strip() for link in links ]
	if len(clean_links) == len(set(clean_links)):
		print('No Duplicate Data Detected')
	else:
		print("List Contains Duplicate Data Bro - Clean This Shit.")
	print(len(clean_links))
	return clean_links


def FindLikes(Content_Link , driver):
	the_users = []
	driver.get(f'{Content_Link}liked_by')
	countDown(7)
	Ids_liked = driver.find_elements(By.XPATH , "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd']")
	
	for like in Ids_liked:
		the_user_id = like.get_attribute('href')
		the_users.append(the_user_id)
		print(f'the user_id {the_user_id} has been added to the list')
	print(f'Total Number of Likes on {Content_Link} is -------------- {len(Ids_liked)} ------------- ')

	FileName_from_link = Content_Link.split('/p/')[1].strip()
	CreateFile(Content_Link , the_users)


def main():
	chromeOptions = Options()
	chromeOptions.add_argument("--user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\GrapheBot")
	driver = webdriver.Chrome('chromedriver.exe' , options=chromeOptions)


	Content_Links = GetData()
	for link in Content_Links:
		FindLikes(link , driver)



def CreateFile(FileName , DataList):
	with open(f'{FileName}.txt' , 'w') as file:
		New_dataList = [f'{data}\n' for data in DataList]
		file.writelines(New_dataList)
	print("DATA SAVED SUCCESSFULLY ---------------------------------- ")


if __name__ == '__main__':
	main()