
#subprocess is a python module which as the name suggests provides the interface for working with processes.Import this module
#in order to run this script.
import subprocess

# subprocess.check_output() will run the command (netsh wlan show profiles) in the command prompt. 
#It will save the results in our variable data. As you can see it is similar to os.command().
# We use check_output() to capture the output for later processing.

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

#Text formatting allows us to seperate the desired text in a formatted way.
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))


#subprocess.check_output will call ipconfig.
#It will show the same result as if you were typing ipconfig in the command prompt in case of windows.

data = subprocess.check_output(['ipconfig']).decode('utf-8').split('/n')

#Some other text formatting to display the python result in a formatted way.
for b in data :
    stringer = ''
    if "IPv4 Address" in b:
        b.split(":")[1][1:-1]
        stringer = stringer + b
        
print(i)

#We have used python file module here to create a new text file and write all the results obtained from above mentioned 
#commands and close the file.

file = open('text.txt','w')
file.write(b)
file.close()
        


