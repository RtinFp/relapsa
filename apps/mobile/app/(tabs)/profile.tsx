import { StyleSheet, Text, View } from "react-native";

import { useAuth } from "@/lib/auth";

export default function ProfileScreen() {
  const { user } = useAuth();

  return (
    <View style={styles.wrap}>
      <Text style={styles.title}>Profile</Text>
      <Text style={styles.sub}>{user?.email}</Text>
      <Text style={styles.hint}>Lesson later — onboarding BMI (UC2)</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: { flex: 1, padding: 24, justifyContent: "center" },
  title: { fontSize: 24, fontWeight: "700" },
  sub: { marginTop: 8 },
  hint: { marginTop: 12, opacity: 0.65 },
});
