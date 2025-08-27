SELECT Customer_number FROM Orders GROUP BY Customer_number ORDER BY COUNT(Order_number) DESC LIMIT 1;
