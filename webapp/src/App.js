import React from 'react';
import Sidebar from './Sidebar.js'; // Assuming Sidebar is in the same directory
import MainDashboard from './MainDashboard.js'; // Assuming MainDashboard is in the same directory
import './App.css'; // Main CSS for the app layout

function App() {
  return (
    <div className="app-container">
      <Sidebar />
      <MainDashboard />
    </div>
  );
}

export default App;
