import { useState } from 'react';
import './App.css';

function App() {
  const [gpus, setGpus] = useState([
    { name: 'NVIDIA RTX 4070', price: '579,99€', shop: 'verkkokauppa.com' },
    { name: 'AMD RX 7800 XT', price: '538,90€', shop: 'multitronic.fi' },
    { name: 'Intel Arc A770', price: '339,00€', shop: 'Jimms.fi' },
    { name: 'NVIDIA RTX 4060 Ti', price: '414,00€', shop: 'multitronic.fi' },
    { name: 'AMD RX 7900 XTX', price: '929,90€', shop: 'Jimms.fi' },
    { name: 'NVIDIA RTX 4080 Super', price: '1249,00€', shop: 'verkkokauppa.com' }
  ]);

  const refreshPrices = () => {
    // In real life, you'd fetch new prices from an API
    alert('Refreshing prices! (Simulated)');
  };

  return (
    <div className="container">
      <h1 className="main-header">
        🇫🇮 Näytönohjainten Hintavertailu: Jimm's, Verkkokauppa & Multitronic
      </h1>

      <button className="refresh-button" onClick={refreshPrices}>
        🔄 Päivitä Hinnat
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
