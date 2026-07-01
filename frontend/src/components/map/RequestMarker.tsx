import { Marker, Popup } from 'react-leaflet';

import type { ServiceRequest } from '../../types';

import { requestIcon } from './icons';

export default function RequestMarker({ request }: { request: ServiceRequest }) {
  return (
    <Marker position={[request.location.lat, request.location.lon]} icon={requestIcon}>
      <Popup>
        <div className="text-xs">
          <p className="font-semibold">{request.customer_name}</p>
          <p>Skill: {request.required_skill}</p>
          <p>Priority: {request.priority}/5</p>
          <p>Status: {request.status}</p>
        </div>
      </Popup>
    </Marker>
  );
}
