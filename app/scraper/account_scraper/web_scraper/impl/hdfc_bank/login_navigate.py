from app.scraper.account_scraper.web_scraper.base.login_navigate import LoginNavigate


class HDFCLoginNavigate(LoginNavigate):

    async def navigate_to_login(self, login_url: str):
        page = self.scraper.page
        await page.goto(login_url, timeout=30000, wait_until='load')
        content = await page.content()
