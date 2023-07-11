# CUBE_SOLVER
this program takes user input of cube and solves it 
Program to solve rubiks cube/rubiks cube copilot 

This program makes use of a module named kociemba 
Kociemba takes the cubes state as an input string. And returns the solution of the puzzle in moves 
R-right face clockwise
L-left face clockwise 
D-bottom face clockwise 
U-top face clockwise 
F-front face clockwise
B-back face clockwise 

And letters indicated with a ' mean anticlockwise moves 

For example R'- right face anticlockwise and so on...

The rubiks cube has 27 pieces 
54 total stickers 
And can result in about 43 quintillion different possibilities *10¹⁸

the cube has 6 faces 
Each sticker is numbered say from 1 to 54 
Now green is put in front , orange to the left and white on top , 
Green color becomes our F color 
Orange becomes our L color 
Red becomes our R color 
And so on...

So now the input string for kociemba goes something like this: 

"Top state | right state | front state | left state | down state | back state "

So let's say on front face , the corner pieces are blue and edges are green
Our top state would be -
FBFBFBFBF
B=back color =blue
F=front color = green 

The input of kociemba of a solved cube will be 
UUUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB


An exception is rased if an invalid state is input 
 
The given input is stored as list first, so that the user can modify which indexes he wishes to change , the modify function prints the piece number format, the user can identify it easily 
#List_change
It also uses proper input function 


There are functions to make sure the user enters colors of the stickers correctly 
#proper_input 
This makes sure user doesn't enter words or letters that don't match the needed input 


Then there is a function that converts proper input to kociembas input format 
#colortokoci 

Then there are a couple of functions to print 
#line_space
#print_statements
#cubestateforinput
#pieces location

There are some which convert input list to string 

Also here is how kociemba works: 

Any combination from the 43 quintillion possibilities can be solved in less than 20 moves 
Kociemba uses khorfs algorithm which is a complex cube solving algorithm that moves the cube into an easier state in each turn .
