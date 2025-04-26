import React, { useState, useEffect } from 'react';
import DateForm from './pages/DateForm';
import { getCurrentUserId } from '../../scripts/security';

interface AppointmentModalProps {
  isOpen: boolean;
  onClose: () => void;
  clientId?: string | null;
}

const AppointmentModal: React.FC<AppointmentModalProps> = ({ isOpen, onClose, clientId: propClientId }) => {
  const [localClientId, setLocalClientId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Si se proporciona clientId como prop, usarlo directamente
    if (propClientId) {
      setLocalClientId(propClientId);
      return;
    }
    
    // Si no hay clientId en props y el modal está abierto, intentar obtenerlo
    if (isOpen && !propClientId) {
      const fetchClientId = async () => {
        try {
          const userId = getCurrentUserId();
          
          if (!userId || userId === '3fa85f64-5717-4562-b3fc-2c963f66afa6') {
            setError('No se ha iniciado sesión');
            return;
          }
          
          const response = await fetch(`https://apipris.kysedomi.lat/clients/user/${userId}`);
          
          if (!response.ok) {
            throw new Error('No se pudo obtener la información del cliente');
          }
          
          const clientData = await response.json();
          console.log('ID del cliente:', clientData);
          setLocalClientId(clientData.id);
          setError(null);
        } catch (err) {
          console.error('Error al obtener ID de cliente:', err);
          setError('No se pudo obtener la información del cliente. Intente más tarde.');
          setLocalClientId(null);
        }
      };
      
      fetchClientId();
    }
  }, [isOpen, propClientId]);

  // No renderizar nada si el modal está cerrado
  if (!isOpen) {
    return null;
  }

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50">
      {/* Fondo oscuro */}
      <div 
        className="fixed inset-0 bg-black bg-opacity-50 transition-opacity" 
        onClick={onClose}
      ></div>
      
      {/* Contenedor del modal */}
      <div className="bg-white rounded-lg shadow-xl z-10 w-11/12 max-w-2xl max-h-[90vh] overflow-y-auto relative">
        {/* Botón para cerrar */}
        <button 
          onClick={onClose}
          className="absolute top-4 right-4 text-gray-500 hover:text-gray-700 focus:outline-none"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
        
        {/* Contenido del modal */}
        <div className="p-6 space-y-6 bg-white rounded-lg">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Agendar Nueva Cita</h2>
          
          {error ? (
            <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 rounded">
              <p className="font-bold">Error</p>
              <p>{error}</p>
            </div>
          ) : !propClientId && !localClientId ? (
            <div className="flex items-center justify-center p-4">
              <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-gray-900"></div>
              <span className="ml-2">Cargando información...</span>
            </div>
          ) : (
            <DateForm/>
          )}
        </div>
      </div>
    </div>
  );
};

export default AppointmentModal;
