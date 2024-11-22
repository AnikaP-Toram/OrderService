# OrderService
The Order Microservice offers a set of endpoints for managing user orders, including order placement, tracking transactions, and maintaining order history. 

# API Endpoints
### 1. Create Order
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST /orders

### 2. Retrieves a list of all orders.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET /orders

### 3. To update a existing order
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PUT /orders

### 3. Fetches all orders placed by a specific user.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET /orders/user/{int:user_id}

### 4. Retrieves all orders containing a specific product
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET /orders/product/{int:product_id}

# Installation
## Prerequistes 
<li>Python</li>
<li>PostgresSQL</li>

## SetUp
**1. Clone the Repository**:<br>
```
   git clone https://github.com/AnikaP-Toram/OrderService.git
```
**2. Create a Virtual Environment:**
```
   python -m venv venv
```

**3. Activate the Virtual Environment and Install Dependencies:**
```
   venv\Scripts\activate
   pip install -r requirements.txt
```

**4. Set Up the Database:**
1. Ensure you have PostgreSQL installed and running.
2. Create a new PostgreSQL database:

```
CREATE DATABASE orderservice;
```

**5. Update Configuration Settings:** <br>
Open config.py and update the following values with your own secure information:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- SQLALCHEMY_DATABASE_URI<br>

**6. Run the Application:** <br>
Start the Flask server:
```
python run.py
```

**8. Access the API:** <br>
Open a tool like Postman to access the API at [http://localhost:5000.](http://localhost:5000)
