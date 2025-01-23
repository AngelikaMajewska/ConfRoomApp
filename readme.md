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
2. [Key Functionality](#key-functionality)
3. [API Endpoints](#api-endpoints)
4. [Screenshots](#screenshots)



---

## Setup
### Requirements
- Python 3.8+
- Django 4.2+
- Django REST Framework


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
