import React, { useState, useEffect } from 'react';
import { getCurrentUserId } from '../../../scripts/security';

interface ConsultaFormData {
  type: string;
  date: string;
  time: string;
  client_id: string;
}

const DateForm: React.FC = () => {
  // Estado para los datos del formulario
  const [formData, setFormData] = useState<ConsultaFormData>({
    type: 'consulta',
    date: '',
    time: '',
    client_id: '', // Este valor se obtendrá del JWT
  });

  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [fetchingClientId, setFetchingClientId] = useState<boolean>(true);

  useEffect(() => {
    // Obtener el client_id del JWT utilizando la función del módulo de seguridad
    const userId = getCurrentUserId() || '3fa85f64-5717-4562-b3fc-2c963f66afa6';

    const fetchClientId = async () => {
      try {
        setFetchingClientId(true);
        const response = await fetch(`https://apipris.kysedomi.lat/clients/user/${userId}`);

        if (!response.ok) {
          throw new Error('No se pudo obtener la información del cliente');
        }

        const clientData = await response.json();
        // Usamos el id del cliente, no el user_id
        console.log('ID del cliente:', clientData);
        setFormData(prev => ({ ...prev, client_id: clientData.id }));
      } catch (err) {
        console.error('Error al obtener ID de cliente:', err);
        setError('No se pudo obtener la información del cliente. Intente más tarde.');
        // Usar el userId como fallback en caso de error
        setFormData(prev => ({ ...prev, client_id: userId }));
      } finally {
        setFetchingClientId(false);
      }
    };

    fetchClientId();
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // Preparamos los datos en el formato esperado por la API
      // La fecha debe estar en formato YYYY-MM-DD
      // La hora debe enviarse como un campo separado

      const requestData = {
        type: formData.type,
        date: formData.date, // Solo enviamos la fecha
        time: formData.time, // Enviamos la hora como campo separado
        client_id: formData.client_id,
      };

      console.log('Enviando datos:', requestData);

      // Realizar la llamada a la API
      const response = await fetch('https://apipris.kysedomi.lat/dates/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || errorData.message || 'Error al crear la consulta');
      }

      const data = await response.json();
      console.log('Respuesta del servidor:', data);
      setSuccess(true);

      // Reset form after success
      setFormData({
        type: 'consulta',
        date: '',
        time: '',
        client_id: formData.client_id,
      });

      // Ocultar mensaje de éxito después de 3 segundos
      setTimeout(() => setSuccess(false), 3000);

    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error desconocido al crear la consulta');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full">
      {error && (
        <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg">
          {error}
        </div>
      )}

      {success && (
        <div className="mb-4 p-3 bg-green-50 border border-green-200 text-green-700 rounded-lg">
          ¡Consulta creada exitosamente!
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        {fetchingClientId && (
          <div className="mb-4 p-3 bg-blue-50 border border-blue-200 text-blue-700 rounded-lg">
            Cargando información del cliente...
          </div>
        )}

        <div className="space-y-2">
          <label htmlFor="type" className="block text-sm font-medium text-gray-700">
            Tipo de Consulta:
          </label>
          <select
            id="type"
            name="type"
            value={formData.type}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-gray-700"
            required
          >
            <option value="consulta">Primera Consulta</option>
            <option value="seguimiento">Seguimiento</option>
          </select>
        </div>

        <div className="space-y-2">
          <label htmlFor="date" className="block text-sm font-medium text-gray-700">
            Fecha:
          </label>
          <input
            type="date"
            id="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-gray-700"
            required
          />
        </div>

        <div className="space-y-2">
          <label htmlFor="time" className="block text-sm font-medium text-gray-700">
            Hora:
          </label>
          <input
            type="time"
            id="time"
            name="time"
            value={formData.time}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-gray-700"
            required
          />
        </div>

        <button
          type="submit"
          disabled={loading || fetchingClientId}
          className={`w-full py-2 px-4 rounded-md text-white font-medium ${
            (loading || fetchingClientId) ? 'bg-gray-400 cursor-not-allowed' : 'bg-gray-800 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-700 focus:ring-offset-2'
          }`}
        >
          {loading ? 'Enviando...' : 'Crear Consulta'}
        </button>
      </form>
    </div>
  );
};

export default DateForm;

