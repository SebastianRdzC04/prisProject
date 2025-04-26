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

      {/* Botón para abrir el modal */}
      <button 
        onClick={handleClick} 
        disabled={loading}
        className={`px-4 py-2 ${loading ? 'bg-gray-400' : 'bg-gray-800 hover:bg-gray-700'} text-white rounded-md focus:outline-none focus:ring-2 focus:ring-gray-700 focus:ring-offset-2 transition-colors`}
      >
        {loading ? 'Cargando...' : 'Agendar nueva cita'}
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

