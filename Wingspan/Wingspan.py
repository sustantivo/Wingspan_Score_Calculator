print("Wingspan Score Calculator")
print("")

# Gets the player list and blank scores

#Generates blank list of players
playerList = {
    'player1' : 0, 'player2' : 0, 'player3' : 0, 'player4' : 0, 'player5' : 0
    }

#Modifies playerList to fit same amount of players
playerCount = int(input("How many players?: "))
if playerCount == int(2):
    del playerList['player3'], playerList['player4'], playerList['player5']
elif playerCount == int(3):
    del playerList['player4'], playerList['player5']
elif playerCount == int(4):
    del playerList['player5']


#Add's names to players
def name_players():
    if 'player1' in playerList:
        playerList[input('Enter player name: ')] = playerList.pop('player1')
    if 'player2' in playerList:
        playerList[input('Enter player name: ')] = playerList.pop('player2') 
    if 'player3' in playerList:
        playerList[input('Enter player name: ')] = playerList.pop('player3') 
    if 'player4' in playerList:
        playerList[input('Enter player name: ')] = playerList.pop('player4') 
    if 'player5' in playerList:
        playerList[input('Enter player name: ')] = playerList.pop('player5') 

name_players()
print(playerList)