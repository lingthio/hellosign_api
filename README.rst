Synopsis
========

This code example illustrates the use of the HelloSign API
by implementing a simple Flask web application that:

- prepares a Signature Request from a Template,
- shows that Document in an IFrame, and
- prompts the user to sign that Document.

| HelloSign API documetation:
| https://www.hellosign.com/api/reference

| HelloSign SDK for Python
| https://github.com/HelloFax/hellosign-python-sdk


Motivation
==========

Before integrating the HelloSign API into our web application,
I wrote a stand-alone prototype to determine its speed and features.

I'm offering this Example web application in case other developers
find it useful.

Though this code example is in Python (using the Flask application framework),
it illustrates the API for developers using other programming languages.


Code organization
=================
* ``example_app/`` contains a simple Flask application that calls the HelloSign SDK.
* ``runserver.py`` starts a development web server that serves the Flask application.


Installation
============
It is assumed that you have virtualenv and virtualenvwrapper installed and configured::

    # Clone this repository
    mkdir ~/dev
    git clone git@github.com:lingthio/hellosign_api.git hellosign_api

    # Create a virtualenv
    mkvirtualenv hellosign_api -p /full/path/to/python

    # Install required python packages (Flask and requests)
    cd ~/dev/hellosign_api
    pip install -r requirements.txt


Configuring HelloSign API Application
======================================
Add a HelloSign API Application:

- Create an account at hellosign.com and log in
- Click on: ``Integrations > API``
- Behind ``API KEY``, click on ``REVEAL KEY``. Make note of this API Key.
- Behind ``API APPS``, click on ``CREATE``

    - Give it a name and a domain name (anything will do)
    - OAuth does NOT need to be enabled

- Once created, the ``Client ID`` is shown. Make note of this Client ID.

Add a HelloSign Template:

- Click on ``Templates > Create Template``
- Upload a document. You can use ``example_app/ExampleAgreement.docx``.
- ``What roles need to be signed``: ``Customer``
- Click on ``PREPARE DOCS FOR SIGNING``

    - Drag-and-drop a Textbox. Double Click.
        - Who fills this out: Me (when sending)
        - Field Label: FIELD1
        - API ID: FIELD1
        - (The above is required to pre-fill this field through the API)
    - Drag-and-drop a Signature.
    - Drag-and-drop a Sign Date.
    - Click Continue (top right)

- Add Title
- Click on ``SAVE TEMPLATE``. Make note of this Template ID


Configure the Example App
=========================
Copy the example settings to a local file::

    cd ~/dev/hellosign_api/example_app
    cp local_settings_example.py local_settings.py

Edit ``local_settings.py`` to reflect your HelloSign settings:

- ``HELLOSIGN_API_KEY`` must reflect the API Key created in the previous section.
- ``HELLOSIGN_CLIENT_ID`` must reflect the Client ID created in the previous section.
- ``HELLOSIGN_TEMPLATE_ID`` must reflect the Template ID created in the previous section.
- ``RECIPIENT_NAME``: use your name.
- ``RECIPIENT_EMAIL``: use your email address.


Starting the web application
============================
::

    workon hellosign_api
    cd ~/dev/hellosign_api
    python runserver.py

You can now point your browser to: http://localhost:5000/


Prepare and Sign a Document
===========================
Click on 'Prepare and Sign Document'. This will perform this sequence::

    signature_request = hs_client.send_signature_request_embedded_with_template()
    signature = signature_request.signatures[0]
    embedded_obj = hs_client.get_embedded_object(signature.signature_id)
    sign_url = embedded_obj.sign_url

In the HTML page, javascript is used to add an IFrame to the page::


See also
========
adobe_sign_api: https://github.com/lingthio/adobe_sign_api


Contributors
============
Ling Thio - ling.thio AT gmail.com

Did you find this useful? Consider tipping me or sending me a thank you email!
