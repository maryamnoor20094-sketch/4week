
# W04-D04 Report
## Frontend, Backend and Database Integration

### 1. Objective
The objective was to connect an HTML contact form to a Flask backend and SQLite database.

### 2. Technologies Used
- HTML
- CSS
- JavaScript
- Python
- Flask
- SQLite

### 3. Implementation
- Created a contact form using HTML.
- Styled the form using CSS.
- Used JavaScript Fetch API to send form data.
- Created a Flask POST endpoint at `/api/contact`.
- Validated the submitted name and message.
- Stored submitted messages in SQLite using the existing add_message() function.

### 4. Testing Results
- Contact form opened successfully in Firefox.
- Name and message fields worked correctly.
- JavaScript successfully sent a POST request.
- Flask received and processed the request.
- SQLite successfully stored submitted messages.
- Database verification confirmed saved records.

### 5. Database Verification
The following records were retrieved successfully:

- Record ID 4: hhhh
- Record ID 5: Maryam

### 6. Conclusion
The frontend contact form was successfully connected to the Flask backend and SQLite database. Submitted messages were stored permanently, and database retrieval confirmed successful integration.
