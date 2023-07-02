import time
from random import randint

import pygame

from engine.pongBall import pongBall


def markPlayerConnected(playerConnexionDictionnary):
  if not playerConnexionDictionnary["0"]:
    playerConnexionDictionnary.update({"0": True})
  elif not playerConnexionDictionnary["1"]:
    playerConnexionDictionnary.update({"1": True})
  elif not playerConnexionDictionnary["2"]:
    playerConnexionDictionnary.update({"2": True})
  elif not playerConnexionDictionnary["3"]:
    playerConnexionDictionnary.update({"3": True})
  return playerConnexionDictionnary


def returnEmptyConnexionSpot(playerConnexionDictionnary):
  if not playerConnexionDictionnary["0"]:
    return 0
  elif not playerConnexionDictionnary["1"]:
    return 1
  elif not playerConnexionDictionnary["2"]:
    return 2
  elif not playerConnexionDictionnary["3"]:
    return 3
  return 99


def displayMaxSizeReached(win, width, height):
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render('Max lobby size reached.', True, "black", "white")
  textRect = text.get_rect()
  textRect.center = (width // 2, height // 2)
  win.fill("white")
  win.blit(text, textRect)
  pygame.display.flip()
  time.sleep(2)
  pygame.quit()


def displayServerNotRunning(win, width, height):
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render('Server not running.', True, "black", "white")
  textRect = text.get_rect()
  textRect.center = (width // 2, height // 2)
  win.fill("white")
  win.blit(text, textRect)
  pygame.display.flip()
  time.sleep(2)
  pygame.quit()


def checkForQuit():
  LeaveGame = False
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      LeaveGame = True
  keys = pygame.key.get_pressed()
  if keys[pygame.K_ESCAPE]:
    LeaveGame = True
  return LeaveGame


def checkForGameStart(numOfConnectedPlayers):
  startGame = False
  if numOfConnectedPlayers >= 2:
    startGame = True
  return startGame


def checkForWinner(list):
  maxValue = max(list)
  if maxValue > 1:
    return list.index(maxValue)
  else:
    return 100


def gameReset():
  playerPoints = [0, 0, 0, 0]
  pong_ball = pongBall(randint(390, 410), randint(350, 400))
  pong_ball.accelerationTicks = 0.5
  winnerId = 100
  startGame = True
  Collision = False
  return playerPoints, pong_ball, winnerId, startGame, Collision
