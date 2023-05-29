from app.account.schemas import Connection
from app.scraper.account_scraper.web_scraper.base import BaseScraper
from app.scraper.account_scraper.web_scraper.base.action import Action


class CredentialInjection(Action):

    async def act(self):
        return await self.inject_credential(self.scraper.conn)

    async def inject_credential(self, conn: Connection):
        raise NotImplementedError("credential injection is important interface needs implementation")
