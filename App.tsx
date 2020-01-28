import * as React from 'react';
import {View, Text} from 'react-native';
import Geolocation from 'react-native-geolocation-service';

export interface AppProps {}

const App: React.SFC<AppProps> = () => {
  const [isLoading, setLoading] = React.useState(true);
  const [position, setPosition] = React.useState(null);

  React.useEffect(() => {
    _getPosition();
  }, []);

  const _getPosition = () => {
    Geolocation.getCurrentPosition(
      position => {
        console.log('position: ', position);
      },
      error => {
        // See error code charts below.
        console.log(error.code, error.message);
      },
      {enableHighAccuracy: true, timeout: 15000, maximumAge: 10000},
    );
  };
  return (
    <View>
      <Text>test</Text>
    </View>
  );
};

export default App;
