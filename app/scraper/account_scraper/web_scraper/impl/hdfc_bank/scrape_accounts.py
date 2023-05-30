import json
from typing import List
import asyncio

from app.account.models import AccountProvider
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

if __name__ == "__main__":
    scraper = Scrape(
        Connection(
            id=1,
            conn_id="hdfc_1",
            provider=AccountProvider.HDFC_BANK,
            login_url="https://netbanking.hdfcbank.com/netbanking/",
            credentials=json.load(open(".credential.json")),
            extra=None
        )
    )
    scraper.scrape()