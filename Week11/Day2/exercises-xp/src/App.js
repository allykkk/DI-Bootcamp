import logo from './logo.svg';
import './App.css';
import Car from './components/Car';
import Event from './components/Events';
import Phone from './components/Phone';
import Color from './components/Color';


const carinfo = { name: "Ford", model: "Mustang" }

function App() {
  return (
    <div className="App">
      <Car model={carinfo.model} />
      <Event />
      <Phone />
      <Color />
    </div>
  );
}

export default App;
