import { Marker, Popup } from 'react-leaflet';

import type { Technician } from '../../types';

import { technicianIcon } from './icons';

export default function TechnicianMarker({ technician }: { technician: Technician }) {
  return (
    <Marker position={[technician.location.lat, technician.location.lon]} icon={technicianIcon}>
      <Popup>
        <div className="text-xs">
          <p className="font-semibold">{technician.name}</p>
          <p>Skills: {technician.skills.join(', ')}</p>
          <p>Utilization: {(technician.utilization * 100).toFixed(0)}%</p>
          <p>Rating: {technician.customer_rating.toFixed(1)}/5</p>
        </div>
      </Popup>
    </Marker>
  );
}
