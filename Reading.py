file=open("Sci.txt","a")
file.write("Minecraft ")
file.close()

try:
    file=open("Scsi.txt","r")
    contents=file.read()
    file.close()
    print(contents)
except:
    print("You chose the wrong file! Creating File...")
    file=open("Scsi.txt","w")
    file.close()
