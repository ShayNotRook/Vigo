import React, { useState } from 'react';
import menuBurgerIcon from "../../assets/icons/menu-burger.png";


const HamburgerMenu: React.FC = () => {
    const [isOpen , setIsOpen] = useState<boolean>(false);

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
                        
                    </ul>
                </nav>
            )}
        </div>
    )

}