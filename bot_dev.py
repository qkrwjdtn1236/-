import random
import discord
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='!!')
bot.remove_command('help')
'''
@bot.command()
async def t(ctx, *,type):
    if type == None:
        await ctx.send('사용법 :  !test 메세지')
    else:
        await ctx.send(type)
'''
game_act = cycle(['정상 작동중 ||도움말은 !!help','개발용 봇','교육용','개발자, 베타테스트 제외한 모든사람은 사용자제'])


@bot.event
async def on_ready():
    change_status.start()
    print('봇 준비 완료')

@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(game_act)))

@bot.command()
async def ping(ctx):
    await ctx.send(f'ping {round(bot.latency*1000)}ms')

@bot.command()
async def text(ctx, *,input):
    random_text = [
        '잘생겼어',
        '못생겼어',
        '맛있는거',
        '맛없는거',
        '동물',
        '사람',
        'True',
        'False',
        'maybe',
    ]
    await ctx.send(f'{random.choice(random_text)}')

@bot.command()
async def 선택(ctx,*,input):
    result = random.choice(input.split(','))
    await ctx.send(f'선택 : {result}')

@bot.command()
async def 주사위(ctx):
    emoji = discord.utils.get(guild.emojis,name='2ero')
    await ctx.send(random.randint(1,6))
    await send.add_reaction(emoji)

'''
@bot.command()
async def dm(ctx,*,msg):
    await user.send(f'{msg}')
'''

@bot.command()
async def 다운로드(ctx, *,type):
    file = [
        discord.File('최적화 프로그램\Scripts.zip'),
        discord.File('image\profile.png')
    ]
    file_type = ['최적화 스크립트','프로필 사진']
    if ctx == '!다운로드':
        embed = discord.Embed(title = '해당 명령어 사용법',description = '!다운로드 [종목]',colour = discord.Colour.blue())
        embed.set_footer(text = '봇 사용하기에 어려우시면 It is not define#4141 에게 DM해주세요!')
        embed.set_field(name = f'[종목]안에 사용할 수 있는 것은{file_type}이 있습니다.')


    if type == '최적화 스크립트':
        await ctx.send(files=file)

@bot.command()
async def 도움말(ctx):
    author = ctx.message.author
    file = 'https://imgur.com/KfuVT7r.png'
    embed = discord.Embed(title = '명령어 사용법',
    description = '개발하는 봇이다보니 정확하지 않을수 있습니다. \n또한 명령어가 추가될수 있고 변동될 수 있습니다.'
    ,colour = discord.Colour.blue())

    embed.set_author(name = '쉬팔봇',icon_url = file)
    embed.set_image(url = file)
    embed.set_thumbnail(url = file)
    embed.set_footer(text = '봇 사용하기에 어려우시면 It is not define#4141 에게 DM해주세요!')
    embed.add_field(name = '!help',value = '봇 명령어 설명서를 출력합니다.',inline = False)
    embed.add_field(name = '!ping',value = '명령어치고 연산한후에 출력하는 시간을 ms단위로 출력합니다.',inline = False)
    embed.add_field(name = '!text [메세지]',value = '[메세지]를 아무나 입력하고 입력할경우 렌덤으로 메세지 출력합니다.',inline = False)
    embed.add_field(name = '!선택 [내용]',value = '[내용]을 구분할경우 ","단위로 하여 여러개 내용중 하나만 선택하여 출력합니다.',inline = False)
    embed.add_field(name = '!주사위(지금 사용불가)',value = '1~6까지 숫자중 렌덤으로 숫자 1개만 출력합니다.',inline = False)
    embed.add_field(name = '!다운로드 [타입]',value = '타입에 알맞은 파일을 업로드하여 출력합니다.\n종류는 !다운로드만 칠경우 더상세히 출력합니다.',inline = False)

    await ctx.send(embed = embed)
bot.run('NjcxMjIyMjQ0MDM4NjcyMzk0.Xi5yzA.i47w5SgUq-ClgMdTP8WuXutsSy0')