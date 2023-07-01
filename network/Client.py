import os

import pygame
from dotenv import load_dotenv

from Network import Network
from engine.Player import Player
from engine.gameEngineLib import redrawWindow
from networkLib import displayMaxSizeReached, displayServerNotRunning, checkForQuit

load_dotenv()

width, height = 900, 700
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Client")

networkIP = os.getenv('NETWORK_IP')
networkPort = os.getenv('NETWORK_PORT')

AllowedPlayerIds = (0, 1, 2, 3)
playerList = []


def main():
  n = Network(networkIP, networkPort)
  clientPlayerId = n.getPlayerId()

  if clientPlayerId in AllowedPlayerIds:
    clientPlayer = Player(clientPlayerId)
    print("Connected as ", clientPlayer.playerId)

    while True:
      global playerList
      checkForQuit()
      playerList, pongBall = n.send(clientPlayer)
      clientPlayer.move()
      redrawWindow(win, playerList, pongBall, clientPlayerId)

  elif clientPlayerId is None:
    displayServerNotRunning(win, width, height)

  elif clientPlayerId not in AllowedPlayerIds:
    displayMaxSizeReached(win, width, height)


main()
