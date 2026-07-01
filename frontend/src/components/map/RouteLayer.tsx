import { Polyline } from 'react-leaflet';

import type { Assignment, ServiceRequest, Technician } from '../../types';

interface RouteLayerProps {
  assignments: Assignment[];
  technicians: Technician[];
  requests: ServiceRequest[];
}

/** Draws a dashed line from each assigned technician to its request. */
export default function RouteLayer({ assignments, technicians, requests }: RouteLayerProps) {
  const techById = new Map(technicians.map((t) => [t.id, t]));
  const reqById = new Map(requests.map((r) => [r.id, r]));

  return (
    <>
      {assignments.map((assignment) => {
        const tech = techById.get(assignment.technician_id);
        const req = reqById.get(assignment.request_id);
        if (!tech || !req) {
          return null;
        }
        return (
          <Polyline
            key={assignment.id}
            positions={[
              [tech.location.lat, tech.location.lon],
              [req.location.lat, req.location.lon],
            ]}
            pathOptions={{ color: '#2563eb', weight: 2, opacity: 0.6, dashArray: '4 6' }}
          />
        );
      })}
    </>
  );
}
