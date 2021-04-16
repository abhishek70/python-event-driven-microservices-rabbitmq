import React, {PropsWithoutRef, useEffect, useState} from 'react'
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import {Col} from 'react-bootstrap';

const ProductCard = (props: PropsWithoutRef<any>) => {

    return (
        <Col>
            <Card className="Card">
              <Card.Img variant="top" src="" />
              <Card.Body>
                <Card.Title>{props.title}</Card.Title>
                <Button variant="primary" onClick={() => props.buy(props.id)}>Buy</Button>
                  <span>{props.cnt}</span>
              </Card.Body>
            </Card>
        </Col>
    );
};


export default ProductCard