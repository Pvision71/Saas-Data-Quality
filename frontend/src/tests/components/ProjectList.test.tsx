import { render, screen } from '@testing-library/react';
import ProjectList from '../../components/ProjectList'; // This component doesn't exist yet

it('renders a list of projects', () => {
  const projects = [
    { id: '1', name: 'Project 1' },
    { id: '2', name: 'Project 2' },
  ];
  render(<ProjectList projects={projects} />);
  
  const project1 = screen.getByText('Project 1');
  const project2 = screen.getByText('Project 2');

  expect(project1).toBeInTheDocument();
  expect(project2).toBeInTheDocument();
});
