import React, {useState, useEffect} from 'react'
import { Link, useParams } from 'react-router-dom'
import { Row, Col, Image, ListGroup, Button, Card } from 'react-bootstrap'
import Rating from '../components/Rating'
import axios from 'axios'

function ProductScreen({ match }) {
  const { id } = useParams();
  const [product, setProduct] = useState([])

  useEffect(() => {
    async function fetchProduct(){

      const { data } = await axios.get(`/api/products/${id}`)
      setProduct(data)

    }

    fetchProduct()
    
  }, [])

  if (!product) {
    return <h2>Product not found</h2>;
  }

  return (
    <div>
      <Link to='/' className='btn prod-screen-btn my-3'>
        <i className='fas fa-arrow-left'></i> Go back</Link>
      <Row>
        <Col md={6}>
          <Image src={product.image} alt={product.name} fluid/>
        </Col>

        <Col md={3}>
          <ListGroup variant='flush'>
            <ListGroup.Item>
              <h3>{product.name}</h3>
            </ListGroup.Item>
            <ListGroup.Item>
              <Rating 
              value={product.rating} 
              text={`${product.num_reviews} reviews`} 
              color={'#f8e825'}/>
            </ListGroup.Item>
            <ListGroup.Item>Price: ${product.price}</ListGroup.Item>
            <ListGroup.Item>Description: {product.description}</ListGroup.Item>
          </ListGroup>
        </Col>

        <Col md={3}>
          <Card>
            <ListGroup variant='flush'>
              <ListGroup.Item>
                <Row>
                  <Col>Price:</Col>
                  <Col>
                    <strong>${product.price}</strong>
                  </Col>
                </Row>
              </ListGroup.Item>
              <ListGroup.Item>
                <Row>
                  <Col>Status:</Col>
                  <Col>
                    {product.count_in_stock > 0 ? 'In Stock' : 'Out of Stock'} 
                  </Col>
                </Row>
              </ListGroup.Item>
              <ListGroup.Item>
                <Button 
                className='btn-block w-100' 
                type='button' 
                disabled={product.count_in_stock === 0}>Add to Cart</Button>
              </ListGroup.Item>
            </ListGroup>
          </Card>
        </Col>
      </Row>
    </div>
  )
}

export default ProductScreen
