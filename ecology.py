import discord
from discord.ext import commands
import os
from random import choice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

facts = ['Примерно 1 миллион видов животных и растений находятся под угрозой исчезновения из-за изменения климата и разрушения их природного местообитания. Это вызывает нарушения в экосистемах и может иметь серьезные последствия для биоразнообразия и благосостояния планеты.',\
         'Некоторые древесные растения способны обмениваться химическими сигналами, называемыми фитоволятилями. Когда одно растение атакуют вредители, оно может испускать фитоволятили в воздух, что предупреждает соседние растения о опасности. В ответ на это, соседние растения могут изменить свою химическую составляющую, чтобы стать менее привлекательными для вредителей или привлечь хищников, которые будут защищать их от нападений. Это явление известно как растительное общение и представляет собой удивительный пример взаимодействия растений и их способности к сотрудничеству в экосистеме.',\
            'Как ясно из археологических исследований, человеческое влияние на окружающую среду и экологию существует уже очень давно. Например, в древнем Риме акведуки служили не только для транспортировки воды, но и для обеспечения резервуаров и фонтанов для охлаждения домов в жаркие летние месяцы. Таким образом, римляне создавали микроклимат, что можно считать одним из первых примеров экосистемного подхода к жилищным потребностям.',\
                'Известно, что океаны занимают около 70% поверхности Земли, однако лишь около 5% океанского дна было исследовано и изучено. Это означает, что большая часть океанов остается неизведанной экосистемой, в которой могут существовать множество неизвестных видов и процессов. Таким образом, исследования океанов и их охрана являются важными задачами в области экологии.',\
                    'Примерно 1 миллион видов животных и растений находятся под угрозой исчезновения из-за изменения климата и разрушения их природного местообитания. Это вызывает нарушения в экосистемах и может иметь серьезные последствия для биоразнообразия и благосостояния планеты.']

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен')

@bot.command()
async def help(ctx):
    await ctx.send("!eco - факт об экологии\n!whatis [предмет] - что можно сделать из переработанного предмета, пока не доступно")

@bot.command()
async def eco(ctx):
    await ctx.send(choice(facts))
