import { Sparkles } from "lucide-react";

export default function Navbar() {
  return (
    <header className="mx-auto flex w-full max-w-7xl items-center justify-between px-8 py-8">
      <div className="flex items-center gap-3">
        <div className="flex h-11 w-11 items-center justify-center rounded-2xl border border-white/10 bg-white/5 backdrop-blur-xl">
          <Sparkles className="h-5 w-5 text-emerald-400" />
        </div>

        <div>
          <p className="font-semibold tracking-tight">
            CRO Intelligence
          </p>

          <p className="text-sm text-zinc-500">
            Shopify CRO Opportunity Engine
          </p>
        </div>
      </div>

      <div className="rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-zinc-400 backdrop-blur-xl">
        AI Powered
      </div>
    </header>
  );
}