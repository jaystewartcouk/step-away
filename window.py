import pygame
import json
import random
import time
import os


class Window:
    pyg = pygame
    exercise_file = "exercises.json"
    sound_file = "sound.wav"

    def __init__(self) -> None:
        self.pyg.init()

    def get_file_path(self, file):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, file)
        return file_path

    def play_sound(self):
        sound = self.pyg.mixer.Sound(self.get_file_path(self.sound_file))
        sound.play()
        self.pyg.time.wait(int(sound.get_length() * 1000))

    def get_random_exercise(self):
        with open(self.get_file_path(self.exercise_file), "r") as f:
            exercises = json.load(f)
        random.seed(time.time())
        return random.choice(exercises)

    def get_text(self):
        duration = self.current_break_duration
        text = str(duration) if duration < 60 else str(int(duration / 60))
        text += " "
        text += "second" if duration < 60 else "minute"
        text += ": "
        text += self.get_random_exercise()
        return text

    def open(self):
        screen_size = (
            self.pyg.display.Info().current_w,
            self.pyg.display.Info().current_h,
        )
        screen = self.pyg.display.set_mode(screen_size, self.pyg.FULLSCREEN)
        screen.fill((0, 0, 0))
        font = self.pyg.font.Font(None, 32)
        text_surface = font.render(self.get_text(), True, (255, 255, 255))
        # get the dimensions of the text surface
        text_width, text_height = text_surface.get_size()
        # calculate the center position for the text
        x = (screen_size[0] / 2) - (text_width / 2)
        y = (screen_size[1] / 2) - (text_height / 2)
        # blit the text surface onto the center of the screen
        screen.blit(text_surface, (x, y))
        # update the display
        self.pyg.display.flip()
        self.play_sound()

    def close(self):
        self.play_sound()
        self.pyg.quit()
