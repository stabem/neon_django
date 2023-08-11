# Projeto Neon - API Django

## Descrição

Este projeto consiste em uma API REST desenvolvida em Python/Django para manipulação de uma base de dados contendo informações de usuários e salários.

## Arquitetura

A arquitetura do projeto segue o padrão Clean, dividido em camadas de controladores, serviços e repositórios. Abaixo está o diagrama de classes representando a estrutura do projeto:

![Diagrama de Classes](https://ummcsnegloedxcrwlucz.supabase.co/storage/v1/object/public/chatgpt-diagrams/2023-08-11/58c020dc-b498-4e2f-90e3-d190a7345abb.png)

## Controladores

### DashboardController
- `get(request, cpf=None)`: Retorna os dados do painel.

### SalaryController
- `post(request)`: Cria um salário.
- `get(request, cpf=None)`: Obtém salários por CPF ou todos os salários.
- `put(request, salary_id)`: Atualiza um salário.
- `delete(request, salary_id)`: Exclui um salário.

### UserController
- `post(request)`: Cria um usuário.
- `get(request, cpf=None)`: Obtém usuários por CPF ou todos os usuários.
- `put(request, cpf)`: Atualiza um usuário.
- `delete(request, cpf)`: Exclui um usuário.

## Serviços

### SalaryService
- `create_salary(date, amount, discount, cpf)`: Cria um salário.
- `get_salary(salary_id)`: Obtém um salário por ID.
- `get_salary_by_cpf(cpf)`: Obtém salários por CPF.
- `get_all_salaries()`: Obtém todos os salários.
- `update_salary(salary_id, update_data)`: Atualiza um salário.
- `delete_salary(salary_id)`: Exclui um salário.
- `get_dashboard_data(cpf=None)`: Obtém dados do painel.

### UserService
- `create_user(cpf, name, birth_date)`: Cria um usuário.
- `get_user(cpf)`: Obtém um usuário por CPF.
- `update_user(cpf, name, birth_date)`: Atualiza um usuário.
- `delete_user(cpf)`: Exclui um usuário.
- `get_all_users()`: Obtém todos os usuários.

## Repositórios

### SalaryRepository
- Métodos para criar, obter, atualizar e excluir salários, além de obter dados do painel.

### UserRepository
- Métodos para criar, obter, atualizar e excluir usuários.

## Instruções de Execução

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local ou servidor:

### 1. Configurar o Ambiente Virtual

Antes de iniciar o projeto, é recomendado criar e ativar um ambiente virtual para isolar as dependências. Utilize os seguintes comandos:

#### Para sistemas Unix ou MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Para sistemas Windows:

```bash
python -m venv venv
venv\\Scripts\\activate
```

### 2. Instalar Dependências

Após ativar o ambiente virtual, instale as dependências necessárias usando o seguinte comando:
```bash
pip install -r requirements.txt
```

### 3. Executar o Servidor
Com o ambiente virtual ativado e as dependências instaladas, você pode iniciar o servidor usando o seguinte comando:
```bash
python manage.py runserver
```
O servidor estará disponível no endereço http://127.0.0.1:8000/, e você pode acessar a API através dos endpoints disponíveis.


### 4. Desativar o Ambiente Virtual
```bash
deactivate
```
