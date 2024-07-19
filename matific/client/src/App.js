// src/App.js
import React, { useState } from 'react';
import Login from './Login';
import Scoreboard from './Scoreboard';

function App() {
  const [token, setToken] = useState(null);

  return (
    <div className="App">
      {!token ? (
        <Login setToken={setToken} />
      ) : (
        <Scoreboard token={token} />
      )}
    </div>
  );
}

export default App;
