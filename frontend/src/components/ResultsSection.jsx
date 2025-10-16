import React, { useState } from 'react';

const ResultsSection = ({ results }) => {
  const [copied, setCopied] = useState(false);

  const handleCopyResume = () => {
    navigator.clipboard.writeText(results.tailored_resume);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="space-y-6 animate-fadeIn">
      <div className="text-center">
        <h2 className="text-2xl font-bold text-gray-900">Results</h2>
        <p className="text-gray-600 mt-1">Your resume has been optimized for the job</p>
      </div>

      {/* Professional Summary */}
      <div className="card border-l-4 border-primary-500">
        <h3 className="text-xl font-semibold text-gray-900 mb-3 flex items-center">
          <svg className="w-6 h-6 mr-2 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          Professional Summary
        </h3>
        <p className="text-gray-700 leading-relaxed bg-primary-50 p-4 rounded-lg">
          {results.summary}
        </p>
      </div>

      {/* Skills Analysis */}
      <div className="grid md:grid-cols-2 gap-6">
        {/* Matched Skills */}
        <div className="card border-l-4 border-green-500">
          <h3 className="text-lg font-semibold text-gray-900 mb-3 flex items-center">
            <svg className="w-5 h-5 mr-2 text-green-600" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
            </svg>
            Matched Skills ({results.matched_skills.length})
          </h3>
          <div className="flex flex-wrap gap-2">
            {results.matched_skills.length > 0 ? (
              results.matched_skills.map((skill, index) => (
                <span key={index} className="badge-success">
                  {skill}
                </span>
              ))
            ) : (
              <p className="text-gray-500 text-sm">No matched skills found</p>
            )}
          </div>
        </div>

        {/* Missing Skills */}
        <div className="card border-l-4 border-amber-500">
          <h3 className="text-lg font-semibold text-gray-900 mb-3 flex items-center">
            <svg className="w-5 h-5 mr-2 text-amber-600" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
            </svg>
            Skills to Develop ({results.missing_skills.length})
          </h3>
          <div className="flex flex-wrap gap-2">
            {results.missing_skills.length > 0 ? (
              results.missing_skills.map((skill, index) => (
                <span key={index} className="badge-warning">
                  {skill}
                </span>
              ))
            ) : (
              <p className="text-gray-500 text-sm">You have all required skills!</p>
            )}
          </div>
        </div>
      </div>

      {/* Tailored Resume */}
      <div className="card">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-xl font-semibold text-gray-900 flex items-center">
            <svg className="w-6 h-6 mr-2 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            Tailored Resume
          </h3>
          <button
            onClick={handleCopyResume}
            className="flex items-center space-x-2 bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded-lg transition-colors duration-200"
          >
            {copied ? (
              <>
                <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                <span className="text-sm font-medium">Copied!</span>
              </>
            ) : (
              <>
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                <span className="text-sm font-medium">Copy</span>
              </>
            )}
          </button>
        </div>
        <div className="bg-gray-50 p-6 rounded-lg border border-gray-200 max-h-96 overflow-y-auto">
          <pre className="whitespace-pre-wrap font-mono text-sm text-gray-800 leading-relaxed">
            {results.tailored_resume}
          </pre>
        </div>
      </div>
    </div>
  );
};

export default ResultsSection;

