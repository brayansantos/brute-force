#!/usr/bin/python
#-*- coding: utf-8 -*-
import string
import time
import getopt, sys
import random
import subprocess
import os
import socket

def gerar_senha(tamanho=8):
   caracters = '0123456789abcdefghijlmnopqrstuwvxz'
   senha = ''
   for char in xrange(tamanho):
      senha += random.choice(caracters)

   return senha

def envia_senha(senha):
  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("10.3.4.33". 8090))

  s.send(senha)
  s.close()

def main():
  achou = False

  while achou == False:
    senha = gerar_senha()
    return_code = subprocess.call('./gerador.py -p ' + senha, shell=True)

    if return_code == 0:
      achou = True
      print "A senha e':", senha
      envia_senha(senha)
    else:
      print senha, "nao e' uma senha valida."

if __name__ == '__main__' :
  main()
