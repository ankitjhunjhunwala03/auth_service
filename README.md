# auth_service

This service handles user authentication and management.

## Project Overview

The `auth_service` provides endpoints for user registration, login, and authentication using JSON Web Tokens (JWT). It ensures secure access to protected resources within the ecommerce platform.

## Setup Instructions

### Normal Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/ankitjhunjhunwala03/auth_service/tree/main
   cd auth_service
   ```

2. **Setup virtual environment (optional but recommended)**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   ```bash
   cp .env.example .env
   nano .env  # Edit with appropriate values
   ```

   Ensure to set up variables like `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, and any specific settings required for your setup.

5. **Run migrations (if applicable)**

   ```bash
   python manage.py migrate
   ```

6. **Start the server**

   ```bash
   python manage.py runserver
   ```

   The auth service should now be running at `http://localhost:8000`.

### Docker Compose Setup

Ensure you have Docker and Docker Compose installed.

1. **Build and start the service**

   ```bash
   # Navigate to the project directory
   cd auth_service
   
   # Build and start the services
   docker-compose up --build
   ```

### Kubernetes Setup

Ensure you have `kubectl` configured and a Kubernetes cluster running.

1. **Apply the Kubernetes configurations**

   ```bash
   # Navigate to the Kubernetes directory
   cd kubernetes/auth_service
   
   # Apply the Kubernetes configurations
   kubectl apply -f .
   ```

## Usage

### Endpoints

- **Registration**: `/api/register/`
  - Method: POST
  - Payload: `username`, `password`, `email`, etc.
  - Description: Register a new user.
  
- **Login**: `/api/login/`
  - Method: POST
  - Payload: `username`, `password`
  - Description: Obtain a JWT token for authentication.
  
- **Protected Endpoint Example**: `/api/user/`
  - Method: GET
  - Headers: `Authorization: Bearer <token>`
  - Description: Access a protected endpoint requiring authentication.

---