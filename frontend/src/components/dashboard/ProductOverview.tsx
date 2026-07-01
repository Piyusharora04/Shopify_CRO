import type { Product } from "../../types/audit";

interface ProductOverviewProps {
  products: Product[];
}

export default function ProductOverview({
  products,
}: ProductOverviewProps) {
  const total = products.length;

  const averageImages =
    total === 0
      ? 0
      : Math.round(
          products.reduce(
            (sum, product) => sum + product.image_count,
            0
          ) / total
        );

  const withReviews = products.filter(
    (product) =>
      product.review_count !== null &&
      product.review_count > 0
  ).length;

  const withShipping = products.filter(
    (product) => product.shipping_information
  ).length;

  const withReturns = products.filter(
    (product) => product.returns_information
  ).length;

  const withATC = products.filter(
    (product) => product.add_to_cart_present
  ).length;

  const withStickyATC = products.filter(
    (product) => product.sticky_add_to_cart
  ).length;

  const cards = [
    {
      title: "Products Crawled",
      value: total,
    },
    {
      title: "Avg Images",
      value: averageImages,
    },
    {
      title: "Products With Reviews",
      value: `${withReviews}/${total}`,
    },
    {
      title: "Shipping Info",
      value: `${withShipping}/${total}`,
    },
    {
      title: "Returns Info",
      value: `${withReturns}/${total}`,
    },
    {
      title: "Add To Cart",
      value: `${withATC}/${total}`,
    },
    {
      title: "Sticky ATC",
      value: `${withStickyATC}/${total}`,
    },
  ];

  return (
    <section>

      <h2 className="mb-6 text-3xl font-bold">
        Product Overview
      </h2>

      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">

        {cards.map((card) => (
          <div
            key={card.title}
            className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur-3xl"
          >
            <p className="text-sm text-zinc-400">
              {card.title}
            </p>

            <h3 className="mt-4 text-4xl font-bold">
              {card.value}
            </h3>
          </div>
        ))}

      </div>

    </section>
  );
}