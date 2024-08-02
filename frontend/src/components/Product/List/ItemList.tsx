import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import { fetchItems, Item } from "../../api/FetchItems";


const ItemList: React.FC = () => {
    const [items, setItems] = useState<Item[]>([]);

    useEffect(() => {
        fetchItems()
            .then(data => setItems(data))
            .catch(error => console.error('Error fetching items:', error));    }, []);
    
    return (
        <div>
            <h1>Items</h1>
            <ul>
                {items.map(item => (
                    <li key={item.id}>
                        <Link to={`/item/${item.id}`}>
                            <img src={item.image} alt={item.name} />
                            <h3>{item.name}</h3>
                            <p>Price: {item.price}</p>
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ItemList;