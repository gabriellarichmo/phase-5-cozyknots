import React from 'react'
import { Link } from 'react-router-dom';

const PurchaseCardTwo = ({ id, pattern_id, price, status, purchase_date }) => {
  
  
  return (
    <div>
      <span>Status: {status}</span>
      <span>Purchase Date: {purchase_date}</span>
      <span>Price: {price}</span>
      <span><Link to={`/patterns/${pattern_id}`}>Purchased Pattern Here!</Link></span>
    </div>
  );
}

export default PurchaseCardTwo