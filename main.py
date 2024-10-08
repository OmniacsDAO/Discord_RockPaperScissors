## Load Libraries
import os
# sudo timedatectl set-timezone America/Chicago
prod = True
if prod:
    os.chdir('/root/discord/RockPaperScissors')
else:
    os.chdir('/root/discord/test')
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
import random
import asyncio

########################################################
## Bot config
########################################################
load_dotenv()
if prod:
    TOKEN = os.getenv('DISCORD_TOKEN')
    channel_id = 869626561282867230
else:
    TOKEN = os.getenv('DISCORD_TOKEN_TEST')
    channel_id = 832466499590815785

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)
########################################################
########################################################


########################################################
## Puzzle Functions and Start Bot
########################################################
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

########################################################
########################################################



########################################################
## Parse Every Message and act Accordingly 
########################################################

# Dictionary to track ongoing games per user
active_games = {}

@bot.command(name="rps", help="Play rock, paper, scissors with the bot using '/rps'")
async def rps(ctx):
    # Define choices and corresponding emojis
    rps_game = ["rock", "paper", "scissors"]
    abbreviations = {"r": "rock", "p": "paper", "s": "scissors"}
    emoji_map = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

    # Check if the user is already in an active game
    if ctx.author.id in active_games:
        await ctx.send("You are already in an ongoing game! Finish it first.")
        return

    await ctx.send("Rock 🪨, Paper 📄, or Scissors ✂️ (You can also use 'r', 'p', or 's')")

    # Check function to ensure the response is valid
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rps_game + list(abbreviations.keys())

    # Register the game state for the user
    active_games[ctx.author.id] = True

    # Wait for the user's response
    try:
        user_msg = await bot.wait_for("message", check=check, timeout=30)  # Wait for 30 seconds for a response
    except asyncio.TimeoutError:
        await ctx.send("⏰ You took too long to respond! Please try again.")
        active_games.pop(ctx.author.id)  # Remove the user from active games
        return

    # Normalize user input to full names
    user_choice_input = user_msg.content.lower()
    user_choice = abbreviations.get(user_choice_input, user_choice_input)

    bot_choice = random.choice(rps_game)

    # Define comments for different outcomes with emojis
    tie_comments = [
        "Well, that was awkward... We tied! 🤔",
        "Great minds think alike... Or maybe we're both just lucky? 😅",
        "A tie! Guess we're evenly matched! 😎",
        "It's a stalemate! Let's go again! 🌀",
        "We tied! Did we just become best friends? 😆",
        "Looks like we're on the same wavelength! ⚡️",
        "A tie? Now that's what I call balance! 🧘‍♂️",
        "Even Steven! Guess we both brought our A-game! 💪",
        "A tie? We're in perfect sync! 🎶",
        "Both winners today! Time for round two? 🚀",
        "Deadlock! It's like we're two sides of the same coin! 🪙",
        "A tie? Well, great minds do think alike! 💡",
        "No winners, no losers—just awesome players! 🎮",
        "It's a draw! Shall we call it a truce or rematch? 🏆",
        "A tie? That's what happens when legends collide! ⚔️",
        "A tie? Looks like we're equally unpredictable! 🎲",
        "No one wins, no one loses—just pure fun! 😄",
        "Stalemate! Let's break the tie next round! 🔥",
        "A tie? We're like two peas in a pod! 🌱",
        "Well played! Shall we settle this with another round? 🎯",
        "A draw? I guess we're both on fire! 🔥",
        "Equal footing! This match just got more exciting! 🏅",
        "It’s a tie! Seems like destiny brought us here! ✨",
        "Both unbeatable this time! Ready for a rematch? ♻️",
        "We tied again! It's like we're thinking in harmony! 🎵",
        "A draw? Looks like neither of us is backing down! 🛡️",
        "Even ground! This just means we’re both awesome! 😎",
        "Perfect balance! Let's see who tips the scale next! ⚖️",
        "A tie? Let's see if the next round changes things! 🌪",
        "We're tied! It's like we're reading each other's minds! 🧠"
    ]

    user_win_comments = [
        "No way! You actually beat me! 😱",
        "Lucky shot, human... Don't get used to it! 😤",
        "Alright, alright... You win this round! 😒",
        "You got me this time! Beginner's luck? 😉",
        "Impressive! But I'm just warming up! 🔥",
        "Well played! But don't let it go to your head! 😏",
        "Enjoy your victory, it won’t happen again! 😎",
        "Congrats! But next time, I won't go easy on you! 💪",
        "You got lucky this time... I'll be back stronger! 🤨",
        "Nice one! But this is far from over! 💥",
        "Victory is yours... for now. 👀",
        "You’ve got skills! But I’m just getting started! 👊",
        "Not bad! I'll give you this win, but watch your back! 😏",
        "Consider this your one freebie! Next time, it’s game on! 💥",
        "Alright, I'll let you have this one... enjoy it while it lasts! 😜",
        "You're getting better, but I've still got a few tricks up my sleeve! 😼",  
        "Alright, alright, but don't think this changes anything! 😤",  
        "Beginner's luck strikes again, I'll be back! 💥",  
        "Okay, you win, but next time, it's serious! 💪",  
        "I'll let you have this one, but don't get too comfortable! 😎",  
        "You've won this round, but I'm not out yet! 👊",  
        "Don't get cocky, this is just the beginning! 😉",  
        "You may have won, but I'm just warming up! 🔥",  
        "Well done, but I'm coming for you in the next round! 👀",  
        "You win, but I'll be back with a vengeance! 💢",  
        "Congrats, but I hope you're ready for round two! 🌀",  
        "I'll give you this one, but don't let it go to your head! 😏",  
        "Alright, you got me, but it's far from over! 💥",  
        "Enjoy the victory while it lasts, because I'll be coming back stronger! 🔄",  
        "Well played, but I'm not done yet! 🧠"
    ]

    bot_win_comments = [
        "Haha! I win! Better luck next time! 😜",
        "Did you really think you could beat me? 🤖",
        "Nice try, but the bot always wins! 🏆",
        "Easy win for me! Ready for a rematch? 😏",
        "You fought bravely, but I prevailed! 💪",
        "Haha! You couldn't defeat me this time! 😎",
        "Nice effort, but the bot always comes out on top! 💥",
        "Close, but I'm still undefeated! 🏅",
        "You tried your best, but I still won! 🎯",
        "Better luck next time, human! The bot rules! 🤖",
        "You’ve met your match again! Ready for a rematch? 😏",
        "Almost had me, but not quite! 😉",
        "Nice try, but victory is mine again! 🔥",
        "You gave it a good shot, but the bot prevails! 🦾",
        "Defeated! Want to give it another go? 😜",
        "Not this time! The bot reigns supreme! 🎮",
        "Outsmarted again! Better luck next time! 😎",
        "Looks like I’m unbeatable! Ready for another round? 😜",
        "Close call, but I still emerged victorious! 🏆",
        "Nice try, but the crown stays with me! 👑",
        "You put up a fight, but I’m still standing! 🥇",
        "Too quick for you this time! Want to go again? 😏",
        "That was fun, but I’m still the champion! 🎯",
        "You can’t outplay me just yet! 👾",
        "Ooh, that was close! But I remain undefeated! 💪",
        "Almost had me there, but not quite! 🔥",
        "Looks like my winning streak is still intact! 😜",
        "You’re improving, but I’m still on top! 🏅",
        "Another victory for me! Try again? 😎",
        "Whoops, not this round! Better luck next time! 🚀",
        "Nice effort, but the bot keeps winning! 💥",
        "The game’s tough, but I’m tougher! Rematch? 💪",
        "That was intense, but I pulled through! 😏",
        "Once again, I’ve claimed victory! 😄",
        "Back to the drawing board, human! The bot triumphs! 🤖"
    ]

    # Determine the outcome and select a random comment
    if user_choice == bot_choice:
        result = "It's a tie!"
        comment = random.choice(tie_comments)
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "scissors" and bot_choice == "paper") or \
         (user_choice == "paper" and bot_choice == "rock"):
        result = "You win!"
        comment = random.choice(user_win_comments)
    else:
        result = "I win!"
        comment = random.choice(bot_win_comments)

    # Send the results with emojis and a funny comment
    await ctx.send(f"Your choice: {user_choice} {emoji_map[user_choice]}\n"
                   f"My choice: {bot_choice} {emoji_map[bot_choice]}\n"
                   f"{result} {comment}")

    # Remove the user from active games after completion
    active_games.pop(ctx.author.id, None)

########################################################
########################################################


# Start the bot asynchronously
async def start_bot():
    await bot.start(TOKEN)

asyncio.run(start_bot())