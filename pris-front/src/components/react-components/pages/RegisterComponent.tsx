"use client"

import { useState } from "react"

export default function RegisterForm() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [isLoading, setIsLoading] = useState(false)
    const [notification, setNotification] = useState({ show: false, type: "", message: "" })

    const showNotification = (type: string, message: string) => {
        setNotification({ show: true, type, message })
        setTimeout(() => {
            setNotification({ show: false, type: "", message: "" })
        }, 3000)
    }

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        setIsLoading(true)

        try {
            const response = await fetch("https://apipris.kysedomi.lat/auth/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email, password }),
            })

            const data = await response.json()

            if (!response.ok) {
                throw new Error(data.message || "Error al registrarse")
            }

            showNotification("success", "Tu cuenta ha sido creada correctamente. Ahora puedes iniciar sesión.")

            // Limpiar el formulario
            setEmail("")
            setPassword("")
        } catch (error: any) {
            showNotification("error", error.message || "Ocurrió un error al registrarse")
        } finally {
            setIsLoading(false)
        }
    }

    return (
        <div>
            {notification.show && (
                <div className={`p-3 mb-4 rounded-lg text-sm ${
                    notification.type === "success"
                        ? "bg-green-100 text-green-800"
                        : "bg-red-100 text-red-800"
                }`}>
                    {notification.message}
                </div>
            )}

            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label htmlFor="email-register" className="block text-sm font-medium text-gray-700 mb-1">
                        Correo electrónico
                    </label>
                    <input
                        id="email-register"
                        type="email"
                        placeholder="correo@ejemplo.com"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    />
                </div>
                <div>
                    <label htmlFor="password-register" className="block text-sm font-medium text-gray-700 mb-1">
                        Contraseña
                    </label>
                    <input
                        id="password-register"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    />
                </div>
                <button
                    type="submit"
                    disabled={isLoading}
                    className={`w-full py-2 px-4 bg-gray-800 text-white rounded-md hover:bg-gray-700 transition-colors ${
                        isLoading ? "opacity-70 cursor-not-allowed" : ""
                    }`}
                >
                    {isLoading ? (
                        <span className="flex items-center justify-center">
                            <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            Procesando...
                        </span>
                    ) : (
                        "Registrarse"
                    )}
                </button>
            </form>
        </div>
    )
}