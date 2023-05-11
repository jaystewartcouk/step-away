import argparse
from dotenv import load_dotenv
import os


class Config:
    DELAY = 0
    SHORT_BREAK_FREQUENCY_MINUTES = 10
    SHORT_BREAK_LENGTH_SECONDS = 5
    LONG_BREAK_FREQUENCY_MINUTES = 30
    LONG_BREAK_LENGTH_MINUTES = 5

    def __init__(self) -> None:
        parser = argparse.ArgumentParser()

        parser.add_argument(
            "--short_break_frequency_minutes",
            help="(Needs to go evenly into long_break_frequency_minutes)",
        )
        parser.add_argument("--short_break_length_seconds")
        parser.add_argument(
            "--long_break_frequency_minutes",
            help="(Needs to be a multiple of short_break_frequency_minutes)",
        )
        parser.add_argument("--long_break_length_minutes")
        parser.add_argument("--delay")

        args = parser.parse_args()

        if args.delay:
            self.DELAY = int(args.delay) * 60

        load_dotenv()

        self.SHORT_BREAK_FREQUENCY_MINUTES = (
            int(args.short_break_frequency_minutes)
            if args.short_break_frequency_minutes
            else int(os.environ.get("SHORT_BREAK_FREQUENCY_MINUTES"))
        )

        self.SHORT_BREAK_LENGTH_SECONDS = (
            int(args.short_break_length_seconds)
            if args.short_break_length_seconds
            else int(os.environ.get("SHORT_BREAK_LENGTH_SECONDS"))
        )

        self.LONG_BREAK_FREQUENCY_MINUTES = (
            int(args.long_break_frequency_minutes)
            if args.long_break_frequency_minutes
            else int(os.environ.get("LONG_BREAK_FREQUENCY_MINUTES"))
        )

        self.LONG_BREAK_LENGTH_MINUTES = (
            int(args.long_break_length_minutes)
            if args.long_break_length_minutes
            else int(os.environ.get("LONG_BREAK_LENGTH_MINUTES"))
        )

        self.WORK_DURATION = self.SHORT_BREAK_FREQUENCY_MINUTES * 60
        self.LONG_BREAK_LENGTH_SECONDS = self.LONG_BREAK_LENGTH_MINUTES * 60
        self.LONG_BREAK_FREQUENCY_SECONDS = self.LONG_BREAK_FREQUENCY_MINUTES * 60

        if self.LONG_BREAK_LENGTH_MINUTES % self.SHORT_BREAK_FREQUENCY_MINUTES != 0:
            print(
                "LONG_BREAK_LENGTH_MINUTES should be a multiple of SHORT_BREAK_FREQUENCY_MINUTES"
            )
