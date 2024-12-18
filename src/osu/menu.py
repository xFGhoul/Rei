"""

██████╗ ███████╗██╗
██╔══██╗██╔════╝██║
██████╔╝█████╗  ██║
██╔══██╗██╔══╝  ██║
██║  ██║███████╗██║
╚═╝  ╚═╝╚══════╝╚═╝
                   
Made with ❤️ By Ghoul
"""

from typing import Tuple, Dict

from .beatmap import Beatmap

__all__: Tuple[str, ...] = (
    "Menu"
)

class Menu:
    def __init__(self, data: Dict) -> None:
        self.state: int = data.get("state")
        self.skin_folder: str = data.get("skin_folder")
        self.game_mode: int = data.get("gameMode")
        self.is_chat_enabled: int = data.get("isChatEnabled")
        self.beatmap: Beatmap = Beatmap(data.get("bm"))