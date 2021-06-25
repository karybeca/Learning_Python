#!/bin/python3

from random import choice 

players = []
#Here Should be a Loop!
players.append = (input ("Enter the name of the Player:"))
players.append = (input ("Enter the name of the Player:"))
players.append = (input ("Enter the name of the Player:"))
players.append = (input ("Enter the name of the Player:"))
players.append = (input ("Enter the name of the Player:"))
players.append = (input ("Enter the name of the Player:"))
players.append = (input ("Enter the name of the Player:"))
players.append = (input ("Enter the name of the Player:"))
players.append = (input ("Enter the name of the Player:"))
players.append = (input ("Enter the name of the Player:"))
print (players)

#players = []
#file = open ('players.txt', 'r')
#players = file.read().splitlines()
#print (players)

teamNames = []
file = open ('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print (teamNames)

teamA = []
teamB = []

while len(players) > 0:
  playerA = choice(players)
  teamA.append(playerA)
  players.remove(playerA)

  playerB = choice(players)
  teamB.append(playerB)
  players.remove(playerB)
  
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
print (teamA)
  
teamNameB = choice(teamNames)
print (teamB)
teamNames.remove(teamNameB)
 
print ('Here are your teams:')
print (teamNameA, teamA)
print (teamNameB, teamB)