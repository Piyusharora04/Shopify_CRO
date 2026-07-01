from urllib.parse import urljoin

import httpx


class ProductDiscovery:
    async def discover(
        self,
        base_url: str,
        limit: int = 8,
    ) -> list[str]:

        endpoint = f"{base_url.rstrip('/')}/products.json?limit={limit}"

        async with httpx.AsyncClient(
            timeout=30,
            follow_redirects=True,
        ) as client:

            response = await client.get(endpoint)

            response.raise_for_status()

            data = response.json()

        urls = []

        for product in data.get("products", []):

            handle = product.get("handle")

            if not handle:
                continue

            urls.append(
                urljoin(
                    base_url,
                    f"/products/{handle}",
                )
            )

        return urls