import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import CaseListPage from './pages/CaseListPage';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<CaseListPage />} />
        {/* Add more routes as needed */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;