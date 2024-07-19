import React, { useEffect, useState, useContext } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './Scoreboard.css';  // Import the CSS file
import UserContext from './userContext';


const GamesTable = ({ games }) => {
  const { userType } = useContext(UserContext);
  return (
      <table className="games-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Home Team</th>
            <th>Away Team</th>
            <th>Home Team Score</th>
            <th>Away Team Score</th>
          </tr>
        </thead>
        <tbody>
          {games.map((game, index) => (
            <tr key={index}>
              <td>{new Date(game.date).toLocaleDateString()}</td>
              <td style={{ fontWeight: game.home_team_score >  game.away_team_score ? 'bold' : 'normal' }}>
                <Link to={userType === 'league_admin' ?  `/team/${game.home_team_id}/${game.home_team}` : `/team_players/${game.home_team_id}/${game.home_team}`}>
                    {game.home_team}
                </Link>
              </td>
              <td style={{ fontWeight: game.away_team_score >  game.home_team_score ? 'bold' : 'normal' }}>
                <Link to={userType === 'league_admin' ?  `/team/${game.away_team_id}/${game.away_team}` : `/team_players/${game.away_team_id}/${game.away_team}`}>
                    {game.away_team}
                </Link>
              </td>
              <td>{game.home_team_score}</td>
              <td>{game.away_team_score}</td>
            </tr>
          ))}
        </tbody>
      </table>
        );
};

const Scoreboard = ({ token }) => {
  const [rounds, setRounds] = useState([]);

  useEffect(() => {
    const fetchGames = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/games/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setRounds(response.data.rounds);
      } catch (error) {
        console.error('Error fetching games', error);
      }
    };

    fetchGames();
  }, [token]);

  if (!rounds.length) return <div className="loading">Loading...</div>;

  return (
    <div className="scoreboard-container">
    <h1><center>Scoreboard</center></h1>
    <small>* winning teams are bolded</small>
      {rounds.map((round, index) => (
        <div key={index}>
          <h2 className="round-heading">Round {round.round}</h2>
          <GamesTable games={round.games} />
        </div>
      ))}
    </div>
  );
};

export default Scoreboard;
