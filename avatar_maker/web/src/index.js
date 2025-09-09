import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './Components/App';
import AppDS from './Components/AppDS';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AppDS />
  </React.StrictMode>
);

reportWebVitals();
