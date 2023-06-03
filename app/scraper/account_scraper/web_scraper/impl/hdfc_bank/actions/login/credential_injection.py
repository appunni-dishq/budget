import asyncio
from asyncio import sleep

from app.account.credentials.hdfc_bank import HDFCBankCredential
from app.account.schemas import Connection
from app.scraper.account_scraper.web_scraper.base.credential_injection import CredentialInjection
from app.scraper.account_scraper.web_scraper.base.login_submission import LoginSubmission


class HDFCCredentialInjection(CredentialInjection):

    async def inject_credential(self, conn: Connection):
        assert self.scraper.page is not None
        page = self.scraper.page
        # Find the username and password input fields
        credentials = HDFCBankCredential(**conn.credentials)
        frame = page.frame_locator("[name='login_page']")
        await frame.locator(".loginData > input").focus()
        await frame.locator(".loginData > input").fill(credentials.customer_id)
        await frame.locator(".loginData > a").click()
        frame = page.frame_locator("[name='login_page']")
        await frame.locator(".loginData > input[name='fldPassword']").focus()
        await frame.locator(".loginData > input[name='fldPassword']").fill(credentials.password)
        await frame.locator(".pwd_field.sec_field > input[type='checkbox']").click()
        await frame.locator(".loginData > a").click()
