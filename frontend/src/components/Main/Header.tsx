import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import HamburgerMenu from './HamburgerMenu';
import logo from '../../assets/vigo-transparent.png';
import userIcon from '../../assets/icons/user.png';
import cartIcon from '../../assets/icons/shopping-cart.png';
import { fetchTopCategories, Category } from "../api/FetchCategories";
import { useAuth } from "../Auth/AuthContext";
import './header.css';


const Header: React.FC = () => {
    const { isAuthenticated, logout } = useAuth();
    const [categories, setCategories] = useState<Category[]>([])

    useEffect(() => {
        fetchTopCategories()
            .then(data => setCategories(data))
            .catch(error => console.log('Error fetching categories:', error));
    })

    return (
        <nav className="navbar navbar-expand-sm sticky-top">
            <Link className="navbar-brand" to="/">
                <img src={logo} alt="Logo" />
            </Link>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item active">
                        <Link className="nav-link" to="/shop">Shop</Link>
                    </li>
                    <li className="nav-item active">
                        <Link className="nav-link" to="/contact">Contact</Link>
                    </li>
                    <li className="nav-item active">
                        {isAuthenticated ? (
                            <a className="nav-link" onClick={logout} style={{ cursor: "pointer" }}>Logout</a>
                        ) : (
                            <Link className="nav-link" to="/login">Login</Link>
                        )}
                    </li>
                    <li className="nav-item active">
                        <Link className="nav-link" to="/about">About Us</Link>
                    </li>
                </ul>
                <div className="right-icons">
                    <div className="search-bar">
                        <form action="/search">
                            <input type="text" placeholder="Search..." name="search" className="search-input" />
                            <button type="submit" className="search-button"><i className="fas fa-search"></i></button>
                        </form>
                    </div>
                    <div className="profile">
                        <Link to='/profile'>
                            <img src={userIcon} alt="profile" />
                        </Link>
                    </div>
                    <div className="cart" id="cart">
                        <div className="cart-summary">
                            <img src={cartIcon} alt="cart" />
                            <div className="item-count">0</div>
                        </div>
                        <div className="cart-details">
                            <ul></ul>
                            <button className="btn btn-primary-outline-success">
                                <Link to="/cart">Go to Cart</Link>
                            </button>
                        </div>
                    </div>
                    <HamburgerMenu categories={categories} />
                </div>
            </div>
        </nav>
    )
}


export default Header;