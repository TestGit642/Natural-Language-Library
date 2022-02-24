from zipfile import ZipFile
from urllib import request
import sys, os
import webbrowser
# Define the remote file to retrieve
remote_url = 'https://github.com/TestGit642/Natural-Language-Library/archive/refs/heads/main.zip'
# Define the local filename to save data
local_file = 'localcopy.zip'
# Download remote and save locally
request.urlretrieve(remote_url, local_file)


with ZipFile('localcopy.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
c=os.getcwd()
#print(c)#curent directory
#os.chdir('\\Users\\Administrator\\Documents\\Python downloads\\nk-main')
s=os.chdir('.\\Natural-Language-Library-main')
webbrowser.open("ସୂଚନା ଦେବା.txt")

with open("nllall.py", "r",encoding="utf8") as input:
    #print(os.getcwd()) current directory change to nk-main
    b=os.path.dirname(sys.executable)
    os.chdir(b)
    os.chdir('.\\Lib')  
    # Creating "gfg output file.txt" as output
    # file in write mode
    with open("nllall.py","w",encoding="utf8") as output:
          
        # Writing each line from input file to
        # output file using loop
        for line in input:
            output.write(line)

print("ଏବେ ଆପଣଙ୍କ  କମ୍ପୁଟରରେ  Natural Language Library ଉପଲବ୍ଧ")
#d=os.getcwd()
#print(d)







