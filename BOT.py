import os
import random
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from typing import Literal, Union
import pathlib
from discord.utils import get_or_create

required_role = "@lcc.buyers"

class Vector2:
    def __init__(self, x: float = None, y: float = None):
        self.x = x
        self.y = y

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

def get_line(value: int) -> Vector2:
    return Vector2(7.015 + -0.01276 * value, 7.1415 + -0.014512 * value)

def random_8_char_string() -> str:
    return "".join(random.choices("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjkklzxcvbnm12345890098765432", k=8))

bot = commands.Bot(command_prefix="__disabled__", intents=discord.Intents.all())
bot.remove_command("help")

