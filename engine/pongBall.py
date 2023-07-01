class pongBall:
  def __init__(self, positionX, positionY):
    self.positionX = positionX
    self.positionY = positionY
    self.isMoving = False
    self.velocity = 0.2
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

  def bounce(self, listOfPlayers):
    for player in listOfPlayers:
      self.checkTouchesPlayer(player.playerId, player.positionX, player.positionY)
    if self.positionY <= 0 or self.positionY >= 700:
      self.dy *= -1
    if self.positionX <= 0 or self.positionX >= 900:
      self.dx *= -1

  def checkTouchesPlayer(self, playerId, playerPositionX, playerPositionY):
    if playerId == 0:
      if playerPositionX + 16.5 <= self.positionX <= playerPositionX + 17 and playerPositionY <= self.positionY <= (
              playerPositionY + 90):
        self.dx *= -1

    if playerId == 1:
      if playerPositionX <= self.positionX <= playerPositionX + 0.1 and playerPositionY <= self.positionY <= (
              playerPositionY + 90):
        self.dx *= -1

    if playerId == 2:
      if playerPositionY + 13 <= self.positionY <= playerPositionY + 15 and playerPositionX <= self.positionX <= (
              playerPositionX + 90):
        self.dy *= -1

    if playerId == 3:
      if playerPositionY <= self.positionY <= playerPositionY + 2 and playerPositionX <= self.positionX <= (
              playerPositionX + 90):
        self.dy *= -1
