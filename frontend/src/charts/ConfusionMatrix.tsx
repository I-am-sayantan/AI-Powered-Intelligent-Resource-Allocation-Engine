import type { ConfusionMatrix as ConfusionMatrixData } from '../types';

export default function ConfusionMatrix({ matrix }: { matrix: ConfusionMatrixData }) {
  const cells = [
    { label: 'True Negative', value: matrix.true_negative, tone: 'bg-emerald-100 text-emerald-700' },
    { label: 'False Positive', value: matrix.false_positive, tone: 'bg-rose-100 text-rose-700' },
    { label: 'False Negative', value: matrix.false_negative, tone: 'bg-rose-100 text-rose-700' },
    { label: 'True Positive', value: matrix.true_positive, tone: 'bg-emerald-100 text-emerald-700' },
  ];

  return (
    <div className="grid grid-cols-2 gap-2">
      {cells.map((cell) => (
        <div key={cell.label} className={`rounded-lg p-4 text-center ${cell.tone}`}>
          <p className="text-2xl font-bold">{cell.value}</p>
          <p className="text-xs">{cell.label}</p>
        </div>
      ))}
    </div>
  );
}
