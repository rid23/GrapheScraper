import pprint

with open('GrapheInstaContentLinks.txt' , 'r') as file:
	links = file.readlines()

clean_links = [link.strip() for link in links ]
No_duplicate_links = list(set(clean_links))


print()
print(len(clean_links))
print(f'Length of non duplicate link ----- {len(No_duplicate_links)}')
print()

if len(No_duplicate_links) == len(set(No_duplicate_links)):
	print("No duplicates bruv")
else:
	print("theres duplicate shit in the list you are fu*ked")