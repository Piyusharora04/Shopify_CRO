import type { Product } from "../../types/audit";

interface Props {
  products: Product[];
}

export default function ProductTable({
  products,
}: Props) {
  return (
    <section>

      <h2 className="mb-6 text-3xl font-bold">
        Crawled Products
      </h2>

      <div className="overflow-hidden rounded-3xl border border-white/10">

        <table className="w-full">

          <thead className="bg-white/5">

            <tr>

              <th className="p-5 text-left">
                Product
              </th>

              <th>
                Price
              </th>

              <th>
                Images
              </th>

              <th>
                Reviews
              </th>

              <th>
                Shipping
              </th>

              <th>
                Returns
              </th>

              <th>
                ATC
              </th>

              <th>
                Sticky
              </th>

            </tr>

          </thead>

          <tbody>

            {products.map((product) => (

              <tr
                key={product.url}
                className="border-t border-white/10"
              >

                <td className="max-w-sm p-5">

                  <div className="font-medium">

                    <td className="max-w-sm truncate font-medium">
                        {product.title}s
                    </td>

                  </div>

                </td>

                <td>
                  {product.price ?? "-"}
                </td>

                <td>
                  {product.image_count}
                </td>

                <td>
                  {product.review_count ?? "-"}
                </td>

                <td>
                  {product.shipping_information ? "✓" : "✗"}
                </td>

                <td>
                  {product.returns_information ? "✓" : "✗"}
                </td>

                <td>
                  {product.add_to_cart_present ? "✓" : "✗"}
                </td>

                <td>
                  {product.sticky_add_to_cart ? "✓" : "✗"}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </section>
  );
}