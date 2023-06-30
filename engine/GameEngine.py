import pygame

from Player import Player

Players = [Player(0)]  # 0 and 1 are left and right, 2 and 3 are top and bottom


def drawPlayers(listOfPlayers, screen):  # Draws the player rectangles
  for player in listOfPlayers:
    pygame.draw.rect(screen, player.color, pygame.Rect(player.positionX, player.positionY, player.width, player.height))


def movePlayers(listOfPlayers):  # Updates the X and Y position of each player based on the current keys pressed
  for player in listOfPlayers:
    player.move()


# Initialize game and screen
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True

while running:
  # Clicking on the X will end the game.
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Fill the screen black
  screen.fill("black")

  # These two basically update the game
  drawPlayers(Players, screen)
  movePlayers(Players)

  pygame.display.flip()
  # Limit the fps to 60
  clock.tick(60)

pygame.quit()
