
import { View, Text, StyleSheet, Button, Alert } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { useEffect, useState } from 'react';

interface ScannedData {
  fullname: string;
  phoneNo: string;
  dob: string;
  nationality: string;
  destination: string;
  duration: string[];
  tripReason: string;
  emergencyContact: string;
}

export default function Details() {
  const { data } = useLocalSearchParams();
  const router = useRouter();
  const [parsedData, setParsedData] = useState<Partial<ScannedData> | null>(null);

  useEffect(() => {
    if (typeof data === 'string') {
      try {
        const jsonData = JSON.parse(data);

        let finalData: Partial<ScannedData> | null = null;

        // Prioritize the 'data' key if it exists and is an object with 'fullname'
        if (jsonData && typeof jsonData === 'object' && jsonData.data && typeof jsonData.data === 'object' && 'fullname' in jsonData.data) {
          finalData = jsonData.data;
        } else if (jsonData && typeof jsonData === 'object' && 'fullname' in jsonData) {
          // Fallback to direct properties if 'data' key is not present or doesn't contain fullname
          finalData = jsonData;
        } else {
          // If neither, iterate through top-level keys to find an object with 'fullname'
          const keys = Object.keys(jsonData);
          for (const key of keys) {
            if (jsonData[key] && typeof jsonData[key] === 'object' && 'fullname' in jsonData[key]) {
              finalData = jsonData[key];
              break;
            }
          }
        }

        if (finalData) {
          setParsedData(finalData);
        } else {
          Alert.alert("Error", "Invalid QR Code: Data structure not recognized.");
          router.back();
        }

      } catch (error) {
        Alert.alert("Error", "Invalid QR Code: The scanned data is not valid JSON.");
        router.back();
      }
    }
  }, [data]);

  if (!parsedData) {
    return (
      <View style={styles.container}>
        <Text>Loading...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Confirm Details</Text>
      <View style={styles.infoContainer}>
        <Text style={styles.label}>Full Name:</Text>
        <Text style={styles.info}>{parsedData.fullname ?? 'N/A'}</Text>
        <Text style={styles.label}>Phone Number:</Text>
        <Text style={styles.info}>{parsedData.phoneNo ?? 'N/A'}</Text>
        <Text style={styles.label}>Date of Birth:</Text>
        <Text style={styles.info}>{parsedData.dob ?? 'N/A'}</Text>
        <Text style={styles.label}>Nationality:</Text>
        <Text style={styles.info}>{parsedData.nationality ?? 'N/A'}</Text>
        <Text style={styles.label}>Destination:</Text>
        <Text style={styles.info}>{parsedData.destination ?? 'N/A'}</Text>
        <Text style={styles.label}>Duration:</Text>
        <Text style={styles.info}>
          {Array.isArray(parsedData.duration) ? parsedData.duration.join(' to ') : 'N/A'}
        </Text>
        <Text style={styles.label}>Reason for Trip:</Text>
        <Text style={styles.info}>{parsedData.tripReason ?? 'N/A'}</Text>
        <Text style={styles.label}>Emergency Contact:</Text>
        <Text style={styles.info}>{parsedData.emergencyContact ?? 'N/A'}</Text>
      </View>
      <Button title="Continue" onPress={() => router.push('/landing')} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  infoContainer: {
    width: '100%',
    backgroundColor: 'white',
    borderRadius: 10,
    padding: 20,
    marginBottom: 20,
  },
  label: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 10,
    color: '#333',
  },
  info: {
    fontSize: 16,
    marginBottom: 10,
    color: '#555',
  },
});
