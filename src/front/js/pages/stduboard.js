import { render } from "node-sass";
import React from "react";
import { Card } from "react-bootstrap";

export const studentDashboard = () =>{
    return(
<div>
    <Card style={{ width: '18rem' }}>
  <Card.Body>
    <Card.Title>Card Title</Card.Title>
    <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
    <Card.Text>
        <div> </div>
    </Card.Text>
    <Card.Link href="#">Card Link</Card.Link>
    <Card.Link href="#">Another Link</Card.Link>
  </Card.Body>
</Card>
</div>)
}