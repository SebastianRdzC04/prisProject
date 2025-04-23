"use client"

import { Search } from "lucide-react"
import { format } from "date-fns"
import { es } from "date-fns/locale"

// Definición del tipo para los datos de la API
interface ApiDate {
    id: string
    type: string
    date: string
    time: string
    status: string
    client_id: string
    client: {
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
}

// Definición del tipo de objeto para las citas
interface Cita {
    nombreCliente: string
    fecha: Date | string
    hora: string
    status: string
}

// Props del componente
interface TablaCitasProps {
    citas: ApiDate[] // Cambiamos a recibir el formato de la API
}

export default function TableCites({ citas = [] }: TablaCitasProps) {
    // Formatear fecha para mostrarla de manera legible
    const formatearFecha = (fecha: Date | string) => {
        if (typeof fecha === "string") {
            fecha = new Date(fecha)
        }
        return format(fecha, "EEEE d 'de' MMMM 'de' yyyy", { locale: es })
    }

    // Convertir los datos de la API al formato que necesita nuestra tabla
    const citasFormateadas: Cita[] = citas.map(cita => ({
        nombreCliente: `${cita.client.user.personal_data.first_name} ${cita.client.user.personal_data.last_name}`,
        fecha: cita.date,
        hora: cita.time,
        status: cita.status
    }))

    return (
        <div className="w-full border border-gray-300 rounded-lg overflow-hidden shadow-lg">
            <div className="bg-gray-800 p-4">
                <h3 className="text-xl font-medium text-white">Agenda de Citas</h3>
            </div>
            <div className="p-0 bg-white">
                {citasFormateadas.length > 0 ? (
                    <table className="w-full">
                        <thead>
                        <tr className="border-b">
                            <th className="w-[30%] text-left p-3 text-gray-800">Paciente</th>
                            <th className="w-[30%] text-left p-3 text-gray-800">Fecha</th>
                            <th className="w-[20%] text-left p-3 text-gray-800">Hora</th>
                            <th className="w-[20%] text-left p-3 text-gray-800">Estado</th>
                        </tr>
                        </thead>
                        <tbody>
                        {citasFormateadas.map((cita, index) => (
                            <tr key={index} className="hover:bg-gray-100 border-b">
                                <td className="font-medium p-3">{cita.nombreCliente}</td>
                                <td className="p-3">{formatearFecha(cita.fecha)}</td>
                                <td className="p-3">{cita.hora}</td>
                                <td className="p-3">{cita.status}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                ) : (
                    <div className="flex flex-col items-center justify-center py-12 px-4 text-center">
                        <div className="rounded-full bg-gray-100 p-4">
                            <Search className="h-8 w-8 text-gray-600" />
                        </div>
                        <h3 className="mt-4 text-lg font-medium text-gray-800">No hay citas programadas</h3>
                        <p className="mt-2 text-sm text-gray-500">
                            Cuando se agreguen citas, aparecerán aquí.
                        </p>
                        <button className="mt-4 px-4 py-2 bg-gray-800 text-white rounded hover:bg-gray-700 transition-colors">
                            Agendar nueva cita
                        </button>
                    </div>
                )}
            </div>
        </div>
    )
}