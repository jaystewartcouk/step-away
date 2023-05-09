import logging as log
import pygame
import time as t
import tkinter as tk

log_format = "%(asctime)s - %(levelname)s - %(message)s"
log.basicConfig(level=log.DEBUG, format=log_format)
log.info("Welcome to Step Away!")

short_break_freq_mins = 10
short_break_len_secs = 20
long_break_freq_mins = 30
long_break_len_mins = 5

root = tk.Tk()


def step_away(len_secs):
    pygame.init()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 0))
    pygame.display.update()
    t.sleep(len_secs)
    pygame.quit()


count = short_break_freq_mins * 60
while True:
    log.info("Starting loop interation")

    log.info(f"Sleeping for {short_break_freq_mins} minutes")
    t.sleep(short_break_freq_mins * 60)

    time_for_long_break = count % (long_break_freq_mins * 60) == 0
    log.info(f"Taking a {'long' if time_for_long_break else 'short'} break")

    if time_for_long_break:
        step_away(long_break_len_mins * 60)
    else:
        step_away(short_break_len_secs)

    count += short_break_freq_mins * 60
