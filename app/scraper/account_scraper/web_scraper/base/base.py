import asyncio
from pyppeteer import launch


class BaseScraper:
    def __int__(self):
        self.loop = asyncio.get_event_loop()
        self.__browser = None
        self.page = None
        self.actions = []

    @staticmethod
    async def initialize():
        browser = await launch()
        page = await browser.newPage()

