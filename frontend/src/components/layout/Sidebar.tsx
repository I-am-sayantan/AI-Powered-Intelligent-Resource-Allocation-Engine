import { NavLink } from 'react-router-dom';

const links = [
  { to: '/', label: 'Dashboard', end: true },
  { to: '/allocation', label: 'Allocation' },
  { to: '/models', label: 'ML Models' },
  { to: '/comparison', label: 'Comparison' },
  { to: '/explainability', label: 'Explainability' },
];

export default function Sidebar() {
  return (
    <aside className="flex w-60 shrink-0 flex-col border-r border-slate-200 bg-white p-4">
      <div className="mb-6 px-2">
        <p className="text-lg font-bold text-brand">RE&middot;ALC</p>
        <p className="text-xs text-slate-400">Resource Allocation</p>
      </div>
      <nav className="flex flex-col gap-1">
        {links.map((link) => (
          <NavLink
            key={link.to}
            to={link.to}
            end={link.end}
            className={({ isActive }) =>
              `rounded-lg px-3 py-2 text-sm font-medium transition ${
                isActive ? 'bg-brand text-white' : 'text-slate-600 hover:bg-slate-100'
              }`
            }
          >
            {link.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
