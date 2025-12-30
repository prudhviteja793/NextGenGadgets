# NextGenGadgets
NextGenGadgets QA Project: Custom E-Commerce Site | Selenium Python (POM) | Katalon Studio Automation | Data-Driven Testing | Cross-Browser Compatibility | Automated Excel Reporting.

## Project Overview
NextGenGadgets is a fully functional front-end e-commerce platform developed as the "System Under Test" (SUT) for the Software Testing Tools course. This project demonstrates a complete Software Testing Life Cycle (STLC), featuring a custom-developed web application and a robust automation framework to validate complex UI/UX and functional requirements.

**Developer:** Prudhvi Teja Reddy Kandula (ID: 5805128)

---

## 🛠️ Project Structure
The repository is organized to showcase a clear separation between the application code and the automation frameworks:

* **`website/`**: Source code for the SUT (HTML, CSS, JS, and Assets).
* **`selenium_tests/`**: Python-based automation scripts using the Page Object Model (POM).
* **`katalon_tests/`**: Katalon Studio test suites for cross-tool validation.
* **`results/`**: Automation execution reports, evidence, and comparison logs.

---

## 🌐 Website Features & Setup
The platform includes modern web features designed to test advanced automation capabilities:
* **Interactive UI**: Drag-and-drop shopping cart and dynamic product filtering.
* **Functional Workflows**: Multi-step checkout, Search functionality, and Order History sorting.
* **Security & Validation**: Regex-based form validation and UI/UX responsiveness.

**To run the website locally:**
1. Clone the repository: `git clone https://github.com/prudhviteja793/NextGenGadgets.git`
2. Navigate to the `website/` directory.
3. Open `index.html` (or `login.html`) in any modern browser.

---

## 🧪 Selenium Automation Framework
A robust framework built with **Python** following the **Page Object Model (POM)** for maintainability.

### Testing Scope:
* **Data-Driven Testing**: 30 unique test cases for authentication validation.
* **E2E Checkout Workflow**: Testing sequential dependencies from cart to payment.
* **Advanced Interactions**: Handling Iframes (Payment Widget), Dynamic Waits, and Modals.

### Installation & Execution:
1. **Install Dependencies**:
   ```bash
   pip install selenium pytest pandas xlsxwriter
