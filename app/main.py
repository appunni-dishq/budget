from fastapi import FastAPI

from .account.endpoints import router as account_router, connection_router
from .report.endpoints import router as report_router
from .transaction.endpoints import router as report_router
from .scraper.endpoints import router as scraper_router

app = FastAPI()

app.include_router(account_router, prefix="/accounts")
app.include_router(scraper_router, prefix="/scrapers")
app.include_router(report_router, prefix="/reports")
app.include_router(report_router, prefix="/transactions")
app.include_router(connection_router, prefix="/connections")
