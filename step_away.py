import os
import time
from tqdm import tqdm
from base import Base
from tray import Tray
from window import Window


class StepAway(Base):
    window = None
    tray = None

    def __init__(self) -> None:
        super().__init__()
        self.window = Window()
        self.tray = Tray()

    def get_file_path(self, file):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, file)
        return file_path

    def play_sound(self):
        os.system(f"aplay {self.get_file_path('sound.wav')}")

    def take_break(self, duration):
        self.pause_players()
        self.window.current_break_duration = duration
        self.window.open()
        self.play_sound()
        self.show_progress_bar(duration)
        if self.tray.stop_flag is not True:
            self.window.close()
            self.play_sound()

    def show_progress_bar(self, seconds):
        # create a tqdm progress bar with the total duration
        with tqdm(total=seconds) as pbar:
            # loop for the duration of the progress bar
            for i in range(seconds):
                # update the progress bar every second
                while self.tray.pause_flag is True:
                    pass
                if self.tray.stop_flag is True:
                    break
                if self.tray.skip_flag is True:
                    self.tray.skip_flag = False
                    break
                pbar.update(1)
                time.sleep(1)

    def run(self):
        if self.config.DELAY > 0:
            self.take_break(self.config.DELAY)

        seconds_worked = 0
        while True and self.tray.stop_flag is False:
            self.log.info(f"Seconds worked: {seconds_worked}")

            # Work time
            self.show_progress_bar(self.config.WORK_DURATION)
            seconds_worked += self.config.WORK_DURATION

            if self.tray.stop_flag is False:
                if self.tray.skip_to_long_flag is True:
                    is_long_break = True
                    self.tray.skip_to_long_flag = False
                else:
                    # true when seconds_worked is a multiple of LONG_BREAK_FREQUENCY_SECONDS
                    is_long_break = (
                        seconds_worked % self.config.LONG_BREAK_FREQUENCY_SECONDS == 0
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
