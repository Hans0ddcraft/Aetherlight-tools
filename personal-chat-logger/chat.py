import os
storage = []
while True:
    with open(f"{os.getenv('APPDATA')}/TheAetherlight/PROD/WIN/3.2.186/TheAetherlight_Data/output_log.txt", 'r') as myfile:
        data = myfile.read()
    data = data.split('Chat, message=')


    for i in data:
        if i[0] == '"':
            if i[0:i.index('\n')] not in storage:
                print(i[0:i.index('\n')])
                storage.append(i[0:i.index('\n')])
    with open(f"{os.getenv('APPDATA')}/TheAetherlight/PROD/WIN/3.2.186/TheAetherlight_Data/output_log.txt", 'r') as myfile2:
        data2 = myfile2.read()
    data2 = data2.split()
    if 'SessionEndGame,' in data2:
        break
    else:
        continue
    
