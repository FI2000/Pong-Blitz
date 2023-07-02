import pygame

from Network import Network
from engine.Player import Player
from engine.gameEngineLib import redrawWindow
from networkLib import displayMaxSizeReached, displayServerNotRunning, checkForQuit

networkIP = input("Enter server IP")
networkPort = int(input("Enter server port"))

AllowedPlayerIds = (0, 1, 2, 3)
playerList = []
width, height = 900, 700
Collision = False


def main():

  pygame.init()
  pygame.font.init()
  crash_sound = pygame.mixer.Sound("../sounds/paddle.wav")
  crash_sound.set_volume(0.05)
  winner_sound = pygame.mixer.Sound("../sounds/winner.wav")
  winner_sound.set_volume(0.1)
  pygame.mixer.music.load('../sounds/audio.mp3')
  pygame.mixer.music.set_volume(0.07)
  win = pygame.display.set_mode((width, height))
  pygame.display.set_caption("Client")
  WinnerSoundPlaying = False
  n = Network(networkIP, networkPort)
  clientPlayerId = n.getPlayerId()

  if clientPlayerId in AllowedPlayerIds:
    pygame.mixer.music.play()
    player = Player(clientPlayerId)
    print("Connected as ", player.playerId)
    while True:

      if checkForQuit():
        pygame.mixer.music.stop()
        break
      playerList, pongBall, playerPoints, winnerId, Collision = n.send(player)
      if Collision:
        pygame.mixer.Sound.play(crash_sound)
        Collision = False
      if winnerId != 100:
        pygame.mixer.music.pause()
        if not WinnerSoundPlaying:
          winner_sound.play()
          WinnerSoundPlaying = True
      if winnerId == 100:
        pygame.mixer.music.unpause()
        WinnerSoundPlaying = False
      player.move()
      redrawWindow(win, playerList, pongBall, clientPlayerId, playerPoints, winnerId)

  elif clientPlayerId is None:
    displayServerNotRunning(win, width, height)

  elif clientPlayerId not in AllowedPlayerIds:
    displayMaxSizeReached(win, width, height)


main()
