*** Settings ***
Library         ServerSpecLibrary
Test Setup      Connect To Server   hostname=192.168.33.10      username=vagrant     password=vagrant
Test Teardown   Close Connection


*** Test Cases ***
VIM on Server
    Package  vim  Should Be Installed


PHP on Server
    Package  php5  Should Not Be Installed
