import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const PurchaseCard = () => {
    const [purchaseHistory, setPurchaseHistory] = useState([]);
    const [loading, setLoading] = useState(true);
    const {purchaseId} = useParams()

    // debugger
    useEffect(() => {
        fetchPurchaseHistory();
    }, []);

    const fetchPurchaseHistory = async () => {
        try {
            const response = await fetch(`/success/${purchaseId}`);
            const data = await response.json();
            setPurchaseHistory(data);
            setLoading(false);
        } catch (error) {
            console.error("Error fetching purchase history:", error);
            setLoading(false);
        }
    };

    
    //figure out why use effect not kicking in


    if (loading) {
        return <div>Loading...</div>; 
    }
    
    
    return (
        <div>
            <h2>Purchase History</h2>
            <div>
                {purchaseHistory.length === 0 ? (
                    <p>No purchase history available.</p>
                ) : (
                    purchaseHistory.map((purchase) => (
                        <div key={purchase.id}>
                            <p>Pattern: {purchase.pattern.title}</p>
                            <p>Purchase Date: {purchase.purchase_date}</p>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default PurchaseCard;
