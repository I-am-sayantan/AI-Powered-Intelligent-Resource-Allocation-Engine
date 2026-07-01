import Card from '../components/common/Card';
import Spinner from '../components/common/Spinner';
import KpiGrid from '../components/kpi/KpiGrid';
import AllocationMap from '../components/map/AllocationMap';
import { useAssignments, useMetrics, useRequests, useTechnicians } from '../hooks/useApi';

export default function DashboardPage() {
  const metrics = useMetrics();
  const technicians = useTechnicians();
  const requests = useRequests();
  const assignments = useAssignments();

  return (
    <div className="space-y-6">
      {metrics.isLoading || !metrics.data ? (
        <Spinner label="Loading KPIs…" />
      ) : (
        <KpiGrid kpis={metrics.data.kpis} />
      )}

      <Card
        title="Live Allocation Map"
        subtitle="Technicians, service requests, and assignment routes"
        className="h-[540px]"
      >
        <div className="h-[452px]">
          {technicians.data && requests.data ? (
            <AllocationMap
              technicians={technicians.data}
              requests={requests.data}
              assignments={assignments.data ?? []}
            />
          ) : (
            <Spinner label="Loading map…" />
          )}
        </div>
      </Card>
    </div>
  );
}
