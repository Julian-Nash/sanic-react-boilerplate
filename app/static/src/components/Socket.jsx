import React from "react";


class Socket extends React.Component {

  constructor(props) {
    super(props);
    this.state = {data: null};
  }

  componentDidMount() {

    this.socket = new WebSocket('ws://localhost:5000/ws/utctime');

    this.socket.addEventListener("open", () => {
      this.socket.send("hello!")
    })

    this.socket.addEventListener('message', (event) => {
      this.setState({
        data: event.data
      })
    });

  }

  componentWillUnmount() {
    this.socket.close();
  }

  render() {
    return (
      <div>
        <h3>Websocket data</h3>
        <span>{this.state.data || "Loading..."}</span>
      </div>
    )
  }

}

export default Socket;