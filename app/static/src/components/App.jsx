import React from "react";
import Home from "./Home";
import Socket from "./Socket";
import Api from "./Api";

import {Switch, Link, Route} from "react-router-dom";


function App(props) {
  return (
    <div>
      <h1>Sanic React App</h1>

      <nav>
        <Link to="/">Home</Link> | <Link to="/socket">Socket</Link> | <Link to="/api">API</Link>
      </nav>

      <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/socket">
            <Socket />
          </Route>
          <Route path="/api">
            <Api />
          </Route>
        </Switch>
    </div>
  )
}

export default App