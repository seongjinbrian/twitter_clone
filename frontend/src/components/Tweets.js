import React from "react";
import {Card} from 'react-bootstrap';

function TweetItem(props) {
    return (
      <Card style={{ marginTop: "2rem" }}>
        <Card.Body>
          <Card.Title>{props.title}</Card.Title>
          <Card.Text>
              <div dangerouslySetInnerHTML={{__html: props.content}}></div>
          </Card.Text>
          <Card.Link href="#">Card Link</Card.Link>
          <Card.Link href="#">Another Link</Card.Link>
        </Card.Body>
      </Card>
    );
}

export default TweetItem;