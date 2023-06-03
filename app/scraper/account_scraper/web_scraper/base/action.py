from typing import Dict

from app.scraper.account_scraper.web_scraper.base import BaseScraper


class Action:
    def __init__(self, scraper: BaseScraper, context: Dict = None):
        self.scraper = scraper
        self.context = context if context is not None else {}

    def act(self):
        raise NotImplementedError("Basic action must be a valid interface")
