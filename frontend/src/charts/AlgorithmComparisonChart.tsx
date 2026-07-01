import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

import type { AlgorithmComparisonRow } from '../types';
import { algorithmLabels } from '../utils/format';

export default function AlgorithmComparisonChart({ rows }: { rows: AlgorithmComparisonRow[] }) {
  const data = rows.map((row) => ({
    name: algorithmLabels[row.algorithm] ?? row.algorithm,
    score: Number(row.total_score.toFixed(2)),
    sla: Number(row.sla_met_pct.toFixed(1)),
  }));

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
        <XAxis dataKey="name" tick={{ fontSize: 12 }} />
        <YAxis tick={{ fontSize: 12 }} />
        <Tooltip />
        <Legend />
        <Bar dataKey="score" name="Total Score" fill="#2563eb" radius={[4, 4, 0, 0]} />
        <Bar dataKey="sla" name="SLA Met %" fill="#16a34a" radius={[4, 4, 0, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
}
