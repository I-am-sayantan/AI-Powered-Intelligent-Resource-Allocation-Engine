interface KpiCardProps {
  label: string;
  value: string;
  hint?: string;
  accent?: string;
}

export default function KpiCard({ label, value, hint, accent = 'text-brand' }: KpiCardProps) {
  return (
    <div className="rounded-xl bg-white p-4 shadow-sm ring-1 ring-slate-200">
      <p className="text-xs font-medium uppercase tracking-wide text-slate-400">{label}</p>
      <p className={`mt-2 text-2xl font-bold ${accent}`}>{value}</p>
      {hint && <p className="mt-1 text-xs text-slate-400">{hint}</p>}
    </div>
  );
}
