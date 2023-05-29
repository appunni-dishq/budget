from app.scraper.account_scraper.web_scraper.base.login_submission import LoginSubmission


class HDFCLoginSubmission(LoginSubmission):

    async def submit_login(self):
        assert self.scraper.page is not None

