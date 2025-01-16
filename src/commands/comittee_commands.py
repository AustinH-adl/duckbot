import logging
import os

from discord import Interaction, app_commands
from dotenv import load_dotenv

load_dotenv()


# Cant handle blank Comittee Role
try:
    COMITTEE_ROLE = [int(i) for i in os.getenv("COMITTEE_ROLE").split(",")]
except ValueError:
    logging.warning("No Comittee roles provided.")
# int(os.getenv("COMITTEE_ROLE", -1).split(","))


class ComitteeCommands(app_commands.Group):
    def __init__(self):
        super().__init__(
            name="comittee", description="Comittee commands for announcements"
        )

    async def checkComittee(self, interaction: Interaction) -> bool:
        """Check if user who called interaction has comittee role"""

        roles = interaction.user.roles

        for role in roles:  # TODO: Optimise
            for allowedrole in COMITTEE_ROLE:
                if role.id == allowedrole:
                    logging.info(f"User {interaction.user.name} is authorised.")
                    return True

        await interaction.response.send_message(
            "You don't have permission to execute that command.", ephemeral=True
        )
        logging.warning(f"User {interaction.user.name} is not authorised.")
        return False


comitteeCommands = ComitteeCommands()
