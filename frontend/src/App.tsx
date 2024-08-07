import { BrowserRouter as  Router, Routes, Route } from 'react-router-dom'
import Footer from './components/Main/Footer'
import ItemList from './components/Product/List/ItemList'
import ItemDetail from './components/Product/Retrieve/ItemDetail'
import Header from './components/Main/Header';
import Home from './components/Main/Home';
import { AuthProvider } from './components/Auth/AuthContext'
import Login from './components/Auth/Login';
import React, { useState } from 'react';

const App: React.FC = () => {

  const [cartItems, setCartItems] = useState<number[]>([]);

  const addToCart = (id: number) => {
    setCartItems([...cartItems, id]);
  }

  return (
    <AuthProvider>
      <Router>
        <div className='App'>
          <Header />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" />
            <Route path="/shop" element={<ItemList addToCart={addToCart} />} />
            <Route path='/login' element={<Login />} />
            <Route path="/shop/product/:id" element={<ItemDetail addToCart={addToCart}/>} />
          </Routes>
          <Footer />
        </div>
      </Router>
      </AuthProvider>
  )
}

export default App
