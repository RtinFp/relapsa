# Class 2 — Accounts / auth

Maps to Django app `accounts` + SimpleJWT.

```mermaid
classDiagram
  direction TB

  class User {
    +UUID id
    +string email
    +string passwordHash
    +datetime createdAt
    +datetime updatedAt
  }

  class AuthService {
    +register(email, password) User
    +login(email, password) TokenPair
    +refresh(refreshToken) TokenPair
  }

  class TokenPair {
    +string access
    +string refresh
  }

  AuthService --> User : creates_or_loads
  AuthService --> TokenPair : issues
```

## Django mapping

- `User` → custom user or `AbstractUser` with email as username.
- Tokens → `rest_framework_simplejwt` (not stored as our own model).
