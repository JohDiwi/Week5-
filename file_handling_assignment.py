with open("my_file.txt", "r") as file:
    content=file.read()
print(content)

with open("my_file.txt", "a") as file:
    file.write("However I am still in week 9\n"+"I shuld pull my socks to fininsh in time\n")
    file.write("Though its a bit challenging")

try:
    with open("Exact.py", "r") as file: 
        message=file.read()
        print(message)
except (FileNotFoundError, PermissionError): 
    print("Error!, Cant open this file") 

