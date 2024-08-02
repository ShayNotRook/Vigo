import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchItemById, Item } from '../../api/FetchItems';
import './itemDetail.css'

const ItemDetail: React.FC = () => {
    const { id } = useParams<{ id: string}>();
    const [item, setItem] = useState<Item | null>(null);


    useEffect(() => {
        fetchItemById(Number(id))
            .then(data => setItem(data))
            .catch(error => console.log('Error fetching item:', error));
    }, [id]);

    if (!item) {
        return <div>Loading...</div>
    }

    return (
        <div className='item-container'>
            <h1>{item.name}</h1>
            <img src={item.image_url} alt={item.name} />
            <p>Price: ${item.price}</p>
            <p>{item.description}</p>
        </div>
    );
};

export default ItemDetail;