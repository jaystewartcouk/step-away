# :radioactive: Step Away!
A simple screen break program. "Step away" typically means to physically remove oneself from a situation or environment in order to take a break, clear one's head, or gain perspective. This program shows you a blank screen with a physical exercise to remind you to take breaks and move.

## :warning: Warnings
- Only tested on Ubuntu 22.04.2 LTS

## :mag: Requirements
pygame is used for the break screen

`pip install pygame`

playerctl is used to pause media

`sudo apt install playerctl`

tqdm is used to quickly see how long until next break

`pip install tqdm`

`pip install python-dotenv`

## :sunglasses: Usage
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
## Configuration
Use command line arguments above or `cp .env.example .env`.

## :bulb: Roadmap
* [x] Cross-platform system tray icon and controls
* [ ] Write tests
* [ ] Add linters and static analyzers
* [ ] Set up CI

## :green_heart: Credits
- Exercises by University Health Service of [University of Michigan](https://uhs.umich.edu/computerergonomics)
- Inspired by [Safe Eyes](https://github.com/slgobinath/SafeEyes)

## License
https://opensource.org/license/mit/
