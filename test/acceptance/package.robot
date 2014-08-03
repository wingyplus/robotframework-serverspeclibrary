*** Settings ***
Library         ServerSpec2Library
Test Setup      Connect To Server   hostname=192.168.33.10      username=vagrant     password=vagrant
Test Teardown   Close Connection


*** Test Cases ***
VIM on Server
    Package  vim  Should Be Installed
