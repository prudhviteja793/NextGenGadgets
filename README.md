# NextGenGadgets QA Project
**Software Testing Tools Final Project** | **Developer:** Prudhvi Teja Reddy Kandula (ID: 5805128)

## 📝 Project Overview
NextGenGadgets is a mock e-commerce platform built to demonstrate advanced automation testing techniques. This project features a custom front-end application and two distinct automation suites—Selenium (Python) and Katalon Studio—to validate functional, data-driven, and responsive requirements.

---

## 🛠️ Project Structure
The repository is organized to showcase a clear separation between application code and automation frameworks:
* **website/**: Source code for the e-commerce site (HTML, CSS, JS).
* **selenium_tests/**: Python-based framework using Page Object Model (POM) and Pytest, featuring automated Excel reporting and dynamic wait handling.
* **katalon_tests/**: Katalon Studio project containing 25 test cases, including data-driven suites, viewport responsiveness tests, and custom XPATH locators.
* **results/**: Automation execution reports, Excel results, and screenshots.

---

## 🌐 Web Application Features
The site includes specific "testable" elements designed to fulfill the academic requirements:
* **Authentication**: Login/Registration with Regex-based validation.
* **Dynamic Content**: A sortable/paginated order history table and a real-time Date & Time banner.
* **User Interaction**: A multi-step checkout process and a drag-and-drop shopping cart reordering feature.
* **Advanced UI**: Simulated secure payment iframe and dynamic navigation menus.

---

## 🧪 Katalon Studio Testing Suite
The Katalon suite leverages built-in reporting and easy maintenance of web objects to provide a robust regression layer.

### Key Test Scenarios:
* **Viewport Testing (TC_K01 & TC_K02)**: Verified site responsiveness on Desktop (1366x768) and Tablet (768x1024) resolutions using built-in execution settings.
* **Data-Driven Registration (TC_K03)**: Validated the registration form using Data Files (Excel) to test 10 sets of data for missing fields and bad formats.
* **Smoke Tests (TC_K04 - TC_K08)**: Ensured primary page loads and critical button visibility for all main sections.
* **Advanced Scripting (TC_K25)**: Implemented a manual Relative XPATH (`//table/thead/tr/th[1]`) to demonstrate dynamic locator management beyond standard capture.

### Setup & Execution:
1. Install Katalon Studio.
2. Open the `katalon_tests/` project folder.
3. Locate `Test Suites/NextGenGadgets_Full_Regression`.
4. Run the suite using the Chrome environment.

---

## 🐍 Selenium Automation Framework
A robust framework built with Python following the Page Object Model (POM) for high maintainability.

### Features:
* **E2E Checkout Workflow**: Automated the full path from login to final payment confirmation.
* **Dynamic Wait Handling**: Used WebDriverWait (Explicit Waits) to handle table loading and filtering.
* **Excel Reporting**: Automatically exports a summary including Test ID, Steps, and Pass/Fail status to an Excel file upon completion.

---

## 📊 Comparison: Selenium vs. Katalon
As required by the project documentation, here is a comparison of the two tools:

| Feature | Selenium (Python) | Katalon Studio |
| :--- | :--- | :--- |
| **Setup & Complexity** | Higher; requires manual POM and utility configuration. | Lower; uses built-in keywords and a GUI-based object repository. |
| **Data-Driven Testing** | Requires custom scripts (Pandas/Openpyxl) to map Excel data. | Native "Data Files" feature allows for easy binding without coding. |
| **Maintenance** | Manual updates to Page Classes are needed when UI changes. | Centralized Object Repository allows for global updates to selectors. |
| **Reporting** | Requires third-party plugins or custom code for Excel output. | Provides professional, built-in visual and log-based reports. |

**Concluding Remarks**: Katalon Studio was significantly more efficient for UI-heavy tasks and rapid smoke testing, while Selenium offered superior flexibility for complex logic and custom framework design.

---

## 🚀 How to Run Locally
1. **Clone the Repo**: `git clone https://github.com/prudhviteja793/NextGenGadgets.git`
2. **Launch Website**: Open `website/index.html` in any browser.
3. **Start the Server**: Open a Command Prompt, navigate to `C:\Users\matrix011K\Desktop\NextGenGadgets\website` and run the following command to start a local server: `python -m http.server 8000`
4. **Run the Selenium Testcase**: Open a new Command Prompt, navigate to `C:\Users\matrix011K\Desktop\NextGenGadgets` and execute all test cases using: `python -m pytest selenium_tests/`
