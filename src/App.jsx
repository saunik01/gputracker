import { useState } from 'react';
import './App.css';

function App() {
  const [gpus, setGpus] = useState([
    { name: 'NVIDIA RTX 4070', price: '639€', shop: 'Jimm\'s.fi' },
    { name: 'AMD RX 7800 XT', price: '569€', shop: 'Verkkokauppa.com' },
    { name: 'Intel Arc A770', price: '389€', shop: 'Proshop.fi' }
  ]);

  const refreshPrices = () => {
    // In real life, you'd fetch new prices from an API
    alert('Refreshing prices! (Simulated)');
  };

  return (
    <div className="container">
      <h1>🇫🇮 GPU Price Tracker</h1>
      <button className="refresh-button" onClick={refreshPrices}>
        🔄 Refresh Prices
      </button>

      <div className="cards">
        {gpus.map((gpu, index) => (
          <div key={index} className="card">
            <h2>{gpu.name}</h2>
            <p className="price">{gpu.price}</p>
            <p className="shop">({gpu.shop})</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
