# Nonogram
This program is my attempt to create a nongram game that can generate its own patterns and user generated ones too.

To mark a square as used (or black), click in a box while the upper left box is black.
To mark a square as unused (or red), click in a box while the upper left box is red.

To change the color of the upper right box, just click it.

When you complete the puzzle (Occurs when you select every black square in the puzzle), it will display a text so you know that you won.

In the main loop at the bottom you can uncomment the code to choose which way you want to play.

Different game modes:

-Line 223, change the puzzle array to one of your own creation (similar to the sailboat example on line 201)

-Line 224, generate a random puzzle and change the difficulty on line 216

-Line 225, custom generate your own puzzle with a more customizable function. Put your max limit first, and then the number that would include all of the numbers below it that you want to be black (This is still random, but gives a higher or lower amount of black squares depending on the numbers you enter

-Line 226, this one randomly selects a puzzle out of the collection list on line 214. You can add your own puzzles to this array and then play them randomly

This project was a way for me to be creative and build a fun working game that I love to play. Enjoy!!
