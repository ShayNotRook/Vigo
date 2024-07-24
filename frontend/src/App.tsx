// import logo from './logo.svg';
import React, { useState } from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';


// import ItemDetail from './components/product/itemDetail';
// import ItemList from './components/product/itemList';
import ListGroup from './components/tests/ListGroup';
import './App.css';
import Alert from './components/tests/Alert';
import Button from './components/tests/Buttons';
// import Footer from './components/base/Footer'


function App() {
  // let items = ['Chicago', 'New York', 'Cairo', 'Toronto']

  // const handleSelectItem = (item: string) => {
  //   console.log(item);
  // }
  const [alertVisible, setAlertVisible] = useState(false);

  return (
    <div>
      { alertVisible && <Alert onClose={() => setAlertVisible(false)}>My Alert</Alert> }

      <Button onClick={() => setAlertVisible(true)}>My Button</Button>
    </div>
  );
}

export default App;
