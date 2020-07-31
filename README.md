# Level Builder by [Void Light](http://voidlight.cf)
## Download in the [Releases tab](https://github.com/SEEK-THE-VOID-LIGHT/level-builder/releases)

As I was making pygame games, the level builing with a grid fast became a good method for level design for me. :smile: For those, who don't know that, you have multidimensional lists in which you define the blocks in rows and collums. *Example (**The first level of my game joho jump'n'run**)*:
```python
level1 = ["....................",
"....................",
"......oo.........oEo",
"o.....xx........oxox",
"x.....xx........xxxx",
"x.....xx.....o..xxxx",
"xooo..xx.....x..xxxx",
"xxxx..xx.....x..xxxx",
"xxxx..xx.....x..xxxx",
"xxxx..oo.....x..xxxx",
"xxxx..xx.....x..xxxx",
"xxxx..xx.....x..xxxx",
"xxxx.ooooo...x..xxxx",
"xxxx.xxxxx..xxx.xxxx",
"xxxxSxxxxx.xxxxxxxxx",
"oooooooooooooooooooo"]
```
##### The design and writing of these levels was long and inconvenient and creating levels in a team is often confusing.
![screenshot of the level builder](https://github.com/SEEK-THE-VOID-LIGHT/SEEK-THE-VOID-LIGHT.github.io/blob/master/images/levelbuilder.jpg)

### You have to start the program from the terminal, to tell the code how many rows and collums of blocks you have:
> python builder.py \<rows\> \<collums\>

In my opinion the controls of the program are intuitive. When you click on export, the program will generate a multi dimensional array that will be displayed in the terminal ready to be copied :wink:

###The only thing you have to do is to implement those to your code. For clarification the characters are:
Block type | Character
---------- | ---------
Spawn block | S
Custom block 1 | x (lowercase)
Custom block 2 | X (uppercase)
Extra block 1 | o (lowercase)
Extra block 2 | O (uppercase)
End block | E
normal platform | p

The cutom and extra blocks are up to you to define :wink:
###### PS: Dont blame me for using pygame

