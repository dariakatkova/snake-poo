The snake game is a type of video game in which the player controls a
snake which grows and thus itself constitutes an obstacle.
The player controls a long, thin line similar to a snake, which must potentially slalom between obstacles that dot the level. To win each level, the player must make his snake eat a certain amount of food, increasing the size of the snake each time. While the snake advances inexorably, the player can only indicate a direction to follow (turn left or right in relation to its current direction) in order to avoid the snake's head touching the walls or his own body, in which case he risks dying. Some variants offer difficulty levels in which the appearance of the level (simple or labyrinthine), the number of foods to eat, the length of the snake or even its speed vary.
The game will also be built here from PlanetTk and an Element Snake whose additional parameters are size, speed and starting direction. A list of contiguous boxes will allow information on the current position of each piece of the snake to be preserved; the value in position 0 corresponding to the cell number of the head.

To move the snake forward, it will be necessary to develop evolutionary programming by assigning:
  — the snake start/stop function on the keyboard space bar
— the function of turning 90 degrees to the left with the left mouse button
— the function of turning 90 degrees to the right with the right mouse button

Note: To move the snake in the current direction, you do not have to move all the squares but only 1! To achieve this, it is enough, for each evolution of the grid, to move the square of the snake's tail to the cell towards which the snake's head should go.

GRADE:
8 points on the basic functionalities shown in class to exploit the final classes of the TP (PlanetTk and Element) in the three requested specializations. Formal ban on not using basic classes without losing 8 points


🟩 a snake made up of blocks
🟥 an apple
🟧 a snake changes color to orange when it dies
⬛ color of obstacles

Functionality:

Snake that dies when it hits a wall
Snake eating an apple
Snake growing
Game win/one score function

Additional:

Pause button
Obstacles
Different levels of play
Bonuses (snake speed, temporary enlargement, etc.)
Creating a Snake, Food, Game class
