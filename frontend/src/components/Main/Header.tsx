import React, { useState } from "react";
import { Link } from "react-router-dom";
import HamburgerMenu from '../../assets/icons/menu-burger.png';
import logo from '../../../public/vigo-transparent.png';
import userIcon from '../../assets/icons/user.png';
import cartIcon from '../../assets/icons/shopping-cart.png';
import { fetchTopCategories, Category } from "../api/FetchCategories";
import useAuth


const Header: React.FC = () => {
    const {isAuthenticated, logout} = useState
}