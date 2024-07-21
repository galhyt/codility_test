import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import './Player.css';

const Player = ({ token }) => {
  const { playerId, playerName } = useParams();
  const [player, setPlayer] = useState({});
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchPlayer = async () => {
      try {
        const response = await axios.post(
          'http://127.0.0.1:8000/api/player/',
          { player: playerId },
          {
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${token}`
            }
          }
        );
        setPlayer(response.data);
      } catch (error) {
        setError(
          error.response
            ? error.response.data
            : 'Error fetching player data'
        );
      }
    };

    fetchPlayer();
  }, [playerId, token]);

  return (
    <div className="player-container">
      <h1>Player: {playerName}</h1>
      {error && <p className="error">{error}</p>}
      {player && (
        <table className="player-table">
          <tbody>
            <tr>
              <th>Name</th>
              <td>{player.name}</td>
            </tr>
            <tr>
              <th>Height</th>
              <td>{player.height}</td>
            </tr>
            <tr>
              <th>Age</th>
              <td>{player.age}</td>
            </tr>
            <tr>
              <th>Average Score</th>
              <td>{player.avg_score.toFixed(2)}</td>
            </tr>
            <tr>
              <th>Number of Games</th>
              <td>{player.games_no}</td>
            </tr>
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Player;
