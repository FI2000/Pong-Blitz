import pygame


def drawPlayers(listOfPlayers, screen):
  for player in listOfPlayers:
    pygame.draw.rect(screen, player.color, pygame.Rect(player.positionX, player.positionY, player.width, player.height))


def redrawWindow(win, listOfPlayers):
  win.fill("black")
  drawPlayers(listOfPlayers, win)
  pygame.display.update()
