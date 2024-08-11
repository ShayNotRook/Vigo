import React, { useEffect, useState } from 'react';
import menuBurgerIcon from "../../assets/icons/menu-burger.png";
import { Category } from '../api/FetchCategories';

interface HamburgerProps {
    categories: Category[];
}


const HamburgerMenu: React.FC = () => {
    const [categories, setCategories] = useState<Category[]>([]);
    const [isActive, setIsActive] = useState(false);
    const [expandedCategory, setExpandedCategory] = useState<number | null>(null);

    useEffect(() => {
        const fetchTopCategories = async() => {
            try {
                const response = await fetch('/api/categories/top_level_categories/')
            if (!response.ok) {
                throw new Error(`Failed to Fetch categories!`)
                }
                const data = await response.json();
                setCategories(data);
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        }

        fetchTopCategories();
    },[])

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