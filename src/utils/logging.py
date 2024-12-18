from loguru import logger
from typing import Dict, TYPE_CHECKING
from pathlib import Path

if TYPE_CHECKING:
    from loguru import Logger

class Logger:
    def __init__(self) -> None:
        self.path: Path = (
            Path.home() / "AppData/Roaming/Rei/logs/Rei.log"
        )
        self.config: Dict = {
                "handlers": [
                    {
                        "sink": self.path,
                        "format": "[{time:YYYY-MM-DD HH:mm:ss}] {module}::{function}({line}) - {message}",
                        "enqueue": True,
                        "rotation": "daily",
                        "mode": "w",
                        "level": "INFO",
                        "serialize": False,
                        "backtrace": False,
                        "catch": False,
                    },
                ],
            }
        self.logger: Logger = logger # tbh this could be exported as a variable but i like OOP :p
        self.logger.configure(**self.config)

    def info(self, text: str) -> None:
        self.logger.info(text)