import { useState } from 'react';
import './App.css';

function App() {
  const [gpus, setGpus] = useState([
    { name: "NVIDIA RTX 4070", price: "649€", store: "Jimms.fi" },
    { name: "AMD RX 7800 XT", price: "579€", store: "Verkkokauppa.com" },
    { name: "Intel Arc A770", price: "399€", store: "Proshop.fi" }
  ]);

  function refreshPrices() {
    // Simulate refreshing prices (in future you would fetch real prices here!)
    const updatedGpus = [
      { name: "NVIDIA RTX 4070", price: "639€", store: "Jimms.fi" },
      { name: "AMD RX 7800 XT", price: "569€", store: "Verkkokauppa.com" },
      { name: "Intel Arc A770", price: "389€", store: "Proshop.fi" }
    ];
    setGpus(updatedGpus);
  }

  return (
    <div className="App">
      <h1>🇫🇮 GPU Price Tracker</h1>
      <button onClick={refreshPrices}>🔄 Refresh Prices</button>
      <ul>
        {gpus.map((gpu, index) => (
          <li key={index}>
            <strong>{gpu.name}</strong> - {gpu.price} ({gpu.store})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
