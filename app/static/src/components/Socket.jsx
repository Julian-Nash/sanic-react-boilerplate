import React from "react";


class Socket extends React.Component {

  constructor(props) {
    super(props);
    this.state = {time: null};
  }

  componentDidMount() {

    this.socket = new WebSocket('ws://localhost:5000/ws/utctime');

    this.socket.addEventListener("open", () => {
      this.socket.send("hello!")
    })

    this.socket.addEventListener('message', (event) => {
      this.setState({
        time: event.data
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
        <span>Socket data: {this.state.time || "..."}</span>
      </div>
    )
  }

}

export default Socket;