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

## Usage
`python main.py`

```
usage: main.py [-h] [--short_break_freq_min SHORT_BREAK_FREQ_MIN] [--short_break_length_sec SHORT_BREAK_LENGTH_SEC] [--long_break_freq_min LONG_BREAK_FREQ_MIN]
               [--long_break_length_min LONG_BREAK_LENGTH_MIN] [--break_now BREAK_NOW]

options:
  -h, --help            show this help message and exit
  --short_break_freq_min SHORT_BREAK_FREQ_MIN
                        Short break frequency in minutes
  --short_break_length_sec SHORT_BREAK_LENGTH_SEC
                        Short break length in minutes
  --long_break_freq_min LONG_BREAK_FREQ_MIN
                        Long break frequency in minutes
  --long_break_length_min LONG_BREAK_LENGTH_MIN
                        Long break length in minutes
  --break_now BREAK_NOW
                        Start with a break in minutes
```

## Testing
Only tested on Ubuntu 22.04.2 LTS.

## :exploding_head: Contribution Ideas :exploding_head:
1. Create a configuration class to store and manage the configuration settings
2. Create a testing plan
3. Create a system tray icon

## Credits
- Exercises by University Health Service of [University of Michigan](https://uhs.umich.edu/computerergonomics)
- Inspired by [Safe Eyes](https://github.com/slgobinath/SafeEyes)