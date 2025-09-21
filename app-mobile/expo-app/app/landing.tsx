
import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, StatusBar } from 'react-native';
import { Link } from 'expo-router';
import { MaterialIcons } from '@expo/vector-icons';

export default function LandingScreen() {
  return (
    <View style={styles.container}>
      <StatusBar barStyle="light-content" />
      <View style={styles.content}>
        <MaterialIcons name="location-pin" size={100} color="white" />
        <Text style={styles.title}>Welcome!</Text>
        <Text style={styles.subtitle}>
          Your journey begins now. Let's get you checked in and ready to explore.
        </Text>
      </View>
      <View style={styles.buttonsContainer}>
        <Link href="/scanner" asChild>
          <TouchableOpacity style={[styles.btn, styles.btnPrimary]}>
            <MaterialIcons name="qr-code-scanner" size={24} color="black" />
            <Text style={styles.btnTextPrimary}>Scan QR Code</Text>
          </TouchableOpacity>
        </Link>
        <TouchableOpacity style={[styles.btn, styles.btnSecondary]}>
          <MaterialIcons name="dialpad" size={24} color="white" />
          <Text style={styles.btnTextSecondary}>Enter Travel ID</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'rgb(25, 169, 226)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 32,
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 16,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 18,
    color: 'white',
    textAlign: 'center',
    maxWidth: 300,
  },
  buttonsContainer: {
    width: '100%',
    maxWidth: 400,
  },
  btn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    width: '100%',
    borderRadius: 12,
    paddingVertical: 16,
    paddingHorizontal: 24,
    marginVertical: 8,
  },
  btnPrimary: {
    backgroundColor: 'white',
  },
  btnSecondary: {
    borderWidth: 2,
    borderColor: 'white',
  },
  btnTextPrimary: {
    color: 'black',
    fontSize: 18,
    fontWeight: 'bold',
  },
  btnTextSecondary: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
});
