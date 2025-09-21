import { render, screen } from '@testing-library/react';
import ProjectList from '../../src/components/ProjectList';

describe('ProjectList', () => {
  it('renders a list of projects correctly', () => {
    const projects = [
      { id: '1', name: 'Test Project 1' },
      { id: '2', name: 'Test Project 2' },
    ];

    render(<ProjectList projects={projects} />);

    expect(screen.getByText('Projects')).toBeInTheDocument();
    expect(screen.getByText('Test Project 1')).toBeInTheDocument();
    expect(screen.getByText('Test Project 2')).toBeInTheDocument();
  });

  it('renders no projects when the list is empty', () => {
    render(<ProjectList projects={[]} />);
    expect(screen.getByText('Projects')).toBeInTheDocument();
    expect(screen.queryByRole('listitem')).not.toBeInTheDocument();
  });
});
