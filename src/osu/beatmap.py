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
    "Beatmap",
    "Metadata",
    "PP",
    "Stats",
    "Mods",
    "Path",
    "Time",
    "BPM"
)

class Beatmap:
    def __init__(self, data: Dict) -> None:
        self.time: Time = Time(data.get("time"))
        self.beatmap_id: int = data.get("id")
        self.set: int = data.get("set")
        self.md5: str = data.get("md5")
        self.rankedStatus: int = data.get("rankedStatus")
        self.metadata: Metadata = Metadata(data.get("metadata"))
        self.stats: Stats = Stats(data.get("stats"))
        self.path: Path = Path(data.get("path"))
        self.mods: Mods = Mods(data.get("mods"))
        self.pp: PP = PP(data.get("pp"))


class Metadata:
    def __init__(self, data: Dict) -> None:
        self.artist: str = data.get("artist")
        self.title: str = data.get("title")
        self.mapper: str = data.get("mapper")
        self.difficulty: str = data.get("difficulty")

class PP:
    def __init__(self, data: Dict) -> None:
        self.pp_100: int = data.get("100")
        self.pp_99: int = data.get("99")
        self.pp_98: int = data.get("98")
        self.pp_97: int = data.get("97")
        self.pp_96: int = data.get("96")
        self.pp_95: int = data.get("95")
        self.strains: List = data.get("strains")
    
class Stats:
    def __init__(self, data: Dict) -> None:
        self.ar: int = data.get("AR")
        self.cs: float = data.get("CS")
        self.od: int = data.get("OD")
        self.hp: float = data.get("HP")
        self.sr: float = data.get("SR")
        self.bpm: BPM = data.get("BPM")
        self.full_sr: float = data.get("fullSR")
        self.memory_ar: float = data.get("memoryAR")
        self.memory_cs: float = data.get("memoryCS")
        self.memory_od: int = data.get("memoryOD")
        self.memory_hp: int = data.get("memoryHP")

class Mods:
    def __init__(self, data: Dict) -> None:
        self.num: int = data.get("num")
        self.str: str = data.get("str")


class Path:
    def __init__(self, data: Dict) -> None:
        self.full: str = data.get("full")
        self.folder: str = data.get("folder")
        self.file: str = data.get("file")
        self.bg: str = data.get("bg")
        self.audio: str = data.get("audio")
    
class BPM:
    def __init__(self, data: Dict) -> None:
        self.min: int = data.get("min")
        self.max: int = data.get("max")


class Time:
    def __init__(self, data: Dict) -> None:
        self.first_object = data.get("firstObj")
        self.current = data.get("current")
        self.mp3 = data.get("mp3")