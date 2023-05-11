import logging
from config import Config
import subprocess


class Base:
    config = None
    tools = None
    log = None
    tray = None

    def __init__(self) -> None:
        self.log = logging
        self.log.basicConfig(
            level=self.log.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.log.info("Welcome to Step Away!")
        self.config = Config()

    def pause_players(self):
        # True players only: vlc, mpv, RhythmBox, web browsers, cmus, mpd, spotify..
        subprocess.call(["playerctl", "pause"])
