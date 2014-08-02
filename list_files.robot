*** Settings ***
Library     ServerSpec2Library


*** Test Cases ***
List Files
    Connect To Server  hostname=192.168.33.10  username=vagrant  password=vagrant
    Command  ls  Should Return Exit Status  0
    Close Connection


Host Name
    Connect To Server  hostname=192.168.33.10  username=vagrant  password=vagrant
    Command  hostname  Should Return Stdout  vagrant
    Close Connection
