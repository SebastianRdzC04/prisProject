"use client"

import { Search } from "lucide-react"

// Definición del tipo para los datos de la API
interface ApiPatient {
    user_id: string
    id: string
    user: {
        email: string
        id: string
        personal_data: {
            first_name: string
            last_name: string
            birth_date: string
            phone_number: string
            address: string
        }
    }
}

// Props del componente
interface TablaPacientesProps {
    pacientes: ApiPatient[]
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
                            <th className="w-[30%] text-left p-3 text-gray-800">Dirección</th>
                            <th className="w-[30%] text-left p-3 text-gray-800">Correo</th>
                        </tr>
                        </thead>
                        <tbody>
                        {pacientes.map((paciente, index) => (
                            <tr key={index} className="hover:bg-gray-100 border-b">
                                <td className="font-medium p-3">
                                    {`${paciente.user.personal_data.first_name} ${paciente.user.personal_data.last_name}`}
                                </td>
                                <td className="p-3">{paciente.user.personal_data.address}</td>
                                <td className="p-3">{paciente.user.email}</td>
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