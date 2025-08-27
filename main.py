import random
import discord
from openai import OpenAI

#------------------------------------------------------------
# get_facts
#------------------------------------------------------------
def get_facts(str_file_name, username):
    if not str_file_name:
        return None

    with open(str_file_name, "r") as file:
        for line in file:
            if username == get_username(line):
                return get_user_facts(line)

    # fallback to first line
    with open(str_file_name, "r") as file:
        return get_user_facts(file.readline())

#------------------------------------------------------------
# get_username
#------------------------------------------------------------
def get_username(line):
    if ':' not in line:
        return None
    return line.split(':')[0].strip()

#------------------------------------------------------------
# get_user_facts
#------------------------------------------------------------
def get_user_facts(line: str):
    if ':' not in line:
        return []
    output = line.split(':', 1)[1].strip()
    output = output.replace('{', "").replace('}', "")
    return [fact.strip() for fact in output.split(',') if fact.strip()]

def rand_fact(fact):
    return random.choice(fact)


def msg_chance():
    return random.randint(1, 3) == 1# 33% chance for bot to msg, change second number to increase or decrease

#------------------------------------------------------------
# Discord Client
#------------------------------------------------------------
class Client(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.openai = OpenAI(api_key=("INSERT YOUR API KEY HERE"))

    async def bot_msg(self, message, author_facts):
        fact = random.choice(author_facts) if author_facts else "nothing"
        print(fact)
        prompt = f'One-sentence insult only (based on fact: "{fact}"). Output nothing else.'

        response = self.openai.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        await message.reply(response.output_text)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.author.name == 'INSERT USERNAME HERE':
            await message.add_reaction('🤓')
            await message.reply(f'{message.author.mention} 🤓')
        if msg_chance():
            facts = get_facts(INSERT YOUR FILE PATH HERE, message.author.name)
            await self.bot_msg(message, facts)

#------------------------------------------------------------
# Run Bot
#------------------------------------------------------------
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

client = Client(intents=intents)
client.run("INSERT APP ID HERE")
