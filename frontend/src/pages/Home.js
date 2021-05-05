import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  background-image: url("https://cdn.vox-cdn.com/thumbor/ab0uBN2icZiIs7JyG6edp8rvjL4=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/20086268/acastro_200715_1777_twitter_0004.0.jpg");
  position: static;
  height: 100vh;
  background-size: cover;
  width: 80vh;
`;

const Msg = styled.div`
  position: absolute;
  top: 5em;
  right: 1em;
  font-size: 3.3em;
  font-weight: 300;
`;

const Joinus = styled.div`
  position: absolute;
  top: 12em;
  right: 2em;
  font-size: 2em;
`;

function Home() {
  return (
    <Wrapper>
      <Msg>지금 일어나고 있는 일</Msg>
      <Joinus>오늘 트위터에 가입하세요</Joinus>
    </Wrapper>
  );
}

export default Home;
