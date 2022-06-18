# **WIFI HACK**



**Using Python _subprocess_ module we can access to wifi passwords that are stored in system**

**To use subprocess module**
```python
import subprocess
```
________
**To display wifi profiles on your system**
```python
list_of_wifiProfiles = subprocess.run(["netsh",'wlan','show','profiles'],capture_output=True,text=True)
print(list_of_wifiProfiles.stdout)
```
==>
```python
wifiProfiles = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
print(wifiProfiles)
```
________

**To Display wlan names**
```python
wifiProfiles = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
profiles = [i.split(":")[1][1:-1] for i in wifiProfiles if "All User Profile" in i]
print(profiles)
```
__________
**To display all wlan passwords**
```python
for i in profiles:
    passwords = (subprocess
    .check_output(["netsh",'wlan','show','profiles',i,'key=clear'])
    .decode("utf-8")
    .split("\n")
    )
    password = [b.split(":")[1][1:-1] for b in passwords if "Key Content" in  b]
    print(password)
```
____________
**TO DISPLAY WLAN NAME AND WLAN PASSWORD**
```python
wlanPasswords = []
for i in profiles:
    passwords = (subprocess
    .check_output(["netsh",'wlan','show','profiles',i,'key=clear'])
    .decode("utf-8")
    .split("\n")
    )
    password = [b.split(":")[1][1:-1] for b in passwords if "Key Content" in  b]
    wlanPasswords.append(password)
    
for i in range(len(profiles)):
    print(profiles[i]," ==> ",*wlanPasswords[i])
```
_________

## Thanks For Checking :innocent:
