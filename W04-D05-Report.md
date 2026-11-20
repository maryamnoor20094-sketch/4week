# W04-D05 — Input Validation and Automated Testing

## Objective
Implement input validation, safely handle invalid API requests, and test the Flask application using Python unittest.

## Work Completed

1. Added backend validation to the contact API.
2. Rejected empty and whitespace-only names and messages.
3. Added a maximum name length of 50 characters.
4. Added a maximum message length of 500 characters.
5. Added handling for invalid JSON requests.
6. Used appropriate HTTP response codes:
   - 201 for successful submissions.
   - 400 for invalid requests.
   - 500 for unexpected server errors.
7. Updated frontend JavaScript validation.
8. Configured database functions to support a temporary test database.
9. Created automated tests in test_app.py.

## Automated Testing

Command used:

python -m unittest -v test_app.py

Result:

- Total tests: 9
- Passed: 9
- Failed: 0
- Status: OK

Test cases covered:

- Homepage response.
- Valid contact submission.
- Empty name.
- Empty message.
- Whitespace-only name.
- Whitespace-only message.
- Name exceeding 50 characters.
- Message exceeding 500 characters.
- Invalid JSON request.

## Manual Browser Testing

- Flask application started successfully using the existing server.
- Website opened in Firefox at http://127.0.0.1:5000/.
- Contact form accepted a sample submission.
- Success message appeared.

## Database Safety

Automated API tests use a temporary database so test submissions do not modify the main training database.

## Files Updated or Created

- app.py
- database.py
- static/script.js
- test_app.py
- W04-D05-Report.md

## Conclusion

The W04-D05 input validation and automated testing tasks were implemented. All nine automated API tests passed successfully.
