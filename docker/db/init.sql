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

CREATE TYPE date_types AS ENUM('primera cita', 'seguimiento de tratamiento');

create table dates(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id uuid REFERENCES clients(id),
    date_type date_types not null,
    date DATE NOT NULL,
    time TIME NOT NULL,
    is_on boolean DEFAULT true
);

CREATE TABLE appointments (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id uuid REFERENCES clients(id),
    date_id uuid REFERENCES dates(id),
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE treatments(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    duration INT NOT NULL,
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







