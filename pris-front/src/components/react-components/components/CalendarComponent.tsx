"use client"

import * as React from "react"
import { ChevronLeft, ChevronRight } from "lucide-react"
import {
    format,
    addMonths,
    subMonths,
    startOfMonth,
    endOfMonth,
    eachDayOfInterval,
    isSameMonth,
    isSameDay,
    isToday,
    isBefore,
    addYears
} from "date-fns"
import { es } from "date-fns/locale"

type CalendarProps = {
    closedDays: Date[]
    possibleDays: Date[]
    disabledDays: Date[]
    closedColor?: string
    possibleColor?: string
    disabledColor?: string
    onSelectDate?: (date: Date) => void
    className?: string
}

export function Calendar({
                             closedDays = [],
                             possibleDays = [],
                             disabledDays = [],
                             closedColor = "bg-red-200 hover:bg-red-300",
                             possibleColor = "bg-green-200 hover:bg-green-300",
                             disabledColor = "bg-gray-200",
                             onSelectDate,
                             className,
                         }: CalendarProps) {
    const [currentMonth, setCurrentMonth] = React.useState(new Date())

    // Fecha límite: un año desde hoy
    const oneYearFromNow = React.useMemo(() => addYears(new Date(), 1), [])

    // Verificar si el siguiente mes excede el límite de un año
    const isNextMonthBeyondLimit = React.useMemo(() => {
        const nextMonthDate = addMonths(currentMonth, 1)
        return !isBefore(startOfMonth(nextMonthDate), startOfMonth(oneYearFromNow))
    }, [currentMonth, oneYearFromNow])

    const nextMonth = () => {
        // Solo avanzar si no excede el límite de un año
        if (!isNextMonthBeyondLimit) {
            setCurrentMonth(addMonths(currentMonth, 1))
        }
    }

    const prevMonth = () => {
        setCurrentMonth(subMonths(currentMonth, 1))
    }

    const monthStart = startOfMonth(currentMonth)
    const monthEnd = endOfMonth(currentMonth)
    const daysInMonth = eachDayOfInterval({ start: monthStart, end: monthEnd })

    // Create a 7x6 grid for the calendar
    const startDay = monthStart.getDay()
    const endDay = 6 - monthEnd.getDay()

    // Get days from previous month to fill the first row
    const prevMonthDays =
        startDay > 0
            ? eachDayOfInterval({
                start: subMonths(monthStart, 1),
                end: subMonths(monthStart, 1),
            }).slice(-startDay)
            : []

    // Get days from next month to fill the last row
    const nextMonthDays =
        endDay > 0
            ? eachDayOfInterval({
                start: addMonths(monthEnd, 0),
                end: addMonths(monthEnd, 0),
            }).slice(0, endDay)
            : []

    // Combine all days
    const calendarDays = [...prevMonthDays, ...daysInMonth, ...nextMonthDays]

    // Helper function to check if a date is in an array of dates
    const isDateInArray = (date: Date, dateArray: Date[]) => {
        return dateArray.some((d) => isSameDay(date, d))
    }

    // Get the appropriate class for a day
    const getDayClass = (day: Date) => {
        if (isDateInArray(day, closedDays)) {
            return closedColor
        } else if (isDateInArray(day, possibleDays)) {
            return possibleColor
        } else if (isDateInArray(day, disabledDays)) {
            return disabledColor
        }
        return "bg-white hover:bg-gray-100"
    }

    // Days of the week
    const weekDays = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]

    return (
        <div className={`w-full max-w-5/6 mx-auto ${className || ''}`}>
            <div className="flex items-center justify-between mb-4">
                <button
                    className="h-9 w-9 rounded-md border border-gray-300 flex items-center justify-center hover:bg-gray-100"
                    onClick={prevMonth}
                    aria-label="Mes anterior"
                >
                    <ChevronLeft className="h-4 w-4" />
                </button>
                <h2 className="text-lg font-semibold">{format(currentMonth, "MMMM yyyy", { locale: es })}</h2>
                <button
                    className={`h-9 w-9 rounded-md border border-gray-300 flex items-center justify-center 
                    ${isNextMonthBeyondLimit
                        ? 'opacity-50 cursor-not-allowed bg-gray-100'
                        : 'hover:bg-gray-100'}`}
                    onClick={nextMonth}
                    aria-label="Mes siguiente"
                    disabled={isNextMonthBeyondLimit}
                >
                    <ChevronRight className="h-4 w-4" />
                </button>
            </div>

            {/* Resto del código igual... */}
            <div className="grid grid-cols-7 gap-1 mb-2">
                {weekDays.map((day) => (
                    <div key={day} className="text-center text-sm font-medium text-gray-500">
                        {day}
                    </div>
                ))}
            </div>

            <div className="grid grid-cols-7 gap-1">
                {calendarDays.map((day, i) => {
                    const isCurrentMonth = isSameMonth(day, currentMonth)
                    const isDisabled = !isCurrentMonth || isDateInArray(day, disabledDays)

                    // Construir las clases manualmente
                    let buttonClasses = "h-10 w-full rounded-md text-sm font-medium transition-colors flex items-center justify-center";

                    if (isCurrentMonth) {
                        buttonClasses += ` ${getDayClass(day)}`;
                    } else {
                        buttonClasses += " text-gray-400 bg-gray-50";
                    }

                    if (isToday(day)) {
                        buttonClasses += " border border-blue-500";
                    }

                    if (isDisabled) {
                        buttonClasses += " cursor-not-allowed opacity-50";
                    }

                    return (
                        <button
                            key={i}
                            onClick={() => !isDisabled && onSelectDate && onSelectDate(day)}
                            disabled={isDisabled}
                            className={buttonClasses}
                        >
                            {format(day, "d")}
                        </button>
                    )
                })}
            </div>

            <div className="mt-4 grid grid-cols-3 gap-2">
                <div className="flex items-center">
                    <div className={`w-4 h-4 rounded mr-2 ${closedColor}`}></div>
                    <span className="text-sm">Días cerrados</span>
                </div>
                <div className="flex items-center">
                    <div className={`w-4 h-4 rounded mr-2 ${possibleColor}`}></div>
                    <span className="text-sm">Días posibles</span>
                </div>
                <div className="flex items-center">
                    <div className={`w-4 h-4 rounded mr-2 ${disabledColor}`}></div>
                    <span className="text-sm">Días deshabilitados</span>
                </div>
            </div>
        </div>
    )
}