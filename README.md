# monMon Arena

This was a little project that spawned out of a game called 
"Pocket Frogs" made by NimbleBit where you tame, breed and sell 
frogs. What interested me was that there were 38,272 unique different
frogs that can be bred there. With 23 diffent base colors,16 
accent colors and 104 patterns. I wanted to see if I could try 
and replicate that. So I came up with monMons.

monMons are little creatures that can be described as many things.
One of those descriptions is the one that I have programed here.
They looked up to their older cousin Pokemon and decided that
they will copy their behavior of fighting. They don't feel that
they should do anything else but to fight and produce more better
and stronger versions of themselves.

### Prerequisites

Python 3 is all that is required to run this.
Pillow is also required to run the painter and forest folders

If you want to create more monMons then you can run the 
```
createChildren(numOfChildren)
```
function in the python console  which will create that many children 
from the pool

Or you can make them fight and have either 1 or a few winners with
```
startBattleRoyale(winnersLeft)
```
I have yet to implement a way to see all the winners and their final
stats cleanly

There are three diffrent descriptions of the monMons.
## Fighter
These monMons have looked up to Pokemon and have decided to take one
thing away, fighting.

Each mon has 3 main attributes:
    + Health
    + Attack
    + Defence

They also have secondary attributes:
    + Wins
    + Lives (chances)
    + Name and Name2 (these don't do anything)

When 2 monMons are pitted against each other, the first mon gets to
attack by generating a number between 1 and the range (set at the 
start). If the number generated is larger than the mon's attack
value then the mon has missed and does no damage. However, if the 
number generated is lower than the attack, then the mon has dealt 
damage equal to that number. The second mon gets to defend using 
the same method. When the mon successfully defends, then generated
defence value is subtracted from the attack value of the attacking
mon. If this value is below 0, then no damage will be done to the 
attacking mon. Only if the calculated value is above 0 will there be
damage to the defending mon.

This process is then repeated with the role swapped and until one of
them drops dead (health <= 0)

Once the total population reaches half it's size, then, they all
reproduce until they are back at full size and repeat the process.

## Painter
These monMons have took on a more peaceful approch to life. In fact,
they don't actually die. All they do is represent a color of a pixel
in an image. They have 3 attributes:
    + Red
    + Green
    + Blue

## Forest Dwellers
These monMons are more interesting. They are a combination of fighters
and painters. They have 6 attributes:
    + Health
    + Attack
    + Defence
    + Red
    + Green
    + Blue

They decided that names were not nessesary and a total waste of space.

They use a 2 stage cycle. The first is fight, see the section on fighters
for how they do so. The next stage is is painting. Collectively, the 
monMons create a picture together using the other three attributes as a
sort of momento for all the bloodshed and the new (hopefully) stronger
generation that has arrived. They store this picture in the 'images' 
folder.

They are quite intelligent, you know. They have created a tool to upscale
their images to a size more suitable for viewing called 'upscale.py' in the
images folder. You still have to manually adjust the settings in the file to
properly upscale all the images.
