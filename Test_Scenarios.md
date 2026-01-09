# Test Scenarios – Login Page

## Application Under Test
https://the-internet.herokuapp.com/login

## Total Test Scenarios
20

## Scenario Categories
- Positive scenarios
- Negative scenarios
- Boundary scenarios
- UI validation scenarios

## Sample Test Scenarios

### TS_01 – Valid Login
**Steps**
1. Open login page
2. Enter valid username and password
3. Click Login

**Expected Result**
User should login successfully

---

### TS_02 – Invalid Username
**Steps**
1. Enter invalid username
2. Enter valid password
3. Click Login

**Expected Result**
Error message should be displayed

---

### TS_03 – Empty Fields
**Steps**
1. Leave username and password empty
2. Click Login

**Expected Result**
Error message should be displayed

---

## Detailed Test Cases
📄 Full detailed test cases are available in:
**test_scenarios.xlsx**
