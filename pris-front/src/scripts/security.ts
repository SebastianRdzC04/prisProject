// Función para decodificar el token JWT
export function parseJwt(token: string): any {
    try {
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        const payload = decodeURIComponent(atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));

        return JSON.parse(payload);
    } catch (e) {
        console.error('Error decodificando token:', e);
        return null;
    }
}

// Obtener el token del localStorage
export function getToken(): string | null {
    return localStorage.getItem('token');
}

// Verificar si el token es válido mediante una llamada a la API
export async function verifyToken(token: string): Promise<boolean> {
    try {
        const response = await fetch(`https://apipris.kysedomi.lat/auth/verify?token=${token}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
        });
        
        return response.status === 200;
    } catch (error) {
        console.error('Error verificando token:', error);
        return false;
    }
}

// Obtener la información del token decodificado
export function getTokenPayload(): any {
    const token = getToken();
    if (!token) return null;
    
    return parseJwt(token);
}

// Verificar si el usuario está logueado
export function isLoggedIn(): boolean {
    return getToken() !== null;
}

// Verificar si el usuario es administrador
export function isAdmin(): boolean {
    const payload = getTokenPayload();
    return payload && payload.is_admin === true;
}

// Obtener el ID del usuario actual
export function getCurrentUserId(): string | null {
    const payload = getTokenPayload();
    return payload ? payload.id : null;
}

// Obtener datos del usuario según su ID y rol
export async function getUserData(userId: string, isAdmin: boolean): Promise<any> {
    try {
        const endpoint = isAdmin 
            ? `https://apipris.kysedomi.lat/admin/user/${userId}`
            : `https://apipris.kysedomi.lat/clients/user/${userId}`;
            
        const response = await fetch(endpoint);
        
        if (response.status === 200) {
            return await response.json();
        } else {
            console.error('Error obteniendo datos del usuario');
            return null;
        }
    } catch (error) {
        console.error('Error en getUserData:', error);
        return null;
    }
}

// Verificar autenticación y obtener datos del usuario
export async function checkAuthentication(): Promise<any> {
    const token = getToken();
    
    if (!token) {
        return null;
    }

    try {
        const isValid = await verifyToken(token);
        
        if (!isValid) {
            localStorage.removeItem('token');
            return null;
        }
        
        const payload = getTokenPayload();
        
        if (!payload || !payload.id) {
            console.error('Token payload es inválido');
            return null;
        }
        
        const userId = payload.id;
        const admin = isAdmin();
        
        return await getUserData(userId, admin);
    } catch (error) {
        console.error('Error en checkAuthentication:', error);
        return null;
    }
}

// Cerrar sesión
export function logout(): void {
    localStorage.removeItem('token');
}
