*** Settings ***
Library  SeleniumLibrary  

*** Variables ***
${REGISTER_LINK}  //a[text()='register']
${USERNAME_INPUT}  //*[@id="root"]/div/div/input[1]
${EMAIL_INPUT}  //*[@id="root"]/div/div/input[2]
${PASSWORD1_INPUT}  //*[@id="root"]/div/div/input[3]
${PASSWORD2_INPUT}  //*[@id="root"]/div/div/input[4]
${REGISTER_BUTTON}  //*[@id="root"]/div/div/button

*** Keywords ***
Test Register Function
    [Arguments]  ${username}  ${email}  ${password1}  ${password2}  ${info_blob}
    Click Link  ${REGISTER_LINK}

    Wait Until Page Contains Element  ${EMAIL_INPUT}  2s
    Input Text  ${EMAIL_INPUT}  ${email}
    Input Password  ${PASSWORD1_INPUT}  ${password1}
    Input Password  ${PASSWORD2_INPUT}  ${password2}
    Click Button  ${REGISTER_BUTTON}  

    Wait Until Page Contains Element  ${info_blob}  10s

    



