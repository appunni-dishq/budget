import asyncio

from playwright.async_api import async_playwright
from app.account.schemas import Connection


class BaseScraper:
    actions = []

    def __init__(self, conn: Connection):
        self.__browser = None
        self.page = None
        self.conn = conn

    async def initialize(self, p):
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        self.page = page
