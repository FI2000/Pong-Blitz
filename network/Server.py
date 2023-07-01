import os
import pickle
import random
import socket
import time
from _thread import *

from dotenv import load_dotenv

from engine.Player import Player
from engine.gameEngineLib import accelerationValue
from engine.pongBall import pongBall
from networkLib import markPlayerConnected, returnEmptyConnexionSpot, checkForGameStart, checkForWinner

load_dotenv()

serverIp = os.getenv('NETWORK_IP')
serverPort = int(os.getenv('NETWORK_PORT'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((serverIp, serverPort))
except socket.error as e:
  print(e)

s.listen(4)
print("Waiting for a connection, Server Started at ", str(serverIp) + ":" + str(serverPort))

players = [Player(99), Player(99), Player(99), Player(99)]
playerPoints = [0, 0, 0, 0]
pong_ball = pongBall(random.randint(390, 410), random.randint(340, 360))
pong_ball.dx = 1 if random.random() < 0.5 else -1
pong_ball.dy = 1 if random.random() < 0.5 else -1
numOfConnectedPlayers = 0
winnerId = 100
startGame = False
connectedPlayersList = {
  "0": False,
  "1": False,
  "2": False,
  "3": False
}


def retractPoints(player_id):
  if players[player_id].playerId != 99:
    if playerPoints[player_id] > 0:
      playerPoints[player_id] -= 1


def gameReset():
  global playerPoints, pong_ball, winnerId, startGame
  playerPoints = [0, 0, 0, 0]
  pong_ball = pongBall(random.randint(390, 410), random.randint(350, 400))
  pong_ball.accelerationTicks = 0.5
  winnerId = 100
  startGame = True


def threaded_client(conn, playerId):
  conn.send(pickle.dumps(playerId))

  global numOfConnectedPlayers, winnerId, startGame, playerPoints
  startGame = checkForGameStart(numOfConnectedPlayers)
  if playerId in (0, 1, 2, 3):
    while True:
      try:
        clientPlayerInfo = pickle.loads(conn.recv(8192))
        if not clientPlayerInfo:
          print("Disconnected")
          break
        else:
          players[playerId] = clientPlayerInfo

        if startGame:
          pong_ball.startGame()
          pong_ball.move()
          bouncedOffWall = pong_ball.wallBounce()
          bouncedOffPlayer, points = pong_ball.checkTouchesPlayer(players)
          if bouncedOffPlayer is not None and points is not None:
            playerPoints[bouncedOffPlayer] += 1
          if bouncedOffWall is not None:
            retractPoints(bouncedOffWall)
          pong_ball.accelerationTicks = accelerationValue(playerPoints)
          winnerId = checkForWinner(playerPoints)

        conn.sendall(pickle.dumps((players, pong_ball, playerPoints, winnerId)))

        if winnerId != 100:
          current = time.time()
          pong_ball.positionX = 5000
          pong_ball.positionY = 5000
          startGame = False
          while not time.time() - current > 10:
            clientPlayerInfo = pickle.loads(conn.recv(8192))
            players[playerId] = clientPlayerInfo
            conn.sendall(pickle.dumps((players, pong_ball, playerPoints, winnerId)))
          gameReset()

      except:
        break

    numOfConnectedPlayers -= 1
    connectedPlayersList.update({str(playerId): False})
    players[playerId] = Player(99)
    conn.close()


while True:
  conn, addr = s.accept()
  print("Connect to: ", addr)
  numOfConnectedPlayers += 1
  start_new_thread(threaded_client, (conn, returnEmptyConnexionSpot(connectedPlayersList)))
  connectedPlayersList = markPlayerConnected(connectedPlayersList)
  if numOfConnectedPlayers <= 1:
    gameReset()
    startGame = False
