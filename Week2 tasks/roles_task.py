import mysql.connector

def show_performance(user_id):
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@sql.01",  # <- replace with your MySQL password
        database="university"
    )
    cursor = conn.cursor()

    # Step 1: Get the user's role
    cursor.execute("SELECT role_id, name FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()

    if not user:
        print("User not found!")
        return

    role_id, user_name = user

    # Step 2: Determine query based on role
    # role_id = 1 -> Student, see only own performance
    # role_id != 1 -> Teacher/Supervisor/Parent, see all students
    if role_id == 1:
        query = """
        SELECT users.name, users.email, roles.role, performance.grade, performance.credits
        FROM users
        JOIN roles ON users.role_id = roles.id
        JOIN performance ON users.user_id = performance.student_id
        WHERE users.user_id = %s
        """
        cursor.execute(query, (user_id,))
    else:
        query = """
        SELECT users.name, users.email, roles.role, performance.grade, performance.credits
        FROM users
        JOIN roles ON users.role_id = roles.id
        JOIN performance ON users.user_id = performance.student_id
        """
        cursor.execute(query)

    results = cursor.fetchall()

    # Step 3: Print results
    if results:
        print(f"\nHello {user_name}! Here is the performance data you can see:\n")
        for name, email, role, grade, credits in results:
            print(f"{name} | {email} | {role} | Grade: {grade} | Credits: {credits}")
    else:
        print("No performance data found.")

    cursor.close()
    conn.close()


# Ask user for ID
try:
    uid = int(input("Enter your user ID: "))
    show_performance(uid)
except ValueError:
    print("Please enter a valid number for user ID.")