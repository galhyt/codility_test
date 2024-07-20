// src/LogoutButton.js
import { useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Logout = ({ token, setToken }) => {
  const navigate = useNavigate();

  useEffect(() => {
    const logout = async () => {
      try {
        await axios.post(
          'http://127.0.0.1:8000/api/logout/',
          {}, // Empty body
          {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`,
            }
          }
        );
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        setToken(null)
        navigate('/');
      } catch (error) {
        console.error('There was an error logging out!', error);
      }
    };

    logout();
  }, [token, navigate, setToken]);

  return null;
};

export default Logout;
