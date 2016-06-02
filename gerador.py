#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
import string
import time
import getopt, sys

SIZE = 8

def analyze(p):
   if len(p) == SIZE:
      chars = []
      chars.extend([i for i in string.ascii_lowercase])
      chars.extend([i for i in string.digits])

      sum = 0
      sumquad = 0
      x = 0
      while x < SIZE:
         sum += ord(p[x]) * (x+1)
         sumquad += ord(p[x]) ** x
         x += 1

      if sum == 2557 and sumquad == 913407662208:
         print "senha candidata encontrada, se ler o texto a seguir achou a senha oficial também"
         mat = [18, 19, 65, 21, 14, 82, 87, 19, 4, 5, 21, 2, 65, 93, 87, 93, 5, 25, 65, 6, 18, 69, 87, 19, 21, 19, 25, 23, 14, 29, 18, 86, 9, 86, 17, 12, 19, 64, 71, 86, 65, 2, 20, 67, 4, 89, 18, 85, 79, 88, 0, 79, 65, 65, 83, 65, 0, 20, 4, 13, 18, 17, 68, 92, 2, 19, 65, 7, 4, 82, 93, 87, 8, 16, 8, 0, 14, 68, 18, 82, 65, 5, 4, 13, 9, 80]
         text = ""
         for i in range(0, len(mat)):
            text += chr(mat[i] ^ ord(p[i%len(p)]))

         print text
         sys.exit(0)
      else:
         sys.exit(1)

   else:
      sys.exit(-1)


def main():
   try:
      opts, args = getopt.getopt(sys.argv[1:], "p:h", ["password", "help"])

   except getopt.GetoptError as err:
      print str(err)
      print str('Use '+sys.argv[0]+' -p senha ou ' +sys.argv[0]+' -h')
      sys.exit(-1)

   for o, a in opts:
      if o in ("-p", "--password"):
         if len(sys.argv) == 3:
            analyze(sys.argv[2])
      elif o in ("-h", "--help"):
         print "Use "+sys.argv[0]+" -p senha"
         sys.exit(1)
      else:
         assert False, "Opção Inválida!"
         sys.exit(-1)

if __name__ == '__main__' :
   main()
