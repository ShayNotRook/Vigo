import { BrowserRouter as  Router, Routes, Route } from 'react-router-dom'
import './App.css'
import Footer from './components/Main/Footer'
import ItemList from './components/Product/List/ItemList'
import ItemDetail from './components/Product/Retrieve/ItemDetail'
function App() {

  return (
    <Router>
      <div className='App'>
        {/* <Header /> */}
        <Routes>
          {/* <Route path="/" /> */}
          <Route path="/about" />
          <Route path="/items" element={<ItemList />} />
          <Route path="/item/:id" element={<ItemDetail />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  )
}

export default App
