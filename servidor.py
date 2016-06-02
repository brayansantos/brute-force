#!/usr/bin/python
#-*- coding: utf-8 -*-

import string
import time
import getopt, sys
import random
import subprocess
import socket
import threading

def gerar_senha(tamanho=8):
   caracters = '0123456789abcdefghijlmnopqrstuwvxz'
   senha = ''
   for char in xrange(tamanho):
      senha += random.choice(caracters)

   return senha

def testa_senha(senha):
  return_code = subprocess.call('./gerador.py -p ' + senha, shell=True)

  if return_code == 0:
    return True
  else:
    return False

class thread_processamento_remoto(threading.Thread):
  def __init__(self, threadID):
    threading.Thread.__init__(self)
    self.threadID = threadID
  def run(self):

    global achou, s
    s.bind(("", 8090))
    s.listen(5)

    while not achou:
      # Escuta os clientes, se um deles tiver retornado uma senha,
      # imprime a senha encontrada na tela e finaliza o programa
      conn, addr = s.accept()
      senha_remota = conn.recv(10)

      if testa_senha(senha_remota):
        print "A senha e':", senha 
        achou = True
        global thread_local
        thread_local.exit()

    s.close()

  def exit(self):
    global s
    conn.close()
    s.close()

class thread_processamento_local(threading.Thread):
  def __init__(self, threadID):
    threading.Thread.__init__(self)
    self.threadID = threadID
  def run(self):    

    global achou
    while not achou:
      #Gera a senha de forma aleatória e testa
      senha = gerar_senha()

      #if testa_senha(senha):
      if testa_senha('avaca123'):
        print "A senha e':", senha
        achou = True
        global thread_remota
        thread_remota.exit()
      else:
        print senha, "nao e' uma senha valida."
    
def main():
  global thread_local, thread_remota
  # Inicializando as Threads
  thread_local.start()
  thread_remota.start()

#Variável que controla a execução das threads
achou = False

#Socket de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Criando as Threads
thread_local = thread_processamento_local(1)
thread_remota = thread_processamento_remoto(2)

if __name__ == '__main__' :
  main()

