import React, {useEffect, useState} from "react";

function Api() {

  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/products")
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setItems(result);
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [])

  if (error) {
    return (
      <div>
        <h3>REST API data</h3>
        <span>Error: {error.message}</span>
      </div>
    )
  } else if (!isLoaded) {
    return (
      <div>
        <h3>REST API data</h3>
        <span>Loading...</span>;
      </div>
    )
  } else {
    return (
      <div>
        <h3>REST API data</h3>
        <ul>
          {items.map(item => (
            <li key={item.id}>
              {item.name} {item.price}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default Api;