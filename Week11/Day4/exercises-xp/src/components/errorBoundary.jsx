import React, { Component } from "react";

class ErrorBoundary extends Component {
  state = { hasError: false };

  componentDidCatch(error, info) {
    console.error("Error caught by ErrorBoundary:", error);
    this.setState({ hasError: true });
  }

  render() {
    if (this.state.hasError) {
      return <h2>An error has occured.</h2>;
    }
    return this.props.children;
  }
}

export default ErrorBoundary;
