import React, { useState, useEffect } from 'react';
import { getCurrentUserId } from '../../../scripts/security';
import AppointmentModal from '../AppointmentModal';

const ButtonDate: React.FC = () => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [showLoginMessage, setShowLoginMessage] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [clientId, setClientId] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    // Verificación básica de autenticación
    const userId = getCurrentUserId();
    setIsAuthenticated(!!userId && userId !== '3fa85f64-5717-4562-b3fc-2c963f66afa6');
  }, []);

  const handleClick = async () => {
    if (!isAuthenticated) {
      // Mostrar mensaje de advertencia si no está autenticado
      setShowLoginMessage(true);
      setTimeout(() => setShowLoginMessage(false), 3000);
      return;
    }
    
    try {
      setLoading(true);
      // Obtenemos el userId utilizando la misma función que en DateForm
      const userId = getCurrentUserId() || '3fa85f64-5717-4562-b3fc-2c963f66afa6';
      
      // Usamos el mismo endpoint que DateForm para obtener el ID del cliente
      const response = await fetch(`https://apipris.kysedomi.lat/clients/user/${userId}`);
      
      if (!response.ok) {
        throw new Error('No se pudo obtener la información del cliente');
      }
      
      const clientData = await response.json();
      console.log('ID del cliente:', clientData);
      setClientId(clientData.id);
      
      // Abrir el modal si todo es correcto
      setIsModalOpen(true);
      
    } catch (error) {
      console.error('Error al obtener ID de cliente:', error);
      setShowLoginMessage(true);
      setTimeout(() => setShowLoginMessage(false), 3000);
    } finally {
      setLoading(false);
    }
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <>
      {/* Mensaje de advertencia cuando no hay cliente */}
      {showLoginMessage && (
        <div className="fixed top-4 left-1/2 transform -translate-x-1/2 bg-yellow-100 border-l-4 border-yellow-500 text-yellow-700 p-4 rounded shadow-md z-50 transition-opacity">
          <p className="font-bold">Información requerida</p>
          <p>Debe iniciar sesión para agendar una cita.</p>
        </div>
      )}

      {/* Botón para abrir el modal - Estilo actualizado */}
      <button 
        onClick={handleClick} 
        disabled={loading}
        className="inline-flex items-center justify-center rounded-md bg-[#44c7d7] hover:bg-[#44c7d7]/90 text-white shadow-md px-6 py-3 text-sm font-medium transition-all"
      >
        <svg 
          xmlns="http://www.w3.org/2000/svg" 
          className="mr-2 h-5 w-5" 
          width="24" 
          height="24" 
          viewBox="0 0 24 24" 
          fill="none" 
          stroke="currentColor" 
          strokeWidth="2" 
          strokeLinecap="round" 
          strokeLinejoin="round"
        >
          <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
          <line x1="16" y1="2" x2="16" y2="6"></line>
          <line x1="8" y1="2" x2="8" y2="6"></line>
          <line x1="3" y1="10" x2="21" y2="10"></line>
        </svg>
        {loading ? 'Cargando...' : 'Agendar Cita'}
      </button>

      {/* Modal de citas integrado directamente */}
      {isModalOpen && (
        <AppointmentModal 
          isOpen={isModalOpen} 
          onClose={closeModal}
          clientId={clientId}
        />
      )}
    </>
  );
};

export default ButtonDate;

