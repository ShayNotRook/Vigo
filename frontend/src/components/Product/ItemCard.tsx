import React from "react";
import './ItemCard.css';
import { Link } from "react-router-dom";


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
                <Link to={`product/${id}`}>{name}</Link>
                <p>Platform: {platform}</p>
                <p>Price: {price}$</p>
                <button onClick={() => addToCart(id)}>Add to Cart</button>
            </div>
        </div>
    )
}


export default ItemCard;