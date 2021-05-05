*** Settings ***
Library  SeleniumLibrary  

*** Variables ***
${LOGIN_LINK}  //a[text()='login']
${EMAIL_INPUT}  //*[@id="root"]/div/div/input[1]
${PASSWORD_INPUT}  //*[@id="root"]/div/div/input[2]
${SUBMIT_BUTTON}  //*[@id="root"]/div/div/button
${RESET_PASSWORD_BUTTON}  //*[@id="root"]/div/div/a
${LOGO}  //h1[text()='The chess club']
${LOGOUT_BUTTON}  //*[@id="root"]/div/div/div[1]/div[2]/button
${MENU}  //h2[text()='MENU']

*** Keywords ***
Test login Function
    [Arguments]  ${email}  ${password}  
    Click Link  ${LOGIN_LINK}

    Wait Until Page Contains Element  ${EMAIL_INPUT}  2s
    Input Text  ${EMAIL_INPUT}  ${email}
    Input Password  ${PASSWORD_INPUT}  ${password}
    Click Button  ${SUBMIT_BUTTON}  

    Wait Until Page Contains  ${LOGO}  10s
    Click Button  ${LOGOUT_BUTTON}
    Wait Until Page Contains  ${MENU}  10s
    


