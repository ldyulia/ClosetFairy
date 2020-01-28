import React from 'react';
import {ActivityIndicator} from 'react-native';
import styled from 'styled-components';

const Loader = () => {
  return (
    <Container>
      <ActivityIndicator size="large" color="#0000ff" />
    </Container>
  );
};

const Container = styled.View`
  flex: 1;
  justify-content: center;
`;
export default Loader;
