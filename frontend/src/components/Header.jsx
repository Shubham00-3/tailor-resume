import React from 'react';

const Header = () => {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4 py-6 max-w-7xl">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">
              Resume Tailor AI
            </h1>
            <p className="text-gray-600 mt-1">
              Optimize your resume for any job description using AI
            </p>
          </div>
          
          <div className="hidden md:flex items-center space-x-2">
            <div className="flex items-center space-x-2 bg-green-50 text-green-700 px-4 py-2 rounded-lg">
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              <span className="text-sm font-medium">API Ready</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;

