import React from "react";
import './ItemCard.css';

interface ItemCardProps {
    id: number;
    name: string;
    price: string;
    image_url: string;
    platform: string;
    addToCart: (id: number) => void;
}


const ItemCard: React.FC<ItemCardProps> = ({ id, name, price, image_url, platform, addToCart }) => {
    return (
        <div className="item-card">
            <img src={image_url} alt={name} className="item-card-image" />
            <div className="item-card-details">
                <h3>{name}</h3>
                <p>Platform: {platform}</p>
                <p>Price: {price}</p>
                <button onClick={() => addToCart(id)}>Add to Cart</button>
            </div>
        </div>
    )
}


export default ItemCard;