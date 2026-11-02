# ADR-001 — SimpleJWT

- Status: accepted
- Date: 2026-11-03

## Context

Need mobile-friendly auth without SMS cost (TFIT OTP deferred).

## Decision

Email + password with `djangorestframework-simplejwt` (access + refresh tokens).

## Consequences

- Expo stores tokens in SecureStore.
- Refresh flow required when access expires.
- No phone OTP in MVP.
