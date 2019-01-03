import os


friends = open(f"{os.getcwd()}/friends.txt","a+")
friends.read()
friends.close()

people = []

while True:
    with open(f"{os.getenv('APPDATA')}/TheAetherlight/PROD/WIN/3.2.186/TheAetherlight_Data/output_log.txt", 'r') as myfile:
        data = myfile.read()
    data = data.split('Name recorded as')
    friends = open(f"{os.getcwd()}/friends.txt","a+")

    for i in data:
        if '||' in i:
            if i[i.index('|')+5:i.index('\n')] not in open(f"{os.getcwd()}/friends.txt","r").read().split('\n'):
                friends.write(i[i.index('|')+5:i.index('\n')]+'\n')
                people.append(i[i.index('|')+5:i.index('\n')])
                print('\n')
                print('You made a new friend: '+i[i.index('|')+5:i.index('\n')])
            
                
    friends.close()
    with open(f"{os.getenv('APPDATA')}/TheAetherlight/PROD/WIN/3.2.186/TheAetherlight_Data/output_log.txt", 'r') as myfile2:
        data2 = myfile2.read()
    data2 = data2.split()
    if 'SessionEndGame,' in data2:
        break
    else:
        continue

