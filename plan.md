PLAN:

PROGRAM OUTLINE:

- on running the file, send to commandline:
"Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:"
with user interfacing via CLI.
- If wrong key entterd, print "invalid input. please specify..."

- for l: print number of secrets available.

- for e: 
    - prompt 'Secret Identifier:' - user enters eg. 'Missile_Launch_Codes'
    - prompt UserId: user enters bidenj
    - prompt Password: user entters Pa55word
        - print EITHER secret saved OR id/password error
        - add secret to secret list

- for r:
    - prompt 'Specify secret to retrieve:'
    - print error message OR Secrets stored in local file secrets.txt

- for d:
    - prompt 'Specify secret to delete:'
    - delete secret, print Deleted or error message

- for x: print 'thank you, goodbye', dissconnect from password manager

- In the shell: (printed from 'r' Missile_Launch_Codes)
    - cat secrets.txt
    - UserId: bidenj
    - Password: Pa55word


BEHIND THE SCENES:

- Connect to boto3 secrets manager (util funct?)
- 