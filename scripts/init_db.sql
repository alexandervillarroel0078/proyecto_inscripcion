CREATE TABLE IF NOT EXISTS carrera (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS plan_estudio (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    año VARCHAR(20) NOT NULL,
    vigente_desde DATE,
    estado BOOLEAN DEFAULT TRUE,
    carrera_id INT NOT NULL REFERENCES carrera(id) ON DELETE CASCADE
);

INSERT INTO carrera (nombre) VALUES ('Ingeniería Informática')
ON CONFLICT DO NOTHING;

INSERT INTO plan_estudio (nombre, año, vigente_desde, estado, carrera_id)
VALUES ('Plan 2025', '2025', '2025-01-01', TRUE, 1)

ON CONFLICT DO NOTHING;
CREATE TABLE IF NOT EXISTS nivel (
    id SERIAL PRIMARY KEY,
    numero INT NOT NULL,
    nombre VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS materia (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(120) NOT NULL,
    creditos INT NOT NULL,
    horas_sem INT NOT NULL,
    nivel_id INT NOT NULL REFERENCES nivel(id) ON DELETE CASCADE,
    plan_id INT NOT NULL REFERENCES plan_estudio(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS prerequisito (
    id SERIAL PRIMARY KEY,
    materia_id INT NOT NULL,
    prerequisito_id INT NOT NULL,
    tipo VARCHAR(20) DEFAULT 'OBLIGATORIO', 
    nota_min INT DEFAULT 51,
    CONSTRAINT fk_materia FOREIGN KEY (materia_id) REFERENCES materia(id),
    CONSTRAINT fk_prerequisito FOREIGN KEY (prerequisito_id) REFERENCES materia(id)
);

 
INSERT INTO nivel (numero, nombre) VALUES 
(1, 'Primer Semestre'),
(2, 'Segundo Semestre'),
(3, 'Tercer Semestre'),
(4, 'Cuarto Semestre')
ON CONFLICT DO NOTHING;


INSERT INTO materia (codigo, nombre, creditos, horas_sem, nivel_id, plan_id)
VALUES 
('MAT101', 'Cálculo I', 5, 5, 1, 1),
('INF119', 'Estructuras Discretas', 4, 4, 1, 1),
('INF110', 'Introducción a la Informática', 4, 4, 1, 1),
('FIS100', 'Física I', 5, 5, 1, 1),
('LIN100', 'Inglés Técnico I', 3, 3, 1, 1),

('MAT102', 'Cálculo II', 5, 5, 2, 1),
('MAT103', 'Álgebra Lineal', 4, 4, 2, 1),
('INF120', 'Programación I', 5, 5, 2, 1),
('FIS102', 'Física II', 5, 5, 2, 1),
('LIN101', 'Inglés Técnico II', 3, 3, 2, 1),

('INF210', 'Programación II', 5, 5, 2, 1),
('INF220', 'Estructuras de Datos I', 5, 5, 3, 1),
('INF310', 'Estructuras de Datos II', 5, 5, 4, 1);

 
INSERT INTO prerequisito (materia_id, prerequisito_id, tipo, nota_min)
VALUES ((SELECT id FROM materia WHERE codigo='INF210'),
        (SELECT id FROM materia WHERE codigo='INF120'),
        'OBLIGATORIO', 51);

 
INSERT INTO prerequisito (materia_id, prerequisito_id, tipo, nota_min)
VALUES ((SELECT id FROM materia WHERE codigo='INF310'),
        (SELECT id FROM materia WHERE codigo='INF220'),
        'OBLIGATORIO', 51);
 
INSERT INTO prerequisito (materia_id, prerequisito_id, tipo, nota_min)
VALUES ((SELECT id FROM materia WHERE codigo='MAT102'),
        (SELECT id FROM materia WHERE codigo='MAT101'),
        'OBLIGATORIO', 51);
