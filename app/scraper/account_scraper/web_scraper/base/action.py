from app.scraper.account_scraper.web_scraper.base import BaseScraper


class Action:
    def __init__(self, scraper: BaseScraper):
        self.scraper = scraper

    def act(self):
        raise NotImplementedError("Basic action must be a valid interface")
