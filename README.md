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

Python 3 is all that is required to run this
The main bulk of the program is in the arena.py file where the
monMons do all of the battling.



If you want to create more monMons then you can run the 
```
createChildren(numOfChildren)
```
function in the python console  which will create that many children 
from the pool

Or you can make them fight and have either 1 or a few winners with
```
startBattleRoyal(winnersLeft)
```
I have yet to implement a way to see all the winners and their final
stats cleanly
