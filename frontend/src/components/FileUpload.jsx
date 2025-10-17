import React, { useState, useCallback } from 'react';

const FileUpload = ({ onFileRead, disabled }) => {
  const [isDragging, setIsDragging] = useState(false);
  const [fileName, setFileName] = useState('');
  const [uploading, setUploading] = useState(false);

  const handleDragEnter = useCallback((e) => {
    e.preventDefault();
    e.stopPropagation();
    if (!disabled) setIsDragging(true);
  }, [disabled]);

  const handleDragLeave = useCallback((e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  }, []);

  const handleDragOver = useCallback((e) => {
    e.preventDefault();
    e.stopPropagation();
  }, []);

  const processFile = async (file) => {
    setUploading(true);
    setFileName(file.name);

    try {
      const fileExtension = file.name.split('.').pop().toLowerCase();

      if (fileExtension === 'txt') {
        // Read text file
        const text = await file.text();
        onFileRead(text);
      } else if (fileExtension === 'pdf') {
        // For PDF, we'll use a basic text extraction approach
        // Note: This requires pdfjs-dist package
        try {
          const pdfjsLib = await import('pdfjs-dist/build/pdf');
          pdfjsLib.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js`;

          const arrayBuffer = await file.arrayBuffer();
          const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
          
          let fullText = '';
          for (let i = 1; i <= pdf.numPages; i++) {
            const page = await pdf.getPage(i);
            const textContent = await page.getTextContent();
            const pageText = textContent.items.map(item => item.str).join(' ');
            fullText += pageText + '\n\n';
          }
          
          onFileRead(fullText.trim());
        } catch (error) {
          console.error('PDF parsing error:', error);
          alert('Error reading PDF. Please copy and paste the text instead.');
        }
      } else if (fileExtension === 'docx') {
        // For DOCX, we'll use mammoth
        try {
          const mammoth = await import('mammoth');
          const arrayBuffer = await file.arrayBuffer();
          const result = await mammoth.extractRawText({ arrayBuffer });
          onFileRead(result.value);
        } catch (error) {
          console.error('DOCX parsing error:', error);
          alert('Error reading DOCX. Please copy and paste the text instead.');
        }
      } else {
        alert('Unsupported file type. Please use TXT, PDF, or DOCX files.');
      }
    } catch (error) {
      console.error('File processing error:', error);
      alert('Error reading file. Please try again or copy and paste the text.');
    } finally {
      setUploading(false);
    }
  };

  const handleDrop = useCallback(
    (e) => {
      e.preventDefault();
      e.stopPropagation();
      setIsDragging(false);

      if (disabled) return;

      const files = e.dataTransfer.files;
      if (files && files.length > 0) {
        processFile(files[0]);
      }
    },
    [disabled, onFileRead]
  );

  const handleFileInput = (e) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      processFile(files[0]);
    }
  };

  return (
    <div className="mb-4">
      <div
        onDragEnter={handleDragEnter}
        onDragLeave={handleDragLeave}
        onDragOver={handleDragOver}
        onDrop={handleDrop}
        className={`
          border-2 border-dashed rounded-lg p-6 text-center transition-all duration-200
          ${isDragging ? 'border-primary-500 bg-primary-50' : 'border-gray-300 bg-gray-50'}
          ${disabled ? 'opacity-50 cursor-not-allowed' : 'hover:border-primary-400 cursor-pointer'}
        `}
      >
        <input
          type="file"
          id="file-upload"
          className="hidden"
          accept=".txt,.pdf,.docx"
          onChange={handleFileInput}
          disabled={disabled || uploading}
        />
        
        <label
          htmlFor="file-upload"
          className={`flex flex-col items-center ${disabled ? 'cursor-not-allowed' : 'cursor-pointer'}`}
        >
          {uploading ? (
            <>
              <div className="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin mb-3"></div>
              <p className="text-sm text-gray-600">Processing {fileName}...</p>
            </>
          ) : (
            <>
              <svg
                className="w-12 h-12 text-gray-400 mb-3"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                />
              </svg>
              
              <p className="text-sm font-medium text-gray-700 mb-1">
                {fileName ? fileName : 'Drop your resume here or click to browse'}
              </p>
              
              <p className="text-xs text-gray-500">
                Supports: TXT, PDF, DOCX (max 10MB)
              </p>
            </>
          )}
        </label>
      </div>
      
      {fileName && !uploading && (
        <div className="mt-2 flex items-center justify-between text-sm">
          <span className="text-green-600 flex items-center">
            <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
            </svg>
            File loaded successfully
          </span>
          <button
            onClick={() => setFileName('')}
            className="text-gray-500 hover:text-gray-700"
          >
            Clear
          </button>
        </div>
      )}
    </div>
  );
};

export default FileUpload;

