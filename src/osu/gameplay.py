"""

██████╗ ███████╗██╗
██╔══██╗██╔════╝██║
██████╔╝█████╗  ██║
██╔══██╗██╔══╝  ██║
██║  ██║███████╗██║
╚═╝  ╚═╝╚══════╝╚═╝
                   
Made with ❤️ By Ghoul
"""

from typing import Tuple, List, Dict

__all__: Tuple[str, ...] = (
    "Gameplay",
    "Hits",
    "Grade",
    "PP",
    "Leaderboard",
    "HP",
    "Combo",
    "Player",
)

class Gameplay:
    def __init__(self, data: Dict) -> None:
        self.gamemode: int = data.get("gameMode")
        self.name: str = data.get("name")
        self.score: int = data.get("score")
        self.accuracy: float = data.get("accuracy")
        self.combo: Combo = Combo(data.get("combo"))
        self.hp: HP = HP(data.get("hp"))
        self.hits: Hits = Hits(data.get("hits"))
        self.pp: PP = PP(data.get("pp"))
        self.leaderboard: Leaderboard = Leaderboard(data.get("leaderboard"))

class Hits:
    def __init__(self, data: Dict) -> None:
        self.map_300: int = data.get("300")
        self.map_200: int = data.get("200")
        self.geki: int = data.get("geki")
        self.map_100: int = data.gt("100")
        self.katu: int = data.get("katu")
        self.map_50: int = data.get("50")
        self.map_miss: int = data.get("0")
        self.slider_breaks: int = data.get("sliderBreaks")
        self.grade: Grade = data.get("grade")
        self.unstable_rate: float = data.get("unstableRate")
        self.hit_error_array: List = data.get("hitErrorArray")

class Grade:
    def __init__(self, data: Dict) -> None:
        self.current: str = data.get("current")
        self.max: str = data.get("maxThisPlay")

class PP:
    def __init__(self, data: Dict) -> None:
        self.current: int = data.get("current")
        self.fc: int = data.get("fc")
        self.max: int = data.get("maxThisPlay")

class Leaderboard:
    def __init__(self, data: Dict) -> None:
        self.has_leaderboard: bool = data.get("hasLeaderboard")
        self.player: Player = Player(data.get("ourplayer"))
        self.slots: List[Player] = [Player(player) for player in data.get("slots")]

class Player:
    def __init__(self, data: Dict) -> None:
        self.name: str = data.get("name")
        self.score: int = data.get("score")
        self.combo: int = data.get("combo")
        self.max_combo: int = data.get("maxCombo")
        self.mods: str = data.get("mods")
        self.hits_300: int = data.get("h300")
        self.hits_100: int = data.get("h100")
        self.hits_50: int = data.get("h50")
        self.hits_miss: int = data.get("h0")
        self.team: int = data.get("team")
        self.position: int = data.get("position")
        self.is_passing: int = data.get("isPassing")

class HP:
    def __init__(self, data: Dict) -> None:
        self.normal: float = data.get("normal")
        self.smooth: float = data.get("smooth")


class Combo:
    def __init__(self, data: Dict) -> None:
        self.current: int = data.get("current")
        self.max: int = data.get("max")
