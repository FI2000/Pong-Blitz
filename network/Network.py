import pickle
import socket


class Network:
  def __init__(self, serverIp, serverPort):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server = serverIp
    self.port = int(serverPort)
    self.addr = (self.server, self.port)
    self.p = self.connect()

  def getPlayerId(self):
    return self.p

  def connect(self):
    try:
      self.client.connect(self.addr)
      return pickle.loads(self.client.recv(1024))
    except:
      pass

  def send(self, data):
    try:
      self.client.send(pickle.dumps(data))
      return pickle.loads(self.client.recv(1024))
    except socket.error as e:
      print(e)
