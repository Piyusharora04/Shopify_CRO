import re

from playwright.async_api import Page

from app.models.pdp import PDPEvidence


class PDPExtractor:

    PRICE_REGEX = re.compile(r"\$?\d+(?:\.\d{1,2})?")

    async def extract(self, page: Page) -> PDPEvidence:

        evidence = PDPEvidence(
            url=page.url,
            title=await page.title(),
        )

        body = (await page.locator("body").inner_text()).lower()

        # -------------------------------
        # Images
        # -------------------------------

        evidence.image_count = await page.locator(
            'img[src]'
        ).count()

        # -------------------------------
        # Breadcrumbs
        # -------------------------------

        evidence.breadcrumbs_present = (
            await page.locator(
                "nav[aria-label*=breadcrumb i], .breadcrumb"
            ).count()
            > 0
        )

        # -------------------------------
        # Size Guide
        # -------------------------------

        evidence.size_guide_present = (
            "size guide" in body
        )

        # -------------------------------
        # Shipping / Returns
        # -------------------------------

        evidence.shipping_information = (
            "shipping" in body
            or "delivery" in body
        )

        evidence.returns_information = (
            "return" in body
            or "refund" in body
        )

        # -------------------------------
        # Add To Cart
        # -------------------------------

        purchase_selectors = [

            "button",

            "[role='button']",

            "input[type=submit]",

        ]

        keywords = [

            "add to bag",

            "add to cart",

            "buy now",

            "purchase",

        ]

        for selector in purchase_selectors:

            locator = page.locator(selector)

            count = await locator.count()

            for i in range(count):

                try:

                    text = (
                        await locator.nth(i).inner_text()
                    ).lower()

                    if any(k in text for k in keywords):

                        evidence.add_to_cart_present = True

                        raise StopIteration

                except StopIteration:

                    break

                except:

                    pass

            if evidence.add_to_cart_present:
                break

        # -------------------------------
        # Sticky Add To Cart
        # -------------------------------

        sticky = page.locator(
            """
            [class*=sticky i],
            [class*=floating i],
            [class*=fixed i]
            """
        )

        sticky_count = await sticky.count()

        for i in range(sticky_count):

            try:

                element = sticky.nth(i)

                if not await element.is_visible():
                    continue

                text = (
                    await element.text_content()
                    or ""
                ).lower()

                if any(
                    keyword in text
                    for keyword in [
                        "add to cart",
                        "add to bag",
                        "buy now",
                        "checkout",
                    ]
                ):
                    evidence.sticky_add_to_cart = True
                    break

            except Exception:
                continue

        # -------------------------------
        # Variants
        # -------------------------------

        variant_buttons = page.locator(
            """
            button,
            label
            """
        )

        variant_count = await variant_buttons.count()

        for i in range(variant_count):

            locator = variant_buttons.nth(i)

            text = await locator.inner_text()

            text = text.strip()

            if (
                text in {
                    "XXS",
                    "XS",
                    "S",
                    "M",
                    "L",
                    "XL",
                    "XXL",
                }
                and text not in evidence.variants
            ):
                evidence.variants.append(text)

        # -------------------------------
        # Rating
        # -------------------------------

        rating_patterns = [

            r"([1-5]\.\d)\s*out of",

            r"rated\s*([1-5]\.\d)",

            r"([1-5]\.\d)\s*stars",

        ]

        for pattern in rating_patterns:

            match = re.search(pattern, body)

            if match:

                try:

                    evidence.rating = float(match.group(1))

                    break

                except:
                    pass

        # -------------------------------
        # Review Count
        # -------------------------------

        review_patterns = [

            r"(\d[\d,]*)\s+reviews",

            r"(\d[\d,]*)\s+ratings",

            r"based on\s+(\d[\d,]*)",

        ]

        for pattern in review_patterns:

            match = re.search(pattern, body)

            if match:

                try:

                    evidence.review_count = int(
                        match.group(1).replace(",", "")
                    )

                    break

                except:
                    pass

        # -------------------------------
        # Prices
        # -------------------------------

        price_candidates = []

        price_selectors = [
            "[data-product-price]",
            "[data-price]",
            ".price",
            ".product-price",
            ".money",
            ".price-item",
            ".price__current",
            ".price__sale",
            ".ProductMeta__Price",
        ]

        for selector in price_selectors:

            locator = page.locator(selector)

            count = await locator.count()

            for i in range(min(count, 10)):

                try:

                    text = await locator.nth(i).inner_text()

                    matches = re.findall(
                        r"\$\s?(\d+(?:\.\d{1,2})?)",
                        text,
                    )

                    for match in matches:

                        value = float(match)

                        if 5 <= value <= 5000:
                            price_candidates.append(value)

                except:
                    pass

        # fallback

        if not price_candidates:

            body_text = await page.locator("body").inner_text()

            matches = re.findall(
                r"\$\s?(\d+(?:\.\d{1,2})?)",
                body_text,
            )

            for match in matches:

                value = float(match)

                if 5 <= value <= 5000:
                    price_candidates.append(value)

        price_candidates = sorted(set(price_candidates))

        if price_candidates:

            evidence.price = price_candidates[0]

        if len(price_candidates) >= 2:

            evidence.compare_at_price = price_candidates[1]

        if (
            evidence.price
            and evidence.compare_at_price
            and evidence.compare_at_price > evidence.price
        ):

            evidence.discount_percent = round(
                (
                    (
                        evidence.compare_at_price
                        - evidence.price
                    )
                    / evidence.compare_at_price
                )
                * 100
            )

        evidence.currency = "USD" if price_candidates else None

        # -------------------------------
        # Trust Badges
        # -------------------------------

        trust_keywords = [
            "secure checkout",
            "free shipping",
            "easy returns",
            "money back",
            "trusted",
            "klarna",
            "afterpay",
            "paypal",
        ]

        for keyword in trust_keywords:

            if keyword in body:

                evidence.trust_badges.append(keyword)

        return evidence