from PIL import Image
import threading
import os

if "TRAVIS" not in os.environ:
    import pystray


class Tray:
    pause_flag = False
    skip_flag = False
    skip_to_long_flag = False
    stop_flag = False
    exit_flag = False
    tools = None

    def __init__(self) -> None:
        super().__init__()

        if "TRAVIS" not in os.environ:
            self.run()

    def pause(self, icon, item):
        self.pause_flag = True

    def resume(self, icon, item):
        self.pause_flag = False

    def skip(self, icon, item):
        self.skip_flag = True

    def skip_to_long(self, icon, item):
        self.skip_flag = True
        self.skip_to_long_flag = True

    def stop(self, icon, item):
        self.stop_flag = True

    def get_file_path(self, file):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, file)
        return file_path

    def run(self):
        # Load an image to use as the tray icon
        image = Image.open(self.get_file_path("icon.png"))

        # Create the tray icon menu
        menu = pystray.Menu(
            pystray.MenuItem("Pause", self.pause),
            pystray.MenuItem("Resume", self.resume),
            pystray.MenuItem("Skip", self.skip),
            pystray.MenuItem("Skip to long", self.skip_to_long),
            pystray.MenuItem("Stop", self.stop),
        )

        # Define a function to run in a separate thread
        def tray_thread():
            # Create the tray icon
            icon = pystray.Icon("Step Away!", image, menu=menu)

            # Run the tray icon in the background
            icon.run()

        # Create a new thread to run the tray icon
        t = threading.Thread(target=tray_thread)
        t.daemon = True
        t.start()
