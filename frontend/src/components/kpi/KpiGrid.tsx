import type { KpiSummary } from '../../types';
import { formatKm, formatPercent } from '../../utils/format';

import KpiCard from './KpiCard';

export default function KpiGrid({ kpis }: { kpis: KpiSummary }) {
  const cards = [
    { label: 'Technicians', value: kpis.total_technicians.toString() },
    { label: 'Requests', value: kpis.total_requests.toString() },
    { label: 'Assignments', value: kpis.total_assignments.toString() },
    { label: 'Avg Utilization', value: formatPercent(kpis.avg_utilization) },
    { label: 'Avg Travel', value: formatKm(kpis.avg_travel_km) },
    { label: 'SLA Met', value: `${kpis.sla_met_pct.toFixed(1)}%` },
    { label: 'Pred. Success', value: formatPercent(kpis.avg_predicted_success) },
    { label: 'Satisfaction', value: `${kpis.customer_satisfaction.toFixed(1)}/5` },
  ];

  return (
    <div className="grid grid-cols-2 gap-4 md:grid-cols-4">
      {cards.map((card) => (
        <KpiCard key={card.label} label={card.label} value={card.value} />
      ))}
    </div>
  );
}
