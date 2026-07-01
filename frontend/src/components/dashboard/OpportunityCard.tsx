import type { Recommendation } from "../../types/audit";

interface OpportunityCardProps {
  item: Recommendation;
}

export default function OpportunityCard({
  item,
}: OpportunityCardProps) {
  return (
    <div className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-3xl">

      <div className="flex items-start justify-between">

        <div>

          <h2 className="text-2xl font-semibold">
            {item.title}
          </h2>

          <p className="mt-3 text-zinc-400">
            {item.evidence}
          </p>

        </div>

        <div className="flex gap-3">

          <Badge
            title="Impact"
            value={item.impact}
          />

          <Badge
            title="Confidence"
            value={item.confidence}
          />

          <Badge
            title="Effort"
            value={item.effort}
          />

        </div>

      </div>

      <div className="mt-8">

        <h4 className="font-semibold">
          Recommendation
        </h4>

        <p className="mt-3 text-zinc-300">
          {item.recommendation}
        </p>

      </div>

      <div className="mt-8 rounded-2xl border border-emerald-500/20 bg-emerald-500/10 p-6">

        <h4 className="font-semibold text-emerald-300">
          Experiment Brief
        </h4>

        <p className="mt-4">
          {item.experiment.hypothesis}
        </p>

        <div className="mt-5 flex gap-8 text-sm text-zinc-300">

          <span>
            Metric :
            {" "}
            {item.experiment.primary_metric}
          </span>

          <span>
            Duration :
            {" "}
            {item.experiment.duration}
          </span>

        </div>

      </div>

    </div>
  );
}

function Badge({
  title,
  value,
}: {
  title: string;
  value: number;
}) {
  return (
    <div className="rounded-xl bg-black/20 px-4 py-3 text-center">

      <p className="text-xs text-zinc-400">
        {title}
      </p>

      <h3 className="mt-1 text-xl font-bold">
        {value}
      </h3>

    </div>
  );
}