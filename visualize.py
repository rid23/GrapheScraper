import matplotlib
import os
import json
from grapheScraper import countDown as countdown



dirs_list = os.listdir("./DATA/")



def SaveSelectedUserData(DataList):
	with Open('SelectedUser.txt' , 'w') as f:
		Data = [f'{data}\n' for data in DataList]
		f.writelines(Data)
		print(f'Total {len(Data)} Selected User Data Has Been Stored Successfully. :)')


if "all_users.json" not in dirs_list:
	with open("./DATA/all_users.json", 'w') as file:
		pass
else :
	dirs_list.remove("all_users.json")

print(f"total {len(dirs_list)} files found...")
countdown(3)

all_users = []
for files in dirs_list:
	with open(f"./DATA/{files}", 'r') as file:
		users_ = file.readlines()
		all_users += users_

print(f"total liked by users {len(all_users)}")
countdown(3)

count_dictionary = {}
for i in all_users:
	i = i.strip().split(",")[0][1:].strip().replace("[",'')
	if  i not in count_dictionary:
		count_dictionary[i] = 1
	else :
		count_dictionary[i] += 1

print(f"total unique users {len(count_dictionary)}")
print("json file loads in...")
countdown(3)

with open("./DATA/all_users.json", 'w') as file:
	json.dump(count_dictionary, file, indent=4)


# with open(f"./DATA/all_users.txt", 'w') as file
# 	for i in all_users:
# 		file.write(i)

keys_ = [ i for i in count_dictionary.keys()]
values =[i for i in count_dictionary.values()]

for i in range(len(values)):
	for j in range(i):
		if values[j] < values[i]:
			values[j], values[i] = values[i], values[j]
			keys_[j], keys_[i] = keys_[i], keys_[j]

AllSelectedUsers = []
for i in range(len(keys_)):
	if values[i] < 40:
		continue
	print(f"{keys_[i]} --> {values[i]}")
	AllSelectedUsers.append(f"{keys_[i]} --> {values[i]}")

SaveSelectedUserData(AllSelectedUsers)\
print('Task Complete Bro --------------- ')
