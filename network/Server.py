import os
import pickle
import random
import socket
from _thread import *

from dotenv import load_dotenv

from engine.Player import Player
from engine.pongBall import pongBall
from networkLib import markPlayerConnected, returnEmptyConnexionSpot

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
pong_ball = pongBall(random.randint(100, 150), random.randint(350, 400))
numOfConnectedPlayers = 0
startGame = False
connectedPlayersList = {
  "0": False,
  "1": False,
  "2": False,
  "3": False
}


def checkForGameStart(numOfConnectedPlayers):
  global startGame
  if numOfConnectedPlayers >= 2:
    startGame = True


def threaded_client(conn, playerId):
  conn.send(pickle.dumps(playerId))

  global numOfConnectedPlayers
  global startGame
  checkForGameStart(numOfConnectedPlayers)

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
          pong_ball.bounce(players)

        conn.sendall(pickle.dumps((players, pong_ball)))
      except:
        break
    numOfConnectedPlayers -= 1
    if numOfConnectedPlayers <= 1:
      startGame = False
    connectedPlayersList.update({str(playerId): False})
    players[playerId] = Player(99)
    conn.close()


while True:
  conn, addr = s.accept()
  print("Connect to: ", addr)
  numOfConnectedPlayers += 1
  print(numOfConnectedPlayers)
  start_new_thread(threaded_client, (conn, returnEmptyConnexionSpot(connectedPlayersList)))
  connectedPlayersList = markPlayerConnected(connectedPlayersList)
