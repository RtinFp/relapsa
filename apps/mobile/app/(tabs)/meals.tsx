import { StyleSheet, Text, View } from "react-native";

export default function MealsScreen() {
  return (
    <View style={styles.wrap}>
      <Text style={styles.title}>Meals</Text>
      <Text style={styles.sub}>Lesson later — UC3 meal log</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: { flex: 1, padding: 24, justifyContent: "center" },
  title: { fontSize: 24, fontWeight: "700" },
  sub: { marginTop: 8, opacity: 0.65 },
});
