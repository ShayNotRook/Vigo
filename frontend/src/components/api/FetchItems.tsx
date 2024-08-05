const API_URL = '/api/';


export const fetchItems = async(): Promise<Item[]> => {
    const response = await fetch(`${API_URL}items/`);
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`)
    }
    return response.json();
}


export const fetchItemById = async(id: number): Promise<Item> => {
    const response = await fetch(`${API_URL}items/${id}`);
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`)
    }
    return response.json();
} 




export interface Item {
    id: number;
    name: string;
    price: number;
    description: string;
    platform: string;
    image_url: string;
}