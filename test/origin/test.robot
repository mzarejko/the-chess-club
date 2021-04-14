*** Settings ***
Documentation  The Chess Club Tests
Library  SeleniumLibrary  
Library  Process


Suite Setup  Start Webserver
Suite Teardown  Stop Webserver

*** Variables ***
${DJANGO URL}  http://127.0.0.1:8000/admin/
${BROWSER}  chrome
${DJANGO LOG}  link:Django administration

*** Test Case ***

Check if clinetion work
    [Documentation]  this test verfies connection to django
    [Tags]  Non-functional
    Check if django connection work

*** Keywords ***

Start Webserver
    ${django process} =  Start Process  python  ../../backend/manage.py  runserver  127.0.0.1:8000
    Set suite variable  ${django process}

Stop Webserver
    Terminate Process  ${django process}
    Close Browser

Check if django connection work
    Sleep  4s
    Open Browser  ${DJANGO URL}  ${BROWSER}
    Wait Until Element Is Visible  ${DJANGO LOG}
