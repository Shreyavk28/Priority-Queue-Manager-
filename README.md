# 🚀 Priority Queue Manager

A data-driven task management system designed to optimize engineering workflows. This application implements a **Priority Queue** algorithm to automatically rank tasks based on urgency (High, Medium, Low) rather than just creation time.

Built with **Python (Django)** and **Bootstrap 5**, focusing on Object-Oriented Programming (OOP) principles and efficient database querying.

---

## 📸 Project Screenshots
![Dashboard Preview](https://via.placeholder.com/800x400.png?text=Upload+Your+App+Screenshot+Here)

---

## 🛠️ Technical Highlights (Engineering Approach)
Unlike standard To-Do apps, this system focuses on **Data Structures** and **Backend Logic**:

* **Priority Queue Algorithm:** Implemented custom sorting logic using **Django Conditional Expressions (`Case`/`When`)**. This assigns numeric weights to string priorities (`High=1`, `Medium=2`, `Low=3`) to ensure critical tasks always bubble to the top.
* **Object-Oriented Design:** utilized Python Classes (`models.Model`) to define schema architecture, leveraging inheritance for modular code.
* **State Management:** Boolean state tracking for task completion (Active vs. Completed) with visual toggle indicators.
* **Optimized Search:** Integrated an ORM-based search engine using `icontains` filters for real-time query processing.

---

## 💻 Tech Stack
* **Backend:** Python, Django 5.0
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsive UI)
* **Database:** SQLite (Development)
* **Version Control:** Git & GitHub

---

## 🚀 Key Features
* ✅ **Smart Sorting:** "High Priority" tasks automatically appear at the top of the stack.
* ✅ **Visual Feedback:** Color-coded badges (Red/Yellow/Green) for instant priority recognition.
* ✅ **Search Functionality:** Filter tasks by keywords dynamically.
* ✅ **Task Toggling:** Mark tasks as done with a strikethrough effect without deleting them (History retention).
* ✅ **Responsive Design:** Fully functional on Desktop and Mobile devices.

---

## ⚙️ How to Run Locally

If you want to clone and run this project on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Shreyavk28/Priority-Queue-Manager.git](https://github.com/Shreyavk28/Priority-Queue-Manager.git)
    ```

2.  **Navigate to the project folder:**
    ```bash
    cd Priority-Queue-Manager
    ```

3.  **Install dependencies:**
    ```bash
    pip install django
    ```

4.  **Run the server:**
    ```bash
    python manage.py runserver
    ```

5.  **Open your browser:**
    Go to `http://127.0.0.1:8000/`

---

### 👤 Author
**Shreya V K** *Aspiring Software Engineer | Final Year Computer Science Student* [LinkedIn Profile](https://www.linkedin.com/in/shreya-vk-666538260/)
