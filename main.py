import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()

  cars.create_car()
  cars.move_cars()

  # Detect if turtle collides with a car
  for car in cars.all_cars:
    if car.distance(player) < 20:
      game_is_on = False

  # Detect if player finished
  if player.is_finished():
    player.goto_start()
    cars.level_up()

screen.exitonclick()
