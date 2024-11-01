# INTEGRATED HOSPITALITY RESERVATION SYSTEM
# Abstract
- The Hotel Management System is a digital platform that automates hotel operations.
- Features:
  - Guest login to view bookings
  - Admin dashboard for staff management
  - Reduces manual processes, improves service quality
  - Chatbot makes you more convenient to about your resort details.
# Installation
1. Install the XAMPP control panel and setup the sql database.
2. Open your browser and navigate to,
   - User page -- http://localhost/Hotel/
   - Admin page -- http://localhost/Hotel/admin/index.php
3. To Run the chatbot which was in the project the following commands need to be Run in the Terminal,
   - cd .\chatbot\
   - cd .\chatbot\
   - cd .\bot\
   - cd .\bot_model\
   - python train.py
   - cd ..
   - cd ..
   - python manage.py runserver
   
# Table of Contents
1. Introduction
2. System Analysis
3. Existing vs Proposed System
4. Software Tools Used
5. System Design

# Introduction

## Project Aims and Objectives
1. Develop an efficient hotel management system.
2. Provide online room booking.
3. Create a guest login dashboard for booking history.
4. Include a search function for room availability.
5. Admin dashboard for staff to manage rooms and amenities.

## Background
1. Centralized customer management improves guest services.
2. Inventory management ensures the availability of amenities.
3. Streamlined operations reduce manual processes.

## Operating Environment
- **Processor**: Intel Core Processor or higher
- **OS**: Windows 7 or Ubuntu
- **Memory**: Minimum 1GB RAM
- **Storage**: Minimum 3GB
- **Database**: MySQL

# System Analysis

## Software Requirement Specification
1. **General Description**:
   - Replaces manual processes with digital management.
2. **Problem Statement**:
   - Manual record-keeping risks: file loss, damage, difficult retrieval.
3. **System Objectives**:
   - Improve control and performance, save costs, and enhance guest experience.


# Existing vs Proposed System
1. **Separate Login for Staff & Guests**.
2. **Online Reservation System**.
3. **Online Notice Board** for hotel announcements.
4. **Document Upload** for staff to share training materials.
5. **Guest Reports**: Generate activity and occupancy reports.
6. **Service Requests** for guests to request services.

# Software Tools Used

## Front End
- HTML: Structure and layout of web pages.
- CSS: Styling and formatting.
- JavaScript: Enhances interactivity.
- PHP: Server-side scripting for database connectivity.

## Back End
- MySQL: Database management.

# System Design

## Database Design
1. Designed using MySQL with tables for managing guests, rooms, inventory, and booking history.
2. Relationship diagrams (class diagram) ensure data integrity and streamline queries.
