import React, {useState, useEffect} from 'react';
import AddTweet from "./AddTweet";
import TweetItem from "./Tweets";
import axios from "axios";
import {Button, Modal} from 'react-bootstrap'

function Main() {
    const [show, setShow] = useState(false);
    const [state, setState] = useState({tweets: []})
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    useEffect(() => {
        axios.get("/api/tweets").then(res => {
            setState({tweets: res.data.reverse()})
        });
      }, []);
    return(
        <>
            <Button variant="primary" onClick={handleShow}>
                Post tweet
            </Button>
            <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <Modal.Header closeButton>
          <Modal.Title>Modal title</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          I will not close if you click outside me. Don't even try to press
          escape key.
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary">Understood</Button>
        </Modal.Footer>
      </Modal>
        </>
    )
}
export default Main;