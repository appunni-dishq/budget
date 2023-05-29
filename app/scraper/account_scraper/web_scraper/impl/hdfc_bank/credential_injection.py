from asyncio import sleep

from app.account.schemas import Connection
from app.scraper.account_scraper.web_scraper.base.credential_injection import CredentialInjection
from app.scraper.account_scraper.web_scraper.base.login_submission import LoginSubmission


class HDFCCredentialInjection(CredentialInjection):

    async def inject_credential(self, conn: Connection):
        assert self.scraper.page is not None
        page = self.scraper.page
        # Find the username and password input fields
        username_input = page.locator(".loginData > input")
        await username_input.type("Bard")
        await sleep(10000)




