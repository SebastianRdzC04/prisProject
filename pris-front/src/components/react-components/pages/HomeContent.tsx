"use client"

import React, { useState, useEffect } from "react"
import SearchBar from "../components/SearchBar"
import TableCites from "../components/TableCites";

export default function HomeContent() {
    const [citas, setCitas] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchCitas = async () => {
            try {
                const response = await fetch("https://apipris.kysedomi.lat/dates/");
                const data = await response.json();
                setCitas(data);
            } catch (error) {
                console.error("Error al obtener las citas:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchCitas();
    }, []);

    const handleSearch = (query: string) => {
        console.log("Búsqueda realizada:", query)
        // Aquí puedes implementar la lógica de búsqueda
    }

    return (
        <div className="space-y-6 p-6 bg-white rounded-lg">
            <SearchBar
                onSearch={handleSearch}
                placeholder="Buscar Citas..."
                className=""
            />
            {loading ? (
                <p>Cargando citas...</p>
            ) : (
                <TableCites citas={citas} />
            )}
        </div>
    )
}