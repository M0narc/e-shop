import { Container } from 'react-bootstrap'


import Header from './components/Headers'
import Footer from './components/Footer'

import HomeScreen from './screens/HomeScreen';

function App() {
  return (
    <div >
      <Header />
      <Container>
      <main className='py-3'>
        <HomeScreen />
      </main>
      </Container>
      <Footer />
    </div>
  );
}

export default App;