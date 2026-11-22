-- Programação e Desenvolvimento de Banco de Dados
-- U1 A1 - Criação de Tabelas

-- Criação e seleção do banco de dados
CREATE DATABASE IF NOT EXISTS empresa
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE empresa;

-- Criação da tabela funcionarios
DROP TABLE IF EXISTS funcionarios;

CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    departamento VARCHAR(50),
    salario DECIMAL(10, 2),
    data_admissao DATE
);

-- Inserção dos dados de exemplo
INSERT INTO funcionarios (nome, departamento, salario, data_admissao) VALUES
('Ana Silva', 'Financeiro', 5000.00, '2018-03-15'),
('Marcos Teixeira', 'TI', 7000.00, '2019-06-23'),
('Leticia Souza', 'Marketing', 4000.00, '2020-12-01'),
('Pedro Lima', 'TI', 4500.00, '2021-05-11'),
('Carla Gomes', 'Financeiro', 4800.00, '2017-02-20');

-- Consulta de verificação: todos os registros
SELECT * FROM funcionarios;

-- Consulta 1: funcionários do departamento de TI
SELECT * FROM funcionarios WHERE departamento = 'TI';

-- Consulta 2: nome em maiúsculas e departamento, com colunas renomeadas
SELECT
    UPPER(nome) AS `Nome do Funcionário`,
    departamento AS `Área de Atuação`
FROM funcionarios;

-- Consulta 3: total de salários por departamento, do maior para o menor
SELECT
    departamento,
    SUM(salario) AS total_salarios
FROM funcionarios
GROUP BY departamento
ORDER BY total_salarios DESC;

-- Consulta 4: funcionários cujo nome começa com a letra A
SELECT * FROM funcionarios WHERE nome LIKE 'A%';
