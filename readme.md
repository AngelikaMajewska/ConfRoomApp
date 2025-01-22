# ConfRoomApp: Conference Room Management System

This Django project is a conference room management application that allows users to manage rooms, bookings, and search for available conference spaces. It also provides an API for retrieving room and booking data.

---

## Features
- **Add Conference Rooms**: Create new rooms with details like name, capacity, and whether it has a projector.
- **Modify Room Details**: Edit existing room information.
- **Delete Rooms**: Remove rooms from the system.
- **Book Rooms**: Reserve rooms for specific dates with comments.
- **View Room Bookings**: See bookings for a specific room, including upcoming reservations.
- **Search Rooms**: Search for rooms based on name, capacity, and projector availability.
- **REST API**: Retrieve room and booking data in JSON format.

---

## Table of Contents
1. [Setup](#setup)
2. [Project Structure](#project-structure)
3. [Key Functionality](#key-functionality)
4. [API Endpoints](#api-endpoints)
5. [Screenshots](#screenshots)



---

## Setup
### Requirements
- Python 3.8+
- Django 4.2+
- Django REST Framework

## Project structure

The project structure for this Django application is organized as follows:
```
confroom_app/
├── migrations/
│   ├── init.py
├── templates/
│   ├── confroom_app/
│   │   ├── add_room.html
│   │   ├── booking.html
│   │   ├── homepage.html
│   │   ├── modify_room.html
│   │   ├── search.html
│   │   ├── show_room.html
├── init.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
api/
├── init.py
├── urls.py
├── views.py
confroom_project/
├── init.py
├── settings.py
├── urls.py
├── wsgi.py
static/
├── css/
│   ├── styles.css
├── js/
│   ├── script.js
db.sqlite3
manage.py
```
### Description of Directories and Files:

- **`confroom_app/`**:  
  This is the main app where the core business logic for managing conference rooms and bookings resides. It contains:
  - **`migrations/`**: Contains the database migration files.
  - **`templates/`**: Contains HTML files for rendering views.
  - **`models.py`**: Defines the database models for `Room` and `Booking`.
  - **`views.py`**: Contains class-based views that implement functionality like adding, modifying, and booking rooms.
  - **`admin.py`**: Registers models to appear in Django's admin interface.
  - **`tests.py`**: Placeholder for unit tests related to the app's functionality.

- **`api/`**:  
  This folder contains the REST API views and URLs for accessing room and booking data in a programmatic way.
  - **`urls.py`**: Defines URL patterns for the API endpoints.
  - **`views.py`**: Contains the views for the API, handling data retrieval and response formatting.

- **`confroom_project/`**:  
  This is the root directory for the Django project that contains settings and project-wide configurations.
  - **`settings.py`**: Contains the Django project settings (database configurations, static files, etc.).
  - **`urls.py`**: Defines URL patterns for the overall application, including the `confroom_app` and `api` URLs.
  - **`wsgi.py`**: The WSGI entry point for the application when deploying.
  - **`__init__.py`**: Marks the directory as a Python package.

- **`static/`**:  
  This folder contains static files such as CSS and JavaScript used in the front end.
  - **`css/`**: Contains CSS files for styling the app.

- **`db.sqlite3`**:  
  The SQLite database where the data for rooms and bookings is stored.

- **`manage.py`**:  
  The command-line tool that allows you to interact with the Django project (e.g., running the server, applying migrations).

## Key Functionality

1. **Add Conference Rooms**:  
   - Create new rooms by providing details such as name, capacity, and projector availability.  
   - Validates room details to prevent duplicates or invalid data.

2. **Modify Room Details**:  
   - Edit existing room information, such as name, capacity, or projector availability.  
   - Ensures updated data is unique and valid.

3. **Delete Rooms**:  
   - Remove rooms from the system with a simple action.

4. **Book Rooms**:  
   - Reserve rooms for specific dates with optional comments.  
   - Prevents double booking for the same date and room.

5. **View Room Bookings**:  
   - Display detailed bookings for individual rooms.  
   - Shows upcoming reservations in a formatted view.

6. **Search Rooms**:  
   - Search for rooms based on name, capacity, and projector availability.  
   - Displays filtered results dynamically.

7. **REST API**:  
   - Access room and booking data programmatically using JSON responses.  
   - Provides easy integration with external applications or services.

---

## API Endpoints

### 1. **List Bookings**
   - **URL**: `/api/bookings/`  
   - **Method**: GET  
   - **Description**: Retrieve a list of all bookings, including room information, date, and comments.  
   - **Response Example**:
     ```json
     [
         {
             "id": 1,
             "room": 1,
             "date": "2025-01-25",
             "comment": "Team meeting"
         },
         {
             "id": 2,
             "room": 2,
             "date": "2025-01-26",
             "comment": "Client presentation"
         }
     ]
     ```

### 2. **List Rooms**
   - **URL**: `/api/rooms/`  
   - **Method**: GET  
   - **Description**: Retrieve a list of all conference rooms, including their name, capacity, and whether they have a projector.  
   - **Response Example**:
     ```json
     [
         {
             "id": 1,
             "name": "Blue",
             "capacity": 20,
             "has_projector": true
         },
         {
             "id": 2,
             "name": "Green",
             "capacity": 15,
             "has_projector": false
         }
     ]
     ```

---

## Screenshots

### Homepage

![img](https://github.com/user-attachments/assets/743a0e11-e03a-43b7-b766-ce0d869d3270)


### Search page

![img_1](https://github.com/user-attachments/assets/fedd1b82-c0f5-476f-96cf-0739f5220bbe)


### Room details

![img_2](https://github.com/user-attachments/assets/40f9ef3c-cdd3-4055-88aa-1f748df1e9ed)


### Booking view

![img_3](https://github.com/user-attachments/assets/f03e8730-ceaa-4d9c-9d05-b4ea583cbe95)


### Django REST framework view

![img_4](https://github.com/user-attachments/assets/d5fff6fb-21b1-48ee-8b0a-a86ad3d95523)
