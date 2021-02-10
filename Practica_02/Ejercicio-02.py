my_objeto = [
	{'nota': 15},
    {'nota': 16},
    {'nota': 12},
    {'nota'}
]
my_list=[]
for llave in my_objeto:
    if llave['nota'] == None:
        my_list.append(llave['nota'])
    else:
        my_list.append('None')
         
print(my_list)