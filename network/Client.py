import os

import pygame
from dotenv import load_dotenv

from Network import Network
from engine.Player import Player
from engine.gameEngineLib import redrawWindow
from networkLib import displayMaxSizeReached, displayServerNotRunning, checkForQuit

load_dotenv()

width, height = 700, 700
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Client")

networkIP = os.getenv('NETWORK_IP')
networkPort = os.getenv('NETWORK_PORT')


def main():
  n = Network(networkIP, networkPort)
  received = n.getPlayerId()

  if received in (0, 1, 2, 3):
    clientPlayer = Player(received)
    print("Connected as ", clientPlayer.playerId)

    while True:
      checkForQuit()
      playerList = n.send(clientPlayer)
      clientPlayer.move()
      redrawWindow(win, playerList, received)

  elif received not in (0, 1, 2, 3):
    displayMaxSizeReached(win, width, height)

  else:
    displayServerNotRunning(win, width, height)


main()
