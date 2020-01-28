import * as React from 'react';
import {View, Text, ActivityIndicator} from 'react-native';
import Geolocation from 'react-native-geolocation-service';
import styled from 'styled-components/native';
import Loader from './components/utils/Loader';

export interface AppProps {}

const App: React.SFC<AppProps> = () => {
  const [isLoading, setLoading] = React.useState(true);
  const [position, setPosition] = React.useState(null);

  console.log(position);

  React.useEffect(() => {
    _getPosition();
  }, []);

  const _getPosition = () => {
    Geolocation.getCurrentPosition(
      position => {
        // console.log('position: ', position);
        setLoading(false);
        setPosition(position);
      },
      error => {
        console.log(error.code, error.message);
      },
      {enableHighAccuracy: false, timeout: 15000, maximumAge: 10000},
    );

    Geolocation.watchPosition(
      position => {
        // console.log('new position: ', position);
        setPosition(position);
      },
      error => {
        console.log(error.code, error.message);
      },
      {
        distanceFilter: 10000,
      },
    );
  };

  return <Container>{isLoading ? <Loader /> : <Text>test</Text>}</Container>;
};

const Container = styled.View`
  flex: 1;
`;

export default App;
