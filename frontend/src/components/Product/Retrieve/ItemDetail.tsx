import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchItemById, Item } from '../../api/FetchItems';
import './itemDetail.css'

interface ItemDetailProps {
    addToCart: (id: number) => void;
}


const ItemDetail: React.FC<ItemDetailProps> = ({ addToCart }) => {
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
            <img src={item.image_url} alt={item.name} className="item-detail-image" />
            <div className='item-detail-info'>
                <h1>{item.name}</h1>
                <p>{item.description}</p>
                <p>Platform: {item.platform}</p>
                <p>Price: {item.price}</p>
                <button onClick={() => addToCart(item.id)}>Add to Cart</button>
            </div>
            
        </div>
    );
};

export default ItemDetail;