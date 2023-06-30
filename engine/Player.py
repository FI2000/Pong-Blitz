import random

import pygame.draw


class Player:

  def __init__(self, playerId):
    self.playerId = playerId  # Player Id
    self.positionX, self.positionY = self.spawnPosition()  # Player starting positions
    self.width, self.height = self.dimensions()  # Player dimensions
    self.color = color()
    self.rect = (self.positionX, self.positionY, self.width, self.height)
    self.velocity = 3  # Player velocity

  def move(self):
    keys = pygame.key.get_pressed()
    up, down, left, right, accelerate = currentMovement(keys)

    if not self.isHorizontal() and up:  # If you are on the vertical plane and are pressing up, move up
      self.positionY -= distance(self.velocity, accelerate)

    if not self.isHorizontal() and down:  # // for down
      self.positionY += distance(self.velocity, accelerate)

    if self.isHorizontal() and left:  # If you are on the horizontal plane and are pressing left, move left
      self.positionX -= distance(self.velocity, accelerate)

    if self.isHorizontal() and right:  # // for right
      self.positionX += distance(self.velocity, accelerate)

  def spawnPosition(self):  # Defining spawn positions, hard coded
    if self.playerId == 0:
      return 15, 305
    if self.playerId == 1:
      return 670, 305
    if self.playerId == 2:
      return 305, 15
    if self.playerId == 3:
      return 305, 670

  def dimensions(self):  # Defining dimensions, hard coded
    if self.isHorizontal():
      return 90, 15
    if not self.isHorizontal():
      return 15, 90

  def isHorizontal(self):  # Checks if you are on the horizontal plane or not
    if self.playerId in (2, 3):
      return True
    return False


def distance(velocity, shiftAccelerate):  # Calculates the distance to move per frame
  if shiftAccelerate:
    return velocity * 3
  return velocity


def color():  # 155 to 255 to avoid dark colors
  red = random.randint(155, 255)
  green = random.randint(155, 255)
  blue = random.randint(155, 255)
  return red, green, blue


def currentMovement(keys):  # The movement keys, in a separate method to help with visibility
  return keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_j]