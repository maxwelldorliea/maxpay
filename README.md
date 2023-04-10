<img src='https://maxpay.maxwelldorliea.tech/images/maxpay_logo.png'
      alt='MaxPay Logo' width='300px' height='300px' style='border-radius: 5px;' />
# MaxPay Backend REST API
* Making Online payment and Integration easy in Liberia.
## Goal
My aim is to make payment processing on E-commerce Platform in Liberia easy and intuitive for both the end-users and E-commerce Platform Owners. This project is not intended to replace traditional payment systems like MTN Mobile Money and Orange MoMo Money but to sit as a middleman and make online payment processing easy and intuitive for both the end-users and E-commerce Platform Owners. This project in no way will have direct competition with either MTN Mobile Money or Orange MoMo Money. I am building this project specifically for Liberia.

## Why Create MaxPay When There Are Platforms Like PayPal, Stripe etc..
In Liberia about less than 15% of the population has access to credit card and more than 60% of the population uses MTN Mobile Money and Orange MOMO Money.
Therefore PayPal and Stripe don't fit in Liberia current economy. Based on these problem it's difficulty to do transactions on E-Commerce Platforms in Liberia.

## How Am I Going To Solve This Problem
I am building MaxPay around MTN Mobile Money and Orange MOMO Money to solve this problem.

## Technologies
- FastApi
- MySQL
- Mailgun

# API Routes

| Method |     Route            | Access Token Require | Role Require  | Description                              |
|:------:|:------------------:  | :-------------------:|:-------------:|:----------------------------------------:|
|  POST  | /api/v1/users        |         NO           | NONE          | Create a new user if all required fields were passed request body|
|  POST  | /api/v1/sign_in      |         NO           | NONE          | Return a new Access Token given the  correct username and password |
|  GET   | /api/v1/users        |         YES          | ADMIN         | Get the first 25 users                   |
|  GET   | /api/v1/users/{id}   |         YES          | USER          | Get an user given the user id            |
|  POST  | /api/v1/transfer     |         YES          | USER          | Send money from the current user to another given the current user has enough fund for the transaction |
|  PUT   | /api/v1/change_pin   |         YES          | USER          | Change user transaction pin given old transaction |
|  GET   | /api/v1/transactions |         YES          | USER          | Get an user transactions history         |
|  GET   | /api/v1/me           |         YES          | USER          | Returns the current user information     |


# Requirements
- MySQL
- Python3.10 (Should Work Fine from 3.8 Up)

# How To Run This Program
```
pip3 install -r requirement.txt
python3 -m api.v1.app
```

