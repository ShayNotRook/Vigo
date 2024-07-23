import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";


const ItemDetail = () => {
    const { id } = useParams();
    const [item, setItem] = useState(null);

    useEffect(() => {
        fetch(`/api/items/${id}`)
            .then(response => response.json())
            .then(data => setItem(data))
            .catch(error => console.error('Error fetching item:', error));
    }, [id]);

    if (!item) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{item.name}</h1>
            <img src={item.image_url} alt={item.name} />
            <p>Price: ${item.price}</p>
            <p>{item.description}</p>
        </div>
    );
};

export default ItemDetail;