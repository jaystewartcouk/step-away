#!/usr/bin/env python3
import os
import time
from tqdm import tqdm
from base import Base
from tray import Tray
from window import Window
import subprocess
import platform


class StepAway(Base):
    window = None
    tray = None
    seconds_worked = 0

    def __init__(self) -> None:
        super().__init__()
        self.window = Window()
        self.tray = Tray()

    def pause_players(self):
        # True players only: vlc, mpv, RhythmBox, web browsers, cmus, mpd, spotify..
        if platform.system() == "Linux" and "TRAVIS" not in os.environ:
            subprocess.call(["playerctl", "pause"])

    def take_break(self, duration):
        self.pause_players()
        self.window.current_break_duration = duration
        if "TRAVIS" not in os.environ:
            self.window.open()
        self.show_progress_bar(duration)
        if self.tray.stop_flag is not True:
            self.window.close()

    def show_progress_bar(self, seconds):
        # create a tqdm progress bar with the total duration
        with tqdm(total=seconds) as pbar:
            # loop for the duration of the progress bar
            for i in range(seconds):
                # update the progress bar every second
                while self.tray.pause_flag is True:
                    pass
                if self.tray.skip_flag | self.tray.restart_flag | self.tray.stop_flag:
                    self.tray.skip_flag = False
                    break
                pbar.update(1)
                time.sleep(1)

    def run(self):
        if self.config.DELAY > 0:
            self.take_break(self.config.DELAY)

        while True and self.tray.stop_flag is False:
            if self.seconds_worked > 0:
                self.log.info(f"Worked {int(self.seconds_worked/60)} minutes")

            # Screen time
            self.show_progress_bar(self.config.WORK_DURATION)
            if self.tray.stop_flag is True:
                break
            elif self.tray.restart_flag is True:
                self.seconds_worked = 0
                self.tray.restart_flag = False
                continue

            self.seconds_worked += self.config.WORK_DURATION

            if self.tray.skip_to_long_flag is True:
                is_long_break = True
                self.tray.skip_to_long_flag = False
            else:
                # true when self.seconds_worked is a multiple of LONG_BREAK_FREQUENCY_SECONDS
                is_long_break = (
                    self.seconds_worked % self.config.LONG_BREAK_FREQUENCY_SECONDS == 0
                )

            # Break time
            self.take_break(
                self.config.LONG_BREAK_LENGTH_SECONDS
                if is_long_break
                else self.config.SHORT_BREAK_LENGTH_SECONDS
            )


def main():
    step_away = StepAway()
    step_away.run()


if __name__ == "__main__":
    main()
