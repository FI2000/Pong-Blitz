import pygame


def drawPongBall(win, positionX, positionY):
  pygame.draw.circle(win, "white", [positionX, positionY], 15)


def drawPlayers(listOfPlayers, win):
  for player in listOfPlayers:
    pygame.draw.rect(win, player.color, pygame.Rect(player.positionX, player.positionY, player.width, player.height))


def drawPoints(listOfPlayers, playerPoints, win):
  font = pygame.font.Font('freesansbold.ttf', 32)
  for player in listOfPlayers:
    if player.playerId in (0, 1, 2, 3):
      text = font.render(str(playerPoints[player.playerId]), True, "white", "black")
      textRect = text.get_rect()
      if player.playerId == 0:
        textRect.center = (60, player.positionY + 45)
      if player.playerId == 1:
        textRect.center = (840, player.positionY + 45)
      if player.playerId == 2:
        textRect.center = (player.positionX + 45, 60)
      if player.playerId == 3:
        textRect.center = (player.positionX + 45, 655)
      win.blit(text, textRect)


def drawPlayerSide(playerId, win):
  if playerId == 0:
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(0, 0, 5, 700))
  if playerId == 1:
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(895, 0, 5, 700))
  if playerId == 2:
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(0, 0, 900, 5))
  if playerId == 3:
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(0, 695, 900, 5))


def displayWinner(win, winnerId):
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render("The winner is " + str(winnerId), True, "white", "black")
  textRect = text.get_rect()
  textRect.center = (880 // 2, 680 // 2)
  win.blit(text, textRect)


def redrawWindow(win, listOfPlayers, pongBall, playerId, playerPoints, winnerId):
  win.fill("black")
  drawPlayers(listOfPlayers, win)
  drawPlayerSide(playerId, win)
  drawPoints(listOfPlayers, playerPoints, win)
  drawPongBall(win, pongBall.positionX, pongBall.positionY)
  if winnerId != 100:
    displayWinner(win, winnerId)
  pygame.display.update()


def accelerationValue(listOfPoints):
  accelerationTick = 0.5
  addition = sum(listOfPoints) / 20
  return accelerationTick + addition
