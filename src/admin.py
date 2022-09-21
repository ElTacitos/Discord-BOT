from discord.ext import commands
import discord


def get_nb_members(ctx, status):
    return len([m for m in ctx.guild.members if m.status == status])

def get_members(ctx, status):
    members = []
    for member in ctx.guild.members:
        if member.status == status:
            members.append(member.name)
    return members

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, user: discord.User):
        await ctx.guild.ban(user)
        await ctx.send(f'Banned {user.mention}')

    @commands.command()
    async def admin(self, ctx, user: discord.Member):
        if not discord.utils.get(ctx.guild.roles, name="Admin"):
            await ctx.guild.create_role(name="Admin", colour=discord.Colour(0x0062ff))
        role = discord.utils.get(ctx.guild.roles, name="Admin")
        await user.add_roles(role)
        await ctx.send(f'Added admin role to {user.mention}')

    @commands.command()
    async def count(self, ctx):
        nb_members_online = get_nb_members(ctx, discord.Status.online)
        nb_members_idle = get_nb_members(ctx, discord.Status.idle)
        nb_members_dnd = get_nb_members(ctx, discord.Status.dnd)
        nb_members_offline = get_nb_members(ctx, discord.Status.offline)
        members_online = get_members(ctx, discord.Status.online)
        members_idle = get_members(ctx, discord.Status.idle)
        members_dnd = get_members(ctx, discord.Status.dnd)
        members_offline = get_members(ctx, discord.Status.offline)
        print()
        message = f'There is {nb_members_online} watiMembers online ({", ".join(members_online)})\n' \
                  f'There is {nb_members_idle} idle watiMembers idle ({", ".join(members_idle)})\n' \
                  f'There is {nb_members_dnd} watiMembers you must not disturb ({", ".join(members_dnd)})\n' \
                  f'And there is {nb_members_offline} watiMembers offline ({", ".join(members_offline)})'
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Admin(bot))
