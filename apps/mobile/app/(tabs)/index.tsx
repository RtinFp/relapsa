import { useEffect, useState } from "react";
import { Pressable, StyleSheet, Text, View } from "react-native";
import { router } from "expo-router";

import { api, getApiBaseUrl } from "@/lib/api";
import { useAuth } from "@/lib/auth";

type Me = { id: string; email: string; created_at: string };

export default function HomeScreen() {
  const { user, accessToken, signOut, refreshMe } = useAuth();
  const [me, setMe] = useState<Me | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    (async () => {
      try {
        const data = await api<Me>("/auth/me/", { token: accessToken });
        setMe(data);
      } catch (e) {
        setError(e instanceof Error ? e.message : "Failed to load /auth/me");
      }
    })();
  }, [accessToken]);

  async function onLogout() {
    await signOut();
    router.replace("/(auth)/login");
  }

  return (
    <View style={styles.wrap}>
      <Text style={styles.brand}>Relapsa</Text>
      <Text style={styles.sub}>Home · API live check</Text>
      <Text style={styles.meta}>{getApiBaseUrl()}</Text>

      <View style={styles.card}>
        <Text style={styles.label}>session user</Text>
        <Text>{user?.email ?? "—"}</Text>
        <Text style={styles.label}>GET /auth/me/</Text>
        {error ? <Text style={styles.error}>{error}</Text> : null}
        {me ? (
          <Text>
            {me.email}
            {"\n"}
            {me.id}
          </Text>
        ) : (
          <Text>…</Text>
        )}
      </View>

      <Pressable
        style={styles.secondary}
        onPress={async () => {
          setError(null);
          try {
            await refreshMe();
            const data = await api<Me>("/auth/me/", { token: accessToken });
            setMe(data);
          } catch (e) {
            setError(e instanceof Error ? e.message : "refresh failed");
          }
        }}
      >
        <Text>Refresh /me</Text>
      </Pressable>

      <Pressable style={styles.btn} onPress={onLogout}>
        <Text style={styles.btnText}>Log out</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: { flex: 1, padding: 24, gap: 12 },
  brand: { fontSize: 32, fontWeight: "700", marginTop: 12 },
  sub: { fontSize: 16, opacity: 0.7 },
  meta: { fontSize: 12, opacity: 0.5 },
  card: {
    marginTop: 8,
    padding: 16,
    borderWidth: 1,
    borderColor: "#ddd",
    borderRadius: 10,
    gap: 6,
  },
  label: { fontSize: 12, opacity: 0.55, marginTop: 6, textTransform: "uppercase" },
  error: { color: "#b00020" },
  secondary: {
    padding: 12,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    alignItems: "center",
  },
  btn: {
    backgroundColor: "#1a1a1a",
    paddingVertical: 14,
    borderRadius: 8,
    alignItems: "center",
  },
  btnText: { color: "#fff", fontWeight: "600" },
});
