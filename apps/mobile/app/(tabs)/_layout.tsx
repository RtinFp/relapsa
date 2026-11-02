import { Tabs } from "expo-router";
import { Text } from "react-native";

import Colors from "@/constants/Colors";
import { useColorScheme } from "@/components/useColorScheme";

function TabLabel({ label, color }: { label: string; color: string }) {
  return <Text style={{ color, fontSize: 11 }}>{label}</Text>;
}

export default function TabLayout() {
  const colorScheme = useColorScheme();
  const tint = Colors[colorScheme ?? "light"].tint;

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: tint,
        tabBarLabel: ({ children, color }) => (
          <TabLabel label={String(children)} color={String(color)} />
        ),
      }}
    >
      <Tabs.Screen name="index" options={{ title: "Home" }} />
      <Tabs.Screen name="meals" options={{ title: "Meals" }} />
      <Tabs.Screen name="activities" options={{ title: "Move" }} />
      <Tabs.Screen name="progress" options={{ title: "Progress" }} />
      <Tabs.Screen name="profile" options={{ title: "Profile" }} />
    </Tabs>
  );
}
