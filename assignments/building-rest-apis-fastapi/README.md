# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST com FastAPI e pratique a definição de endpoints, a validação de dados de entrada e o uso de métodos HTTP e códigos de status para gerenciar recursos.

## 📝 Tasks

### 🛠️ Implement a Books Collection Endpoint

#### Descrição
Instale as dependências com `python -m pip install fastapi uvicorn`. Renomeie o arquivo `starter-code.py` para `main.py` e implemente um endpoint que retorne todos os livros da coleção em memória. Execute a API localmente e consulte a documentação gerada.

#### Requisitos
O programa concluído deve:

- Iniciar uma aplicação FastAPI chamada `app` em `main.py`
- Implementar `GET /books` para retornar a coleção completa como JSON
- Executar com `uvicorn main:app --reload` e disponibilizar a documentação interativa em `/docs`

### 🛠️ Retrieve and Create Books

#### Descrição
Adicione endpoints para consultar um livro pelo ID e incluir um novo livro na coleção. Use o modelo `Book` para que o FastAPI valide os dados recebidos.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` e retornar HTTP 404 quando o ID não existir
- Implementar `POST /books` usando um corpo de requisição validado pelo modelo `Book`
- Retornar HTTP 201 ao criar um livro e incluí-lo nas consultas seguintes da coleção

### 🛠️ Update and Delete Books

#### Descrição
Complete a API permitindo que clientes substituam e removam livros pelo ID. Verifique o comportamento usando a documentação interativa.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para substituir um livro existente
- Implementar `DELETE /books/{book_id}` para remover um livro existente
- Retornar HTTP 404 em solicitações de atualização ou remoção para um ID desconhecido
- Confirmar que cada alteração aparece em `GET /books`