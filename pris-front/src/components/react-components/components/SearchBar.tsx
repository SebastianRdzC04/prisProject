"use client"

import type React from "react"
import { useState } from "react"
import { Search } from "lucide-react"

interface SearchBarProps {
    onSearch?: (query: string) => void
    placeholder?: string
    className?: string
}

export default function SearchBar({ onSearch, placeholder = "Search...", className = "" }: SearchBarProps) {
    const [query, setQuery] = useState("")

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        if (onSearch) {
            onSearch(query)
        }
    }

    return (
        <form onSubmit={handleSubmit} className={`flex w-full items-center space-x-2 ${className}`}>
            <div className="relative flex-1">
                <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
                <input
                    type="text"
                    placeholder={placeholder}
                    value={query}
                    onChange={(e: React.ChangeEvent<HTMLInputElement>) => setQuery(e.target.value)}
                    className="w-full px-3 py-2 pl-8 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
            </div>
            <button
                type="submit"
                className="x-4 py-2 px-3 bg-gray-800 text-white rounded hover:bg-gray-800 transition-colors"
            >
                Buscar
            </button>
        </form>
    )
}