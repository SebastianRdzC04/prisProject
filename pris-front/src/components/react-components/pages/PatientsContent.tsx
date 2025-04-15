"use client"

import React from "react"
import SearchBar from "../components/SearchBar"
import TablePatients from "../components/TablePatients.tsx";

export default function PatientsContent() {
    const handleSearch = (query: string) => {
        console.log("Búsqueda realizada:", query)
        // Aquí puedes implementar la lógica de búsqueda
    }

    const cites: any[] = []

    return (
        <div className="space-y-6 p-6 bg-white rounded-lg ">
            <SearchBar
                onSearch={handleSearch}
                placeholder="Buscar pacientes..."
                className=""
            />
            <TablePatients pacientes={cites}/>


        </div>
    )
}