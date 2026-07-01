from playwright.async_api import Page

from app.models.evidence import HomepageEvidence


class HomepageExtractor:

    async def extract(self, page: Page) -> HomepageEvidence:

        evidence = HomepageEvidence()

        evidence.title = await page.title()

        #
        # Hero Heading
        #
        headings = page.locator("h1")

        if await headings.count():

            evidence.hero_heading = (
                await headings.first.inner_text()
            ).strip()

        #
        # Hero Sub Heading
        #
        paragraphs = page.locator("main p")

        if await paragraphs.count():

            evidence.hero_subheading = (
                await paragraphs.first.inner_text()
            ).strip()

        #
        # Hero CTA
        #
        hero_button = page.locator(
            "main a, main button"
        ).first

        if await hero_button.count():

            text = await hero_button.inner_text()

            if text.strip():
                evidence.hero_cta = text.strip()

        #
        # Search
        #
        evidence.search_present = (
            await page.locator(
                'input[type="search"], [aria-label*="search" i]'
            ).count()
            > 0
        )

        #
        # Account
        #
        evidence.account_present = (
            await page.locator(
                '[aria-label*="account" i]'
            ).count()
            > 0
        )

        #
        # Wishlist
        #
        evidence.wishlist_present = (
            await page.locator(
                '[aria-label*="wishlist" i]'
            ).count()
            > 0
        )

        #
        # Cart
        #
        evidence.cart_present = (
            await page.locator(
                '[aria-label*="cart" i]'
            ).count()
            > 0
        )

        #
        # Navigation
        #
        nav_links = page.locator("header nav a")

        for i in range(await nav_links.count()):

            text = (
                await nav_links.nth(i).inner_text()
            ).strip()

            if text and text not in evidence.navigation_links:

                evidence.navigation_links.append(text)

        #
        # Featured Collections
        #
        cards = page.locator("main section a")

        for i in range(min(await cards.count(), 20)):

            text = (
                await cards.nth(i).inner_text()
            ).strip()

            if (
                len(text) > 2
                and len(text) < 40
                and text not in evidence.featured_collections
            ):

                evidence.featured_collections.append(text)

        #
        # Trust Signals
        #
        page_text = (
            await page.locator("body").inner_text()
        ).lower()

        keywords = [
            "free shipping",
            "easy returns",
            "secure checkout",
            "money back",
            "trusted",
            "fast delivery",
            "30 day",
            "free returns",
        ]

        for keyword in keywords:

            if keyword in page_text:

                evidence.trust_signals.append(keyword)

        #
        # Newsletter
        #
        evidence.newsletter_present = (
            "newsletter" in page_text
            or "subscribe" in page_text
        )

        #
        # Footer
        #
        evidence.footer_present = (
            await page.locator("footer").count()
            > 0
        )

        #
        # Announcement Bar
        #
        evidence.announcement_bar = (
            await page.locator(
                '[class*="announcement"], [id*="announcement"]'
            ).count()
            > 0
        )

        return evidence