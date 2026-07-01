import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

import type { ModelMetrics } from '../types';

export default function MetricsChart({ metrics }: { metrics: ModelMetrics }) {
  const data = [
    { name: 'Accuracy', value: Number(metrics.accuracy.toFixed(3)) },
    { name: 'Precision', value: Number(metrics.precision.toFixed(3)) },
    { name: 'Recall', value: Number(metrics.recall.toFixed(3)) },
    { name: 'F1', value: Number(metrics.f1.toFixed(3)) },
    { name: 'ROC-AUC', value: Number(metrics.roc_auc.toFixed(3)) },
  ];

  return (
    <ResponsiveContainer width="100%" height={280}>
      <BarChart data={data}>
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
        <XAxis dataKey="name" tick={{ fontSize: 12 }} />
        <YAxis domain={[0, 1]} tick={{ fontSize: 12 }} />
        <Tooltip />
        <Bar dataKey="value" name="Score" fill="#16a34a" radius={[4, 4, 0, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
}
