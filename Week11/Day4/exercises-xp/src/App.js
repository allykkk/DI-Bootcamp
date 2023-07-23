import logo from './logo.svg';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import { Routes, Route } from "react-router-dom";
import NavBar from './components/navbar';
import HomeScreen from './components/homeScreen';
import ProfileScreen from './components/profileScreen';
import ShopScreen from './components/shopScreen';
import NotFound from './components/notFound';
import ErrorBoundary from "./components/errorBoundary";
import PostList from './components/postList';
import SocialMedias from './components/exercise3/socialMedias';
import Skills from './components/exercise3/skills';
import Experiences from './components/exercise3/experiences';
import Button from './components/button';


function App() {
  return (
    <div className='container'>
      <NavBar />
      <div className="content">
        <Routes>
          <Route path="/profile" element={<ErrorBoundary><ProfileScreen /></ErrorBoundary>} />
          <Route path="/shop" element={<ErrorBoundary><ShopScreen /></ErrorBoundary>} />
          <Route exact path="/" element={<ErrorBoundary><HomeScreen /></ErrorBoundary>} />
          <Route path='*' element={<ErrorBoundary><NotFound /></ErrorBoundary>} />
        </Routes>
      </div>
      <div className='exercise4'>
        <hr /><Button />
      </div>
      <div className='exercise2'>
        <hr /><PostList />
      </div>
      <div className='exercise3'>
        <SocialMedias />
        <Skills />
        <Experiences />
      </div>
    </div>
  );
}

export default App;
