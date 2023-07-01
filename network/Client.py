import os

import pygame
from dotenv import load_dotenv

from Network import Network
from engine.Player import Player
from engine.gameEngineLib import redrawWindow
from networkLib import displayMaxSizeReached, displayServerNotRunning, checkForQuit

load_dotenv()

networkIP = os.getenv('NETWORK_IP')
networkPort = os.getenv('NETWORK_PORT')

AllowedPlayerIds = (0, 1, 2, 3)
playerList = []
width, height = 900, 700


def main():

  pygame.init()
  pygame.font.init()
  pygame.mixer.music.load('audio.mp3')
  pygame.mixer.music.set_volume(0.07)
  win = pygame.display.set_mode((width, height))
  pygame.display.set_caption("Client")

  n = Network(networkIP, networkPort)
  clientPlayerId = n.getPlayerId()
  if clientPlayerId in AllowedPlayerIds:
    pygame.mixer.music.play()
    player = Player(clientPlayerId)
    print("Connected as ", player.playerId)
    while True:
      global playerList
      checkForQuit()
      playerList, pongBall, playerPoints, winnerId = n.send(player)
      player.move()
      redrawWindow(win, playerList, pongBall, clientPlayerId, playerPoints, winnerId)

  elif clientPlayerId is None:
    displayServerNotRunning(win, width, height)

  elif clientPlayerId not in AllowedPlayerIds:
    displayMaxSizeReached(win, width, height)


main()
