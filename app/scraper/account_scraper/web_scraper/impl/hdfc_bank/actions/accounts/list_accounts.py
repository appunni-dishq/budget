from app.account.models import AccountType, AccountProvider
from app.account.schemas import Account, AccountCreate
from app.scraper.account_scraper.web_scraper.base.list_accounts import ListAccounts


class ListHDFCAccounts(ListAccounts):

    async def list_account(self):
        page = self.scraper.page
        frame = page.frame_locator("[name='main_part']")
        savings_accounts = frame.locator("tr.hideSavingAccts")
        await savings_accounts.focus()
        await self.account_creator(savings_accounts, AccountType.SAVINGS)

        pf_accounts = frame.locator("tr.hidePpfAccts")
        await self.account_creator(savings_accounts, AccountType.SAVINGS)
        print("yes")

    async def account_creator(self, accounts, account_type: AccountType):
        all_accounts = []
        if await accounts.count() == 1:
            all_accounts = [accounts]
        elif await accounts.count() > 1:
            all_accounts = await accounts.all()

        for account in all_accounts:
            account_no = await account.locator('td:nth-child(1) span.headingLable + a').text_content()
            if account_no == "":
                continue
            description = await account.locator('td:nth-child(2) span:nth-child(2)').text_content()
            name = await account.locator('td:nth-child(3) span:nth-child(2)').text_content()
            balance_string = await account.locator('td:nth-child(4) span:nth-child(2)').text_content()
            acct: AccountCreate = AccountCreate(
                name=name,
                account_no=account_no,
                description=description,
                balance_string=balance_string,
                connection_id=self.scraper.conn.id,
                account_type=account_type,
                account_provider=AccountProvider.HDFC_BANK
            )
            self.add_account(acct)





