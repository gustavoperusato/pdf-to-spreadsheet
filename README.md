<h2> PFD File to Google Spreadsheets </h2>
<h3>Read tables in your <b>PDF files</b> and send it to a <b>Google Spreadsheet</b></h3>

This repository have the goal of help you to colect data from tables in PDF files and store it on a Google Spreadsheet

<h3>Prerequisites:</h3>
<li>Python 2.6 or greater;</li>
<li>A Google Cloud Platform project with the API enabled. To create a project and enable an API, go to https://developers.google.com/workspace/guides/create-project </li>

<h3>Instructions</h3>
<li>Step 1: Install the Google client library, running the command:</li>

<code>  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib </code>

<li> Step 2: Instal the camelot library running this command:

<code> pip install camelot </code>

<li>Step 3: Copy the files in this repository, modifying the "pdf_read_n_send.py" with your relative infos (follow the commented lines)</li>
<ol></ol>
<li>Step 4: Run "pdf_read_n_send.py"</li>
