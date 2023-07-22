import requests
import os

print("-"*64)
print("created by max johnson")
print("simple subdomain finder")
print("-"*64)
ab = input("enter you domain without https , www : ")

os.system("clear")

a = open("file.txt","r")
for i in a:
#for b in i:
  c = requests.get(f"https://www.{i}.{ab}")
  d = requests.status(c)
  if d == 200:
    print(f"[+] found https://www.{i}.{ab}")
