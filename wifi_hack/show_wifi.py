# el_introvertid0
import subprocess

# all wlan profiles
wifiProfiles = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
profiles = [i.split(":")[1][1:-1] for i in wifiProfiles if "All User Profile" in i]

#storing passwords in array
wlanPasswords = []
for i in profiles:
    passwords = (subprocess
    .check_output(["netsh",'wlan','show','profiles',i,'key=clear'])
    .decode("utf-8")
    .split("\n")
    )
    password = [b.split(":")[1][1:-1] for b in passwords if "Key Content" in  b]
    wlanPasswords.append(password)

#passwords output
for i in range(len(profiles)):
    print(profiles[i]," ==> ",*wlanPasswords[i])
