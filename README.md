# Financial Portfolio Management API Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [API Endpoints](#api-endpoints)
   - [Fetch User Profile](#fetch-user-profile)
   - [Manage User Profile](#manage-user-profile)
   - [Manage User Risk Profile](#manage-user-risk-profile)
   - [Risk Profiling Questions](#risk-profiling-questions)
   - [Manage User Portfolio](#manage-user-portfolio)
   - [Portfolio Recommendations](#portfolio-recommendations)
   - [Portfolio Price Trends](#portfolio-price-trends)
   - [Portfolio Past Performance](#portfolio-past-performance)
   - [LLM Response](#llm-response)
3. [Installation and Setup](#installation-and-setup)
4. [Usage](#usage)
5. [Contributing](#contributing)

## Introduction
This API provides a suite of endpoints for managing user profiles, portfolios, and risk profiles in a financial portfolio management context. It integrates with language models for recommendations and uses a ticker manager for portfolio management.

## API Endpoints

### Fetch User Profile
- **Endpoint:** `/profile/{login_name}`
- **Method:** GET
- **Description:** Retrieves the profile of a user based on their login name.

### Manage User Profile
- **Endpoint:** `/profile/`
- **Method:** PUT
- **Description:** Creates or updates a user profile with provided details.

### Manage User Risk Profile
- **Endpoint:** `/profile/questions/{login_name}`
- **Method:** PUT
- **Description:** Updates user risk profile based on questionnaire responses.

### Risk Profiling Questions
- **Endpoint:** `/questions`
- **Method:** GET
- **Description:** Retrieves a set of risk profiling questions for the user.

### Manage User Portfolio
- **Endpoint:** `/portfolio/{login_name}`
- **Method:** GET
- **Description:** Manages the user's investment portfolio based on their risk profile.

### Portfolio Recommendations
- **Endpoint:** `/portfolio/recommendations/{login_name}`
- **Method:** GET
- **Description:** Provides portfolio recommendations using a language model.

### Portfolio Price Trends
- **Endpoint:** `/portfolio/pricetrends/{ticker}`
- **Method:** GET
- **Description:** Fetches price trends for a specified stock ticker.

### Portfolio Past Performance
- **Endpoint:** `/portfolio/pastperformance/{login_name}`
- **Method:** GET
- **Description:** Evaluates the past performance of a user's portfolio.

### LLM Response
- **Endpoint:** `/llm/{login_name}`
- **Method:** GET
- **Description:** Fetches responses from a language model for specific questions.

## Installation and Setup
Instructions on setting up the API server and its dependencies.

## Usage
Examples and guidelines on how to interact with the API endpoints.

## Contributing
Guidelines for contributing to the development and improvement of this API.

