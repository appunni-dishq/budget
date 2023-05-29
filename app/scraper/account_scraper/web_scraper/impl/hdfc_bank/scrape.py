from typing import List
import asyncio
from app.account.schemas import Connection
from playwright.async_api import async_playwright
from app.scraper.account_scraper.web_scraper.base import BaseScraper
from app.scraper.account_scraper.web_scraper.base.action import Action
from app.scraper.account_scraper.web_scraper.impl.hdfc_bank.credential_injection import HDFCCredentialInjection
from app.scraper.account_scraper.web_scraper.impl.hdfc_bank.login_navigate import HDFCLoginNavigate
from app.scraper.account_scraper.web_scraper.impl.hdfc_bank.login_submission import HDFCLoginSubmission


class Scrape(BaseScraper):
    actions: List[Action.__class__] = [HDFCLoginNavigate,
                                       HDFCCredentialInjection,
                                       HDFCLoginSubmission]
    def scrape(self):
        return asyncio.run(self.__scrape())

    async def __scrape(self):
        async with async_playwright() as p:
            await self.initialize(p)
            for action in self.actions:
                await action(self).act()


if __name__ == "__main__":
    scraper = Scrape(
        None
    )
    scraper.scrape()