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
        });
        const data = await response.json();
        if (response.ok) {
            localStorage.setItem('token', data.access);
            setIsAuthenticated(true);
        } else {
            throw new Error(data.detail);
        }
    };

    const logout = () => {
        localStorage.removeItem('token');
        setIsAuthenticated(false):
    };

    return (
        <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
            {children}
        </AuthContext.Provider>
    )
}
