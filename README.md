# Subprocess in Python

### The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. 

we can use it by importing subprocess in python

```python
import subprocess
```

### if you want to look hidden (.) files in directory run this program
```python 
subprocess.run(['ls','-la'])
```

### to capture result into variable
```python
result = subprocess.run(['ls','-la'])
print(result)
```
### to capture returncode
```python
result = subprocess.run(['ls','-la'])
print(result.returncode)
```
### to print captured variable, pass argument capture_output = True
```python
result = subprocess.run(['ls','-la'],capture_output=True)
print(result.stdout)
```

### to decode binary data
```python
result = subprocess.run(['ls','-la'],capture_output=True)
print(result.stdout.decode())
```
### TO  convert result into text without decoding, using text argument
```python
result = subprocess.run(['ls','-la'],capture_output=True,text=True)
print(result.stdout)
```
### ==>
```python
result = subprocess.run(['ls','-la'],stdout=subprocess.PIPE,text=True)
print(result.stdout)
```
