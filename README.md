# Snake

The snake's main function is devided into three parts: snake behavior, monster behavior and food behavior.
Firstly, the snake's behavior can be divided into two parts, namely the movement of the snakehead and the following of the snake's body. 
The monster's behavior is to chase the snakehead.
The behavior of food is divided into two parts, the placement and the consumption, in which the consumption process is associated with the lengthening of the snake body. Each food is an instance of a turtle and is placed in the same list. The value of the food number minus 1 is its index value in the list. The position of each food is determined by a randomly generated horizontal and vertical coordinate on the screen. 
After implementing the main functions, I set up the introduction of the game on the starting screen, the counters and timers on the title of the game, and the parts of stopping the game when the game wins or loses.

**Data Types**

Snake heads, monsters, and food are set as turtle instances. This arrangement of snakehead and monsters allows them to move and turn flexibly, and a turtle instance of food allows them to write a number in their place and remove the writing marks when consumed. When the distance between the snakehead and the food is less than 20 units (that is, the length of the snakehead), the food is consumed, its position is shifted off the screen, and the food disappears from the field of vision.

**Motion Logic for Both Snake and Monster**

Snakehead movement is achieved by setting snakehead as a turtle instance and moving the turtle position. Use the arrow keys to change the direction of the snakehead and advance it 20 units in each ontimer loop. Snake body uses stamp function. Add this coordinate to the list of coordinates of the snake stamp by copying the coordinates of the latest stamp in each ontimer loop and letting the change of its coordinates be determined by the latest movement of the snake head. Remove the earliest stamp from the coordinates list of the stamp, remove all the original seals, and use the new coordinates list to make the stamp to move the snake. The monster's behavior is also realized by setting the monster as a turtle instance, and the monster's movement direction is determined by dividing the range of the Angle between the snakehead and the monster, so that the monster can continue to chase the snake head.

**The Expansion Logic for the Snake Tail**

The snake's growth length is the same as the number name of the food consumed. Whenever a food is consumed, if the food name size is set to n, the earliest stamp is not removed in this n-round ontimer cycle, thus achieving the growth of snake body.

**Body Contact Logic Between the Monster and the Snake**

Whenever the distance between the monster and the position in the list of position coordinates is less than 15 units, count one contact.
