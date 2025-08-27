# Master-Baiter
Short discord bot that utilizes chat-gpt 4.1 mini api. The bot generates a unique insult based on a prompt that is associate with a person

To begin create a new file (Can be called anything)
first line should be reserved for default facts that can be used for anyone, example : "Dumb as rocks"

any other line should be formated as so 
PERSONS_DISCORD_USERNAME_GOES_HERE : {PERSONAL_FACT_0, PERSONAL_FACT_1}

personal facts can be enclosed in strings or not, it does not matter. Ensure the persons discord username is used and not their nickname

once this is done inside of main.py insert your Chat-gpt api key into the "bot_msg" function, then insert your discord app client ID near the end of the file

additionally there is a function that makes the bot reply with a nerd face emoji, just insert a discord username into it, then un-comment it, from then on the bot will automatically respond to that person with the nerd face.
