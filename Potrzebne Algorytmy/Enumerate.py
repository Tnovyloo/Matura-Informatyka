things = ['siemasz', 'tomasz']

for i in range(len(things)):
    print(f'{i+1}.{things[i]}')

for i, thing in enumerate(things, start=1):
    print(f'{i}.{things}')