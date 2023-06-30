import pickle
import socket
from _thread import *

from engine.Player import player

server = "192.168.2.28"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((server, port))
except socket.error as e:
  print(e)

s.listen(4)
print("Waiting for a connection, Server Started")

players = [player(99), player(99), player(99), player(99)]

connectedPlayersList = {
  "0": False,
  "1": False,
  "2": False,
  "3": False
}


def markPlayerConnected():
  global connectedPlayersList
  if not connectedPlayersList["0"]:
    connectedPlayersList.update({"0": True})
  elif not connectedPlayersList["1"]:
    connectedPlayersList.update({"1": True})
  elif not connectedPlayersList["2"]:
    connectedPlayersList.update({"2": True})
  elif not connectedPlayersList["3"]:
    connectedPlayersList.update({"3": True})


def returnEmptySpot():
  global connectedPlayersList
  if not connectedPlayersList["0"]:
    return 0
  elif not connectedPlayersList["1"]:
    return 1
  elif not connectedPlayersList["2"]:
    return 2
  elif not connectedPlayersList["3"]:
    return 3


def threaded_client(conn, playerId):
  conn.send(pickle.dumps(playerId))
  if playerId in (0, 1, 2, 3):
    while True:
      try:
        clientPlayerInfo = pickle.loads(conn.recv(8192))

        if not clientPlayerInfo:
          print("Disconnected")
          break
        else:
          players[playerId] = clientPlayerInfo
          reply = players

        conn.sendall(pickle.dumps(reply))
      except:
        break

    connectedPlayersList.update({str(playerId): False})
    players[playerId] = player(99)
    conn.close()


while True:
  conn, addr = s.accept()
  print("Connect to: ", addr)
  start_new_thread(threaded_client, (conn, returnEmptySpot()))
  markPlayerConnected()
