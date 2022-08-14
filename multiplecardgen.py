#Based on ENIGMAS gift card Generators

#setup
import time
import os
import random

os.system("title Multiple card Generator - ENIGMA#0420")

#functions
def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

#interface
print("Multiple card generator by ENIGMA#0420")
print("")
print("What card you want to generate?")

tt = input("\nAmazon\nRoblox\nFortnite\nEbay\nNetflix\niTunes\nPaypal\nPlaystation\nSteam\nXbox\nPlayStore\nMinecraft\n\n>")

t = tt.lower()
print("")
print("How many of them?")
nn = input(">")
print("")
n = int(nn)

if t == "minecraft":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))

if t == "paypal":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))

if t == "playstation":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4))

if t == "amazon":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))

if t == "netflix":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(4))

if t == "steam":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(6)+"-"+g(5))

if t == "fortnite":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(4)+"-"+g(4))

if t == "robolox":
	for x in range(n):
		print("")
		print(g(3)+"-"+g(3)+"-"+g(4))

if t == "itunes":
	for x in range(n):
		print("")
		print(g(16))

if t == "ebay":
	for x in range(n):
		print("")
		print(g(10))

if t == "playstore":
	for x in range(n):
		print("")
		print(g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4))

if t == "xbox":
	for x in range(n):
		print("")
		print(g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5))

print("")
print("-----Generation completed-----")
time.sleep(360)
