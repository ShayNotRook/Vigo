import React, { useEffect, useState } from "react";
import { fetchItems, Item } from "../../api/FetchItems";
import ItemCard from "../ItemCard";
import './Item.css'

interface ItemListProps {
    addToCart: (id: number) => void;
}

// interface Item {
//     id: number;
//     name: string;
//     price: number;
//     image_url: string;
//     platform: string;
// }


const ItemList: React.FC<ItemListProps> = ({ addToCart }) => {
    const [items, setItems] = useState<Item[]>([]);

    useEffect(() => {
        fetchItems()
            .then(data => setItems(data))
            .catch(error => console.error('Error fetching items:', error));    
        }, []);
    
    return (
        <div className="item-list">
            {items.map(item => (
                <li key={item.id}>
                    <ItemCard
                        id={item.id}
                        name={item.name}
                        price={item.price}
                        image_url={item.image_url}
                        platform={item.platform}
                        addToCart={addToCart}
                        />
                </li>
            ))}
        </div>
    );
};

export default ItemList;