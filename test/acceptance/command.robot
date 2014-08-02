*** Settings ***
Library     ServerSpec2Library
Test Setup     Connect To Server  hostname=192.168.33.10  username=vagrant  password=vagrant
Test TearDown  Close Connection


*** Test Cases ***
Run Command And Expect Return Exit Status
    Command  ls  Should Return Exit Status  0


Run Command And Expect Return Stdout
    Command  hostname  Should Return Stdout  vagrant\n


Run Command And Expect Return Stder
    Command  ls foo  Should Return Stderr  ls: cannot access foo: No such file or directory\n
