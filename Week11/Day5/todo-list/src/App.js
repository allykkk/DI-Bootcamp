import './App.css';
import React, { Component } from 'react';
import TodoItem from './components/todoItem';
import TodoForm from './components/todoForm';


class App extends Component {
  state = { tasks: [{ content: 'Buy some milk' }, { content: 'Do my homework' }] }

  addNewItem = (event) => {
    event.preventDefault();
    const value = event.target[0].value
    if (value === "") return alert("empty item!")
    const tasks = [...this.state.tasks]
    tasks.push({ content: value })
    this.setState({ tasks })
    event.target.reset()
  }

  deleteItem = (task) => {
    const taskIndex = this.state.tasks.indexOf(task)
    const tasks = [...this.state.tasks]
    tasks.splice(taskIndex, 1);
    this.setState({ tasks })
  }

  render() {
    const { tasks } = this.state
    return (
      <div className='todo-app container'>
        <h1 className='center blue-text'>Todo's</h1>
        <TodoItem tasks={tasks} handleDelete={this.deleteItem} />
        <TodoForm handleSubmit={this.addNewItem} />
      </div>
    );
  }
}

export default App;