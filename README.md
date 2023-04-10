<img src='https://maxpay.maxwelldorliea.tech/images/maxpay_logo.png'
      alt='MaxPay Logo' width='300px' height='300px' style='border-radius: 5px;' />
# MaxPay Backend REST API
* Making Online payment and Integration easy in Liberia.
* Live Version
   https://maxpay.maxwelldorliea.tech
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
- SvelteKit
- Tailwind CSS

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


# Backend

# Requirements
- MySQL
- Python3.10 (Should Work Fine from 3.8 Up)

```bash
# Clone the repo
git clone https://github.com/Maxcarrassco/maxpay_backend
# Move into maxpay directory
cd maxpay_backend
# Copy env template to .env
cp env .env
```
- Edit .env
```bash
HOST=your-db-host
DB_USER=your-db-username
DB_PASS=your-db-password
DB=your-db-name
ENV=test
JWT_SECRET=your-jwt-secret-key
JWT_TIME_TO_LIVE=user-access-token-expiring-time(in minute)
JWT_ALGORITHM=your-jwt-algorithm
DEFAULT_PIN=user-default-transaction-pin
MAIL_API_KEY=your-mailgun-api-key
MAIL_DOMAIN=your-mailgun-domain_name(example mail.yourdomain.com)
SYSTEM_MAIL=your-company-mail(mail use to send  verification code and transaction notification)
```
# How to run the backend
```bash
pip3 install -r requirement.txt
python3 -m api.v1.app
```

# Frontend
# Requirement
- Node 16.x.x

```bash
# Move into the frontend directory
cd frontend
# install all dependency
npm install
```

## How to run the frontend

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## How to run production version

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

<b>Created By Maxwell Dorliea With ♥️.</b>
