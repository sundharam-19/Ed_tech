# GUVI Automation Testing Framework

## Project Title

Automation Testing of GUVI Web Application using Python Selenium

---

## Project Objective

The objective of this project is to automate the testing of the GUVI web application using Selenium with Python. The framework validates important UI functionalities such as:

- URL validation
- Page title verification
- Login functionality
- Sign-Up navigation
- Menu validation
- Dobby chatbot presence
- Logout functionality

The framework is designed using real-time automation testing standards and follows the Page Object Model (POM) architecture.

---

## Website Under Test

https://www.guvi.in

---

## Technologies Used

- Python 3.11
- Selenium WebDriver
- Pytest
- Allure Reports
- Pytest HTML Reports
- WebDriver Manager
- Chrome Browser

---

## Framework Features

- Page Object Model (POM)
- Cross-browser support
- Positive and negative test scenarios
- Reusable components
- Exception handling
- Screenshot capturing
- HTML reporting
- Allure reporting
- Scalable framework structure
- Easy maintenance

---

## Project Structure

```text
guvi-automation-framework/
│
├── screenshots/
├── reports/
├── allure-results/
├── allure-report/
│
├── base_page.py
├── home_page.py
├── login_page.py
├── driver_factory.py
├── conftest.py
├── test_guvi.py
├── requirements.txt
└── README.md
```

---

## Installation Steps

### Step 1: Clone Repository

```bash
git clone https://github.com/sundharam-19/Ed_tech.git

```

---

### Step 2: Navigate to Project

```bash
cd guvi-automation-framework
```

---

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

### Step 4: Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execute Test Cases

Run all test cases:

```bash
pytest -v
```

---

## Generate HTML Report

```bash
pytest --html=reports/report.html
```

Open:

```text
reports/report.html
```

---

## Generate Allure Report

### Generate Allure Results

```bash
pytest --alluredir=allure-results
```

---

### Generate Allure Report

```bash
allure generate allure-results -o allure-report --clean
```

---

### Open Allure Report

```bash
allure open allure-report
```

OR

```bash
allure serve allure-results
```

---

## Test Cases Covered

| Test Case ID | Scenario |
|---|---|
| TC_01 | Verify URL validity |
| TC_02 | Verify webpage title |
| TC_03 | Verify Login button |
| TC_04 | Verify Sign-Up button |
| TC_05 | Verify Sign-Up navigation |
| TC_06 | Verify valid login |
| TC_07 | Verify invalid login |
| TC_08 | Verify menu items |
| TC_09 | Verify Dobby chatbot |
| TC_10 | Verify logout functionality |

---

## Design Pattern Used

### Page Object Model (POM)

The framework follows the Page Object Model design pattern to improve:

- Code reusability
- Maintainability
- Readability
- Scalability

---

## Exception Handling

The framework includes exception handling to:

- Prevent abrupt test termination
- Capture screenshots on failure
- Improve debugging capability

---

## Reporting

### HTML Report

Pytest HTML reports provide detailed execution summary.

### Allure Report

Allure reports provide:

- Graphical dashboards
- Test timelines
- Failure screenshots
- Execution history

---

## Future Enhancements

- Jenkins CI/CD Integration
- Docker Integration
- Parallel Execution
- Data-Driven Testing
- Excel Reporting
- API Testing Integration

---

## Author

S Sundharam

---

## Conclusion

This project demonstrates a real-time Selenium automation framework using Python and Pytest. The framework successfully automates important GUVI web application functionalities and generates professional test execution reports using Allure and Pytest HTML Reporting.
