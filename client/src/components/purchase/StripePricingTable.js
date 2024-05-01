import React, { useEffect } from 'react';

const StripePricingTable = () => {
  useEffect(() => {
    const script = document.createElement('script');
    script.src = 'https://js.stripe.com/v3/pricing-table.js';
    script.async = true;
    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    };
  }, []);

  return (
    <stripe-pricing-table
      pricing-table-id="prctbl_1PBKIp01oc5MNduHsJ5BjWks"
      publishable-key="pk_live_51P8nqZ01oc5MNduHmjCsjaPW94inoNxFqeefOnL3zkpLZ7PyM1d2ipqKmTbXt0hbQ1DksnzF96QX2fioSvTMWjnK00j60AHDud">
    </stripe-pricing-table>
  );
};

export default StripePricingTable;