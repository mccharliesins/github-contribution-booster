import subprocess
import time
import random

directory = r'YOUR_FOLDER_DIRECTORY_HERE'
waittime=120 #Use integer value here, default is 120 seconds!

######

#You can add list of messages for your commit here!
listofmessages=['bug fixes','style added','new functionality','section added','more bug fixes','feature update','few extra lines added','testing a new section','testing']

while True:
    if waittime < 20:
        print("Please keep the waittime above 20 seconds! ")
        waittime=20
    random_number = random.randint(0, len(listofmessages))
    time.sleep(waittime)
    command = fr'cd /d "{directory}" && git add . && git commit -m "{listofmessages[random_number]}"'
    subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, creationflags=subprocess.DETACHED_PROCESS)
    print(f'Commits Made! Last was: {listofmessages[random_number]}')


#Keep coding! And at the end after you finish coding! see the results on your github account!
