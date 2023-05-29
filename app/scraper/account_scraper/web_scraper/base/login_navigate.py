from app.scraper.account_scraper.web_scraper.base import BaseScraper
from app.scraper.account_scraper.web_scraper.base.action import Action


class LoginNavigate(Action):

    async def act(self):
        return await self.navigate_to_login()


    """
    Default is to simply provide the page loaded
    """
    async def navigate_to_login(self):
        pass

