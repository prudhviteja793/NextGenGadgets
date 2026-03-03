# NextGenGadgets QA & DevOps Project
**Software Testing Tools Final Project** | **Developer:** Prudhvi Teja Reddy Kandula (ID: 5805128)

## 📝 Project Overview
NextGenGadgets is a comprehensive e-commerce platform built to demonstrate a full-stack Quality Assurance lifecycle. This project integrates functional automation (Selenium & Katalon), performance stress testing (JMeter), and Continuous Integration (GitHub Actions) to ensure a robust, production-ready application.

---

## 🛠️ Project Structure
The repository is organized into distinct layers of the testing pyramid:
* **website/**: Front-end application (HTML5, CSS3, JavaScript).
* **backend/**: Python/Flask API and database connection logic.
* **selenium_tests/**: Python POM framework with Pytest and Excel reporting.
* **katalon_tests/**: GUI-based regression suite for viewport and data-driven testing.
* **jmeter_tests/**: Performance test plans (.jmx) and HTML dashboard reports.
* **.github/workflows/**: CI/CD pipeline configuration for automated testing.
  
---

## 🌐 Web Application Features
The site includes specific "testable" elements designed to fulfill the academic requirements:
* **Authentication**: Login/Registration with Regex-based validation.
* **Dynamic Content**: A sortable/paginated order history table and a real-time Date & Time banner.
* **User Interaction**: A multi-step checkout process and a drag-and-drop shopping cart reordering feature.
* **Advanced UI**: Simulated secure payment iframe and dynamic navigation menus.
* **Database Backend**: Persistent storage using MySQL/phpMyAdmin for users and orders.

---

## 🐍 Automated Functional Testing (Selenium & Katalon)
The project utilizes a dual-tool approach to maximize test coverage:

### Selenium POM Framework
* **End-to-End (E2E) Workflow**: Full automation of the "Login to Checkout" user journey.
* **Explicit Wait Handling**: Utilization of `WebDriverWait` for dynamic elements and asynchronous table loading.
* **Custom Reporting**: Automated generation of test execution summaries in `.xlsx` format for stakeholder review.

### Katalon Studio Suite
* **Viewport & Cross-Device Testing**: Automated verification of UI responsiveness across Desktop and Tablet resolutions.
* **Data-Driven Testing (DDT)**: Validation of registration forms using external Excel data files to test boundary conditions.
* **Dynamic Locators**: Implementation of relative XPATHs to ensure test stability against UI shifts.

---

## 📊 Performance Engineering (JMeter)
To ensure system stability under high-traffic conditions, a comprehensive JMeter suite was implemented:
* **Stress Testing**: Simulating concurrent user loads (20-100 threads) on critical endpoints (`/login`, `/cart`).
* **Response Time Analysis**: Monitoring server latency and throughput (TPS) for the checkout process.
* **Reporting**: Detailed HTML dashboards featuring APDEX scores, latency histograms, and error-rate pie charts.

---

## 🚀 CI/CD Pipeline (GitHub Actions)
This project implements **Continuous Integration** via GitHub Actions to maintain a "Fail-Fast" development cycle:
* **Automated Triggers**: Tests execute automatically on every `push` or `pull_request` to the main branch.
* **Dependency Management**: Automated environment setup including Python installation and library caching.
* **Quality Gates**: Builds are marked as "Failed" if functional unit tests do not pass 100% of cases.

---

## 📊 Comparison: Selenium vs. Katalon
As required by the project documentation, here is a comparison of the two tools:

| Feature | Selenium (Python) | Katalon Studio |
| :--- | :--- | :--- |
| **Setup & Complexity** | Higher; requires manual POM and utility configuration. | Lower; uses built-in keywords and a GUI-based object repository. |
| **Data-Driven Testing** | Requires custom scripts (Pandas/Openpyxl) to map Excel data. | Native "Data Files" feature allows for easy binding without coding. |
| **Maintenance** | Manual updates to Page Classes are needed when UI changes. | Centralized Object Repository allows for global updates to selectors. |
| **Reporting** | Requires third-party plugins or custom code for Excel output. | Provides professional, built-in visual and log-based reports. |

---

## 💻 Local Setup & Execution

Follow these instructions to set up the environment and execute the various testing suites locally.

### 1. Prerequisites
Ensure the following are installed and configured on your machine:
* **Python 3.11+**: [Download here](https://www.python.org/downloads/)
* **XAMPP**: For MySQL and Apache services. [Download here](https://www.apachefriends.org/index.html)
* **Java JDK 17+**: Required to run Apache JMeter. [Download here](https://www.oracle.com/java/technologies/downloads/)
* **Git**: To clone and manage the repository.

### 2. Environment Setup

1. **Database Configuration**:
   * Launch the **XAMPP Control Panel**.
   * Start the **Apache** and **MySQL** modules.
   * Access `http://localhost/phpmyadmin` in your browser.
   * Create a new database named `nextgen_db`.
   * Click the **Import** tab and select the `db_setup.sql` file located in the project root to initialize tables.

2. **Install Dependencies**:
   Execute the following command in your terminal to install the required Python libraries:
   ```bash
   pip install pytest selenium flask mysql-connector-python

### 3. Launch the Application
To run the platform locally, you must host the web files:

1. **Open a Command Prompt** and navigate to the `website/` directory:
   ```bash
   cd C:\Users\matrix011K\Desktop\NextGenGadgets\website

2. **Start the local Python server:**
   ```bash
   python -m http.server 8000

### 4. Execute Automation Suites

1. **Selenium Functional Tests**:
   Open a new Command Prompt, navigate to the project root, and run:
   ```bash
   python -m pytest selenium_tests/

2. **JMeter Performance Tests (Non-GUI Mode)**:
   To execute the stress test and generate the HTML Dashboard report:
   ```bash
   jmeter -n -t jmeter_tests/NextGen_Performance.jmx -l results.csv -e -o jmeter_tests/dashboard_report/

3. **Katalon Studio Regression**:
   * Open Katalon Studio.
   * Import the katalon_tests/ project folder.
   * Open Test Suites > NextGenGadgets_Full_Regression and click Run.

---
