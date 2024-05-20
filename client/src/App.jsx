import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from './components/navbar/Navbar';
import Home from './components/home/Home';
import Register from './components/authentication/Register';
import Login from './components/authentication/Login';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

const App = () => {
  return (
    <div>
      <Router>
        <Navbar />
        <Routes>
          <Route
            path="/"
            element={<Home />}
          />
          <Route
            path="/login"
            element={<Login />}
          />
          <Route
            path="/register"
            element={<Register />}
          />
        </Routes>
      </Router>
    </div>
  );
};

export default App;
