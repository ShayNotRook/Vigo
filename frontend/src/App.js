// import logo from './logo.svg';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import ItemDetail from './components/product/itemDetail';
import ItemList from './components/product/itemList';
 
import './App.css';
import Footer from './components/base/Footer'

function App() {
  return (
    <Router>
      <div className="App">
        {/* <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header> */}
        <Routes>
            <Route exact path='/' component={ItemList} />
            <Route exact path='/item/:id' component={ItemDetail} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
