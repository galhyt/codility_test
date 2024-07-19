// src/App.js
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Scoreboard from './Scoreboard';

function App() {
  const [token, setToken] = useState(null);

  return (
  <Router>
      <Routes>
          <Route path="/" element={!token ? <Login setToken={setToken} /> : <Scoreboard token={token} />} />
      </Routes>
    </Router>
  );
}

export default App;
