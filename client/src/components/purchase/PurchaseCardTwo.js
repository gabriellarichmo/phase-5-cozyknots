import React from 'react'
import { Link } from 'react-router-dom';
import "./PurchaseCardTwo.css";

const PurchaseCardTwo = ({ id, pattern_id, price, status, purchase_date }) => {
  
  
  return (
    <div className='purchase-container'>
      <span>Status: {status}</span>
      <br></br>
      <span>Purchase Date: {purchase_date}</span>
      <br></br>
      <span>Price: {price}</span>
      <br></br>
      <span><Link to={`/patterns/${pattern_id}`}>Purchased Pattern Here!</Link></span>
    </div>
  );
}

export default PurchaseCardTwo