# Authentication information
HELLOSIGN_CLIENT_ID = 'ExampleApp'                     # Must match HelloSign's Application Name
HELLOSIGN_CLIENT_SECRET = "Must match HelloSign's generated API Key"
HELLOSIGN_USERNAME = 'yourname@example.com'            # Your HelloSign username
HELLOSIGN_PASSWORD = 'yourpassword'                    # Your HelloSign password
HELLOSIGN_SCOPE = HELLOSIGN_USERNAME                  # Authorization scope

# Document information
HELLOSIGN_LIBRARY_DOCUMENT_ID = 1234                   # Must match the ID of a HelloSign Library Document
HELLOSIGN_TEMPLATE_NAME = 'ExampleContractTemplate'    # Must match the name of a HelloSign Template

# Information about the Recipient that signs the document
RECIPIENT_USER_NAME = 'Your Name'
RECIPIENT_USER_EMAIL = 'yourname@example.com'
RECIPIENT_FIELD_NAME = 'SH_FF_TEXT_314'                 # Must match the field name in a HelloSign Template
RECIPIENT_FIELD_VALUE = 'Some text field value'
