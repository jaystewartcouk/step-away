import argparse
import logging
import os
import pygame
import time
import subprocess
import json
import random
from tqdm import tqdm


class StepAway:
    short_break_freq_min = None
    short_break_length_sec = None
    long_break_freq_min = None
    long_break_length_min = None
    args = []
    current_break_type = None

    def __init__(
        self,
        short_break_freq_min=10,
        short_break_length_sec=20,
        long_break_freq_min=30,
        long_break_length_min=5,
    ) -> None:
        self.short_break_freq_min = short_break_freq_min
        self.short_break_length_sec = short_break_length_sec
        self.long_break_freq_min = long_break_freq_min
        self.long_break_length_min = long_break_length_min

        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logging.info("Welcome to Step Away!")

        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--short_break_freq_min", help="Short break frequency in minutes"
        )
        parser.add_argument(
            "--short_break_length_sec", help="Short break length in minutes"
        )
        parser.add_argument(
            "--long_break_freq_min", help="Long break frequency in minutes"
        )
        parser.add_argument(
            "--long_break_length_min", help="Long break length in minutes"
        )
        parser.add_argument("--break_now", help="Start with a break in minutes")
        self.args = parser.parse_args()

        if self.args.short_break_freq_min:
            self.short_break_freq_min = int(self.args.short_break_freq_min)
        if self.args.short_break_length_sec:
            self.short_break_length_sec = int(self.args.short_break_length_sec)
        if self.args.long_break_freq_min:
            self.long_break_freq_min = int(self.args.long_break_freq_min)
        if self.args.long_break_length_min:
            self.long_break_length_min = int(self.args.long_break_length_min)

    def get_random_exercise(self):
        with open("exercises.json", "r") as f:
            exercises = json.load(f)
        random.seed(time.time())
        return random.choice(exercises)

    def open_window(self):
        pygame.init()
        screen_size = pygame.display.Info().current_w, pygame.display.Info().current_h
        screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 32)
        text = ""
        text = f"{self.current_break_type}: " if self.current_break_type else ""
        text += self.get_random_exercise()
        text_surface = font.render(text, True, (255, 255, 255))
        # get the dimensions of the text surface
        text_width, text_height = text_surface.get_size()
        # calculate the center position for the text
        x = (screen_size[0] / 2) - (text_width / 2)
        y = (screen_size[1] / 2) - (text_height / 2)
        # blit the text surface onto the center of the screen
        screen.blit(text_surface, (x, y))
        # update the display
        pygame.display.flip()

    def take_break(self, s):
        logging.info(
            f"Taking a {str(s if s < 60 else int(s/60))} {'second' if s < 60 else 'minute'} break"
        )
        # For true players only: vlc, mpv, RhythmBox, web browsers, cmus, mpd, spotify and others.
        subprocess.call(["playerctl", "pause"])
        self.open_window()
        os.system("aplay sound.wav")
        time.sleep(s)
        pygame.quit()
        os.system("aplay sound.wav")

    def run(self):
        if self.args.break_now:
            self.take_break(int(self.args.break_now) * 60)

        count = self.short_break_freq_min * 60
        while True:
            work_duration_seconds = self.short_break_freq_min * 60
            # create a tqdm progress bar with the total duration
            with tqdm(total=work_duration_seconds) as pbar:
                # loop for the duration of the progress bar
                for i in range(work_duration_seconds):
                    # update the progress bar every second
                    pbar.update(1)
                    time.sleep(1)

            time_for_long = count % (self.long_break_freq_min * 60) == 0
            logging.info(f"Taking a {'long' if time_for_long else 'short'} break")

            if time_for_long:
                self.current_break_type = "Long break"
                self.take_break(self.long_break_length_min * 60)
            else:
                self.current_break_type = "Short break"
                self.take_break(self.short_break_length_sec)

            count += self.short_break_freq_min * 60


def main():
    step_away = StepAway()
    step_away.run()


if __name__ == "__main__":
    main()
