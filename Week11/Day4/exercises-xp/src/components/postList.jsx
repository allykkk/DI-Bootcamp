import React, { Component } from "react";
import posts from "../data/posts.json";

class PostList extends Component {
  state = { posts };
  render() {
    return (
      <>
        <h1>Hi This is a Title</h1>
        {this.state.posts.map((post) => {
          return (
            <div key={post.id}>
              <h2>{post.title}</h2>
              <p>{post.content}</p>
            </div>
          );
        })}
      </>
    );
  }
}

export default PostList;
