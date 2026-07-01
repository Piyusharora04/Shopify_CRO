import os

from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    async_playwright,
)


class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser: Browser | None = None

    async def start(self):
        self.playwright = await async_playwright().start()

        self.browser = await self.playwright.chromium.launch(
            headless=True,
        )

    async def take_screenshot(
        self,
        page: Page,
        path: str,
        full_page: bool = False,
    ):

        directory = os.path.dirname(path)

        if directory:

            os.makedirs(
                directory,
                exist_ok=True,
            )

        await page.screenshot(
            path=path,
            full_page=full_page,
        )

        return path

    async def stop(self):
        if self.browser:
            await self.browser.close()

        if self.playwright:
            await self.playwright.stop()

    async def new_page(self) -> tuple[BrowserContext, Page]:
        if self.browser is None:
            raise RuntimeError(
                "Browser has not been started."
            )

        context = await self.browser.new_context(
            viewport={
                "width": 1440,
                "height": 900,
            },
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "Chrome/137.0.0.0 Safari/537.36"
            ),
        )

        page = await context.new_page()

        return context, page