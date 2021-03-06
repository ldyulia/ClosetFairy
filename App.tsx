import * as React from 'react';
import {View, Text} from 'react-native';
import Geolocation from 'react-native-geolocation-service';
import styled from 'styled-components/native';
import Loader from './components/utils/Loader';
// import cityKR from './APIs/city.kr.json';
import cityUS from './APIs/city.us.json';

export interface AppProps {}

const App: React.SFC<AppProps> = () => {
  const [isLoading, setLoading] = React.useState(true);
  const [id, setId] = React.useState<number | null>(null);

  console.log(id);

  React.useEffect(() => {
    _getPosition();
  }, []);

  const _getPosition = () => {
    Geolocation.getCurrentPosition(
      position => {
        setLoading(false);

        const lon2 = position.coords.longitude;
        const lat2 = position.coords.latitude;
        _getId(lon2, lat2);
      },
      error => {
        console.log(error.code, error.message);
      },
      {enableHighAccuracy: false, timeout: 15000, maximumAge: 60000},
    );

    Geolocation.watchPosition(
      position => {
        const lon2 = position.coords.longitude;
        const lat2 = position.coords.latitude;
        _getId(lon2, lat2);
      },
      error => {
        console.log(error.code, error.message);
      },
      {
        distanceFilter: 10000,
      },
    );
  };

  const _getId = (lon2: number, lat2: number) => {
    let distArr: number[] = [];
    cityUS.map(city => {
      const lon1 = city.coord.lon;
      const lat1 = city.coord.lat;

      const lon = lon2 - lon1;
      const lat = lat2 - lat1;

      const distance = Math.sqrt(Math.pow(lon, 2) + Math.pow(lat, 2));
      distArr.push(distance);
    });
    const newDistArr = [...distArr];
    newDistArr.sort((a, b) => {
      return a - b;
    });

    const i = distArr.indexOf(newDistArr[0]);
    console.log(cityUS[i].name);
    setId(cityUS[i].id);
  };

  return <Container>{isLoading ? <Loader /> : <Text>test</Text>}</Container>;
};

const Container = styled.View`
  flex: 1;
`;

export default App;
