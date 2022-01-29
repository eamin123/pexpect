import pexpect


COMMAND_PROMPT = '[#$] '
#child = pexpect.spawn('ls -la')


child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('ls -ltrh')
child.expect(r'\$')
myoutput = child.before
print(myoutput.decode('ASCII'))

child.sendline ('iostat')
child.expect (COMMAND_PROMPT)
myoutput2 = child.before
print(myoutput2.decode('ASCII'))

# Run vmstat.
child.sendline ('netstat -arn')
child.expect (COMMAND_PROMPT)
myoutput3 = child.before
print(myoutput3.decode('ASCII'))



