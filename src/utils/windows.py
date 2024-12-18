"""

██████╗ ███████╗██╗
██╔══██╗██╔════╝██║
██████╔╝█████╗  ██║
██╔══██╗██╔══╝  ██║
██║  ██║███████╗██║
╚═╝  ╚═╝╚══════╝╚═╝
                   
Made with ❤️ By Ghoul
"""

import win32gui
import win32con

class Window:
    def __init__(self) -> None:
        self.window = None
        
    def _hide_window(self) -> None:
        window = win32gui.GetForegroundWindow()
        title  = win32gui.GetWindowText(window)
        if title.endswith("ghoul"):
            self.window = window #save the window you are hiding
            win32gui.ShowWindow(window, win32con.SW_HIDE)

        def _show_window(self) -> None:
            window = self.window or win32gui.GetForegroundWindow()
            win32gui.ShowWindow(window, win32con.SW_SHOW)