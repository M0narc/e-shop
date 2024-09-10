import { Container } from 'react-bootstrap'

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Header from './components/Headers'
import Footer from './components/Footer'

import HomeScreen from './screens/HomeScreen';
import ProductScreen from './screens/ProductScreen';

function App() {
  return (
    <Router>
      <Header />
      <Container>
      <main className='py-3'>
        <Routes>
          <Route path='/' Component={HomeScreen} exact />
          <Route path='/Product/:id' Component={ProductScreen} />
        </Routes>
      </main>
      </Container>
      <Footer />
    </Router>
  );
}

export default App;
