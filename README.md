# Event Management System

This is a **Server-Side Rendered (SSR)** Event Management System built using the Django framework. The project facilitates managing events by allowing users to create, view, and manage event details through an intuitive interface.

---

## Features

- **User Authentication**
  - Sign Up, Login, and Logout functionalities.
  - Role-based access control (Admin and User roles).

- **Event Management**
  - Create, Update, and Delete Events.
  - View event details and attendees.

- **Responsive Design**
  - Optimized for desktops and mobile devices.

- **Django Admin Panel**
  - Manage users and events efficiently through Django's built-in admin interface.

---

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap (for responsiveness)
- **Backend**: Python, Django
- **Database**: SQLite (default Django database)
- **Template Engine**: Django Templates

---

## Installation

Follow the steps below to set up and run the project on your local system:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd event-management-system
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## Usage

1. **Admin Role**:
   - Login to the admin panel at `http://127.0.0.1:8000/admin/`.
   - Use the admin panel to manage events and users.

2. **User Role**:
   - Sign up to create a new account.
   - Login to view available events and manage personal event details.

---

## Project Structure

```
Event Management System/
|
├── event_management/         # Main Django app folder
│   ├── templates/            # HTML templates
│   ├── static/               # Static files (CSS, JS, images)
│   ├── models.py             # Database models
│   ├── views.py              # Business logic
│   ├── urls.py               # URL routing
│   └── ...
|
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Contributors

This project is developed and maintained by:

- [Sugam Pokharel](#)
- [Milan Shahi](#)
- [Milan Magar](#)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Feedback and Contributions

We welcome feedback and contributions! Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---
