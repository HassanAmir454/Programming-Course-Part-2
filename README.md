# Object-Oriented Programming in Python - Programming Course Part 2

**Course Institution**: Lab University of Applied Sciences (AMKE)  
**Language**: Python  
**Level**: Intermediate to Advanced

---

## 📋 Course Overview

This comprehensive course covers **Object-Oriented Programming (OOP)** principles and practical applications in Python. The curriculum progresses from foundational OOP concepts to real-world projects involving file handling, data serialization, database integration, and software design patterns. Students learn through hands-on exercises and progressively complex projects.

---

## 🎯 Learning Objectives

By completing this course, you will:
- Master OOP principles: encapsulation, inheritance, polymorphism, and abstraction
- Work with file I/O operations (CSV, JSON, encrypted files)
- Implement data serialization and deserialization patterns
- Integrate with databases using SQL
- Design scalable applications with clean architecture
- Build real-world projects with multiple components

---

## 📚 Course Structure

### **Week 0: Foundations & Basics**
Introduction to programming fundamentals and early OOP concepts.

**Projects:**
- **Task 1**: Counter Application - Basic class implementation
- **Task 2**: Temperature Converter - Simple utility functions
- **Task 3**: Coin Acceptor - State management
- **Task 4**: CLI Coin Acceptor - Command-line interface design

**Topics**: Classes, objects, methods, basic properties

---

### **Week 1: Intermediate OOP Concepts**
Deep dive into inheritance, polymorphism, and practical OOP patterns.

**Projects:**
- **Task 1**: IoT Devices - Device abstraction and control
- **Task 2**: Game Character - Character system with attributes and methods
- **Task 3**: Smart Device - Advanced device management
- **Task 4**: Crypto Wallet - Financial application with transactions
- **Task 5**: Entity System - Generic entity management framework

**Topics**: Inheritance, polymorphism, abstract classes, entity patterns

---

### **Week 2: Advanced Topics & Integration**
Database integration, role-based systems, and MySQL connectivity.

**Projects:**
- **Practice MySQL**: Database connectivity and queries
- **Roles Task**: Role-based access control system

**Topics**: Database integration, SQL queries, role-based architecture

---

### **Week 3: Real-World Projects**
Complex projects involving mathematical concepts and data structures.

**Projects:**
- **Cube Rotater**: 3D transformation and rotation algorithms
- **Maths Task**: Advanced mathematical operations
- **Rockets**: Physics simulation and object dynamics
- **Rotate Square**: Geometric transformations
- **Tasklist Application**: Task management system

**Topics**: Advanced algorithms, data structures, visual computing concepts

---

### **Week 4: Data Analysis & Visualization**
Real-world data analysis using Python libraries.

**Projects:**
- **NY Housing Analysis** (`housing_analysis.ipynb`): Data exploration and visualization
  - Dataset: NY-House-Dataset.csv
  - Tools: Jupyter Notebook, Pandas, Matplotlib
  - Output: Interactive HTML map (`ny_map.html`)

**Topics**: Data analysis, visualization, exploratory data analysis (EDA)

---

## 🏗️ Practice Projects (In-Depth)

### **Car Rental System** (Version 2.0)
Complete vehicle rental management system with OOP principles.

```
Paractice/Car rental 2.0/
├── main.py              # Entry point
├── vehicles.py          # Vehicle base class
├── cars.py              # Car subclass
├── bikes.py             # Bike subclass
├── file_handler.py      # File I/O operations
└── vehicles.csv         # Vehicle inventory data
```

**Concepts**: Inheritance, polymorphism, file handling, CSV operations

---

### **E-Commerce Platform**
Full-featured online shopping system with payment processing.

```
Paractice/ecommerce project/
├── main.py              # Application controller
├── model.py             # Product, Customer, Order, Payment classes
└── data.json            # Product and customer data
```

**Concepts**: Encapsulation, multiple payment methods, JSON serialization

---

### **Doctor Management System**
Healthcare system for managing doctors, appointments, and patient data.

```
Paractice/doctor system/
├── main.py
├── model.py             # Doctor, Patient, Appointment classes
├── paracticesql.py      # SQL database operations
└── (database integration)
```

**Concepts**: Database integration, complex relationships, CRUD operations

---

### **Deserialization Pattern**
Advanced data transformation from CSV to Python objects.

```
Paractice/Decerialization/
├── main.py              # Deserialization logic
├── item.py              # Item model
├── file_handler.py      # File operations
├── inventory.csv        # Raw data
└── paractice.py         # Additional exercises
```

**Concepts**: Data deserialization, factory pattern, type mapping

---

### **Additional Practice Projects**

| Project | Location | Focus |
|---------|----------|-------|
| School System | `School System/` | Data management, student/class organization |
| Hospital Task | `Hosipital Task/` | Patient records, CSV handling |
| Library System | `library task/` | Book management, search functionality |
| Ride Booking | `ride_booking/` | Booking system, user matching |
| Sodabottle | `Sodabottle/` | Simple state machine |
| Encapsulation Practice | `encapsulationpractice/` | Access modifiers, data hiding |

---

## 🛠️ Technologies & Tools

### **Core Technologies**
- **Language**: Python 3.x
- **Database**: MySQL/SQL
- **Data Formats**: CSV, JSON, Encrypted files
- **IDEs**: VS Code, PyCharm

### **Libraries & Frameworks**
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Notebooks**: Jupyter Notebook
- **File Handling**: Built-in modules (csv, json, pickle)
- **Database**: MySQL connector

### **File Formats**
- `.csv` - Comma-separated values (structured data)
- `.json` - JSON objects (flexible data format)
- `.enc` - Encrypted files (security)
- `.ipynb` - Jupyter notebooks (interactive analysis)

---

## 🚀 Running the Projects

### **Python Projects (Standard)**

```bash
# Navigate to project directory
cd "Programming-Course-Part-2/Paractice/Car rental 2.0"

# Run main.py
python main.py
```

### **Jupyter Notebooks (Week 4)**

```bash
# Navigate to Week 4
cd "Programming-Course-Part-2/Week 4"

# Start Jupyter
jupyter notebook housing_analysis.ipynb
```

### **Projects with Database**

Ensure MySQL is running before executing:
```bash
# Doctor system (requires database)
cd "Programming-Course-Part-2/Paractice/doctor system"
python paracticesql.py
```

---

## 📂 Directory Organization

```
Programming-Course-Part-2/
│
├── Week0 tasks/          # Foundational concepts (4 tasks)
├── Week1 tasks/          # Intermediate OOP (5 tasks)
├── Week2 tasks/          # Advanced & Database (2 projects)
├── Week 3(project)/      # Complex algorithms (5 projects)
├── Week 4/               # Data analysis (1 Jupyter notebook)
│
├── Paractice/            # Comprehensive practice projects
│   ├── Car rental/       # v1.0
│   ├── Car rental 2.0/   # v2.0 (improved)
│   ├── ecommerce project/
│   ├── doctor system/
│   ├── Decerialization/
│   ├── School System/
│   ├── Hospital Task/
│   ├── Library Task/
│   ├── Ride Booking/
│   ├── Sodabottle/
│   ├── Encapsulation Practice/
│   └── [Additional exercises]
│
├── Notes/                # Course notes & references
├── Testing/              # C# backup files (reference)
│
├── devices.csv           # Sample data files
├── devices_dec.csv
├── devices.enc
├── vehicles.csv
└── README.md             # This file
```

---

## 🎓 Key Concepts Covered

### **Object-Oriented Programming**
- ✅ Classes and Objects
- ✅ Encapsulation & Data Hiding
- ✅ Inheritance (single and multiple)
- ✅ Polymorphism & Method Overriding
- ✅ Abstract Base Classes
- ✅ Static and Class Methods

### **Data Handling**
- ✅ CSV file I/O operations
- ✅ JSON serialization/deserialization
- ✅ File encryption (basic)
- ✅ Error handling and validation

### **Database Programming**
- ✅ SQL queries (SELECT, INSERT, UPDATE, DELETE)
- ✅ Database design and relationships
- ✅ CRUD operations
- ✅ Transaction management

### **Software Design Patterns**
- ✅ Factory Pattern (deserialization)
- ✅ Singleton Pattern
- ✅ Observer Pattern
- ✅ Strategy Pattern (payment methods)
- ✅ MVC Architecture

### **Data Analysis**
- ✅ Exploratory Data Analysis (EDA)
- ✅ Data visualization
- ✅ Statistical analysis
- ✅ Interactive maps and charts

---

## 📊 Course Progress Tracker

| Week | Status | Topics | Projects |
|------|--------|--------|----------|
| Week 0 | ✅ Complete | Fundamentals | 4 Tasks |
| Week 1 | ✅ Complete | Intermediate OOP | 5 Tasks |
| Week 2 | ✅ Complete | Advanced & DB | 2 Projects |
| Week 3 | ✅ Complete | Complex Algorithms | 5 Projects |
| Week 4 | ✅ Complete | Data Analysis | 1 Jupyter NB |
| **Practice** | ✅ Complete | Real-world Projects | 12+ Projects |

---

## 💡 How to Use This Repository

1. **Learning**: Start with Week 0 tasks, progress sequentially through weeks
2. **Practice**: Explore practice projects in `/Paractice` for advanced patterns
3. **Reference**: Use Notes/ for quick reference and construction examples
4. **Projects**: Pick a project to understand how multiple concepts integrate
5. **Review**: Re-examine old code with new knowledge for deeper understanding

---

## 🔗 File Handling Guide

### **Reading CSV Files**
```python
from file_handler import FileHandler
fh = FileHandler("vehicles.csv")
rows = fh.read()
```

### **Working with JSON**
```python
import json
with open("data.json", "r") as f:
    data = json.load(f)
```

### **Database Operations**
```python
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_db"
)
```

---

## 🎯 Project Highlights

### **Most Comprehensive**
- Car Rental System 2.0 - Best practices for vehicle management
- E-Commerce Platform - Multiple design patterns implementation

### **Most Educational**
- Deserialization - Understanding factory pattern
- Doctor System - Real-world database integration

### **Most Creative**
- Cube Rotater - 3D transformations
- NY Housing Analysis - Data-driven insights

---

## 📝 Notes

- **Paractice** directory name has a typo (Practice) - contains all major projects
- CSV data files (`devices.csv`, `vehicles.csv`) are shared across multiple projects
- Encrypted files (`.enc`) demonstrate file security concepts
- Week 4 includes Jupyter Notebook for interactive analysis
- C# files in Testing/ are from parallel coursework (reference only)

---

## 🎯 Next Steps for Learning

1. Review Week 0-1 to strengthen OOP fundamentals
2. Deep-dive into any practice project of interest
3. Modify and extend projects with new features
4. Combine multiple projects into a larger system
5. Explore database optimization and scaling

---

## 📞 Course Resources

**Course Institution**: Lab University of Applied Sciences (AMKE)  
**Subject**: Object-Oriented Programming  
**Language**: Python 3.x  
**Difficulty**: Intermediate to Advanced

---

*This comprehensive course demonstrates professional software development practices through progressive projects and real-world applications.*
