class pongBall:
  def __init__(self, positionX, positionY):
    self.positionX = positionX
    self.positionY = positionY
    self.isMoving = False
    self.velocity = 0.4
    self.accelerationTicks = 0.5
    self.accelerationValue = 0.1
    self.dx = 1
    self.dy = 1

  def startGame(self):
    self.isMoving = True

  def newPoint(self, positionX, positionY):
    self.accelerationTicks = 0
    self.isMoving = False
    self.positionX = positionX
    self.positionY = positionY

  def move(self):
    if self.isMoving:
      self.positionX += self.dx * (self.velocity + (self.accelerationValue * self.accelerationTicks))
      self.positionY += self.dy * (self.velocity + (self.accelerationValue * self.accelerationTicks))

  def wallBounce(self):
    if self.positionX <= 0:
      self.dx *= -1
      return 0
    if self.positionX >= 900:
      self.dx *= -1
      return 1
    if self.positionY <= 0:
      self.dy *= -1
      return 2
    if self.positionY >= 700:
      self.dy *= -1
      return 3

  def checkTouchesPlayer(self, listOfPlayers):
    for player in listOfPlayers:
      playerId = player.playerId
      playerPositionX = player.positionX
      playerPositionY = player.positionY

      if playerId == 0:
        if playerPositionX + 16.5 <= self.positionX <= playerPositionX + 17 and playerPositionY <= self.positionY <= (
                playerPositionY + 90):
          print("touched player 0")
          self.dx *= -1
          return playerId, 1

      if playerId == 1:
        if playerPositionX <= self.positionX <= playerPositionX + 0.5 and playerPositionY <= self.positionY <= (
                playerPositionY + 90):
          print("touched player 1")
          self.dx *= -1
          return playerId, 1

      if playerId == 2:
        if playerPositionY + 13 <= self.positionY <= playerPositionY + 15 and playerPositionX <= self.positionX <= (
                playerPositionX + 90):
          print("touched player 2")
          self.dy *= -1
          return playerId, 1

      if playerId == 3:
        if playerPositionY <= self.positionY <= playerPositionY + 2 and playerPositionX <= self.positionX <= (
                playerPositionX + 90):
          print("touched player 3")
          self.dy *= -1
          return playerId, 1

    return None, None
