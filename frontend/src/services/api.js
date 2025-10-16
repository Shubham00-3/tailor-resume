import axios from 'axios';

// Create axios instance with base configuration
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  timeout: 60000, // 60 seconds (API can take time for LLM processing)
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
api.interceptors.request.use(
  (config) => {
    console.log('API Request:', config.method?.toUpperCase(), config.url);
    return config;
  },
  (error) => {
    console.error('Request Error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    console.log('API Response:', response.status, response.config.url);
    return response;
  },
  (error) => {
    console.error('Response Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

/**
 * Check API health status
 * @returns {Promise<{status: string}>}
 */
export const checkHealth = async () => {
  const response = await api.get('/health');
  return response.data;
};

/**
 * Tailor resume to job description
 * @param {Object} data
 * @param {string} data.resume_text - The original resume text
 * @param {string} data.job_description - The target job description
 * @returns {Promise<Object>} Tailored resume data
 */
export const tailorResume = async ({ resume_text, job_description }) => {
  const response = await api.post('/tailor', {
    resume_text,
    job_description,
  });
  return response.data;
};

export default api;

