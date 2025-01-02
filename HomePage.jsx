import React from 'react';
import Header from '/src/assets/comp/Header.jsx';
import Footer from '/src/assets/comp/Footer.jsx';
import ContactForm from '/src/assets/comp/ContactForm.jsx';  
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div>
        <Header />

      {/* Hero Section */}
      <section id="home" className="hero">
        <div className="hero-content">
          <h2>
            Premium Marble <br /> for Exquisite <br /> Spaces
          </h2>
          <p>Transform your home with luxurious and elegant marble.</p>
          <br />
          <a href="Catalog.jsx" className="btn">Explore Our Catalog</a>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="features">
        <h2>Why Choose Marble Co.</h2>
        <div className="features-grid">
          <div className="feature">
            <img src="/src/assets/data/img/high-quality.png" alt="High Quality" />
            <h3>Superior Quality</h3>
            <p>We source only the finest marble to ensure lasting beauty.</p>
          </div>
          <div className="feature">
            <img src="/src/assets/data/img/design.png" alt="Exclusive Designs" />
            <h3>Exclusive Designs</h3>
            <p>Custom marble designs tailored to your vision.</p>
          </div>
          <div className="feature">
            <img src="/src/assets/data/img/support.jpg" alt="Customer Support" />
            <h3>Exceptional Support</h3>
            <p>Dedicated team to assist you every step of the way.</p>
          </div>
        </div>
      </section>

      {/* Ratings Section */}
      <section id="ratings" className="ratings">
        <h2>Our Customers Love Us</h2>
        <div className="ratings-content">
          <div className="rating-box">
            <span className="rating-score">4.9</span>
            <span className="rating-stars">★★★★★</span>
            <p>Average Rating</p>
          </div>
          <p>Over 1,000 satisfied customers have rated Marble Co. for our exceptional quality and service.</p>
        </div>
      </section>

      {/* Contact Form Section */}
      {/* Adding ContactForm component here */}

      <Footer />
    </div>
  );
};

export default HomePage;
