[![Discord server](https://discord.com/api/guilds/843994109366501376/embed.png)](https://discord.gg/DFDUpXJNdc)
[![Discord.py](https://img.shields.io/badge/Discord.py-2.0-blue)](https://github.com/Rapptz/discord.py)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.python.org/pypi/discord.py)

# discord.py-paginator
Buttons pagination template for discord bots.

# Example
```py
import discord
from paginator import Paginator


@discord.app_commands.command()
async def command_name(interaction: discord.Interaction):
    data = {...}
    pages = []
    page_content = ""

    for i, (key, value) in enumerate(data.items()):
        if (i > 0) and (i + 1 % 5 == 0):
            pages.append(page_content)

            page_content += f"{i+1}. {key.capitalize()} `{value}`\n")

    await Paginator(interaction, pages).start()
```

# Preview
![layout-preview](images/layout.jpg)
![quick-navigation-preview](images/quick-navigation.jpg)
![custom-children-preview](images/custom_children.jpg)

### :scroll: [LICENSE](LICENSE)
