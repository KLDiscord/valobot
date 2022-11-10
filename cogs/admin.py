from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import discord
from discord import Interaction, app_commands, ui
from discord.ext import commands

if TYPE_CHECKING:
    from bot import ValorantBot


class Admin(commands.Cog):
    """Error handler"""

    def __init__(self, bot: ValorantBot) -> None:
        self.bot: ValorantBot = bot

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, sync_type: Literal['guild', 'global']) -> None:
        """Sync the application commands"""

        async with ctx.typing():
            if sync_type == 'guild':
                self.bot.tree.copy_global_to(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Synced guild !")
                return

            await self.bot.tree.sync()
            await ctx.reply(f"Synced global !")

    @commands.command()
    @commands.is_owner()
    async def unsync(self, ctx: commands.Context, unsync_type: Literal['guild', 'global']) -> None:
        """Unsync the application commands"""

        async with ctx.typing():
            if unsync_type == 'guild':
                self.bot.tree.clear_commands(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Un-Synced guild !")
                return

            self.bot.tree.clear_commands()
            await self.bot.tree.sync()
            await ctx.reply(f"Un-Synced global !")

    @app_commands.command(description='봇에 대한 기본적인 정보들을 줍니다')
    async def 정보(self, interaction: Interaction) -> None:
        """Shows basic information about the bot."""

        owner_url = f'https://discord.gg/AtqSu6Q63q'
        support_url = 'https://discord.gg/AtqSu6Q63q'

        embed = discord.Embed(color=0xFFFFFF)
        embed.set_author(name='발로봇 by 권유빈')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/1036883566627389443/1040219514559795301/unknown.png')
        embed.add_field(name='개발자:', value=f"[권유빈#7184]({owner_url})", inline=False)
        embed.add_field(
            name='상세 정보:',
            value=f"[개발 날짜] 2022.11.10 ~ \n"
            "[현재버전] 1.0\n"
            "==========**크레딧**==========\n"
            "[HeyM1ke - 비공식 발로란트 API ](https://github.com/HeyM1ke/ValorantClientAPI)\n"
            "[colinhartigan - 파이썬 발로란트 엔드포인트](https://github.com/colinhartigan/valclient.py)\n"
            "[techchrism - API 문서](https://github.com/techchrism/valorant-api-docs/)\n"
            "[valorant-api.com - 스킨 이름괴 이미지](https://valorant-api.com/)\n"
            "[디스코드 VAD - VAPI를 위한 개발자 커뮤니티](https://discord.gg/a9yzrw3KAm)\n"
            "==========**봇 초대하기**==========\n"
            "[여기](https://discord.com/api/oauth2/authorize?client_id=1040206071417012234&permissions=8&scope=bot)를 눌러 초대하기\n",
            inline=False,
        )
        view = ui.View()
        view.add_item(ui.Button(label='깃허브', url="https://github.com/KLDiscord/KLDiscord", row=0))
        view.add_item(ui.Button(label='지원 서버', url=support_url, row=0))
        view.add_item(ui.Button(label='봇 초대하기', url="https://discord.com/api/oauth2/authorize?client_id=1040206071417012234&permissions=8&scope=bot", row=0))
        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot: ValorantBot) -> None:
    await bot.add_cog(Admin(bot))
