import { useState } from 'react';
import { tailorResume } from './services/api';
import InputSection from './components/InputSection';
import ResultsSection from './components/ResultsSection';
import Header from './components/Header';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorAlert from './components/ErrorAlert';

function App() {
  const [resumeText, setResumeText] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleTailorResume = async () => {
    // Validation
    if (!resumeText.trim()) {
      setError('Please enter your resume text');
      return;
    }
    
    if (!jobDescription.trim()) {
      setError('Please enter the job description');
      return;
    }

    if (resumeText.length < 50) {
      setError('Resume text must be at least 50 characters long');
      return;
    }

    if (jobDescription.length < 50) {
      setError('Job description must be at least 50 characters long');
      return;
    }

    // Reset states
    setError(null);
    setResults(null);
    setLoading(true);

    try {
      const data = await tailorResume({
        resume_text: resumeText,
        job_description: jobDescription,
      });
      
      setResults(data);
    } catch (err) {
      console.error('Error tailoring resume:', err);
      
      let errorMessage = 'An unexpected error occurred. Please try again.';
      
      if (err.response) {
        // Server responded with error
        errorMessage = err.response.data?.detail || err.response.data?.error || errorMessage;
      } else if (err.request) {
        // Request made but no response
        errorMessage = 'Unable to connect to the server. Make sure the backend is running on http://localhost:8000';
      } else {
        // Something else happened
        errorMessage = err.message;
      }
      
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setResumeText('');
    setJobDescription('');
    setResults(null);
    setError(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <Header />
      
      <main className="container mx-auto px-4 py-8 max-w-7xl">
        {/* Error Alert */}
        {error && <ErrorAlert message={error} onClose={() => setError(null)} />}
        
        {/* Input Section */}
        <InputSection
          resumeText={resumeText}
          setResumeText={setResumeText}
          jobDescription={jobDescription}
          setJobDescription={setJobDescription}
          onTailor={handleTailorResume}
          onClear={handleClear}
          loading={loading}
        />

        {/* Loading Spinner */}
        {loading && <LoadingSpinner />}

        {/* Results Section */}
        {results && !loading && <ResultsSection results={results} />}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-16">
        <div className="container mx-auto px-4 py-6 text-center text-gray-600">
          <p className="text-sm">
            Powered by{' '}
            <span className="font-semibold text-primary-600">FastAPI</span>,{' '}
            <span className="font-semibold text-primary-600">LangGraph</span>, and{' '}
            <span className="font-semibold text-primary-600">Groq API</span>
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;

