import Header from "/src/assets/comp/Header.jsx";
import Footer from "/src/assets/comp/Footer.jsx";
import HomePage from "/src/HomePage.jsx";
import Catalog from "./assets/comp/Catalog";
import ContactForm from "./assets/comp/ContactForm";
import Testimonials from "./assets/comp/Testimonials";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import About from './assets/comp/About';
function App() {
  return (
    <>
    <Router>

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/catalog" element={<Catalog />} />
        <Route path="/about" element={<About />} />
        <Route path="/contactform" element={<ContactForm />} />
        <Route path="/testimonials" element={<Testimonials />} />
      </Routes>

      <Footer />
    </Router>
      
    </>
  );
}



export default App;
