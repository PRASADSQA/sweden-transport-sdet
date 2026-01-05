# Sweden Public Transport Ticketing – SDET QA Automation

## Overview
This project demonstrates a real-world, SDET-focused approach to quality engineering using a simulated Sweden public transport ticketing system.

It showcases the transition from **manual QA to Software Development Engineer in Test (SDET)** by connecting:
- Advanced requirements engineering
- Manual test planning and test case design
- Selective UI automation using Playwright and Python

The goal of the project is not to automate everything, but to apply **engineering judgment** to decide what should be automated based on business criticality, regression risk, and return on investment (ROI).

---

## Project Objectives
- Apply advanced requirements engineering concepts to define testable requirements
- Design structured manual test plans and test cases
- Identify high-value test cases suitable for automation
- Implement maintainable UI automation using Playwright (Python)
- Demonstrate SDET best practices such as the test pyramid and Page Object Model

---

## System Under Test (SUT)
The system under test is a simulated public transport ticketing platform inspired by Swedish public transport services. Core user journeys include:
- User authentication
- Ticket selection and purchase
- Purchase confirmation

---

## What Is Automated
- User login (business-critical path)
- Ticket purchase flow (high regression risk)

## What Is Not Automated
- UI text translations
- Visual styling and layout
- Administrative and low-risk features

These decisions reflect an SDET mindset focused on automation value rather than automation quantity.

---

## Tech Stack
- Python 3
- Playwright (UI automation)
- Pytest (test execution)
- Page Object Model (design pattern)

---

## How to Run the Project

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install
pytest
