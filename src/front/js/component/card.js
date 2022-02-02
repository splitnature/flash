import React, { Component, useContext, useEffect, useState } from "react";

export const card = () =>{
    const {actions,store} = useContext(Context);
    useEffect(()=>{actions.getcards();})=

<Card style={{ width: '18rem' }}>
  <Card.Img variant="top" src="holder.js/100px180" />
  <Card.Body>
    <Card.Title>Card Title</Card.Title>
    <Card.Text>
     
    </Card.Text>
    <Button variant="primary">Go somewhere</Button>
  </Card.Body>
</Card>
}