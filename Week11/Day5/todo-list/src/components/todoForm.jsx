import React from "react";

const TodoForm = ({ handleSubmit }) => {
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>Add a new todo:</label>
        <input type="text" name="newItem"/>
      </form>
    </div>
  );
};

export default TodoForm;
