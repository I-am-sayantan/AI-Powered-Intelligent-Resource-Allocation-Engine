import type { FeatureContribution } from '../../types';

interface ExplanationPanelProps {
  score: number;
  contributions: FeatureContribution[];
}

export default function ExplanationPanel({ score, contributions }: ExplanationPanelProps) {
  const maxContribution = Math.max(...contributions.map((c) => Math.abs(c.contribution)), 1);

  return (
    <div>
      <div className="mb-4 flex items-baseline gap-2">
        <span className="text-3xl font-bold text-brand">{(score * 100).toFixed(0)}%</span>
        <span className="text-sm text-slate-400">assignment score</span>
      </div>
      <ul className="space-y-2">
        {contributions.map((contribution) => (
          <li key={contribution.feature}>
            <div className="flex justify-between text-xs text-slate-600">
              <span className="capitalize">{contribution.feature}</span>
              <span>{(contribution.contribution * 100).toFixed(0)}%</span>
            </div>
            <div className="mt-1 h-2 rounded bg-slate-100">
              <div
                className="h-2 rounded bg-brand"
                style={{ width: `${(Math.abs(contribution.contribution) / maxContribution) * 100}%` }}
              />
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
