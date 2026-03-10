Yu = {
    'name' : 'Mingwang',
    'age' : 89,
    'gender' : 'unknown',
    'hobby' : 'play with stones',
}
print(Yu['age'])
Yu['age'] = 90
print(Yu)
print(f"It's great fun playing with {Yu['name']}!")
del Yu['hobby']
print(Yu)
Yu['appearance'] = 'cute'
print(Yu)
for key,value in Yu.items():
    print(f"{key} : {value}")
for key in Yu.keys():
    print(f"{key}")
for value in Yu.values():
    print(f"{value}")
    