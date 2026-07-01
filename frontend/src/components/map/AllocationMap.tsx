import { MapContainer, TileLayer } from 'react-leaflet';

import type { Assignment, ServiceRequest, Technician } from '../../types';

import RequestMarker from './RequestMarker';
import RouteLayer from './RouteLayer';
import TechnicianMarker from './TechnicianMarker';

interface AllocationMapProps {
  technicians: Technician[];
  requests: ServiceRequest[];
  assignments?: Assignment[];
  center?: [number, number];
  zoom?: number;
}

export default function AllocationMap({
  technicians,
  requests,
  assignments = [],
  center = [37.7749, -122.4194],
  zoom = 12,
}: AllocationMapProps) {
  return (
    <MapContainer center={center} zoom={zoom} scrollWheelZoom className="h-full w-full rounded-xl">
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <RouteLayer assignments={assignments} technicians={technicians} requests={requests} />
      {technicians.map((technician) => (
        <TechnicianMarker key={technician.id} technician={technician} />
      ))}
      {requests.map((request) => (
        <RequestMarker key={request.id} request={request} />
      ))}
    </MapContainer>
  );
}
