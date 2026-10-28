CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    email VARCHAR(160) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    tipo VARCHAR(20) NOT NULL DEFAULT 'cliente',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE imoveis (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT NOT NULL,
    preco DECIMAL(12,2) NOT NULL CHECK (preco > 0),
    tipo VARCHAR(30) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL,
    endereco VARCHAR(180) NOT NULL,
    quartos INTEGER NOT NULL DEFAULT 0,
    banheiros INTEGER NOT NULL DEFAULT 0,
    usuario_id INTEGER NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE favoritos (
    id INTEGER PRIMARY KEY,
    usuario_id INTEGER NOT NULL,
    imovel_id INTEGER NOT NULL,
    UNIQUE(usuario_id, imovel_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (imovel_id) REFERENCES imoveis(id) ON DELETE CASCADE
);
