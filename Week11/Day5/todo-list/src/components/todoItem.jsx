import React from "react";

const TodoItem = ({ tasks, handleDelete }) => {
  if (tasks.length === 0)
    return (
      <div className="todos collection">
        <p class="center">You have no todo's left, yay!</p>
      </div>
    );

  return (
    <div className="todos collection">
      {tasks.map((task, index) => (
        <div
          key={index}
          className="collection-item"
          onClick={() => handleDelete(task)}
        >
          {task.content}
        </div>
      ))}
    </div>
  );
};

export default TodoItem;
