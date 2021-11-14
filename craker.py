import hashlib

print("this tool is made by tolt")
print("i am not responsable for the bad use of this tool")

wlist=input("wordlist: ")
hash2crack=input("hash: ")


wlistlines=open(wlist, "r").readlines()

for i in range(0, len(wlistlines)):
    hash2comp=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
    if hash2crack == hash2comp:
        print("succes: "+wlistlines[i].replace("\n",""))
        exit()
print("sorry better luck nex time")