import discord 
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import sys, traceback
import random
import datetime
import time
import idioticapi


class Idiotic:
    """These commands are simply to idiotic for me."""
    def __init__(self, bot):
        self.bot = bot
        self.token = "TxdGgJJl3C1jBCZYzmmd"
        self.client = idioticapi.Client(self.token, dev=True)

    @commands.group(invoke_without_command=True)
    async def idiotic(self, ctx):
        """Usage: [prefix] + [idiotic command]"""
        await ctx.send("Usage: `[prefix] + [idiotic command]` Note: Use all lowercase and no hyphons (-)")
        
        
    def format_avatar(self, avatar_url):
        if avatar_url.endswith(".gif"):
            return avatar_url + "?size=2048"
        return avatar_url.replace("webp", "png")


    @idiotic.command()
    async def blame(self, ctx, *, text=None):
        try:
            await ctx.send(file=discord.File(await self.client.blame(str(text)), "blame.png"))
        except Exception as e:
            await ctx.send(f"An error occured. \nMore details: \n{e}")
            
            
    @idiotic.command()
    async def triggered(self, ctx, user: discord.Member = None):
        """T R I G Gered!!!"""
        if user is None:
            user = ctx.author
        try:
            await ctx.trigger_typing()
            av = self.format_avatar(user.avatar_url)
            await ctx.send(f"B O I! {ctx.author} just made {user.name} T R I G G E R E D!!", file=discord.File(await self.client.triggered(av), "triggered.gif"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")
            
    @idiotic.command()
    async def shit(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"oh deer :deer:, {user.name} got stepped on. how unfortunate.", file=discord.File(await self.client.stepped(user.avatar_url), "stepped.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")        
           
    @idiotic.command()
    async def facepalm(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"oml, {user.name} had to facepalm. smh.", file=discord.File(await self.client.facepalm(user.avatar_url), "facepalm.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")

    @idiotic.command()
    async def insult(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"aw eggplants! :eggplant:, {user.name} got insulted. how unfortunate.", file=discord.File(await self.client.waifu_insult(user.avatar_url), "waifuinsult.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")
            
    
    @idiotic.command()
    async def batslap(self, ctx, user: discord.Member = None):
        """Tag someone to give them A TASTE OF YOUR P A L M"""
        if user is None:
            await ctx.send("Tag the user first bro")
        else:
            await ctx.trigger_typing()
            try:

                av = self.format_avatar(user.avatar_url)
                avatar = self.format_avatar(ctx.author.avatar_url)
                await ctx.send(f"OOF! **{ctx.author.name}** slapped **{user.name}!**", file=discord.File(await self.client.batslap(avatar, av), "batslap.png"))
            except Exception as e:
                await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")
    
    
    @idiotic.command()
    async def scary(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"**{user.name}** scared off a poor kid.", file=discord.File(await self.client.wreckit(user.avatar_url), "scary.png"))
        except Exception as e:
            await ctx.send(f"An error occured with IdioticAPI. \nMore details: \n{e}")

    @idiotic.command()
    async def approved(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"**{user.name}** is now approved.", file=discord.File(await self.client.approved(user.avatar_url), "approved.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")

    @idiotic.command()
    async def rejected(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"**{user.name}** got rejected.", file=discord.File(await self.client.rejected(user.avatar_url), "rejected.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")

    @idiotic.command()
    async def gay(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"**{user.name}** is GAY.", file=discord.File(await self.client.rainbow(user.avatar_url), "gay.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")

    @idiotic.command()
    async def greyscale(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"**{user.name}** is in greyscale.", file=discord.File(await self.client.greyscale(user.avatar_url), "greyscale.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")

    @idiotic.command()
    async def invert(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"**{user.name}** has inverted color!", file=discord.File(await self.client.invert(user.avatar_url), "invert.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")

    @idiotic.command()
    async def crush(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        if user is None:
            return await ctx.send("I'm sorry, can you *tag the person you have a crush on?*")
        try:
            await ctx.send(f"**{ctx.author.name}** has a crush on **{user.name}**!", file=discord.File(await self.client.crush(ctx.author.avatar_url, user.avatar_url), "crush.png"))
        except Exception as e:
            await ctx.send(f"An error occured with IdioticAPI. \nMore details: \n{e}")


    @idiotic.command()
    async def snapchat(self, ctx, *, text=None):
        await ctx.trigger_typing()
        if text is None:
            return await ctx.send("I'm sorry, *what did you want to write on the Snapchat?*")
        try:
            await ctx.send(f"**{ctx.author.name}** sent a Snapchat!", file=discord.File(await self.client.snapchat(text), "snapchat.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")


    @idiotic.command(aliases=["respect"])
    async def respeck(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"**{user.name}** is being respecked!!", file=discord.File(await self.client.respect(user.avatar_url), "respe.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")


    @idiotic.command()
    async def cursive(self, ctx, *, text=None):
        """Turn your text into cursive!"""
        try:
            await ctx.message.delete()
        except:
            pass
        try:
            await ctx.send(await self.client.cursive(text, 'bold'))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")


    @idiotic.command()
    async def spank(self, ctx, user: discord.Member = None):
        """Spank someone. Spank someone hARD!"""
        await ctx.trigger_typing()
        if user is None:
            return await ctx.send("I'm sorry, can you *tag the person you wanna spank*")
        try:
            await ctx.send(f"Ouch! **{ctx.author.name}** spanked **{user.name}** hard on the ass.", file=discord.File(await self.client.super_spank(ctx.author.avatar_url, user.avatar_url), "spank.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")

    @idiotic.command()
    async def garbage(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"**{user.name}** is garbage.", file=discord.File(await self.client.garbage(user.avatar_url), "garbage.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")

    @idiotic.command()
    async def confused(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(f"**{user.name}** is confused?!", file=discord.File(await self.client.confused(user.avatar_url, self.bot.get_user(277981712989028353).avatar_url), "confused.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")

    
    @idiotic.command()
    async def mock(self, ctx, *, text=None):
        """Send someone in a MoCKinG voIcE."""
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(await self.client.mock(text))


    @idiotic.command()
    async def tiny(self, ctx, *, text=None):
        """Send your text in ᵗᶦⁿʸ ˡᵉᵗᵗᵉʳˢ."""
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(await self.client.tiny(text, 'superscript'))

    @idiotic.command()
    async def tindermatch(self, ctx, user: discord.Member = None):
        """Match yourself with someone like Tinder!"""
        await ctx.trigger_typing()
        if user is None:
            return await ctx.send("I'm sorry, can you *tag the person you wanna match with?*")
        try:
            await ctx.send(f"**{ctx.author.name}** got matched with **{user.name}**.", file=discord.File(await self.client.tinder_match(ctx.author.avatar_url, user.avatar_url), "tindermatch.png"))
        except Exception as e:
            await ctx.send(f"O H S N A P! something went wrong. kthnxbai. \n{e}")
    
    
def setup(bot):
    bot.add_cog(Idiotic(bot))