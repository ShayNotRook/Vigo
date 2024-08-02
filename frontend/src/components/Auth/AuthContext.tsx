import React, { createContext, useContext, useState, ReactNode, useEffect} from 'react';


interface AutContextType {
    isAuthenticated : boolean;
    login: (username: string, password: string) => Promise<void>;
    logout: () => void;
}

const AuthContext = createContext<AutContextType | undefined>(undefined);


export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
}


export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }): any => {
    const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token) { 
            setIsAuthenticated(true);
        }
    }, []);

    const login = async(username: string, password: string) => {
        const response = await fetch('/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        }) 
    }
}
