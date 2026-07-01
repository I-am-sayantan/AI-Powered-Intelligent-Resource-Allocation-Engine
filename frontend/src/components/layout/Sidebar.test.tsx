import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';

import Sidebar from './Sidebar';

describe('Sidebar', () => {
  it('renders all navigation links', () => {
    render(
      <MemoryRouter>
        <Sidebar />
      </MemoryRouter>,
    );

    expect(screen.getByText('Dashboard')).toBeInTheDocument();
    expect(screen.getByText('Allocation')).toBeInTheDocument();
    expect(screen.getByText('ML Models')).toBeInTheDocument();
    expect(screen.getByText('Comparison')).toBeInTheDocument();
    expect(screen.getByText('Explainability')).toBeInTheDocument();
  });
});
