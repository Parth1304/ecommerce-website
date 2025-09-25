# Django E-commerce Website with Recommendation System

A Django-based e-commerce web application that supports product browsing, cart management, and a personalized recommendation system based on user likes and product image similarity. It also integrates Stripe for payments.

---
### Demo video

[![Video Title](https://img.youtube.com/vi/RJMWc1myCt4/0.jpg)](https://youtu.be/RJMWc1myCt4)

---

## 🚀 Features

### Core E-commerce Features
- **User Authentication**: Registration, login, logout, and profile management
- **Product Catalog**: Browse products by categories with search and filtering
- **Product Details**: View product information (title, price, discount, description, image)
- **Shopping Cart**: Add/remove products to/from cart with persistent sessions
- **Checkout System**: Complete order processing with **Stripe payment integration**
- **Order Management**: Order history and tracking

### Recommendation System
- **User Likes**: Users can **like** products to build preferences
- **Image Similarity**: Recommendations based on precomputed image embeddings
- **Product Page Display**: Recommended products are displayed on the **same product page**
- **Content-Based Filtering**: Recommendations based on user preferences from liked products

---


## 📊 Database Models

### Core Models
- **Item**: Stores product information and precomputed image embeddings
- **UserLike**: Tracks which products a user liked
- **Order & OrderItem**: Cart and order management
- **UserProfile**: Stores additional user info (Stripe integration)
- **Address & Payment**: Billing/shipping information

---

## 🛠️ Technology Stack

### Backend
- **Django**
- **Python**
- **SQLite/PostgreSQL**
- **Stripe**

### Frontend
- **Bootstrap**
- **JavaScript/jQuery**
- **HTML Templates**
- **AJAX**

### Machine Learning
- **Image Embeddings**
- **Content-Based Filtering**

---

## 📋 Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ecommerce_website
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the project root:
```
SECRET_KEY=your-secret-key-here
STRIPE_PUBLIC_KEY=your-stripe-public-key
STRIPE_SECRET_KEY=your-stripe-secret-key
DEBUG=True
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to view the application.

---

## 🤖 Recommendation System

### How It Works
The recommendation system uses a **content-based filtering** approach:

1. **User Likes**: Users can like products they're interested in
2. **Image Similarity**: Each product has precomputed image embeddings
3. **Recommendation Generation**: When a user likes products, the system finds similar products based on:
   - Image similarity using precomputed embeddings
   - Product categories and attributes
4. **Display**: Recommended products appear on product detail pages

### User Interactions
- **Like Products**: Users can like products to indicate preferences
- **View Recommendations**: Similar products are suggested based on likes
- **Browse by Category**: Products organized by categories

---

## 🎯 Usage Guide

### For Customers
1. **Browse Products**: Navigate categories or search for products
2. **Product Details**: View comprehensive product information
3. **Like Products**: Click the like button to save preferences
4. **Add to Cart**: Build your shopping cart
5. **Checkout**: Complete purchase with Stripe payment
6. **View Recommendations**: See suggested products based on your likes

### For Administrators
1. **Admin Dashboard**: Access via `/admin/`
2. **Product Management**: Add, edit, and manage products with images
3. **Order Processing**: Handle customer orders and payments
4. **User Management**: Monitor user accounts and preferences

---

## 💳 Payment Integration

The application integrates **Stripe** for secure payment processing:
- Secure checkout process
- Credit card payments
- Order confirmation
- Payment history

### Stripe Setup
1. Create a Stripe account
2. Get your API keys from the Stripe dashboard
3. Add keys to your environment variables
4. Configure webhook endpoints (if needed)

---

## 📱 User Interface

### Key Pages
- **Home Page**: Featured products and categories
- **Product Listing**: Browse all products with filters
- **Product Detail**: Individual product pages with recommendations
- **Shopping Cart**: Review items before checkout
- **Checkout**: Stripe payment integration
- **Order History**: Track past purchases
- **User Profile**: Manage account information

---

## 📝 API Endpoints

Basic API structure for cart and recommendations:
- `/products/` - Product listings
- `/cart/` - Shopping cart management
- `/checkout/` - Payment processing
- `/recommendations/` - Get recommended products

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

---


## 🔮 Future Enhancements

- **Enhanced Recommendations**: Add collaborative filtering
- **Real-time Updates**: Live recommendation updates
- **User Reviews**: Product rating and review system
- **Wishlist**: Save products for later
- **Mobile App**: Companion mobile application
- **Analytics Dashboard**: Business intelligence features

