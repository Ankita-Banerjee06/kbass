import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const container = document.getElementById('root');
// public/index.html is the real "Sage" app (plain HTML/CSS/JS) and has no
// #root div — this CRA entry point is unused leftover scaffolding, so only
// mount if a root element actually exists (avoids a console error on load).
if (container) {
  const root = ReactDOM.createRoot(container);
  root.render(<App />);
}