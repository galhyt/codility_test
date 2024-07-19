import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';
import './TeamPlayers.css';  // Import a CSS file if needed

const TeamPlayers = ({ token }) => {
  const { teamId, teamName } = useParams();
  const [players, setPlayers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/team_players/', {
          'team': teamId
        }, {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
          method: 'POST'
        });
        setPlayers(response.data.players);
        setLoading(false);
      } catch (error) {
        // Check if error.response is available
        if (error.response) {
          // Server responded with a status other than 2xx
          setError(`Error: ${error.response.data.detail || error.response.statusText}`);
        } else if (error.request) {
          // The request was made but no response was received
          setError('Error: No response received from server');
        } else {
          // Something happened in setting up the request
          setError(`Error: ${error.message}`);
        }
        setLoading(false);
      }
    };

    fetchPlayers();
  }, [teamId, teamName, token]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="team-players-container">
      <h1>Players for Team {teamName}</h1>
      <table className="players-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Height</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {players.map((player) => (
            <tr key={player.id}>
              <td>
                <Link to={`/player/${player.id}/${player.name}`}>
                    {player.name}
                </Link>
              </td>
              <td>{player.height}</td>
              <td>{player.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TeamPlayers;
