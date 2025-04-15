"use client"

import { Search } from "lucide-react"

// Definición del tipo de objeto para los pacientes
interface Paciente {
    nombre: string
    direccion: string
    enTratamiento: boolean
}

// Props del componente
interface TablaPacientesProps {
    pacientes: Paciente[]
}

export default function TablePatients({ pacientes = [] }: TablaPacientesProps) {
    return (
        <div className="w-full border border-gray-300 rounded-lg overflow-hidden shadow-lg">
            <div className="bg-gray-800 p-4">
                <h3 className="text-xl font-medium text-white">Lista de Pacientes</h3>
            </div>
            <div className="p-0 bg-white">
                {pacientes.length > 0 ? (
                    <table className="w-full">
                        <thead>
                        <tr className="border-b">
                            <th className="w-[40%] text-left p-3 text-gray-800">Nombre</th>
                            <th className="w-[40%] text-left p-3 text-gray-800">Dirección</th>
                            <th className="w-[20%] text-left p-3 text-gray-800">Estado</th>
                        </tr>
                        </thead>
                        <tbody>
                        {pacientes.map((paciente, index) => (
                            <tr key={index} className="hover:bg-gray-100 border-b">
                                <td className="font-medium p-3">{paciente.nombre}</td>
                                <td className="p-3">{paciente.direccion}</td>
                                <td className="p-3">
                                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                                        paciente.enTratamiento
                                            ? "bg-green-100 text-green-800"
                                            : "bg-red-100 text-red-800"
                                    }`}>
                                        {paciente.enTratamiento ? "En tratamiento" : "Sin tratamiento"}
                                    </span>
                                </td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                ) : (
                    <div className="flex flex-col items-center justify-center py-12 px-4 text-center">
                        <div className="rounded-full bg-gray-100 p-4">
                            <Search className="h-8 w-8 text-gray-600" />
                        </div>
                        <h3 className="mt-4 text-lg font-medium text-gray-800">No hay pacientes registrados</h3>
                        <p className="mt-2 text-sm text-gray-500">
                            Cuando se agreguen pacientes, aparecerán aquí.
                        </p>
                        <button className="mt-4 px-4 py-2 bg-gray-800 text-white rounded hover:bg-gray-700 transition-colors">
                            Registrar nuevo paciente
                        </button>
                    </div>
                )}
            </div>
        </div>
    )
}