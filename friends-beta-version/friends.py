#Import os module used to find the AppData directory
import os
import sys

#Open the text file. This block creates the file if I didn't previously exist or runs it if the Aetherlight session is over

file = sys.argv[0]
pathname = os.path.dirname(file)

friends = open(f"{os.path.abspath(pathname)}friends.txt","a+")
friends.read()
friends.close()

#This list is currently unnecessary
people = []

#The while loop is required to keep the program running the entire session of the game
while True:
    #Call the output log file from TheAetherlight_Data
    with open(f"{os.getenv('APPDATA')}/TheAetherlight/PROD/WIN/3.2.186/TheAetherlight_Data/output_log.txt", 'r') as myfile:
        data = myfile.read()
    #Split the string into a list where the name occures 
    data = data.split('Name recorded as')
    #Open the friends file
    friends = open(f"{os.path.abspath(pathname)}/friends.txt","a+")
    #Iterate through the output file
    for i in data:
        #Identify the names
        if '||' in i:
            if i[i.index('|')+5:i.index('\n')] not in open(f"{os.path.abspath(pathname)}/friends.txt","r").read().split('\n'):
                #Append the names to the text file
                friends.write(i[i.index('|')+5:i.index('\n')]+'\n')
                people.append(i[i.index('|')+5:i.index('\n')])
                #Print the names
                print('\n')
                print('You made a new friend: '+i[i.index('|')+5:i.index('\n')])
            
                
    friends.close()
    #When the game is quit the program relizes it and terminates the while loop and ends the program
    with open(f"{os.getenv('APPDATA')}/TheAetherlight/PROD/WIN/3.2.186/TheAetherlight_Data/output_log.txt", 'r') as myfile2:
        data2 = myfile2.read()
    data2 = data2.split()
    if 'SessionEndGame,' in data2:
        break
    else:
        continue

