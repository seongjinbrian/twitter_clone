import React, { useState, useEffect } from "react";
import { Editor } from "@tinymce/tinymce-react/lib/cjs/main/ts";
import axios from "axios";
import { Form, Button, Modal } from "react-bootstrap";
import styled from "styled-components";

const Msg = styled.p`
  display: inline;
  padding-top: 1em;
  padding-right: 1em;
  justify-content: center;
`;

function AddTweet() {
  const [currentUser, setCurrentUser] = useState(0);
  useEffect(() => {
    axios.get("/api/tweet/uid").then((res) => {
      setCurrentUser(res.data["uid"]);
    });
  }, []);

  const [state, setState] = useState({ content: "" });
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  const handleEditorChange = (content, editor) => {
    setState({ content });
  };

  const submit = (e) => {
    e.preventDefault();
    console.log(document.getElementById("title").value, state.content);
    axios
      .post("api/tweet/add", {
        title: document.getElementById("title").value,
        content: state.content,
        uid: currentUser,
      })
      .then((res) => {
        if (res.data.success) {
          window.location.reload();
        } else {
          console.log("cannot proceed your request");
        }
      });
  };

  return (
    <>
      <Msg>Share your thoughts</Msg>
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
          <Modal.Title>Post tweets</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={submit}>
            <Form.Group>
              <Form.Label>Title</Form.Label>
              <Form.Control id="title" placeholder="Enter title" />
            </Form.Group>
            <Editor
              initialValue="<p>This is the initial content of the editor</p>"
              init={{
                height: 300,
                menubar: false,
                statusbar: false,
                toolbar_mode: "sliding",
                plugins: [
                  "advlist autolink lists link image imagetools media emoticons preview anchor",
                  "searchreplace visualblocks code fullscreen",
                  "insertdatetime media table paste code help wordcount",
                ],
                toolbar:
                  "undo redo | formatselect | bold italic underline strikethrough | image anchor media | \
                                    alignleft aligncenter alignright alignjustify | \
                                    outdent indent | bulllist numlist | fullscreen preview | emoticons help",
                contextmenu: "bold italic underline indent outdent help",
              }}
              onEditorChange={handleEditorChange}
            />
            <Button variant="primary" type="submit">
              Post
            </Button>
          </Form>
        </Modal.Body>
      </Modal>
    </>
  );
}

export default AddTweet;
