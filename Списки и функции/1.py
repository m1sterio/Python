n = int(input())
adress = []
for i in range(n):
  ip = input()
  adress.append(ip)

def sum(ip):
  step = 3
  ip = ip.split('.')
  sm = 0
  for i in ip:
    sm = sm + (int(i) * (256 ** step))
    step -= 1
  return sm

def local(array):
  flag = False
  for i in array:
    i.split()
    if ((ip[0] == "10") and (ip[1] == "0")) or ((ip[0] == "172") and (ip[1] == "16")) or ((ip[0] == "192") and (ip[1] == "168")):
      flag = True
      break
  return flag

def obrat(num):
  step = 3
  ip = ''
  for i in range (step, -1):
    ip += str((num // 256  ** step)) + '.'
    num -= (num // 256 ** step)
  return ip[:-1]


def sortirovka(ar):
  c = []
  for i in ar:
    c.append(sum(i))
  c.sort()
  for i in c:
    print(obrat(i))



if local(adress):
  print("The list contains the local IP!")
  exit(0)
else:
  sortirovka(adress)

