import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

allowed_channels = [
    1467175336428175442
]

banned_words = [
    "hi", "hello", "你好", "早安", "晚安", "謝謝", "thanks", "ok",
    "哈哈", "lol", "?", "!", "笑死",
    "我", "你", "他", "是", "的", "在",
    "roblox", "審核", "封號", "ban"
]

appeal_words = [
    "申訴", "appeal", "為什麼", "why", "解封"
]

ban_reasons = [
    "使用不當語言",
    "嘗試進行正常社交",
    "訊息內容不符合社群標準",
    "疑似繞過審核系統",
    "違反未公開的規則"
]

appeal_responses = [
    "我們已收到你的申訴。\n\n目前案件正在審核中。\n請勿重複提交申訴。",
    "Your appeal has been received.\n\nStatus: Under Review\nEstimated completion time: N/A",
    "申訴案件仍在處理中。\n\n重複查詢可能導致處理時間延長。",
    "你的申訴已進入下一階段審核。\n\n請耐心等待。",
    "經系統重新檢視後，\n原審核結果維持不變。\n\n此為最終決定。"
]

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Moderating accounts 24/7"))
    print("ROBLOX 審核員系統已啟動")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id not in allowed_channels:
        return

    content = message.content.lower()

    for word in appeal_words:
        if word in content:
            await message.channel.send(random.choice(appeal_responses))
            return

    for word in banned_words:
        if word in content:
            await message.channel.send(
                "⚠️你已違反規範你被封禁了⚠️\n原因：" + random.choice(ban_reasons)
            )
            return

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))


