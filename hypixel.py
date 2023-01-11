import profile
from typing import KeysView
import requests
import json
from os import system
from nbt import nbt
import base64, io


from pprint import pprint

#https://api.hypixel.net/player?key={API_KEY}&name={name}
#https://api.hypixel.net/player?key=70b8d745-f75c-4485-8009-2c605f9c87ec&name=penguujr
#https://api.hypixel.net/skyblock/profiles?key=70b8d745-f75c-4485-8009-2c605f9c87ec&uuid=7e5a3369ab4141879098ba266078fd32 # player
#https://api.hypixel.net/skyblock/profile?key=70b8d745-f75c-4485-8009-2c605f9c87ec&profile=8d020af47a2c46e0bc266dffa674a61a     profile

#https://api.hypixel.net/resources/skyblock/items   item prices, ids, names, tags




def getInfo(call):
    r = requests.get(call)
    return r.json()

def get_inventory(raw):
    return nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(raw))) # decodes inventory stuff



#constants
name = "Penguujr" #username, my name
UUID = "" #usr uuid, enter your uuID
DASHED_UUID = "" # user uuid, enter your dashed uuid
apikey = "" # enter your api key
name_link = f"https://api.hypixel.net/player?key={apikey}&name={name}" # api link for user with name(never use this one)
uuid_link = f"https://api.hypixel.net/player?key={apikey}&uuid={UUID}" # api link for user
skyblock_link = f"https://api.hypixel.net/skyblock/profile?key={apikey}&profile=8d020af47a2c46e0bc266dffa674a61a" ## api link for skyblock profile
prices = getInfo("https://api.hypixel.net/resources/skyblock/items")





running = True



profileJsonData = getInfo(skyblock_link) # initial load
#pprint(playerJson) # initial print



userItem = input("Enter id of item you would like to monitor: ") ## alows user input of item instead of changing code


def getItem(userInput):
    for x in range(len(prices['items'])): ## finds information about specific item using item api
        if(prices['items'][x]['id'] == userInput): ## goes through entire dict to find id if not in it, this will just close program
            print('Found item')
            npcPrice = prices['items'][x]['npc_sell_price']
            itemName = prices['items'][x]['name']
            return prices['items'][x]
    print('Item not found exiting program.')
    running = False




def changeItem():
    beginColAmount = profileJsonData['profile']['members'][f'{UUID}']['collection'][item['id']]
    gainedAmount = 0
    curColAmount = 0
    profit = 0


#presetting variables
item = getItem(userItem)
beginColAmount = profileJsonData['profile']['members'][f'{UUID}']['collection'][item['id']]
gainedAmount = 0
curColAmount = 0
profit = 0



# running program
while(running):
    gainedAmount = curColAmount - beginColAmount
    profit = item['npc_sell_price'] * gainedAmount

    system('cls') ## clears screen
    currentColAmount = profileJsonData['profile']['members'][f'{UUID}']['collection'][item['id']]

    print('Npc sell price: ' + f"{item['npc_sell_price']}") # shows selling price to user
    print('Item name: ' + f"{item['name']}") # show's item name to user
    print("Started collection amount: " + f"{beginColAmount}")
    print("Current collection amount: " + f"{currentColAmount}")
    print("Amount gained since start of program: " + f"{gainedAmount}")
    print("profit: " + f"{profit}")
    


    print("\n \n \nEnter C to change item")
    print("Enter R for refresh")
    print("Enter Q to quit")
    userAnswer = input()


    if(userAnswer == "R"):
        #Refreshing
        system("cls") ## clears screen to make it pretty
        profileJsonData = getInfo(skyblock_link) # reloading new JSON from api
        curColAmount = profileJsonData['profile']['members'][f'{UUID}']['collection'][f'{userItem}'] # getting new collection amount
    if(userAnswer == "Q"):
        running = False
    if(userAnswer == "C"):
        changeItem()
    
