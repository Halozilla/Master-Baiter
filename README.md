# Master-Baiter
Short discord bot that utilizes chat-gpt 4.1 mini api. The bot generates a unique insult based on a prompt that is associate with a person

  To begin create a new file (Can be called anything)
first line should be reserved for default facts that can be used for anyone, any other line should be formated as so 

default : {FACT_0, FACT_1}

PERSONS_DISCORD_USERNAME_GOES_HERE_1 : {PERSONAL_FACT_0, PERSONAL_FACT_1}

PERSONS_DISCORD_USERNAME_GOES_HERE_2 : {PERSONAL_FACT_0, PERSONAL_FACT_1}


PERSONS_DISCORD_USERNAME_GOES_HERE_3 : {PERSONAL_FACT_0, PERSONAL_FACT_1}

  As many facts can be added, but keep in mind to limit the length of each one to keep token usage to a minimum, I.E 2 - 5 words

  Personal facts can be enclosed in strings or not. Ensure the persons discord username is used and not their nickname

  Once this is done, inside of main.py insert your Chat-gpt api key into the "bot_msg" function, then insert your discord app client ID near the end of the file. Additonally insert your txt doc path into the get_facts funciton inside of on_message.

  Additionally there is a function that makes the bot reply with a nerd face emoji, just insert a discord username into it, then un-comment it, from then on the bot will automatically respond to that person with the nerd face.
