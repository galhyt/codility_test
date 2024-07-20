// src/App.js
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Logout from './Logout';
import Scoreboard from './Scoreboard';
import TeamPlayers from './TeamPlayers';
import Player from './Player';
import Team from './Team';
import UserStatistics from './UserStatistics';
import Layout from './Layout';
import { UserProvider } from './userContext';

function App() {
  const [token, setToken] = useState(null);

  return (
  <UserProvider>
      <Router>
          <Layout>
              <Routes>
                  <Route path="/" element={!token ? <Login setToken={setToken} /> : <Scoreboard token={token} />} />
                  <Route path="/team_players/:teamId/:teamName" element={!token ? <Login setToken={setToken} /> : <TeamPlayers token={token} />} />
                  <Route path="/player/:playerId/:playerName" element={<Player token={token} />} />
                  <Route path="/team/:teamId/:teamName" element={<Team token={token} />} />
                  <Route path="/user_statistics/" element={<UserStatistics token={token} />} />
                  <Route path="/logout/" element={<Logout token={token} setToken={setToken} />} />
              </Routes>
          </Layout>
       </Router>
   </UserProvider>
  );
}

export default App;
