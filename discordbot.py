# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzEwODExMzU4NzA2NTMyMzcy.Xr6vZg.AuRc5knOsa5UxntBa2OdphE_AYc'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「x」と発言したら「y」が返る処理
    if message.content == 'おはよう':
        await message.channel.send('今日も一日頑張ろう！')

    if message.content == 'おやすみ':
        await message.channel.send('ゆっくり休んでね')

    if message.content == 'ただいま':
        await message.channel.send('おかえり')

    if message.content == '疲れた':
        await message.channel.send('疲れた時は休もうね')

    if message.content == '大好き':
        await message.channel.send('ありがとう')

    if message.content == 'いってきます':
        await message.channel.send('いってらっしゃい')

    if message.content == '行ってきます':
        await message.channel.send('いってらっしゃい')

    if message.content == '眠い':
        await message.channel.send('はよ寝ろ')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
