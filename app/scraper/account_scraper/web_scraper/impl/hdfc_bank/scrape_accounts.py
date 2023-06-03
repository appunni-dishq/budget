import json
from typing import List

from app.account.models import AccountProvider
from app.account.schemas import Connection
from app.scraper.account_scraper.web_scraper.base import BaseScraper
from app.scraper.account_scraper.web_scraper.base.action import Action
from app.scraper.account_scraper.web_scraper.impl.hdfc_bank.actions.accounts.list_accounts import ListHDFCAccounts
from app.scraper.account_scraper.web_scraper.impl.hdfc_bank.actions.login.credential_injection import HDFCCredentialInjection
from app.scraper.account_scraper.web_scraper.impl.hdfc_bank.actions.login.login_navigate import HDFCLoginNavigate
from app.scraper.account_scraper.web_scraper.impl.hdfc_bank.actions.login.login_submission import HDFCLoginSubmission


class Scrape(BaseScraper):
    actions: List[Action.__class__] = [HDFCLoginNavigate,
                                       HDFCCredentialInjection,
                                       HDFCLoginSubmission,
                                       ListHDFCAccounts]

if __name__ == "__main__":
    scraper = Scrape(
        Connection(
            id=1,
            conn_name="hdfc_1",
            provider=AccountProvider.HDFC_BANK,
            login_url="https://netbanking.hdfcbank.com/netbanking/",
            credentials=json.load(open(".credential.json")),
            extra=None
        )
    )
    scraper.scrape()