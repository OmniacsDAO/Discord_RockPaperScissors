# Discord_RockPaperScissors

This is a simple Discord bot that allows users to play Rock Paper Scissors in a Discord server. The bot is built using Python and the `discord.py` library.

## Features

- Allows users to play Rock Paper Scissors by typing commands in a Discord server.
- Supports multiple players.
- Easy to deploy with environment variables for token management.
- Customizable with different channels for production and test environments.

## Prerequisites

To run this bot, you'll need:

- Python 3.8 or higher
- A Discord account
- A Discord bot token (from the [Discord Developer Portal](https://discord.com/developers/applications))
- The following Python libraries:
  - `discord.py`
  - `python-dotenv`
  - `asyncio`

You can install the necessary dependencies using pip:

```bash
pip install discord.py python-dotenv asyncio
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/OmniacsDAO/Discord_RockPaperScissors
   cd Discord_RockPaperScissors
   ```

2. Create a `.env` file in the root directory of the project with the following content:

   ```
   DISCORD_TOKEN=your_discord_token
   DISCORD_TOKEN_TEST=your_test_discord_token
   ```

   Replace `your_discord_token` with the bot token for your production bot and `your_test_discord_token` with the token for your test bot.

3. Run the bot:

   ```bash
   python main.py
   ```

## Commands

- `/rps`: Starts a Rock Paper Scissors game. The bot will ask users to choose between rock, paper, or scissors.

## Environment Variables

- `DISCORD_TOKEN`: The token for your production bot.
- `DISCORD_TOKEN_TEST`: The token for your test bot.
- `channel_id`: You can specify different channel IDs for production and testing.

## How to Play

1. Type `/rps` in a text channel where the bot is active.
2. The bot will respond, prompting you to choose between rock, paper, or scissors.
3. The bot will randomly choose its move and declare the winner.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Make sure to follow the coding guidelines.

---
