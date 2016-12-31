import json
from flask import Flask, request, current_app, render_template, redirect, url_for
from hellosign_sdk import HSClient

# Create a web application with Flask
app = Flask(__name__)

# Copy local_settings.py from local_settings_example.py
# Edit local_settings.py to reflect your CLIENT_ID and CLIENT_SECRET
app.config.from_pyfile('local_settings.py')    # Read example_app.local_settings.py

# Initialize the HelloSign API wrapper
hs_client = HSClient(api_key=app.config.get('HELLOSIGN_API_KEY'))


# Display the home page
@app.route('/')
def home_page():
    access_token = request.args.get('token')

    # Render the home page
    return render_template('home.html',
            access_token=access_token)


# Create and render an Adobe Sign Widget
@app.route('/show_iframe')
def show_iframe():

    # Create a Signature Request, using a Template, for Embedded us
    print('before send_signature_request_embedded_with_template()')
    signature_request = hs_client.send_signature_request_embedded_with_template(
        test_mode=True,
        client_id=app.config.get('HELLOSIGN_CLIENT_ID'),
        template_id=app.config.get('HELLOSIGN_TEMPLATE_ID'),
        subject='Example Agreement',
        message='Please sign this document',
        signers=[{
            'role_name': 'Customer',
            'email_address': app.config.get('RECIPIENT_EMAIL', 'yourname@example.com'),
            'name': app.config.get('RECIPIENT_NAME', 'Your Name'),
        }],
        custom_fields=[{ app.config.get('FIELD1_NAME'): app.config.get('FIELD1_VALUE') }]
    )
    print(type(signature_request), signature_request)

    # Retrieve first signer in signature request - we know it only has one signature
    signature = signature_request.signatures[0]

    # Retrieve the embedded URL for this signer
    embedded_obj = hs_client.get_embedded_object(signature.signature_id)
    sign_url = embedded_obj.sign_url

    # Render the IFrame
    return render_template('show_iframe.html',
                           client_id = app.config.get('HELLOSIGN_CLIENT_ID'),
                           sign_url=sign_url)



