import React, { Component, useState } from "react";
import { Login } from "../pages/login";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import { Register } from "../pages/register";
export const Modallogin = () => {
	const [show, setShow] = useState(false);

	const handleClose = () => setShow(false);
	const handleShow = () => setShow(true);

	return (
		<div>
			<Button variant="primary" onClick={handleShow} />
			register
			<Modal show={show} onHide={handleClose}>
				<Modal.Header closeButton>
					<Modal.Title>Register</Modal.Title>
				</Modal.Header>
				<Modal.Body /> <Register />
				<Modal.Footer>
					<Button variant="secondary" onClick={handleClose}>
						Close
					</Button>
					<Button variant="primary" onClick={handleClose}>
						Save Changes
					</Button>
				</Modal.Footer>
			</Modal>
		</div>
	);
};

export const Modalregister = () => {
	const [show, setShow] = useState(false);

	const handleClose = () => setShow(false);
	const handleShow = () => setShow(true);

	return (
		<div>
			<Button variant="primary" onClick={handleShow} />
			log in
			<Modal show={show} onHide={handleClose}>
				<Modal.Header closeButton>
					<Modal.Title>log in</Modal.Title>
				</Modal.Header>
				<Modal.Body /> <Login />
				<Modal.Footer>
					<Button variant="secondary" onClick={handleClose}>
						Close
					</Button>
					<Button variant="primary" onClick={handleClose}>
						Save Changes
					</Button>
				</Modal.Footer>
			</Modal>
		</div>
	);
};
