import time

import pygame

from Network import Network
from engine.Player import player

width, height = 700, 700
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Client")


def redrawWindow(win, listOfPlayers):
  win.fill("black")
  drawPlayers(listOfPlayers, win)
  pygame.display.update()


def drawPlayers(listOfPlayers, win):
  for player in listOfPlayers:
    pygame.draw.rect(win, player.color, pygame.Rect(player.positionX, player.positionY, player.width, player.height))


def displayMaxSizeReached():
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render('Max lobby size reached.', True, "black", "white")
  textRect = text.get_rect()
  textRect.center = (width // 2, height // 2)
  win.fill("white")
  win.blit(text, textRect)
  pygame.display.flip()


def displayServerNotRunning():
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render('Server not running.', True, "black", "white")
  textRect = text.get_rect()
  textRect.center = (width // 2, height // 2)
  win.fill("white")
  win.blit(text, textRect)
  pygame.display.flip()


def main():
  n = Network()
  received = n.getPlayerId()
  if received in (0, 1, 2, 3):
    clientPlayer = player(received)
    print("Connected as ", clientPlayer.playerId)
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          break

      playerList = n.send(clientPlayer)
      redrawWindow(win, playerList)
      clientPlayer.move()
  elif received not in (0, 1, 2, 3):
    displayMaxSizeReached()
    time.sleep(2)
    pygame.quit()
  else:
    displayServerNotRunning()
    time.sleep(2)
    pygame.quit()


main()
