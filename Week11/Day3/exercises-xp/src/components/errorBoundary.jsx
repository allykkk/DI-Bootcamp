import React, { Component } from "react";

class ErrorBoundry extends Component {
  state = {
    error: null,
    errorInfo: null,
  };

  componentDidCatch(error, errorInfo) {
    this.setState({
      error: error,
      errorInfo: errorInfo,
    });
  }

  render() {
    if (this.state.error) {
        console.log("Entered!")
      return (
        <>
        <h1>Somthing went wrong. </h1>
        <details style={{ whiteSpace: "pre-wrap" }}>
          {this.state.error && this.state.error.toString()}
          <br />
          {this.state.errorInfo.componentStack}
        </details>
        </>
      );
    }
    return this.props.children;
  }
}

export default ErrorBoundry;
