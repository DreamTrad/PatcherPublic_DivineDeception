"""
File        : tool.py
Author      : Silous
Created on  : 2025-10-08
Description : call tool to repack the game.
"""

# == Imports ==================================================================

from logging import Logger

# -------------------- Import Lib User -------------------
from patcher import config
from patcher.utils import steam
from patcher.utils.logger import get_logger

# == Global Variables =========================================================

_logger: Logger = get_logger(__name__)


# == Functions ================================================================


def repack() -> None:
    """whole patching process."""
    steam.copy_data_in_steam_game_folder(str(config.GAME_FOLDER), config.PATCH_FOLDER)
