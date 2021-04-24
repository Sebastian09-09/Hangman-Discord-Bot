#Error: The Following Error occured: list index out of range   
#the bot shows this error it PyDictionary isnt able to find definatins for the word

import discord 
from discord.ext import commands
from discord import Embed 
import asyncio
import os
import random 
from random_word import RandomWords
from PyDictionary import PyDictionary
dictionary=PyDictionary()  
rw = RandomWords() 

client = commands.Bot(command_prefix=["^",",","e","E"]) 
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name="Hangman", type=discord.ActivityType.playing))
    print("Ready to play Hangman!") 

#HANGMAN 
hangman_ = [] 
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs 

async def correct_embed(ctx , x , msg , index , wrong):  
    if index == 0:
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│                                                         
│                                                                                     
│                                                                   
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)
    if index == 1: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│                                                                                     
│                                                                   
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)
    
    if index == 2: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│                                                                   
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)

    if index == 3: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│         │                                                          
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)

    if index == 4: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│         │\                                                          
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)
    
    if index == 5: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│        /│\                                                          
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)

    if index == 6: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│        /│\                                                          
│          \                                                                       
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)

async def wrong_embed(ctx , x , msg , index , wrong , word):  
    if index == 1: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│                                                                                     
│                                                                   
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)
    
    if index == 2: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│                                                                   
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)

    if index == 3: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│         │                                                          
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)

    if index == 4: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│         │\                                                          
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)
    
    if index == 5: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│        /│\                                                          
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)

    if index == 6: 
        em = Embed(title = f"`{x}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│         │                                                
│         O                                                                            
│        /│\                                                          
│          \                                                                       
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Wrong Guesses - {wrong}") 
        await ctx.send(embed = em)
    
    if index == 7: 
        em = Embed(title = f"`{x}`" , description =f"""```
___________________ 𝐻𝒶𝓃𝑔{ctx.author.name}  
│         │                                                
│         O                                                                            
│        /│\                                                          
│        / \                                                                       
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
        em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)
        em.set_footer(text = f"LMAO YOU LOST , THE CORRECT WORD WAS {word}")
        await ctx.send(embed = em)

@client.command()
async def hangman(ctx): 
    if ctx.author.id in hangman_:
        await ctx.send("`Baka! you are already in a game type '^end' to end this one and start a new one!`")
        return 

    hangman_.append(ctx.author.id)  
    hint = [] 
    wrong_guess = []  
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '`', '~', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', ')', '0', '-', '=', '+', '/', '*', '-', '+', '/', '?', ';', ':', "'", '"', ',', '<', '>', '[', ']', '{', '}', '.'] 
    secret_word = rw.get_random_word(hasDictionaryDef="true") 
    secret_word = secret_word.lower()
    x = (dictionary.meaning(secret_word))
    if x != None:
        hint__ = []   
        for i in x:
            y = x.get(i) 
            ne = " | ".join(str(elem) for elem in y)
            dic = f"{i} : {ne}"
            hint__.append(dic) 
        dichint = " , ".join(str(elem) for elem in hint__)  
    if not x:
        dichint = "sorry! no hints for ya ;)"

    secret_word_index = list(secret_word)  
    secret_word_index_display = []
    for i in secret_word:
        secret_word_index_display.append("_")    
    secret_word_display = " ".join(str(elem) for elem in secret_word_index_display)  
    em = Embed(title = f"`{secret_word_display}`" , description ="""```
___________________ 𝐻𝒶𝓃𝑔𝓂𝒶𝓃
│                                                          
│                                                                                     
│                                                                   
│                                                                                
│                                                                               
│                                                                 
│                                                                   
│                                                                
│________________________________```""" , colour = ctx.author.colour)
    em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url) 
    wrong_letters = ",".join(str(elem) for elem in wrong_guess) 
    em.set_footer(text=f"Wrong Guesses - {wrong_letters} | Hint - {dichint}") 

    emwin = Embed(description = "`YOU WIN!`"  , colour = ctx.author.colour )
    emwin.set_footer(text = secret_word)
    emwin.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url)

    emto = Embed(description = f"`HAHA BAKA! YOU LOST , THE WORD WAS {secret_word}`"  , colour = ctx.author.colour )

    msg = await ctx.send(embed = em)

    def check(m):
        return m.content in secret_word_index or m.content in characters or m.content in ["^hint",",hint","ehint","Ehint",f"{secret_word}" , "^end",",end","eend","Eend"] and m.channel == ctx.channel
    
    while True:
        try:
            msg1 = await client.wait_for('message', check=check , timeout = 600) 
            if msg1.author == ctx.author:
                if msg1.content in secret_word_index:
                    counter = 0 
                    for i in secret_word_index_display:
                        if i == "_": 
                            counter += 1
                    if counter != 1:   
                        x = (list_duplicates_of(secret_word,msg1.content))  
                        for i in x:
                            secret_word_index_display[i] = msg1.content
                        secret_word_display = " ".join(str(elem) for elem in secret_word_index_display)
                        wrong_letters = ",".join(str(elem) for elem in wrong_guess)  
                        await correct_embed(ctx , secret_word_display , msg , len(wrong_guess),wrong_letters) 

                    else:
                        await ctx.send(embed = emwin) 
                        await ctx.send("`Dammit , You win ;-;`") 
                        hangman_.remove(ctx.author.id)  
                        break       

                if msg1.content not in secret_word_index and msg1.content in characters:
                    if msg1.content in wrong_guess:
                        await ctx.send(f"`Baka!, HOW MANY TIMES DO I NEED TO TELL YOU THAT '{msg1.content}' IS NOT A PART OF THE WORD!`" , delete_after = 5)
                    else: 
                        await ctx.send(f"`Baka!, '{msg1.content}' is not a part of the word!`" , delete_after = 5)
                        wrong_guess.append(msg1.content)
                    x = len(wrong_guess)
                    if x != 7: 
                        wrong_letters = ",".join(str(elem) for elem in wrong_guess)  
                        await wrong_embed(ctx , secret_word_display , msg , x , wrong_letters , secret_word)

                    else:
                        wrong_letters = ",".join(str(elem) for elem in wrong_guess)  
                        await wrong_embed(ctx , secret_word_display , msg , 7 , wrong_letters , secret_word) 
                        hangman_.remove(ctx.author.id)  
                        break  


                if msg1.content == "^hint" or msg1.content == ",hint" or msg1.content == "ehint" or msg1.content == "Ehint":
                    if len(hint) < len(secret_word)/2:  
                        r = random.choice(secret_word_index) 
                        while r in secret_word_index_display and r in  hint: 
                            r = random.choice(secret_word_index)
                        await ctx.send(f"`'{r}' is a part of the word`" , delete_after = 5)
                        hint.append(r)

                    else:
                        ri = ",".join(str(elem) for elem in hint) 
                        await ctx.send(f"`woopsies! you cant get anymore hints`\n`{ri} is all you have got`")  

                if msg1.content == "^end" or msg1.content == ",end" or msg1.content == "eend" or msg1.content == "Eend":
                    await ctx.send(embed = emto) 
                    hangman_.remove(ctx.author.id) 
                    break 
                
                if msg1.content == secret_word:
                    await ctx.send(embed = emwin) 
                    await ctx.send("`Dammit , You win ;-;`")  
                    hangman_.remove(ctx.author.id) 
                    break 
        except:
            await ctx.send(embed = em)
            hangman_.remove(ctx.author.id) 
            break

@client.event
async def on_command_error(ctx, error):
    return 

client.run(os.environ["DISCORD_TOKEN"])  
