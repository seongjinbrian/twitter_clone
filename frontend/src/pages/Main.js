import React, { useState, useEffect } from "react";
import AddTweet from "../components/AddTweet";
import TweetItem from "../components/Tweets";
import axios from "axios";
import { Button, Modal } from "react-bootstrap";
import styled from "styled-components";

const AddWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  border: solid 1px #ced4da;
  margin-top: 3em;
  padding: 3em;
  background-color: #f8f9fa;
`;

const TweetWrapper = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 3em;
`;

function Main() {
  const [state, setState] = useState({ tweets: [] });
  const [user, setUser] = useState(0);
  useEffect(() => {
    axios.get("/api/tweets").then((res) => {
      setState({ tweets: res.data.reverse() });
    });
    axios.get("/api/uid").then((res) => {
      setUser(res.data["uid"]);
    });
  }, []);
  return (
    <>
      <AddWrapper>
        <AddTweet />
      </AddWrapper>
      <TweetWrapper>
        {state.tweets.length === 0 ? (
          <p style={{ marginLeft: "2rem" }}>There's nothing to show</p>
        ) : (
          state.tweets.map((item, index) => {
            return (
              <TweetItem
                title={item.title}
                content={item.content}
                author={item.user.username}
                ownership={user === item.user.id}
                key={index}
                id={item.id}
              />
            );
          })
        )}
      </TweetWrapper>
    </>
  );
}
export default Main;
