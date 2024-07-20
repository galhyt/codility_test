// src/UserStatistics.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './UserStatistics.css';

function secondsToHms(d) {
  d = Number(d);
  const h = Math.floor(d / 3600).toString().padStart(2, '0');
  const m = Math.floor((d % 3600) / 60).toString().padStart(2, '0');
  const s = Math.floor((d % 3600) % 60).toString().padStart(2, '0');

  return `${h}:${m}:${s}`;
}

const UserStatistics = ({ token }) => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/user_statistics/', {
      headers: {
        'Authorization': `Bearer ${token}`,
      }})
      .then(response => {
        setUsers(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the user statistics!', error);
      });
  }, [token]);

  return (
    <div>
      <h1>User Statistics</h1>
      <table>
        <thead>
          <tr>
            <th>Username</th>
            <th>User Type</th>
            <th>Login Count</th>
            <th>Total Time Spent</th>
            <th>Is Online</th>
            <th>Current Session Duration</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.username}>
              <td>{user.username}</td>
              <td>{user.user_type}</td>
              <td>{user.login_count}</td>
              <td>{secondsToHms(user.total_time_spent)}</td>
              <td>{user.is_online ? 'Yes' : 'No'}</td>
              <td>{secondsToHms(user.current_session_duration)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UserStatistics;
