CREATE TABLE machines(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    is_on boolean DEFAULT true
);

CREATE TABLE users (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_on boolean DEFAULT true
);

CREATE TABLE personal_data (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE admins (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id),
    is_on boolean DEFAULT true
);
CREATE TABLE clients (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id),
    is_on boolean DEFAULT true
);

CREATE TABLE workers (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id),
    is_on boolean DEFAULT true
);

CREATE TABLE history(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    machine_id uuid REFERENCES machines(id),
    client_id uuid REFERENCES clients(id),
    action VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TYPE date_types AS ENUM('consulta', 'seguimiento');
CREATE TYPE date_status AS ENUM('pendiente', 'confirmada', 'cancelada', 'finalizada');

create table dates(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id uuid REFERENCES clients(id),
    type date_types not null,
    status date_status not null DEFAULT 'pendiente',
    date DATE NOT NULL,
    time TIME NOT NULL,
    is_on boolean DEFAULT true
);


CREATE TYPE appoitment_status AS ENUM('en proceso', 'finalizada');
CREATE TABLE appointments (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id uuid REFERENCES clients(id),
    date_id uuid REFERENCES dates(id),
    status appoitment_status NOT NULL DEFAULT 'en proceso',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TYPE treatment_status AS ENUM('en proceso', 'finalizado', 'cancelado');

CREATE TABLE treatments(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    duration INT NOT NULL,
    status treatment_status NOT NULL DEFAULT 'en proceso',
    price INT NOT NULL,
    is_on boolean DEFAULT true
);

CREATE TABLE treatment_details(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    date_id uuid REFERENCES dates(id),
    treatment_id uuid REFERENCES treatments(id),
    machine_id uuid REFERENCES machines(id),
    session_number INT NOT NULL,
    is_on boolean DEFAULT true
);




-- Insertar máquinas (necesarias para referencias posteriores)
INSERT INTO machines (name) VALUES
                                ('Láser Depilación Alpha X3'),
                                ('Radiofrecuencia Tensor Pro'),
                                ('Criolipólisis CryoSculpt'),
                                ('LPG Endermologie'),
                                ('Láser Rejuvenecimiento Skin Pro'),
                                ('Presoterapia Digital'),
                                ('Ultrasonido Cavitacional'),
                                ('HIFU Facial'),
                                ('Electroestimulación Muscular'),
                                ('Microdermoabrasión Avanzada');

-- Insertar 50 usuarios
INSERT INTO users (email, password) VALUES
                                        ('maria.lopez@email.com', '$2a$10$XyZ123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('carlos.rodriguez@email.com', '$2a$10$AbC123XyZdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('ana.martinez@email.com', '$2a$10$CdE123AbCXyZfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('juan.perez@email.com', '$2a$10$EfG123AbCdXyZhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('laura.sanchez@email.com', '$2a$10$GhI123AbCdEfXyZjK.lmnOPQrStUvWxYz12345678'),
                                        ('pedro.diaz@email.com', '$2a$10$IjK123AbCdEfGhXyZ.lmnOPQrStUvWxYz12345678'),
                                        ('carmen.torres@email.com', '$2a$10$KlM123AbCdEfGhIjXyZ.nOPQrStUvWxYz12345678'),
                                        ('javier.gonzalez@email.com', '$2a$10$MnO123AbCdEfGhIjK.XyZPQrStUvWxYz12345678'),
                                        ('sofia.ruiz@email.com', '$2a$10$OPQ123AbCdEfGhIjK.lmXyZrStUvWxYz12345678'),
                                        ('miguel.herrera@email.com', '$2a$10$QrS123AbCdEfGhIjK.lmXyZPtUvWxYz12345678'),
                                        ('elena.gomez@email.com', '$2a$10$StU123AbCdEfGhIjK.lmnOPQrVwXyZ12345678'),
                                        ('david.castro@email.com', '$2a$10$UvW123AbCdEfGhIjK.lmnOPQrStXyZ12345678'),
                                        ('cristina.moreno@email.com', '$2a$10$Wxy123AbCdEfGhIjK.lmnOPQrStUvZ12345678'),
                                        ('jose.navarro@email.com', '$2a$10$YzA123AbCdEfGhIjK.lmnOPQrStUvWx12345678'),
                                        ('raquel.ortiz@email.com', '$2a$10$AaB123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('fernando.jimenez@email.com', '$2a$10$BbC123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('lucia.romero@email.com', '$2a$10$CcD123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('pablo.serrano@email.com', '$2a$10$DdE123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('natalia.molina@email.com', '$2a$10$EeF123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('roberto.ramos@email.com', '$2a$10$FfG123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('susana.alonso@email.com', '$2a$10$GgH123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('alberto.gutierrez@email.com', '$2a$10$HhI123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('monica.santos@email.com', '$2a$10$IiJ123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('victor.martin@email.com', '$2a$10$JjK123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('patricia.dominguez@email.com', '$2a$10$KkL123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('ismael.vazquez@email.com', '$2a$10$LlM123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('alicia.suarez@email.com', '$2a$10$MmN123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('hector.blanco@email.com', '$2a$10$NnO123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('esther.flores@email.com', '$2a$10$OoP123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('joaquin.delgado@email.com', '$2a$10$PpQ123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('teresa.vega@email.com', '$2a$10$QqR123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('ignacio.leon@email.com', '$2a$10$RrS123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('pilar.rios@email.com', '$2a$10$SsT123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('ricardo.guerra@email.com', '$2a$10$TtU123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('silvia.mendez@email.com', '$2a$10$UuV123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('daniel.pascual@email.com', '$2a$10$VvW123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('dolores.bravo@email.com', '$2a$10$WwX123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('adrian.rojas@email.com', '$2a$10$XxY123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('mercedes.fuentes@email.com', '$2a$10$YyZ123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('diego.nieto@email.com', '$2a$10$ZzA123AbCdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('victoria.iglesias@email.com', '$2a$10$AaB123CdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('guillermo.medina@email.com', '$2a$10$BbC123DdEfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('olga.carrasco@email.com', '$2a$10$CcD123EeFfGhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('mario.cortes@email.com', '$2a$10$DdE123FfGgHhIjK.lmnOPQrStUvWxYz12345678'),
                                        ('lidia.nunez@email.com', '$2a$10$EeF123GgHhIiJjK.lmnOPQrStUvWxYz12345678'),
                                        ('enrique.villanueva@email.com', '$2a$10$FfG123HhIiJjKkL.lmnOPQrStUvWxYz12345678'),
                                        ('claudia.gil@email.com', '$2a$10$GgH123IiJjKkLlM.lmnOPQrStUvWxYz12345678'),
                                        ('ruben.soto@email.com', '$2a$10$HhI123JjKkLlMmN.lmnOPQrStUvWxYz12345678'),
                                        ('beatriz.cano@email.com', '$2a$10$IiJ123KkLlMmNnO.lmnOPQrStUvWxYz12345678'),
                                        ('raul.reyes@email.com', '$2a$10$JjK123LlMmNnOoP.lmnOPQrStUvWxYz12345678'),
                                        ('angela.campos@email.com', '$2a$10$KkL123MmNnOoPpQ.lmnOPQrStUvWxYz12345678');

-- Insertar datos personales para los usuarios
INSERT INTO personal_data (user_id, first_name, last_name, birth_date, phone_number, address)
SELECT id,
       CASE
           WHEN position('.' in email) > 0 THEN substring(email from 1 for position('.' in email) - 1)
           ELSE substring(email from 1 for position('@' in email) - 1)
           END as first_name,
       CASE
           WHEN position('.' in email) > 0 AND position('@' in email) > position('.' in email)
               THEN substring(email from position('.' in email) + 1 for position('@' in email) - position('.' in email) - 1)
           ELSE 'Apellido'
           END as last_name,
       '1980-01-01'::date + (random() * 365 * 25)::integer,
       '6' || lpad(floor(random() * 100000000)::text, 8, '0'),
       'Calle ' ||
       CASE
           WHEN position('.' in email) > 0 THEN substring(email from 1 for position('.' in email) - 1)
           ELSE substring(email from 1 for position('@' in email) - 1)
           END || ' ' || floor(random() * 100 + 1)::text || ', Ciudad'
FROM users;

-- Insertar 40 clientes (usuarios 1-40)
INSERT INTO clients (user_id)
SELECT id FROM users ORDER BY id LIMIT 40;

-- Insertar 10 administradores (usuarios 41-50)
INSERT INTO admins (user_id)
SELECT id FROM users ORDER BY id DESC LIMIT 10;

-- Insertar algunos tratamientos
INSERT INTO treatments (user_id, name, description, duration, price, status)
SELECT
    (SELECT id FROM users ORDER BY id DESC LIMIT 1),
    unnest(ARRAY[
        'Depilación Láser Facial',
        'Depilación Láser Piernas',
        'Rejuvenecimiento Facial',
        'Tratamiento Anti-Celulitis',
        'Reducción de Grasa Localizada',
        'Limpieza Facial Profunda',
        'Peeling Químico',
        'Microdermoabrasión',
        'Radiofrecuencia Facial',
        'Tratamiento Anti-Acné'
        ]),
    unnest(ARRAY[
        'Eliminación del vello facial mediante tecnología láser de diodo',
        'Eliminación del vello en piernas mediante láser de alta potencia',
        'Tratamiento para reducir arrugas y mejorar la textura de la piel',
        'Tratamiento combinado para reducir la apariencia de la celulitis',
        'Técnica no invasiva para reducir acumulaciones de grasa',
        'Limpieza profunda con extracción de impurezas y puntos negros',
        'Exfoliación química para renovar la piel y tratar manchas',
        'Exfoliación mecánica para mejorar textura y luminosidad',
        'Tratamiento para tensar la piel y estimular colágeno',
        'Tratamiento especializado para pieles con acné'
        ]),
    unnest(ARRAY[30, 60, 45, 75, 50, 60, 40, 30, 45, 50]),
    unnest(ARRAY[80, 150, 120, 200, 180, 90, 110, 80, 130, 100]),
    unnest(ARRAY['en proceso', 'en proceso', 'finalizado', 'en proceso', 'finalizado', 'en proceso', 'finalizado', 'en proceso', 'en proceso', 'finalizado']::treatment_status[]);

-- Insertar 30 citas
INSERT INTO dates (client_id, type, status, date, time)
SELECT
    client_id,
    CASE WHEN random() > 0.5 THEN 'consulta'::date_types ELSE 'seguimiento'::date_types END,
    (ARRAY['pendiente', 'confirmada', 'cancelada', 'finalizada'])[floor(random() * 4 + 1)]::date_status,
    CURRENT_DATE + floor(random() * 30)::integer,
    ('08:00:00'::time + floor(random() * 18) * interval '30 min')::time
FROM (
         SELECT id AS client_id FROM clients ORDER BY random() LIMIT 30
     ) AS random_clients;

-- Insertar 20 citas programadas (appointments)
INSERT INTO appointments (client_id, date_id)
SELECT
    c.id,
    d.id
FROM
    dates d
        JOIN clients c ON d.client_id = c.id
ORDER BY random() LIMIT 20;

-- Insertar detalles de tratamiento para algunas citas
INSERT INTO treatment_details (date_id, treatment_id, machine_id, session_number)
SELECT
    d.id,
    (SELECT id FROM treatments ORDER BY random() LIMIT 1),
    (SELECT id FROM machines ORDER BY random() LIMIT 1),
    floor(random() * 5 + 1)::integer
FROM
    dates d
ORDER BY random() LIMIT 15;

-- Insertar algunos registros en el historial
INSERT INTO history (machine_id, client_id, action)
SELECT
    (SELECT id FROM machines ORDER BY random() LIMIT 1),
    (SELECT id FROM clients ORDER BY random() LIMIT 1),
    unnest(ARRAY['inicio sesión', 'fin sesión', 'mantenimiento', 'calibración'])
FROM generate_series(1, 25);






