import React, { useState } from 'react';
import menuBurgerIcon from "../../assets/icons/menu-burger.png";
import { Category } from '../api/FetchCategories';

interface HamburgerProps {
    categories: Category[];
}


const HamburgerMenu: React.FC<HamburgerProps> = ({ categories }) => {
    const [isOpen , setIsOpen] = useState(false);

    const toggleMenu = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className='hamburger-menu' id='hamburger-menu'>
            <div className='menu-toggle' id='menu-toggle' onClick={toggleMenu}>
                <img src={menuBurgerIcon} alt="Menu" />
            </div>
            {isOpen && (
                <nav className='menu-content' id='menu-content'>
                    <ul>
                        {categories.map(category => (
                            <li key={category.id}>
                                <a href={`/category/${category.slug}`} className='top-level-categories'>{category.title}</a>
                                {category.subcategories.length > 0 && (
                                    <ul className='subcategories'>
                                        {category.subcategories.map(subcategory => (
                                            <li key={subcategory.id}>
                                                <a href={`/category/${subcategory.slug}`}>{subcategory.title}</a>
                                            </li>
                                        ))}
                                    </ul>
                                )}
                            </li>
                        ))}
                    </ul>
                </nav>
            )}
        </div>
    )

}

export default HamburgerMenu;