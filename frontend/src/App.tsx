import { BrowserRouter as  Router, Routes, Route } from 'react-router-dom'
import Footer from './components/Main/Footer'
import ItemList from './components/Product/List/ItemList'
import ItemDetail from './components/Product/Retrieve/ItemDetail'
import Header from './components/Main/Header';
import Home from './components/Main/Home';
import { AuthProvider } from './components/Auth/AuthContext'
import Login from './components/Auth/Login';
import { useState } from 'react';

function App() {

  const [cartItem, setCartItems] = useState<Number[]>([]);

  const addToCart = (id: Number) => {
    setCartItems([...cartItem, id]);
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
            <Route path="/item/:id" element={<ItemDetail />} />
          </Routes>
          <Footer />
        </div>
      </Router>
      </AuthProvider>
  )
}

export default App
