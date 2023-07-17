CREATE TABLE tbClinica_Petshop(
	idCadrastro	SERIAL PRIMARY KEY,
	NomeCliente	TEXT NOT NULL,
	SexoCliente	CHAR NOT NULL,
	CPF			VARCHAR(14),
	Endereço	VARCHAR(250) NOT NULL,
	Telefone	VARCHAR(15) NOT NULL,
	EspeciedeAnimal TEXT,
	RaçaMultaçãoAnimal TEXT,
	IdadedoAnimal INT, 
	SexoAnimal	  CHAR
);