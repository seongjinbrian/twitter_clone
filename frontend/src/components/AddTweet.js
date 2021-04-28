import React, {useState} from "react";
import {Editor} from "@tinymce/tinymce-react/lib/cjs/main/ts";
import axios from "axios";
import {Form, Row, Button, Modal} from 'react-bootstrap'

function AddTweet() {
    const [state, setState] = useState({content: ""})
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    const handleEditorChange = (content, editor) => {
        this.setState({content})
    }

    const submit = (e) => {
        e.preventDefault()
        axios.post("/api/addtweet", {title:document.getElementById("title").val, content: this.state.content}, {
            headers: {
                Autorization: "Bearer " + localStorage.getItem("access_token")
            }
        }).then(res => {
            if (res.data.success) {
                window.location.reload()
            }
        })
    }

    return (
      <div id="addTweet">
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
      </div>
    );
}

export default AddTweet