

def haiku(N,k):
      x=0
      if N%k:
            x=N/k
      else:
            x=N/k-1
      s=(x*(x+1))/2
      return s*k


t=input()
while t:
    t-=1
    n=input()
    print haiku(n,3)+haiku(n,5)-haiku(n,15)

