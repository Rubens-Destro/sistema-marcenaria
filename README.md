# Projeto Django

Este projeto é uma aplicação Django para controle de estoque.

## Configuração do Ambiente

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Crie e ative um ambiente virtual

No Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

No Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

### 4. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 5. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse o projeto em: http://127.0.0.1:8000/

---

Siga estes passos para garantir que o ambiente está pronto para desenvolvimento e testes.
