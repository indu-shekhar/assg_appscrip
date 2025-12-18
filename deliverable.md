Trade Opportunities API - Developer Task

Project Overview
Build a FastAPI service that analyzes market data and provides trade opportunity
insights for specific sectors in India.
Core Requirement
Create one main endpoint that accepts a sector name (e.g.,
"pharmaceuticals", "technology", "agriculture") and returns a structured market
analysis report with current trade opportunities.
Technical Requirements
Backend Framework
 FastAPI
 Session management
 Rate limiting
 Security best practices
 Input validation
AI/Data Sources
 LLM: Google Gemini API for analysis (can make a free account and can
use it) / any other model of your choice
 Web Search: Various APIs available (DuckDuckGo, etc.)
 Data Collection: Manual scraping or through scrapping API requests etc
Storage
 In-memory storage only (no database required)
Security
 Authentication (simple auth/JWT/guest auth - your choice)
 Input validation
 Rate limiting implementation
API Specification

Single Endpoint
GET /analyze/{sector}
Sample Request
GET /analyze/pharmaceuticals
Expected Response Format
The API should return a structured markdown report that can be saved as a .md
file.
Implementation Expectations
Core Workflow
1. Accept sector name as input
2. Search for current market data/news for that sector
3. Use Gemini API to analyze collected information
4. Generate a structured markdown report
5. Apply rate limiting and security measures
System Architecture
 Clean separation between data collection, AI analysis, and API layers
 Proper error handling for external API failures
 Session tracking for API usage
 Rate limiting per user/session
Evaluation Criteria
 FastAPI Implementation: Proper async handling, error responses,
documentation
 AI Integration: Effective use of Gemini API for analysis
 Data Collection: Ability to gather relevant market information
 Security: Authentication, input validation, rate limiting
 Code Quality: Organization, error handling, logging
Deliverables
1. Working FastAPI application
2. Single endpoint that produces markdown market analysis reports
3. Security features implemented
4. API documentation
5. README with setup instructions

Time Allocation
0-1 day maximum
Success Criteria
 API accepts sector names and returns markdown analysis reports
 Reports contain relevant, current market information
 Security measures prevent abuse
 System handles errors gracefully
 Code is clean and well-organized