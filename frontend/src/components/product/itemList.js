import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const ItemList = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetch('/api/items/')
            .then(response => response.json())
            .then(data => setItems(data))
            .then(error => console.error('Error fetching items:', error));
    }, []);

    return (
        <div>
            <h1>Items</h1>
            <ul>
                {items.map(item => (
                    <li key={item.id}>
                        <Link to={`/item/${item.id}`}>
                            <img src={item.image_url} alt={item.name} />
                            <h3>{item.name}</h3>
                            <p>Price: ${item.price}</p>
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ItemList;