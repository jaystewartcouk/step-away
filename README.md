# :radioactive: Step Away!
"Step away" typically means to physically remove oneself from a situation or environment in order to take a break, clear one's head, or gain perspective.

A simple screen break program which shows you a blank screen with a physical exercise to remind you to take breaks and move.

## Features
- Configure a short break interval and duration
- Configure a long break interval and duration
- System tray icon controls (Pause, Resume, Skip, Skip to long, Stop)

## :warning: Warnings
- Only tested on Ubuntu 22.04.2 LTS

## :mag: Requirements
`pip install -r requirements.txt`

## :sunglasses: Usage
`python main.py`

```
usage: main.py [-h] [--short_break_frequency_minutes SHORT_BREAK_FREQUENCY_MINUTES] [--short_break_length_seconds SHORT_BREAK_LENGTH_SECONDS]
               [--long_break_frequency_minutes LONG_BREAK_FREQUENCY_MINUTES] [--long_break_length_minutes LONG_BREAK_LENGTH_MINUTES] [--delay DELAY]

options:
  -h, --help            show this help message and exit
  --short_break_frequency_minutes SHORT_BREAK_FREQUENCY_MINUTES
                        (Needs to go evenly into long_break_frequency_minutes)
  --short_break_length_seconds SHORT_BREAK_LENGTH_SECONDS
  --long_break_frequency_minutes LONG_BREAK_FREQUENCY_MINUTES
                        (Needs to be a multiple of short_break_frequency_minutes)
  --long_break_length_minutes LONG_BREAK_LENGTH_MINUTES
  --delay DELAY
```
## :high_brightness: Configuration
Please use the command line arguments above or `cp .env.example .env`.

:warning: SHORT_BREAK_FREQUENCY_MINUTES needs to go evenly into LONG_BREAK_FREQUENCY_MINUTES

:warning: LONG_BREAK_FREQUENCY_MINUTES needs to be a multiple of SHORT_BREAK_FREQUENCY_MINUTES

## :bulb: Roadmap
* [x] Cross-platform system tray icon and controls
* [ ] Write tests
* [ ] Add linters and static analyzers
* [ ] Set up CI

## :green_heart: Credits
- Exercises by University Health Service of [University of Michigan](https://uhs.umich.edu/computerergonomics)
- Inspired by [Safe Eyes](https://github.com/slgobinath/SafeEyes)

## :scroll: License
https://opensource.org/license/mit/

## :cartwheeling: Break screen exercises
```
[
    "Neck Rotation: Slowly rotate your head as far as comfortable to the right, then left.",
    "Shoulder Rotation: Circle your shoulders, then reverse directions.",
    "Head Side to Side: Bend your neck so left ear approaches left shoulder, then repeat for right.",
    "Chin Tuck: Slide your chin inward, without bending your neck up or down.",
    "Shoulder Blade Retraction: Pull your shoulders down and back.",
    "Shrug: Slowly raise your shoulders toward ears and hold for a few seconds.",
    "Shoulder Squeeze: Raise your arms in front of body, with elbows bent and thumbs up. Pull elbows back, squeezing shoulder blades together.",
    "Stretch Up: Sit up straight and imagine a cable attached to the top of your head. Gradually stretch up, then relax.",
    "Arm Relaxation: Drop your arms and hands to your sides. Gently shake them for a few seconds.",
    "Arm Rotation: Raise your arms in front of your body. Rotate arms so palms face up, then rotate so backs of hands face each other.",
    "Wrist Flex: With your elbows on desk, gently use left hand to bend right hand back toward forearm. Repeat on other side.",
    "Finger Fan: Spread your fingers as far apart as possible, hold, then clench fists, then release.",
    "Toe Curl: Flex toes up, then curl toes under. Release.",
    "Foot Rotation: Circle foot slowly from the ankle, then reverse.",
    "Eye Rolls: Roll your eyes clockwise then counterclockwise briefly.",
    "Palm Eyes: Without touching your eyes, cup hands lightly over eyes for 30 seconds to rest them from light.",
    "Look Away: Exercise your eyes by periodically looking away from your computer to focus on distant objects."
]
```

## :camera: Screenshots
![alt text](https://github.com/jaystewartcouk/step-away/blob/main/screenshots/tray.png?raw=true)
![alt text](https://github.com/jaystewartcouk/step-away/blob/main/screenshots/window.png?raw=true)

