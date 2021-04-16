import React, {useEffect, useState} from 'react';
import './App.css';
import {Container, Row} from 'react-bootstrap';
import ProductCard from './components/ProductCard';
import { Product } from './product';
import { API_BASE_URL} from './constants';

function App() {

  const [products, setProducts] = useState([] as Product[]);

    useEffect(() => {
        (
            async () => {
                const response = await fetch(API_BASE_URL+'/api/products');
                const data = await response.json();
                data.map(
                    (p: Product) => {
                        p.product_purchase_count = 0;
                        return p
                    }
                )
                setProducts(data)
            }
        )();
    },[]);

    const buy = async (id: number) => {
        await fetch(API_BASE_URL+`/api/products/${id}/order`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        })

        setProducts(products.map(
            (p: Product) => {
                if (p.id === id) {
                    p.product_purchase_count++;
                }
                return p;
            }
        ));
    }

  return (
    <div className="App">
      <Container>
        <Row>
            {products.map(
                (p: Product) => {
                    return(
                        <ProductCard key={p.id}
                                     title={p.title}
                                     image={p.image}
                                     id={p.id}
                                     cnt={p.product_purchase_count}
                                     buy={buy} />
                    )
                }
            )}
        </Row>
      </Container>
    </div>
  );
}

export default App;
