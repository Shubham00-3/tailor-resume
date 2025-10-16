import React from 'react';

const InputSection = ({
  resumeText,
  setResumeText,
  jobDescription,
  setJobDescription,
  onTailor,
  onClear,
  loading,
}) => {
  return (
    <div className="grid md:grid-cols-2 gap-6 mb-8">
      {/* Resume Input */}
      <div className="card">
        <label htmlFor="resume" className="block text-lg font-semibold text-gray-900 mb-3">
          Your Resume
        </label>
        <textarea
          id="resume"
          className="textarea-field"
          rows="12"
          placeholder="Paste your resume here...

Example:
John Doe
Software Engineer

Experience:
- 5 years in Python development
- Built REST APIs with FastAPI
- Worked with PostgreSQL databases..."
          value={resumeText}
          onChange={(e) => setResumeText(e.target.value)}
          disabled={loading}
        />
        <p className="text-sm text-gray-500 mt-2">
          {resumeText.length} characters
          {resumeText.length > 0 && resumeText.length < 50 && (
            <span className="text-amber-600 ml-2">
              (minimum 50 characters required)
            </span>
          )}
        </p>
      </div>

      {/* Job Description Input */}
      <div className="card">
        <label htmlFor="jobDescription" className="block text-lg font-semibold text-gray-900 mb-3">
          Job Description
        </label>
        <textarea
          id="jobDescription"
          className="textarea-field"
          rows="12"
          placeholder="Paste the job description here...

Example:
Senior Python Developer

Requirements:
- 5+ years of Python experience
- FastAPI or Django expertise
- PostgreSQL knowledge
- Docker and Kubernetes
- Cloud deployment (AWS/GCP)..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          disabled={loading}
        />
        <p className="text-sm text-gray-500 mt-2">
          {jobDescription.length} characters
          {jobDescription.length > 0 && jobDescription.length < 50 && (
            <span className="text-amber-600 ml-2">
              (minimum 50 characters required)
            </span>
          )}
        </p>
      </div>

      {/* Action Buttons */}
      <div className="md:col-span-2 flex flex-col sm:flex-row gap-4 justify-center">
        <button
          onClick={onTailor}
          disabled={loading || resumeText.length < 50 || jobDescription.length < 50}
          className="btn-primary flex items-center justify-center space-x-2 text-lg"
        >
          {loading ? (
            <>
              <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              <span>Tailoring Resume...</span>
            </>
          ) : (
            <>
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              <span>Tailor Resume</span>
            </>
          )}
        </button>

        <button
          onClick={onClear}
          disabled={loading}
          className="bg-gray-200 hover:bg-gray-300 text-gray-700 font-semibold py-3 px-6 rounded-lg transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Clear All
        </button>
      </div>
    </div>
  );
};

export default InputSection;

