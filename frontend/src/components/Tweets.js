import React from "react";
import { Card, Button } from "react-bootstrap";
import styled from "styled-components";
import axios from "axios";

const DeleteButton = styled(Button)`
  // float: right;
`;

const StyledCard = styled(Card)`
  margin-top: 2rem;
  width: 50em;
  justify-content: center;
  align-items: center;
  text-align: center;
`;

function removeTweet(tweetId) {
  axios.delete("api/tweet/delete/" + tweetId).then((res) => {
    console.log(res.data);
    window.location.reload();
  });
}

function TweetItem(props) {
  return (
    <StyledCard>
      <Card.Body>
        <Card.Title>{props.title}</Card.Title>
        <Card.Text>
          <div dangerouslySetInnerHTML={{ __html: props.content }}></div>
        </Card.Text>
      </Card.Body>
      <Card.Footer>
        <Button variant="link">
          Like
        </Button>
        <Button variant="link">
          Comment
        </Button>
        <Button variant="link">
          Reply
        </Button>
        {props.ownership && (
          <DeleteButton variant="danger" onClick={() => removeTweet(props.id)}>
            Delete
          </DeleteButton>
        )}
      </Card.Footer>
    </StyledCard>
  );
}

export default TweetItem;
