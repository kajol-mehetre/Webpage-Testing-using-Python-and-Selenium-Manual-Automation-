
# ---- Manual Test Cases - Login Page ----

## Test Case 1 : Valid Login

- Test Case ID: TC_01
- Description: Login with valid username and password
- Preconditions: User is on login page
- Test Steps:
    1. Enter Valid Username
    2. Enter Valid Password
    3. Click Login

- Test Data:
    - Username : tomsmith
    - Password : SuperSecretPassword!
- Expected results: User should login Successfully
- Actual Result:
- Status:

## Test Case 2: Invalid Username
- Test Case ID: TC_02
- Description: Login with invalid username and valid password
- Preconditions: User is on login page
- Test Steps:
  1. Enter invalid username
  2. Enter valid password
  3. Click Login
- Test Data:
  - Username: wronguser
  - Password: SuperSecretPassword!
- Expected Result: Error message displayed
- Actual Result:
- Status:

## Test Case 3: Invalid Password
- Test Case ID: TC_03
- Description: Login with valid username and invalid password
- Preconditions: User is on login page
- Test Steps:
  1. Enter valid username
  2. Enter invalid password
  3. Click Login
- Test Data:
  - Username: tomsmith
  - Password: WrongPassword
- Expected Result: Error message displayed
- Actual Result:
- Status:

## Test Case 4: Empty Fields
- Test Case ID: TC_04
- Description: Login with both username and password empty
- Preconditions: User is on login page
- Test Steps:
  1. Leave username empty
  2. Leave password empty
  3. Click Login
- Test Data: None
- Expected Result: Error message displayed
- Actual Result:
- Status:

## Test Case 5: Error Message Verification
- Test Case ID: TC_05
- Description: Verify error message appears correctly after invalid login
- Preconditions: User is on login page
- Test Steps:
  1. Enter invalid credentials
  2. Click Login
- Test Data:
  - Username: wronguser
  - Password: WrongPassword
- Expected Result: "Your username is invalid!" message displayed
- Actual Result:
- Status:
