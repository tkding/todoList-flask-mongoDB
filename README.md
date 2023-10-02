# Todo App

[![Video demo](https://img.youtube.com/vi/qNFYxW8aXsc/0.jpg)](https://youtu.be/qNFYxW8aXsc)

This is a simple Todo app built using Flask and MongoDB. It allows users to create, delete, and update tasks in a to-do list.

## Features

- **Create:** Add new tasks to your to-do list.
- **Delete:** Remove tasks from the list once they are completed or are no longer relevant.
- **Update:** Modify existing tasks to reflect changes or updates.

## Technologies Used

- **Flask:** A lightweight Python web framework used for building the backend of the application.
- **MongoDB:** A NoSQL database used for storing task data.

## Getting Started

### Prerequisites

Make sure you have Python, Flask, and MongoDB installed on your system.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tkding/todoList-flask-mongoDB.git
    cd todo-app
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up MongoDB:
   
   - Install MongoDB on your system if you haven't already.
   - Start the MongoDB server.

4. Run the application:

    ```bash
    python run.py
    ```

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

- **Create Task:** Click on the "Add Task" button and enter the task details.
- **Delete Task:** Click on the "Delete" button next to the task you want to remove.
- **Update Task:** Click on the task you want to edit, make changes, and click the "Update" button.
