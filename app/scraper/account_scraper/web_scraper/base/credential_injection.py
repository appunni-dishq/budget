from app.account.schemas import Connection
from app.scraper.account_scraper.web_scraper.base import BaseScraper


class CredentialInjection(BaseScraper):

    async def inject_credential(self):
        raise NotImplementedError("credential injection is important interface needs implementation")
