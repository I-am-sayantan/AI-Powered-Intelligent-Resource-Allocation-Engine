import type { ReactNode } from 'react';

interface CardProps {
  title?: string;
  subtitle?: string;
  actions?: ReactNode;
  className?: string;
  children: ReactNode;
}

export default function Card({ title, subtitle, actions, className = '', children }: CardProps) {
  return (
    <div className={`rounded-xl bg-white p-5 shadow-sm ring-1 ring-slate-200 ${className}`}>
      {(title || actions) && (
        <div className="mb-4 flex items-start justify-between gap-4">
          <div>
            {title && <h3 className="text-sm font-semibold text-slate-700">{title}</h3>}
            {subtitle && <p className="text-xs text-slate-400">{subtitle}</p>}
          </div>
          {actions}
        </div>
      )}
      {children}
    </div>
  );
}
