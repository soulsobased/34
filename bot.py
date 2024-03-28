import discord
from discord.ext import commands, app_commands
import json
import os
import requests
from typing import Dict, List, Literal, Optional, Union

# Constants
EMBED_COLOR = discord.Color.blue()
ADMIN_ROLE = "@ ++"
ERROR_EMBED = discord.Embed(title="Error", description="Try again later.", color=0xa61c1c)

