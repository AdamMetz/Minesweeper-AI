# Devlog

## May 17, 2022

Started the project, currently just making the game itself.

The board being drawn, and random bomb generation, is what's completed so far.

![alt text](https://github.com/AdamMetz/Minesweeper-AI/blob/main/devlog-images/05-17-22/board.PNG)

## May 18, 2022

Added a bomb detection for each Tile, so each Tile can see how many bombs are surrounding it.

~~Then I realized quite the oversight in my bomb generation, I can't just randomly assign any Tile to a bomb,
it has to be done so in an algorithmic way so that every Tile has at least one surrounding bomb.~~
Not sure why I thought this at the time ^

![alt text](https://github.com/AdamMetz/Minesweeper-AI/blob/main/devlog-images/05-18-22/board.PNG)

## May 26, 2022

The construction of the game itself is pretty much complete now. Did a ton of reorganizing, moving each class into seperate files,
and moved all variable accessing to getters and setters.

![alt text](https://github.com/AdamMetz/Minesweeper-AI/blob/main/devlog-images/05-26-22/board.PNG)
