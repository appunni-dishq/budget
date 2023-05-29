from app.scraper.account_scraper.web_scraper.base.login_navigate import LoginNavigate


class HDFCLoginNavigate(LoginNavigate):

    async def navigate_to_login(self):
        page = self.scraper.page
        await page.goto("https://netbanking.hdfcbank.com/netbanking/", timeout=30000, wait_until='load')
        content = await page.content()
