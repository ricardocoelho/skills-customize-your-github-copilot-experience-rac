# 📘 Assignment: Persisting API Data with SQLite

## 🎯 Objective

Adapte uma API REST feita com FastAPI para armazenar livros em um banco SQLite, em vez de mantê-los apenas na memória. Pratique consultas SQL parametrizadas e confirme que os dados continuam disponíveis após reiniciar a API.

## 📝 Tasks

### 🛠️ Implement Database Reads

#### Descrição
Instale `fastapi` e `uvicorn` com `python -m pip install fastapi uvicorn`. Renomeie `starter-code.py` para `main.py` e complete as rotas de consulta para ler os livros do banco SQLite inicializado pelo starter code.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` para retornar todos os livros do banco como JSON
- Implementar `GET /books/{book_id}` para retornar o livro solicitado
- Retornar HTTP 404 quando o ID solicitado não existir
- Converter os registros SQLite em objetos `Book` antes de retorná-los

### 🛠️ Persist Book Changes

#### Descrição
Substitua as operações em memória por comandos SQL para criar, atualizar e remover livros. Use parâmetros SQL para fornecer valores às consultas, sem montar comandos por concatenação de strings.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` e retornar HTTP 201 após salvar o livro
- Implementar `PUT /books/{book_id}` para atualizar o título e o autor do livro existente
- Implementar `DELETE /books/{book_id}` para remover o livro existente
- Retornar HTTP 404 quando uma atualização ou remoção usar um ID inexistente

### 🛠️ Verify Persistence After Restart

#### Descrição
Inicie a API com `uvicorn main:app --reload`, crie ou atualize um livro e consulte a coleção. Pare e inicie a API novamente para confirmar que as alterações foram gravadas no arquivo do banco de dados.

#### Requisitos
O programa concluído deve:

- Salvar os livros no arquivo SQLite indicado por `DATABASE_PATH`
- Manter os livros criados e atualizados depois que a API for reiniciada
- Manter as respostas de consulta consistentes com as alterações feitas