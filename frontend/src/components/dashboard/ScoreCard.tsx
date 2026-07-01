import { motion } from "framer-motion";

interface ScoreCardProps {
  score: number;
  report: string;
}

export default function ScoreCard({
  score,
  report,
}: ScoreCardProps) {
  const color =
    score >= 80
      ? "text-emerald-400"
      : score >= 60
      ? "text-yellow-400"
      : "text-red-400";

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-3xl"
    >
      <p className="text-sm uppercase tracking-widest text-zinc-400">
        Overall CRO Score
      </p>

      <h1 className={`mt-5 text-7xl font-bold ${color}`}>
        {score}
      </h1>

      <a
        href={`http://127.0.0.1:8000${report}`}
        target="_blank"
        rel="noreferrer"
        className="mt-6 inline-flex rounded-xl bg-emerald-500 px-5 py-3 font-semibold text-black hover:bg-emerald-400"
    >
        Download PDF Report
    </a>

      <div className="mt-8 h-3 overflow-hidden rounded-full bg-white/10">
        <motion.div
          initial={{ width: 0 }}
          animate={{
            width: `${score}%`,
          }}
          transition={{
            duration: 1.2,
          }}
          className="h-full rounded-full bg-emerald-400"
        />
      </div>

      <p className="mt-4 text-zinc-400">
        Based on homepage, product pages and
        merchandising signals.
      </p>
    </motion.div>
  );
}