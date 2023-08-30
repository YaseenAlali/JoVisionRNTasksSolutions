import { StyleSheet } from 'react-native';
import { useState, useEffect } from 'react';
import EditScreenInfo from '../../components/EditScreenInfo';
import { Text, View } from '../../components/Themed';
import * as Location from 'expo-location';


export default function TabTwoScreen() {
  const [location, setLocation] = useState({
    latitude : 0,
    longitude : 0,
    altitude : 0,
    accuracy : 0,
    lastMeasurement : ''
  });
  let subscription = undefined;

  useEffect(() => {
    // Location.requestBackgroundPermissionsAsync().then((status) => {
    //   if (status.granted){
    //     subscription = Location.watchPositionAsync({accuracy : Location.LocationAccuracy.High}, (locationData) => {
    //       if (locationData){
            
    //       }
    //     })
    //   }
    // })

    // Return a cleanup function
    return () => {
    };
  }, []); 




  return (
    <View style={styles.container}>
      <Text style={styles.title}>Location</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
