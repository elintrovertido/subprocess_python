import subprocess

# listOfFiles = subprocess.run("ls -la")
listOfFiles = subprocess.run(['ls','-la'],capture_output=True,text=True)

print(listOfFiles.stdout)