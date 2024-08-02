import { BrowserRouter as  Router, Routes, Route } from 'react-router-dom'
import './App.css'
import Footer from './components/Main/Footer'
function App() {

  return (
    <Router>
      <div className='App'>
        {/* <Header /> */}
        <Routes>
          <Route path="/" />
          <Route path="/about" />
          <Route path="/items" />
          <Route path="/item/:id" />
        </Routes>
        <Footer />
      </div>
    </Router>
  )
}

export default App
