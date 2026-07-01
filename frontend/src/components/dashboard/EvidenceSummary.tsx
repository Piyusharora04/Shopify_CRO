import type { Homepage } from "../../types/audit";
import {
  CheckCircle2,
  XCircle,
} from "lucide-react";

interface Props {
  homepage: Homepage;
}

export default function EvidenceSummary({
  homepage,
}: Props) {
  const items = [
    {
      label: "Search",
      value: homepage.search_present,
    },
    {
      label: "Account",
      value: homepage.account_present,
    },
    {
      label: "Wishlist",
      value: homepage.wishlist_present,
    },
    {
      label: "Cart",
      value: homepage.cart_present,
    },
    {
      label: "Announcement Bar",
      value: homepage.announcement_bar,
    },
    {
      label: "Newsletter",
      value: homepage.newsletter_present,
    },
    {
      label: "Footer",
      value: homepage.footer_present,
    },
  ];

  return (
    <section>

      <h2 className="mb-6 text-3xl font-bold">
        Homepage Evidence
      </h2>

      <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">

        {items.map((item) => (
          <div
            key={item.label}
            className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur-3xl"
          >
            <div className="flex items-center justify-between">

              <span className="text-zinc-300">
                {item.label}
              </span>

              {item.value ? (
                <CheckCircle2 className="text-emerald-400" />
              ) : (
                <XCircle className="text-red-400" />
              )}

            </div>

            <p
              className={`mt-5 text-2xl font-bold ${
                item.value
                  ? "text-emerald-400"
                  : "text-red-400"
              }`}
            >
              {item.value ? "Detected" : "Missing"}
            </p>

          </div>
        ))}

      </div>

    </section>
  );
}