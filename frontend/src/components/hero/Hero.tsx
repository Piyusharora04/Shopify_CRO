import { Sparkles } from "lucide-react";

interface HeroProps {
  url: string;
  setUrl: React.Dispatch<React.SetStateAction<string>>;
  onAnalyze: () => void;
  loading: boolean;
}

export default function Hero({
  url,
  setUrl,
  onAnalyze,
  loading,
}: HeroProps) {
  return (
    <section className="relative z-10 mx-auto mt-16 max-w-6xl px-6">
      <div className="rounded-[32px] border border-white/10 bg-white/5 p-12 backdrop-blur-2xl">

        <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-emerald-500/20 bg-emerald-500/10 px-4 py-2 text-sm text-emerald-300">
          <Sparkles size={16} />
          AI Powered CRO Intelligence
        </div>

        <h1 className="max-w-4xl text-6xl font-bold leading-tight tracking-tight">
          Find Revenue Opportunities Hidden Inside Any Shopify Store
        </h1>

        <p className="mt-8 max-w-3xl text-lg leading-8 text-zinc-400">
          Analyze homepage experience, product pages, merchandising,
          conversion funnel and receive prioritized CRO recommendations
          backed by real evidence.
        </p>

        <div className="mt-12 flex flex-col gap-4 lg:flex-row">

          <input
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://gymshark.com"
            className="h-16 flex-1 rounded-2xl border border-white/10 bg-white/5 px-6 text-lg outline-none transition focus:border-emerald-400"
          />

          <button
            onClick={onAnalyze}
            disabled={loading}
            className="h-16 rounded-2xl bg-emerald-400 px-10 font-semibold text-black transition hover:scale-[1.02] disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? "Analyzing..." : "Analyze Store"}
          </button>

        </div>

        <div className="mt-8 flex flex-wrap gap-3">

          {[
            "Homepage",
            "Product Pages",
            "Cart",
            "Navigation",
            "Trust Signals",
          ].map((item) => (
            <span
              key={item}
              className="rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-zinc-300"
            >
              {item}
            </span>
          ))}

        </div>

      </div>
    </section>
  );
}