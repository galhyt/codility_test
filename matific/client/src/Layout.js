// src/Layout.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Layout.css';

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <header>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/user_statistics/">User Statistics</Link></li>
            {/* Add more links as needed */}
          </ul>
        </nav>
      </header>
      <main>
        {children}
      </main>
      <footer>
        <p>© 2024 Your Company</p>
      </footer>
    </div>
  );
};

export default Layout;
