from config import Config
from window import Window
import logging
import os
import time
import subprocess
from tqdm import tqdm
import json
import random
import time


class StepAway:
    current_break_type = None
    config = None

    def __init__(self) -> None:
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logging.info("Welcome to Step Away!")
        self.config = Config()

    def pause_player(self):
        # True players only: vlc, mpv, RhythmBox, web browsers, cmus, mpd, spotify..
        subprocess.call(["playerctl", "pause"])

    def play_sound(self):
        os.system("aplay sound.wav")

    def get_text(self, seconds):
        text = str(seconds) if seconds < 60 else str(int(seconds / 60))
        text += " "
        text += "second" if seconds < 60 else "minute"
        text += ": "
        text += self.get_random_exercise()
        return text

    def get_random_exercise(self):
        with open("exercises.json", "r") as f:
            exercises = json.load(f)
        random.seed(time.time())
        return random.choice(exercises)

    def take_break(self, seconds):
        self.pause_player()
        Window.open(self.get_text(seconds))
        self.play_sound()
        self.show_pbar(seconds)
        Window.close()
        self.play_sound()

    def show_pbar(self, seconds):
        # create a tqdm progress bar with the total duration
        with tqdm(total=seconds) as pbar:
            # loop for the duration of the progress bar
            for i in range(seconds):
                # update the progress bar every second
                pbar.update(1)
                time.sleep(1)

    def run(self):
        if self.config.DELAY:
            self.take_break(self.config.DELAY)

        break_stopwatch = 0
        while True:
            self.show_pbar(self.config.SHORT_BREAK_FREQUENCY_SECONDS)
            break_stopwatch += self.config.SHORT_BREAK_FREQUENCY_SECONDS
            is_long_break = (
                break_stopwatch % self.config.LONG_BREAK_FREQUENCY_SECONDS == 0
            )
            self.current_break_type = "long" if is_long_break else "short"
            logging.info(f"Taking a {self.current_break_type} break")
            self.take_break(
                self.config.LONG_BREAK_LENGTH_SECONDS
                if is_long_break
                else self.config.SHORT_BREAK_LENGTH_SECONDS
            )
            break_stopwatch += self.config.SHORT_BREAK_FREQUENCY_SECONDS


def main():
    step_away = StepAway()
    step_away.run()


if __name__ == "__main__":
    main()
