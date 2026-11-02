import * as SecureStore from "expo-secure-store";
import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";
import { Platform } from "react-native";

import { api, type TokenPair } from "./api";

const ACCESS_KEY = "relapsa_access";
const REFRESH_KEY = "relapsa_refresh";

type User = { id: string; email: string; created_at: string };

type AuthContextValue = {
  ready: boolean;
  user: User | null;
  accessToken: string | null;
  signIn: (email: string, password: string) => Promise<void>;
  signUp: (email: string, password: string) => Promise<void>;
  signOut: () => Promise<void>;
  refreshMe: () => Promise<void>;
};

const AuthContext = createContext<AuthContextValue | null>(null);

async function saveTokens(tokens: TokenPair) {
  if (Platform.OS === "web") {
    localStorage.setItem(ACCESS_KEY, tokens.access);
    localStorage.setItem(REFRESH_KEY, tokens.refresh);
    return;
  }
  await SecureStore.setItemAsync(ACCESS_KEY, tokens.access);
  await SecureStore.setItemAsync(REFRESH_KEY, tokens.refresh);
}

async function loadAccess(): Promise<string | null> {
  if (Platform.OS === "web") {
    return localStorage.getItem(ACCESS_KEY);
  }
  return SecureStore.getItemAsync(ACCESS_KEY);
}

async function clearTokens() {
  if (Platform.OS === "web") {
    localStorage.removeItem(ACCESS_KEY);
    localStorage.removeItem(REFRESH_KEY);
    return;
  }
  await SecureStore.deleteItemAsync(ACCESS_KEY);
  await SecureStore.deleteItemAsync(REFRESH_KEY);
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [ready, setReady] = useState(false);
  const [accessToken, setAccessToken] = useState<string | null>(null);
  const [user, setUser] = useState<User | null>(null);

  const refreshMe = useCallback(async () => {
    const token = await loadAccess();
    if (!token) {
      setAccessToken(null);
      setUser(null);
      return;
    }
    setAccessToken(token);
    const me = await api<User>("/auth/me/", { token });
    setUser(me);
  }, []);

  useEffect(() => {
    (async () => {
      try {
        await refreshMe();
      } catch {
        await clearTokens();
        setAccessToken(null);
        setUser(null);
      } finally {
        setReady(true);
      }
    })();
  }, [refreshMe]);

  const signIn = useCallback(async (email: string, password: string) => {
    const tokens = await api<TokenPair>("/auth/login/", {
      method: "POST",
      body: { email, password },
    });
    await saveTokens(tokens);
    setAccessToken(tokens.access);
    const me = await api<User>("/auth/me/", { token: tokens.access });
    setUser(me);
  }, []);

  const signUp = useCallback(async (email: string, password: string) => {
    const data = await api<User & TokenPair>("/auth/register/", {
      method: "POST",
      body: { email, password },
    });
    await saveTokens({ access: data.access, refresh: data.refresh });
    setAccessToken(data.access);
    setUser({ id: data.id, email: data.email, created_at: data.created_at });
  }, []);

  const signOut = useCallback(async () => {
    await clearTokens();
    setAccessToken(null);
    setUser(null);
  }, []);

  const value = useMemo(
    () => ({ ready, user, accessToken, signIn, signUp, signOut, refreshMe }),
    [ready, user, accessToken, signIn, signUp, signOut, refreshMe],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used inside AuthProvider");
  }
  return ctx;
}
