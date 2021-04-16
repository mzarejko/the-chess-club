*** Settings ***
Documentation  The Chess Club Tests
Library  SeleniumLibrary  


Suite Setup  Start Webserver
Suite Teardown  Stop Webserver


*** Variables ***
${DJANGO URL}  http://0.0.0.0:8000/admin/
${BROWSER}  chrome
${DJANGO LOG}  link:Django administration

*** Test Case ***

Check if clinetion work
    [Documentation]  this test verfies connection to django
    [Tags]  Non-functional
    Check if django connection work

*** Keywords ***

Start Webserver
    Open Browser  ${DJANGO URL}  ${BROWSER}

Stop Webserver
    Close Browser

Check if django connection work
    Wait Until Element Is Visible  ${DJANGO LOG} 10
