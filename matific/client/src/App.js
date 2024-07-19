// src/App.js
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Scoreboard from './Scoreboard';
import TeamPlayers from './TeamPlayers';

function App() {
  const [token, setToken] = useState(null);

  return (
  <Router>
      <Routes>
          <Route path="/" element={!token ? <Login setToken={setToken} /> : <Scoreboard token={token} />} />
          <Route path="/team_players/:teamId" element={!token ? <Login setToken={setToken} /> : <TeamPlayers token={token} />} />
      </Routes>
    </Router>
  );
}

export default App;
