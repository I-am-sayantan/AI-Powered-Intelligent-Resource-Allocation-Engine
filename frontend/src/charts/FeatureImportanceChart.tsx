import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

import type { FeatureImportance } from '../types';

export default function FeatureImportanceChart({ items }: { items: FeatureImportance[] }) {
  const data = [...items].sort((a, b) => b.importance - a.importance);

  return (
    <ResponsiveContainer width="100%" height={Math.max(280, data.length * 26)}>
      <BarChart data={data} layout="vertical" margin={{ left: 40, right: 16 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
        <XAxis type="number" tick={{ fontSize: 12 }} />
        <YAxis type="category" dataKey="feature" width={150} tick={{ fontSize: 11 }} />
        <Tooltip />
        <Bar dataKey="importance" name="Importance" fill="#7c3aed" radius={[0, 4, 4, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
}
