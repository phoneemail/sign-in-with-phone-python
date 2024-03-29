# Sign in with Phone - Django(Python) Demo

Welcome to the Django demo repository for integrating "Sign in with Phone" functionality into your python applications. This repository showcases how you can seamlessly implement phone verification and authentication using our innovative plugin.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example Demo](#example-demo)
5. [Documentation](#documentation)
6. [Website](#website)

## Introduction

Phone Email introduces an innovative solution for user authentication - "Sign in with Phone". Our plugin empowers websites to offer seamless phone number verification to users at minimal or no cost. Similar to Firebase phone authentication, our solution embeds a "Log in with phone" button on client websites. Upon clicking, a verification window prompts users to enter their country code and mobile number. After successful verification through OTP sent to the user's mobile, control redirects back to the client website with an access token. Subsequently, passing this access token to the `getuser` REST API retrieves the verified mobile number.

### Key Benefits:
- **Cost-Effective:** Minimal or no cost for phone verification.
- **Enhanced Security:** OTP-based verification ensures secure authentication.
- **Seamless Integration:** Easy integration into existing web applications.
- **Improved User Experience:** Streamlined authentication process for users.

## Installation

To integrate the "Sign in with Phone" functionality into your Django project, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/phoneemail/sign-in-with-phone-python.git
    ```


2. **Navigate to the project directory:**

    ```bash
    cd sign-in-with-phone-python
    ```


3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Change the configuration:**
Replace `CLIENT_ID` with your client ID and `YOUR_REDIRECT_URL` with your success page URL in the `page.js` file.

## Usage

To utilize the application:

1. **Start the application:**

    ```bash
    python manage.py runserver
    ```

2. **Open URL on a browser:**
Access the application on your browser using the provided URL.

## Example Demo

Experience the seamless authentication process firsthand with our [demo](https://www.phone.email/demo-login). Our demo provides a live demonstration of the "Sign in with Phone" plugin, showcasing its functionality and ease of use. Explore the demo to understand how the plugin can enhance the authentication experience on your website. 

## Documentation

For comprehensive documentation on integrating the "Sign in with Phone" plugin into your Django python application, refer to our [documentation](https://www.phone.email/docs#python). The documentation provides detailed instructions, code samples, and configuration options to help you seamlessly integrate the plugin into your project. 

## Website

Visit our [website](https://www.phone.email) to learn more about our authentication solutions and explore additional features and services. Experience the future of authentication with Phone Email's "Sign in with Phone" plugin.
By implementing our plugin, you can elevate the security of your website, enhance user experience, and streamline the authentication process for your users. Embrace the power of phone verification with Phone Email's innovative solution.


---
Developed by [Phone Email](https://www.phone.email)



