"use client"

import React, { useState, useEffect } from "react"
import SearchBar from "../components/SearchBar"
import TablePatients from "../components/TablePatients";

export default function PatientsContent() {
    const [pacientes, setPacientes] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchPacientes = async () => {
            try {
                const response = await fetch("https://apipris.kysedomi.lat/clients/");
                const data = await response.json();
                setPacientes(data);
            } catch (error) {
                console.error("Error al obtener los pacientes:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchPacientes();
    }, []);

    const handleSearch = (query: string) => {
        console.log("Búsqueda realizada:", query)
        // Aquí puedes implementar la lógica de búsqueda
    }

    return (
        <div className="space-y-6 p-6 bg-white rounded-lg ">
            <SearchBar
                onSearch={handleSearch}
                placeholder="Buscar pacientes..."
                className=""
            />
            {loading ? (
                <p>Cargando pacientes...</p>
            ) : (
                <TablePatients pacientes={pacientes} />
            )}
        </div>
    )
}