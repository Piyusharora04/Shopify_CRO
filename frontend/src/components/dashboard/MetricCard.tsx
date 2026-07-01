interface MetricCardProps {
  title: string;
  value: string | number;
}

export default function MetricCard({
  title,
  value,
}: MetricCardProps) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur-3xl">
      <p className="text-sm text-zinc-400">
        {title}
      </p>

      <h3 className="mt-4 text-3xl font-bold">
        {value}
      </h3>
    </div>
  );
}