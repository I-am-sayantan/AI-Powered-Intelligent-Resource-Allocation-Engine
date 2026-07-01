import { render, screen } from '@testing-library/react';

import KpiCard from './KpiCard';

describe('KpiCard', () => {
  it('renders the label, value, and hint', () => {
    render(<KpiCard label="Technicians" value="12" hint="active today" />);

    expect(screen.getByText('Technicians')).toBeInTheDocument();
    expect(screen.getByText('12')).toBeInTheDocument();
    expect(screen.getByText('active today')).toBeInTheDocument();
  });

  it('omits the hint when not provided', () => {
    render(<KpiCard label="Requests" value="8" />);

    expect(screen.getByText('Requests')).toBeInTheDocument();
    expect(screen.queryByText('active today')).not.toBeInTheDocument();
  });
});
