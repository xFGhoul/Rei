"""

██████╗ ███████╗██╗
██╔══██╗██╔════╝██║
██████╔╝█████╗  ██║
██╔══██╗██╔══╝  ██║
██║  ██║███████╗██║
╚═╝  ╚═╝╚══════╝╚═╝
                   
Made with ❤️ By Ghoul
"""
import websockets

from typing import Tuple, Dict

from .menu import Menu
from .gameplay import Gameplay

class GoOsuMemoryData:
    def __init__(self, data: Dict) -> None:
        self.menu: Menu = Menu(data.get("menu"))
        self.gameplay: Gameplay = Gameplay(data.get("gameplay"))


class GoOsuMemory:
    def __init__(self) -> None:
        self.URL = "ws://localhost:24050/json"

    async def get_data(self) -> GoOsuMemoryData:
        async with websockets.connect(self.URL) as websocket:
            data = await websocket.recv()
            return GoOsuMemoryData(data)