import { render, screen, waitFor } from '@testing-library/react';
import Dashboard from '../../pages/dashboard'; // This page doesn't exist yet
import api from '../../services/api';

jest.mock('../../services/api');

it('fetches and displays projects on the dashboard', async () => {
  const mockProjects = [
    { id: '1', name: 'Project Alpha' },
    { id: '2', name: 'Project Beta' },
  ];
  api.getProjects.mockResolvedValue(mockProjects);

  render(<Dashboard />);

  await waitFor(() => {
    expect(screen.getByText('Project Alpha')).toBeInTheDocument();
    expect(screen.getByText('Project Beta')).toBeInTheDocument();
  });
});
