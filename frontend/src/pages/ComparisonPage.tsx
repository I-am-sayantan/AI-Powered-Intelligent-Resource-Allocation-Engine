import { useEffect } from 'react';

import AlgorithmComparisonChart from '../charts/AlgorithmComparisonChart';
import Button from '../components/common/Button';
import Card from '../components/common/Card';
import Spinner from '../components/common/Spinner';
import Table from '../components/common/Table';
import type { Column } from '../components/common/Table';
import { useCompare } from '../hooks/useApi';
import type { AlgorithmComparisonRow } from '../types';
import { algorithmLabels, formatKm, formatMs, formatPercent } from '../utils/format';

export default function ComparisonPage() {
  const compare = useCompare();
  const { mutate } = compare;

  useEffect(() => {
    mutate();
  }, [mutate]);

  const result = compare.data;

  const columns: Column<AlgorithmComparisonRow>[] = [
    { key: 'algo', header: 'Algorithm', render: (r) => algorithmLabels[r.algorithm] ?? r.algorithm },
    { key: 'score', header: 'Total Score', render: (r) => r.total_score.toFixed(2) },
    { key: 'assigned', header: 'Assigned', render: (r) => r.assigned_count.toString() },
    { key: 'travel', header: 'Avg Travel', render: (r) => formatKm(r.avg_travel_km) },
    { key: 'util', header: 'Avg Utilization', render: (r) => formatPercent(r.avg_utilization) },
    { key: 'sla', header: 'SLA Met', render: (r) => `${r.sla_met_pct.toFixed(1)}%` },
    { key: 'runtime', header: 'Runtime', render: (r) => formatMs(r.runtime_ms) },
  ];

  return (
    <div className="space-y-6">
      <Card
        title="Algorithm Comparison"
        subtitle="Classical optimization vs ML/DL allocation"
        actions={
          <Button variant="secondary" onClick={() => mutate()} disabled={compare.isPending}>
            Re-run
          </Button>
        }
      >
        {result ? <AlgorithmComparisonChart rows={result.rows} /> : <Spinner label="Comparing…" />}
        {result && (
          <p className="mt-3 text-sm text-slate-500">
            Best algorithm:{' '}
            <span className="font-semibold text-brand">{algorithmLabels[result.best_algorithm]}</span>
          </p>
        )}
      </Card>

      <Card title="Details">
        {result ? (
          <Table columns={columns} rows={result.rows} getRowKey={(r) => r.algorithm} />
        ) : (
          <Spinner />
        )}
      </Card>
    </div>
  );
}
