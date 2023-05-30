from app.account.schemas import Connection
from app.scraper.account_scraper.web_scraper.base import BaseScraper
from app.scraper.account_scraper.web_scraper.base.action import Action


class LoginNavigate(Action):

    async def act(self):
        return await self.navigate_to_login(self.scraper.conn.login_url)


    """
    Default is to simply provide the page loaded
    """
    async def navigate_to_login(self, login_url: str):
        pass

