# :radioactive: Step Away! :radioactive:
A simple screen break program. "Step away" typically means to physically remove oneself from a situation or environment in order to take a break, clear one's head, or gain perspective. This program shows you a blank screen with an exercise to remind you to take breaks and move.

## Warnings
- This is an MVP.
- This is hardcoded to 20 second breaks every 10 minutes and 5 minute breaks every 30 minutes.

## Requirements
Pygame is used for the break screen

`pip install pygame`

Playerctl is used to pause media

`sudo apt install playerctl`

## Usage
`python main.py`

```
usage: main.py [-h] [--take_break TAKE_BREAK]

options:
  -h, --help            show this help message and exit
  --take_break TAKE_BREAK
                        Start with a break in minutes
```

## Testing
Only tested on Ubuntu 22.04.2 LTS.

## :exploding_head: Contribution Ideas :exploding_head:
1. As a screen addict, I want configure my break times so that I don't go square eyed.

## Credits
- "gong.wav" by InspectorJ ([www.jshaw.co.uk](https://www.jshaw.co.uk)) of [Freesound.org](http://freesound.org/)
- Exercises by University Health Service of [University of Michigan](https://uhs.umich.edu/computerergonomics)
- Inspired by [Safe Eyes](https://github.com/slgobinath/SafeEyes)