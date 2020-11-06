import os, time
os.system("figlet by youssef")
def function():
    lhost = str(input("entre your lhost:"))
    lport = str(input("entre your lport:"))
    payload = str(input("generate payload with msf or cobaltstrike:"))
    name = str(input("entre payload name:"))
    print(lhost , lport , payload , name)
    correct = input("is those informations correct:")
    if correct == "yes":
        os.system("python2 Fuck-Antivirus.py" " " + lhost + " " + lport + " " + payload + " " + name)
    elif correct == "no":
        function()
function()
