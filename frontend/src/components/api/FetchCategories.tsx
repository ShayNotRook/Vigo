import { Item } from "./FetchItems";


const API_URL = '/api/categories/';


export const fetchTopCategories = async(): Promise<Category[]> => {
    const response = await fetch(`${API_URL}top_level_categories/`);
    if (!response.ok) {
        throw new Error(`HTTP Error! Status: ${response.status}`)
    }
    return response.json()
}


export interface Category {
    id: number;
    title: string;
    url: string;
    slug: string;
    subcategories: Category[];
    products: Item[];
}