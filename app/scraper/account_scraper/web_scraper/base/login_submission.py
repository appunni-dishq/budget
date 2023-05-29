from app.scraper.account_scraper.web_scraper.base.action import Action


class LoginSubmission(Action):

    async def act(self):
        return await self.submit_login()

    async def submit_login(self):
        raise NotImplementedError("login navigation is a required interface not implemented")
