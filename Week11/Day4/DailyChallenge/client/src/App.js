import logo from './logo.svg';
import './App.css';
import Header from './components/header';
import PostForm from './components/postForm';

function App() {
  return (
    <div className='container'>
      <Header />
      <PostForm />
    </div>
  );
}

export default App;
