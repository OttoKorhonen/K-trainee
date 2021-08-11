import './App.css';
import React, { useEffect, useState } from 'react'
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import AddShoppingCartIcon from '@material-ui/icons/AddShoppingCart';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import { withStyles } from '@material-ui/core/styles';
import Badge from '@material-ui/core/Badge';

const StyledBadge = withStyles((theme) => ({
  badge: {
    right: -3,
    top: 13,
    border: `2px solid ${theme.palette.background.paper}`,
    padding: '0 4px',
  },
}))(Badge);

function App() {
  const [products, setProducts] = useState([])
  const [items, setItems] = useState(0)

  useEffect(() => {
    getData()
  }, [])

  //url for development and local use
  //http://127.0.0.1:5000/api/products"
  const getData = () => {
    fetch("https://k-trainee.herokuapp.com/api/products")
      .then(response => response.json())
      .then(responseData => {
        console.log(responseData.Products)
        setProducts(responseData.Products)
      })
      .catch(err => console.error(err))
  }
  //url for development and local use
  //"http://127.0.0.1:5001/api/shoppingcart"
  const addToCart = (product) =>{
    console.log({name:product.name, price:product.price})
    let amount = items +1
    setItems(amount)
    fetch("https://k-trainee.herokuapp.com/api/shoppingcart",
    {
        method: 'POST', 
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify({name:product.name, price:product.price})
    }
    )
    .catch(err => console.error(err))
}


  return (
    <div className="App">
      <AppBar position="static">
        <Toolbar>
          <Typography style={{ color: 'white', fontSize: 24, paddingRight: '30%' }}>
            Hardware store
          </Typography>
          <StyledBadge badgeContent={items} color="secondary">
            <ShoppingCartIcon style={{}}/>
          </StyledBadge>
        </Toolbar>
      </AppBar>
      <div>
        <table >
          <tbody>
            <tr ><th style={{paddingLeft:30, paddingRight: 30}}>Product id</th><th  style={{paddingLeft:30, paddingRight: 30}}>Name</th><th  style={{paddingLeft:30, paddingRight: 30}}>Price €</th><th style={{paddingLeft:30, paddingRight: 30}}>Stock</th><th style={{paddingLeft:30, paddingRight: 30}}>Add to Cart</th></tr>
            {
              products.map((product) =>
                <tr key={product.id} >
                  <td>{product.id}</td>
                  <td>{product.name}</td>
                  <td>{product.price}</td>
                  <td>{product.stock}</td>
                 <td><AddShoppingCartIcon onClick={() => {addToCart(product)}}  style={{paddingLeft:30, paddingRight: 30}}/></td>
                </tr>)
            }
          </tbody>
        </table>
      </div>
    </div>

  );
}

export default App;
