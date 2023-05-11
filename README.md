# :radioactive: Step Away! :radioactive:
A simple screen break program. "Step away" typically means to physically remove oneself from a situation or environment in order to take a break, clear one's head, or gain perspective. This program shows you a blank screen with an exercise to remind you to take breaks and move.

## Warnings
- This is an MVP.
- This is hardcoded to 20 second breaks every 10 minutes and 5 minute breaks every 30 minutes.

## Requirements
pygame is used for the break screen

`pip install pygame`

playerctl is used to pause media

`sudo apt install playerctl`

tqdm is used to quickly see how (long) until next break

`pip install tqdm`

`pip install python-dotenv`

## Usage
`python main.py`

```
usage: main.py [-h] [--short_break_frequency_minutes SHORT_BREAK_FREQUENCY_MINUTES] [--short_break_length_seconds SHORT_BREAK_LENGTH_SECONDS]
               [--long_break_frequency_minutes LONG_BREAK_FREQUENCY_MINUTES] [--long_break_length_minutes LONG_BREAK_LENGTH_MINUTES] [--delay DELAY]

options:
  -h, --help            show this help message and exit
  --short_break_frequency_minutes SHORT_BREAK_FREQUENCY_MINUTES
  --short_break_length_seconds SHORT_BREAK_LENGTH_SECONDS
  --long_break_frequency_minutes LONG_BREAK_FREQUENCY_MINUTES
  --long_break_length_minutes LONG_BREAK_LENGTH_MINUTES
  --delay DELAY
```

## Testing
Only tested on Ubuntu 22.04.2 LTS.

## :exploding_head: Contribution Ideas :exploding_head:
1. Create a testing plan
2. Create a system tray icon

## Credits
- Exercises by University Health Service of [University of Michigan](https://uhs.umich.edu/computerergonomics)
- Inspired by [Safe Eyes](https://github.com/slgobinath/SafeEyes)