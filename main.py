import argparse
import logging
import os
import pygame
import time
import subprocess
import json
import random


class StepAway:
    short_freq_min = None
    short_length_s = None
    long_freq_min = None
    long_length_min = None
    args = []
    current_break_type = None

    def __init__(
        self, short_freq_min=10, short_length_s=20, long_freq_min=30, long_length_min=5
    ) -> None:
        self.short_freq_min = short_freq_min
        self.short_length_s = short_length_s
        self.long_freq_min = long_freq_min
        self.long_length_min = long_length_min

        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logging.info("Welcome to Step Away!")

        parser = argparse.ArgumentParser()
        parser.add_argument("--break_now", help="Start with a break in min")
        self.args = parser.parse_args()

    def take_break(self, s):
        self.pause_media_player()
        pygame.init()
        screen_size = pygame.display.Info().current_w, pygame.display.Info().current_h
        screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
        screen.fill((0, 0, 0))
        self.show_message(screen)
        pygame.display.update()
        logging.info(
            f"Taking a {str(s if s < 60 else s/60)} {'second' if s < 60 else 'minute'} break"
        )
        time.sleep(s)
        pygame.quit()
        os.system("aplay gong.wav")

    def get_random_exercise(self):
        with open("exercises.json", "r") as f:
            exercises = json.load(f)
        return random.choice(exercises)

    def show_message(self, screen):
        font_size = 32
        font = pygame.font.Font(None, font_size)
        line1 = font.render(self.current_break_type, True, (255, 255, 255))
        line2 = font.render(self.get_random_exercise(), True, (255, 255, 255))

        # get the text surface dimensions
        line1_width, line1_height = line1.get_size()
        line2_width, line2_height = line2.get_size()

        # calculate the position to center the text
        display_info = pygame.display.Info()
        x1 = display_info.current_w // 2 - line1_width // 2
        y1 = display_info.current_h // 2 - (line1_height + line2_height) // 2
        x2 = display_info.current_w // 2 - line2_width // 2
        y2 = y1 + line1_height

        # blit the text surfaces onto the screen surface
        screen.blit(line1, (x1, y1))
        screen.blit(line2, (x2, y2))

        # update the screen
        pygame.display.flip()

    def pause_media_player(self):
        subprocess.call(["playerctl", "pause"])

    def run(self):
        if self.args.break_now:
            self.take_break(int(self.args.break_now) * 60)

        count = self.short_freq_min * 60
        while True:
            logging.info("Starting loop interation")

            logging.info(f"Sleeping for {self.short_freq_min} min")
            time.sleep(self.short_freq_min * 60)

            time_for_long = count % (self.long_freq_min * 60) == 0
            logging.info(f"Taking a {'long' if time_for_long else 'short'} break")

            if time_for_long:
                self.current_break_type = "Long break"
                self.take_break(self.long_length_min * 60)
            else:
                self.current_break_type = "Short break"
                self.take_break(self.short_length_s)

            count += self.short_freq_min * 60


step_away = StepAway()
step_away.run()
