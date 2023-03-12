import matplotlib
import os
import json

dirs_list = os.listdir("./DATA/")

if "all_users.json" not in dirs_list:
	with open("./DATA/all_users.json", 'w') as file:
		pass
else :
	dirs_list.remove("all_users.json")


all_users = []
for files in dirs_list:
	with open(f"./DATA/{files}", 'r') as file:
		users_ = file.readlines()
		all_users += users_


count_dictionary = {}
for i in all_users:
	i = i.strip().split(",")[0][1:].strip().replace("[",'')
	if  i not in count_dictionary:
		count_dictionary[i] = 1
	else :
		count_dictionary[i] += 1

print(len(count_dictionary))

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

for i in range(len(keys_)):
	print(f"{keys_[i]} --> {values[i]}")