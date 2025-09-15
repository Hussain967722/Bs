# Copyright: 2021 LIRIK SPENCER

"""
Importation of all public required methods and classes
You can directly use these like 
>>> from methods import *
"""

from core.handle import (
    inventory,
    display_stats,
    find_tickets,
    convert,
    handle_msg,
    command_help,
    get_user_from_rank,
)
from core.internal import (
    bot,
    master,
    absue_filter,
    get_player,
    get_brain_path,
    load_bot_brain,
    locale,
    split_list,
    chat_log,
    get_data_folder_path,
    current_time,
    list_files,
    get_parent_path,
    get_file,
    save_file,
)
from core.register import register_commands, register_perks, register_powerups

# system.chat
from system.chat.manager import chat_functions
from system.chat.penalty import Punishment
from system.chat.spam import check_spam

# system.commands
from system.commands.engine import ChatCommandsEngine

# Tools
# NOTE: You can use this API for storing and accessing files and data on internet
from tools.api import LirikApi, generate_token
from tools.objects import (
    Prefix,
    Airstrike,
    AutoAim,
    CompanionCube,
    Portals,
    TreatmentArea,
)

# Errors
from errors import (
    FewArgumentsError,
    DataTypeError,
    ManyArgumentsError,
    NonImplementedError,
    MustBeIntegerError,
    RoleNameError,
    ConfigClassError,
    ArgumentDoesntMatchError,
)
