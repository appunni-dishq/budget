from app.scraper.account_scraper.web_scraper.base import BaseScraper


class Scrape(BaseScraper):

    def scrape(self):
        return self.loop.run_until_complete(self.__scrape())

    async def __scrape(self):
        await self.initialize()


