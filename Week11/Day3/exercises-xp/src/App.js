import logo from './logo.svg';
import './App.css';
import BuggyCounter from './components/buggyCounter';
import ErrorBoundry from './components/errorBoundary';
import Color from './components/color';


function App() {
  return (
    <>
      <div className='Exercise1'>
      <p>
        <b>Click on the numbers to increase the counters.<br/>
        The counter is programmed to throw error when it reaches 5. This simulates a JavaScript error in a component.</b>
       
      </p>

      <hr/>

      <p>These two counters are inside the same error boundary. If one crashes, the error boundary will replace both of them.</p>
      <ErrorBoundry>
        <BuggyCounter/>
        <BuggyCounter/>
      </ErrorBoundry>
      <hr/>

      <p>These two counters are each inside of their own error boundary. So if one crashes, the other is not affected.</p>    
      <ErrorBoundry><BuggyCounter/></ErrorBoundry>  
      <ErrorBoundry><BuggyCounter/></ErrorBoundry>  
      <hr/>

      <p>This counter is not inside of boundary. So if crashes, all other components are deleted.</p>
      <BuggyCounter/>
      <hr/>
      </div>

      <div className='Exercise2'>
        <Color/>
      </div>
    </>
  );
}

export default App;
