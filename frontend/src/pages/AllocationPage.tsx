import Button from '../components/common/Button';
import Card from '../components/common/Card';
import Spinner from '../components/common/Spinner';
import Table from '../components/common/Table';
import type { Column } from '../components/common/Table';
import AllocationMap from '../components/map/AllocationMap';
import { useAllocate, useRequests, useTechnicians } from '../hooks/useApi';
import { useAppStore } from '../store/appStore';
import type { AlgorithmType, Assignment } from '../types';
import { algorithmLabels, formatKm, formatMs, formatPercent } from '../utils/format';

const algorithms: AlgorithmType[] = ['greedy', 'hungarian', 'ml', 'dl'];

export default function AllocationPage() {
  const { algorithm, setAlgorithm } = useAppStore();
  const allocate = useAllocate();
  const technicians = useTechnicians();
  const requests = useRequests();
  const result = allocate.data;

  const columns: Column<Assignment>[] = [
    { key: 'tech', header: 'Technician', render: (a) => a.technician_id },
    { key: 'req', header: 'Request', render: (a) => a.request_id },
    { key: 'dist', header: 'Distance', render: (a) => formatKm(a.distance_km) },
    { key: 'success', header: 'Pred. Success', render: (a) => formatPercent(a.predicted_success) },
    { key: 'score', header: 'Score', render: (a) => a.score.toFixed(2) },
  ];

  return (
    <div className="space-y-6">
      <Card title="Run Allocation" subtitle="Select an algorithm and assign technicians to requests">
        <div className="flex flex-wrap items-center gap-2">
          {algorithms.map((option) => (
            <Button
              key={option}
              variant={option === algorithm ? 'primary' : 'secondary'}
              onClick={() => setAlgorithm(option)}
            >
              {algorithmLabels[option]}
            </Button>
          ))}
          <Button onClick={() => allocate.mutate(algorithm)} disabled={allocate.isPending}>
            {allocate.isPending ? 'Running…' : 'Allocate'}
          </Button>
        </div>
        {result && (
          <p className="mt-3 text-sm text-slate-500">
            Total score{' '}
            <span className="font-semibold text-slate-700">{result.total_score.toFixed(2)}</span> ·{' '}
            {result.assignments.length} assignments · {formatMs(result.runtime_ms)}
          </p>
        )}
      </Card>

      <div className="grid gap-6 lg:grid-cols-2">
        <Card title="Assignment Routes" className="h-[480px]">
          <div className="h-[392px]">
            {technicians.data && requests.data ? (
              <AllocationMap
                technicians={technicians.data}
                requests={requests.data}
                assignments={result?.assignments ?? []}
              />
            ) : (
              <Spinner label="Loading map…" />
            )}
          </div>
        </Card>

        <Card title="Assignments">
          {result ? (
            <Table columns={columns} rows={result.assignments} getRowKey={(a) => a.id} />
          ) : (
            <p className="text-sm text-slate-400">Run an allocation to see assignments.</p>
          )}
        </Card>
      </div>
    </div>
  );
}
