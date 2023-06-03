from app.account.schemas import AccountCreate
from app.scraper.account_scraper.constants import ACCOUNTS_CONTEXT_KEY
from app.scraper.account_scraper.web_scraper.base.action import Action


class ListAccounts(Action):

    async def act(self):
        return await self.list_account()

    async def list_account(self):
        raise NotImplementedError("list account is a required interface not implemented")

    def add_account(self, account: AccountCreate):
        if self.context is None:
            self.context = {}
        if self.context.get(ACCOUNTS_CONTEXT_KEY) is None:
            self.context[ACCOUNTS_CONTEXT_KEY] = []
        self.context[ACCOUNTS_CONTEXT_KEY].append(account)
