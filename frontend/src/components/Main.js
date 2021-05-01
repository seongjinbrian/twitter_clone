import React, { useState, useEffect } from "react";
import AddTweet from "./AddTweet";
import TweetItem from "./Tweets";
import axios from "axios";
import { Button, Modal } from "react-bootstrap";

function Main() {
  const [state, setState] = useState({ tweets: [] });
  useEffect(() => {
    axios.get("/api/tweets").then((res) => {
      setState({ tweets: res.data.reverse() });
    });
  }, []);
  return (
    <React.Fragment>
      <div
        className="w3-container w3-jumbo"
        style={{ margin: "3rem", paddingLeft: "1rem" }}
      >
        Tweets
      </div>
      <AddTweet />
      <div className="w3-container">
        {state.tweets.length === 0 ? (
          <p className="w3-xlarge w3-opacity" style={{ marginLeft: "2rem" }}>
            No tweets! Create one
          </p>
        ) : (
          state.tweets.map((item, index) => {
            return (
              <TweetItem
                title={item.title}
                content={item.content}
                key={index}
              />
            );
          })
        )}
      </div>
    </React.Fragment>
  );
}
export default Main;
