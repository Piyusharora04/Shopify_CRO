import os
import uuid

from fastapi import APIRouter

from app.services.pdf_export import PDFExporter
from app.crawler.browser import BrowserManager
from app.extractors.homepage import HomepageExtractor
from app.extractors.pdp import PDPExtractor
from app.models.audit import AnalyzeRequest
from app.services.product_discovery import ProductDiscovery
from app.services.recommendation_engine import RecommendationEngine

router = APIRouter(prefix="/api", tags=["Analysis"])


@router.post("/analyze")
async def analyze(request: AnalyzeRequest):

    browser = BrowserManager()

    await browser.start()

    analysis_id = uuid.uuid4().hex

    analysis_dir = os.path.join(
        "screenshots",
        analysis_id,
    )

    context, page = await browser.new_page()

    #
    # Homepage
    #

    print("=" * 60)
    print("Opening homepage...")
    print("=" * 60)

    await page.goto(
        request.url,
        wait_until="domcontentloaded",
        timeout=60000,
    )

    await page.wait_for_timeout(3000)

    await page.evaluate(
        "window.scrollTo(0, 0)"
    )

    await page.wait_for_timeout(500)

    await browser.take_screenshot(
        page,
        os.path.join(
            analysis_dir,
            "homepage.png",
        ),
    )

    homepage = await HomepageExtractor().extract(page)

    #
    # Discover Products
    #

    print("=" * 60)
    print("Discovering products...")
    print("=" * 60)

    discovery = ProductDiscovery()

    product_urls = await discovery.discover(
        request.url,
        limit=8,
    )

    print(product_urls)

    #
    # Analyze Products
    #

    extractor = PDPExtractor()

    products = []

    for index, url in enumerate(product_urls, start=1):

        print(f"\nOpening: {url}")

        try:

            await page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000,
            )

            await page.wait_for_timeout(2000)

            await page.evaluate(
                "window.scrollTo(0, 250)"
            )

            await page.wait_for_timeout(500)

            await browser.take_screenshot(
                page,
                os.path.join(
                    analysis_dir,
                    f"product_{index}.png",
                ),
            )

            print(f"Loaded: {page.url}")

            evidence = await extractor.extract(page)

            products.append(evidence)

            print("Success")

        except Exception as e:

            print("FAILED")
            print(e)

    #
    # Generate Audit
    #

    audit = RecommendationEngine().generate(
        homepage=homepage,
        products=products,
    )
    
    pdf_path = os.path.join(
        analysis_dir,
        "report.pdf",
    )

    PDFExporter().export(
        audit,
        homepage,
        products,
        pdf_path,
    )

    await context.close()

    await browser.stop()

    return {
        "analysis_id": analysis_id,
        "homepage": homepage.model_dump(),
        "products": [p.model_dump() for p in products],
        "audit": audit.model_dump(),
        "screenshots": {
            "homepage": f"/screenshots/{analysis_id}/homepage.png",
            "products": [
                f"/screenshots/{analysis_id}/product_{i}.png"
                for i in range(
                    1,
                    len(products) + 1,
                )
            ],
        },
        "report": f"/screenshots/{analysis_id}/report.pdf",
    }