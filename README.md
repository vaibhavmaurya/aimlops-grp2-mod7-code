# Detailed API Endpoint Documentation

## Table of Contents
1. [Fetch User Profile](#1-fetch-user-profile)
2. [Manage User Profile](#2-manage-user-profile)
3. [Manage User Risk Profile](#3-manage-user-risk-profile)
4. [Risk Profiling Questions](#4-risk-profiling-questions)
5. [Manage User Portfolio](#5-manage-user-portfolio)
6. [Portfolio Recommendations](#6-portfolio-recommendations)
7. [Portfolio Price Trends](#7-portfolio-price-trends)
8. [Portfolio Past Performance](#8-portfolio-past-performance)
9. [LLM Response](#9-llm-response)

## 1. Fetch User Profile
- **Endpoint:** `/profile/{login_name}`
- **Method:** GET
- **Description:** 
  - Retrieves the profile of a user based on their unique login name.
  - Accesses user-specific data, including investment preferences and profile details.
  - Returns profile data if the user exists; otherwise, reports an error.

## 2. Manage User Profile
- **Endpoint:** `/profile/`
- **Method:** PUT
- **Description:** 
  - Allows creation or updating of a user's profile.
  - Accepts user details such as name and investible amount.
  - Useful for setting up a new profile or updating existing information.

## 3. Manage User Risk Profile
- **Endpoint:** `/profile/questions/{login_name}`
- **Method:** PUT
- **Description:** 
  - Updates the user's risk profile based on questionnaire responses.
  - Essential for tailoring investment strategies to the user's risk tolerance.
  - Users provide answers to assess their investment risk profile.

## 4. Risk Profiling Questions
- **Endpoint:** `/questions`
- **Method:** GET
- **Description:** 
  - Fetches questions to understand the user's risk tolerance.
  - Questions gauge the user's comfort with different investment risks.

## 5. Manage User Portfolio
- **Endpoint:** `/portfolio/{login_name}`
- **Method:** GET
- **Description:** 
  - Manages the user's investment portfolio based on their risk profile.
  - Automates investment allocation or adjusts portfolios as needed.

## 6. Portfolio Recommendations
- **Endpoint:** `/portfolio/recommendations/{login_name}`
- **Method:** GET
- **Description:** 
  - Provides investment recommendations using language models.
  - Considers the user's risk profile and preferences for suitable options.

## 7. Portfolio Price Trends
- **Endpoint:** `/portfolio/pricetrends/{ticker}`
- **Method:** GET
- **Description:** 
  - Offers historical price trends for specific stock tickers.
  - Useful for analyzing the price history of stocks.

## 8. Portfolio Past Performance
- **Endpoint:** `/portfolio/pastperformance/{login_name}`
- **Method:** GET
- **Description:** 
  - Assesses the past performance of a user's investment portfolio.
  - Helps users understand the effectiveness of their investment strategies.

## 9. LLM Response
- **Endpoint:** `/llm/{login_name}`
- **Method:** GET
- **Description:** 
  - Fetches language model responses to user queries.
  - Can be used for insights on market trends or specific stock information.
