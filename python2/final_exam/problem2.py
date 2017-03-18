import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

pylab.figure('alle')
pylab.title('vsjo')
pylab.plot(xVals,'r')

pylab.plot(yVals,'g')
pylab.plot(zVals,'b')
pylab.plot(wVals,'k')
pylab.plot(tVals,'m')
pylab.figure('x')
pylab.title('xVals')
pylab.plot(xVals,'r')
pylab.figure('y')
pylab.title('yVals')
pylab.plot(yVals,'g')
pylab.figure('z')
pylab.title('zVals')
pylab.plot(zVals,'b')
pylab.figure('w')
pylab.title('wVals')

pylab.plot(wVals,'k')
pylab.figure('t')
pylab.title('tVals')

pylab.plot(tVals,'m')

pylab.figure('2-3')
pylab.title('2-3')
pylab.plot(xVals, zVals,'r')
pylab.figure('2-4')
pylab.title('2-4')
pylab.plot(xVals, yVals,'g')
pylab.figure('2-5')
pylab.title('2-5')
pylab.plot(xVals, sorted(yVals),'b')
pylab.figure('2-6')
pylab.title('2-6')
pylab.plot(sorted(xVals), yVals,'k')
pylab.figure('2-7')
pylab.title('2-7')
pylab.plot(sorted(xVals), sorted(yVals),'m')
pylab.show()

