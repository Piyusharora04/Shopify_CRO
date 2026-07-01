import { useState } from "react";

import AuroraBackground from "../components/layout/AuroraBackground";
import Navbar from "../components/layout/Navbar";
import Hero from "../components/hero/Hero";
import LoadingTimeline from "../components/hero/LoadingTimeline";

import ProductOverview from "../components/dashboard/ProductOverview";
import ScoreCard from "../components/dashboard/ScoreCard";
import MetricCard from "../components/dashboard/MetricCard";
import OpportunityCard from "../components/dashboard/OpportunityCard";
import EvidenceSummary from "../components/dashboard/EvidenceSummary";
import ProductTable from "../components/dashboard/ProductTable";
import ScreenshotGallery from "../components/dashboard/ScreenshotGallery";

import { useAudit } from "../hooks/useAudit";

export default function HomePage() {
  const [url, setUrl] = useState("");

  const { loading, data, analyze } = useAudit();

  async function handleAnalyze() {
    if (!url.trim()) return;

    await analyze(url);
  }

  return (
    <AuroraBackground>
      <div className="min-h-screen text-white">

        <Navbar />

        <Hero
          url={url}
          setUrl={setUrl}
          onAnalyze={handleAnalyze}
          loading={loading}
        />

        {loading && (
          <div className="mx-auto mt-16 max-w-5xl px-6">
            <LoadingTimeline loading={loading} />
          </div>
        )}

        {!loading && data && (
          <main className="mx-auto mt-16 max-w-7xl space-y-10 px-6 pb-20">

            <section className="grid gap-6 lg:grid-cols-4">

                <div className="lg:col-span-2">
                    <ScoreCard score={data.audit.score} report={data.report} />
                </div>

                <MetricCard
                    title="Recommendations"
                    value={data.audit.opportunities.length}
                />

                <MetricCard
                    title="Homepage Features"
                    value={
                    [
                        data.homepage.search_present,
                        data.homepage.account_present,
                        data.homepage.wishlist_present,
                        data.homepage.cart_present,
                    ].filter(Boolean).length
                    }
                />

                </section>

                <ProductOverview
                products={data.products}
                />

                <EvidenceSummary
                    homepage={data.homepage}
                />

                <ProductTable
                    products={data.products}
                />

            <section className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">

              <MetricCard
                title="Search"
                value={data.homepage.search_present ? "Yes" : "No"}
              />

              <MetricCard
                title="Wishlist"
                value={data.homepage.wishlist_present ? "Yes" : "No"}
              />

              <MetricCard
                title="Account"
                value={data.homepage.account_present ? "Yes" : "No"}
              />

              <MetricCard
                title="Cart"
                value={data.homepage.cart_present ? "Yes" : "No"}
              />

            </section>

            <section>

              <h2 className="mb-8 text-3xl font-bold">
                CRO Opportunities
              </h2>

              <div className="space-y-6">

                {data.audit.opportunities.map((item) => (
                  <OpportunityCard
                    key={item.title}
                    item={item}
                  />
                ))}

              </div>

            </section>

            <ScreenshotGallery
                screenshots={data.screenshots}
            />

          </main>
        )}

      </div>
    </AuroraBackground>
  );
}