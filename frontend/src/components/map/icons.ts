import * as L from 'leaflet';

/** Build a small circular DivIcon so we avoid bundler image-path issues. */
function dotIcon(color: string, glyph: string): L.DivIcon {
  return L.divIcon({
    className: 'realc-marker',
    html:
      `<span style="display:flex;align-items:center;justify-content:center;` +
      `width:26px;height:26px;border-radius:9999px;background:${color};` +
      `color:#fff;font-size:13px;box-shadow:0 1px 4px rgba(0,0,0,.3)">${glyph}</span>`,
    iconSize: [26, 26],
    iconAnchor: [13, 13],
    popupAnchor: [0, -13],
  });
}

export const technicianIcon = dotIcon('#2563eb', '\u{1F527}'); // wrench
export const requestIcon = dotIcon('#dc2626', '\u{1F4CD}'); // round pin
