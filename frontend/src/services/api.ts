const API_BASE_URL = 'http://localhost:8000'; // Replace with your backend API URL

interface Project {
  id: string;
  name: string;
}

const api = {
  getProjects: async (): Promise<Project[]> => {
    const response = await fetch(`${API_BASE_URL}/projects`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  },
};

export default api;
