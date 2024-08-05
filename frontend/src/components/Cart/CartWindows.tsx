import React, { useState, useEffect} from 'react';
import cartIcon from '../../assets/icons/shopping-cart.png';
interface CartItem {
    id: number;
    name: string;
    price: number;
    quantity: number;
    image_url: string; 
}

const CartWindows: React.FC = () => {

    const [isOpen, setIsOpen] = useState(false);
    const [cartItems, setCartItems] = useState<CartItem[]>([]);  

    useEffect(() => {
        // Fetch cart Items from backend or local storage
        const fetchCartItems = async() => {
            const items = await fetch('/api/cart/details/').then(res => res.json());
            setCartItems(items);
        };

        fetchCartItems();
    }, []);

    const toggleCart = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className="cart">
            <div className='cart-summary' onClick={toggleCart}>
                <img src={cartIcon} alt="cart" />
                <div className='item-count'>{cartItems.reduce((acc, item) => acc + item.quantity, 0)}</div>
            </div>
            {isOpen && (
                <div className='cart-details'>
                    <ul>
                        {cartItems.map(cartItem => (
                            <li key={cartItem.id}>
                                <div className='cart-item-details'>
                                    <p>{cartItem.name}</p>
                                    <p>{cartItem.price} x {cartItem.quantity}</p>
                                </div>
                            </li>
                        ))}
                    </ul>
                    <button className='btn btn-outline-primary'>
                        Go to Cart
                    </button>
                </div>
            )}
        </div>
    )
}

export default CartWindows