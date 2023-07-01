import pygame


def drawPongBall(win, positionX, positionY):
  pygame.draw.circle(win, "white", [positionX, positionY], 15)


def drawPlayers(listOfPlayers, win):
  for player in listOfPlayers:
    pygame.draw.rect(win, player.color, pygame.Rect(player.positionX, player.positionY, player.width, player.height))


def drawPlayerSide(playerId, win):
  if playerId == 0:
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(0, 0, 5, 700))
  if playerId == 1:
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(895, 0, 5, 700))
  if playerId == 2:
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(0, 0, 900, 5))
  if playerId == 3:
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(0, 695, 900, 5))


def redrawWindow(win, listOfPlayers, pongBall, playerId):
  win.fill("black")
  drawPlayers(listOfPlayers, win)
  drawPlayerSide(playerId, win)
  drawPongBall(win, pongBall.positionX, pongBall.positionY)
  pygame.display.update()
