def check(n):
  s=0
  for i in xrange(1,n/2+1):
    if n%i==0:
      s+=i
  return s>n
l=100
sieve=[True]*l
for i in xrange(12):
  sieve[i]=False

abundant=[]
for i in xrange(12,l):
  if check(i):
    abundant.append(i)

for i in xrange(len(abundant)-1):
  for j in xrange(i+1,len(abundant)):
    if abundant[i]+abundant[j]<l:
      if sieve[abundant[i]+abundant[j]]==True:
        sieve[abundant[i]+abundant[j]]=False
        print abundant[i]+abundant[j]

print sum([i for i in xrange(len(sieve)) if sieve[i]])
