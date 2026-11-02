# Activity 1 — Auth (register / login + JWT)

Focused on authentication only. Profile completion is [activity-profile.md](activity-profile.md).

```mermaid
flowchart TD
  startNode([Start]) --> choose{Has_account?}
  choose -->|No| register[POST_auth_register]
  register --> tokens1[Receive_access_and_refresh_JWT]
  choose -->|Yes| login[POST_auth_login]
  login --> tokens2[Receive_access_and_refresh_JWT]
  tokens1 --> store[Client_stores_tokens]
  tokens2 --> store
  store --> me[GET_auth_me]
  me --> gate{Profile_complete?}
  gate -->|No| toProfile[Go_to_profile_onboarding]
  gate -->|Yes| home[Enter_home]
  toProfile --> endNode([End])
  home --> endNode
```

## Notes

- Auth: email + password → SimpleJWT access/refresh.
- Failed login: stay on auth screen with error (not shown for brevity).
