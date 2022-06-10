# Devlog

## May
<details closed>
<summary>May 17, 2022</summary>
Started the project, currently just making the game itself.

The board being drawn, and random bomb generation, is what's completed so far.

![alt text](https://github.com/AdamMetz/Minesweeper-AI/blob/main/devlog-images/05-17-22/board.PNG)
</details>

<details closed>
<summary>May 18, 2022</summary>

Added a bomb detection for each Tile, so each Tile can see how many bombs are surrounding it.

~~Then I realized quite the oversight in my bomb generation, I can't just randomly assign any Tile to a bomb,
it has to be done so in an algorithmic way so that every Tile has at least one surrounding bomb.~~
Not sure why I thought this at the time ^

![alt text](https://github.com/AdamMetz/Minesweeper-AI/blob/main/devlog-images/05-18-22/board.PNG)
</details>

<details closed>
<summary>May 16, 2022</summary>

The construction of the game itself is pretty much complete now. Did a ton of reorganizing, moving each class into seperate files,
and moved all variable accessing to getters and setters.

![alt text](https://github.com/AdamMetz/Minesweeper-AI/blob/main/devlog-images/05-26-22/board.PNG)
</details>

## June
<details closed>
<summary>June 8, 2022</summary>

Worked on touching up some of the code and improving the readability. Also adjusted the y offsets for grid generation, to 
allow for the addition of a header at the top of the game window.
Header to be implemented, will included a reset game button, timer, and bomb count.

![alt text](https://github.com/AdamMetz/Minesweeper-AI/blob/main/devlog-images/06-08-22/board.PNG)
</details>

<details closed>
<summary>June 9, 2022</summary>

Worked on the header, timer will be next. Then it will be time to focus on the main component of the project, learning how to use/implement AI

![alt text](https://github.com/AdamMetz/Minesweeper-AI/blob/main/devlog-images/06-09-22/board.PNG)
</details>