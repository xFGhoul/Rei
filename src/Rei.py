"""

██████╗ ███████╗██╗
██╔══██╗██╔════╝██║
██████╔╝█████╗  ██║
██╔══██╗██╔══╝  ██║
██║  ██║███████╗██║
╚═╝  ╚═╝╚══════╝╚═╝
				   
Made with ❤️ By Ghoul
"""

import sys
import os

import asyncio
import humanize
import psutil
import datetime
import platform

from threading import Thread
from rich.console import Console

from utils.constants  import Constants
from utils.logging import Logger

from osu.goosumemory import GoOsuMemory

from gui.gui import App

class Rei:
	def __init__(self) -> None: 
		self.console = Console()
		self.logger = Logger()
		self.osu = GoOsuMemory()

	async def run(self) -> None:
		# -- Check For Windows Platform
		if sys.platform != "win32":
			os._exit(1)

		self.console.print(f"""[blue3]
______     _ 
| ___ \   (_)
| |_/ /___ _ 
|    // _ \ |
| |\ \  __/ |
\_| \_\___|_|
			 
			 
Rei: {Constants.VERSION}
Dev: heartghoul""")
		
		self.console.print("[blue3]Welcome To Rei, Going Through Setup Process...[/blue3]")
		self.logger.info("Rei Starting")
		self.logger.info(f"Version: {Constants.VERSION}")
		self.logger.info(f"Current Path: {os.path.abspath(os.curdir)}")
		self.logger.info(
			f"Operating System: {platform.uname().system} {platform.uname().release} {platform.win32_edition()} ({platform.architecture(sys.executable)[0]})"
		)

		bt = datetime.datetime.fromtimestamp(psutil.boot_time())
		self.logger.info(
			f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
			)
		self.logger.info(f"Python: {platform.python_version()}")

		vmem = psutil.virtual_memory()

		self.logger.info(f"Total Memory: {humanize.naturalsize(vmem.total)}")
		self.logger.info(
			f"Memory Availability: {humanize.naturalsize(vmem.available)}"
			)
		self.logger.info(f"Memory Percentage: {vmem.percent}%")

		self.console.print("[blue3]Setting Up Configuration... [/blue3]")
		# set up config
		self.console.print("[blue3]Config Set Up![/blue3]")


		self.console.print("[blue3]Checking if osu! is running[/blue3]")
		# check if osu is running
		self.console.print("[blue3]osu! is running! [/blue3]")

		self.console.print("[blue3]Checking if goosumemory is running... [/blue3]")
		# check if go osu memory is running
		self.console.print("[blue3]go osu memory is running![/blue3]")

		# run gui
		self.console.print("[blue3]Running GUI! [/blue3]")

		data = await self.osu.get_data()

		app = App(data)
		app.mainloop()

		#self.console.print(f"[blue3] PP 100: {data.menu.beatmap.pp.pp_100}")



if __name__ == "__main__":
	rei = Rei()
	asyncio.run(rei.run())

