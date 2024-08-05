import React, { useState } from 'react';
import menuBurgerIcon from "../../assets/icons/menu-burger.png";
import { Category } from '../api/FetchCategories';

interface HamburgerProps {
    categories: Category[];
}


const HamburgerMenu: React.FC<HamburgerProps> = ({ categories }) => {
    const [isActive, setIsActive] = useState(false);
    const [expandedCategory, setExpandedCategory] = useState<number | null>(null);

    const toggleMenu = () => {
        setIsActive(!isActive);

    };

    const toggledSubcategories = (categoryId: number) => {
        setExpandedCategory( expandedCategory === categoryId ? null: categoryId)
    }

    return (
        <div className={`hamburger-menu ${isActive ? 'active': ''}`} id='hamburger-menu'>
            <div className='menu-toggle' id='menu-toggle' onClick={toggleMenu}>
                <img src={menuBurgerIcon} alt="Menu" />
            </div>
            {isActive && (
                <nav className={`menu-content ${isActive ? 'active': ''}`} id='menu-content'>
                    <ul>
                        {categories.map(category => (
                            <li key={category.id}>
                                <a
                                href="#"
                                className='top-level-categories'
                                onClick={() => toggledSubcategories(category.id)}
                                    >{category.title}
                                </a>
                                {expandedCategory === category.id && category.subcategories.length > 0 && (
                                    <ul className="subcategories">
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