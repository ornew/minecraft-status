#!/usr/bin/env python

# This script from follow answer by Nope.
# https://gaming.stackexchange.com/questions/166463/query-number-of-players-on-a-minecraft-server

import sys,json,struct,socket

def popint(s):
  acc = 0
  b = ord(s.recv(1))
  while b & 0x80:
    acc = (acc<<7)+(b&0x7f)
    b = ord(s.recv(1))
  return (acc<<7)+(b&0x7f)

def pack_varint(d):
  return bytes([(0x40*(i!=d.bit_length()//7))+((d>>(7*(i)))%128) for i in range(1+d.bit_length()//7)])

def pack_data(d):
  return pack_varint(len(d)) + d

def get_info(host,port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, port))
  s.send(pack_data(bytes(2)+pack_data(bytes(host,'utf8'))+struct.pack('>H',port)+bytes([1]))+bytes([1,0]))
  popint(s)   # Packet length
  popint(s)   # Packet ID
  l,d = popint(s),bytes()
  while len(d) < l: d += s.recv(1024)
  s.close()
  return json.loads(d.decode('utf8'))

if __name__ == '__main__':
  h = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
  p = int(sys.argv[2]) if len(sys.argv) > 2 else 25565
  print(get_info(h,p))
