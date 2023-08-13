#solution une & plus simple
def factorielle(n) :
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
print(factorielle(4))    


#solution deux & plus longue 
def factorielle(n):
   if n == 0:
      return 1
   else:
      F = 1
      for k in range(2,n+1):
         F = F * k

      return F
print(factorielle(5))