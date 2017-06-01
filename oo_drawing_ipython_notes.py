In [1]: import cs1graphics as cg

In [2]: paper = cg.Canvas()

In [3]: paper.setBackgroundColor('skyBlue')

In [4]: paper.setWidth(800)

In [5]: paper.setHeight(600)

In [6]: paper.setTitle('My World')

In [7]: dir(paper)




: sun = cg.Circle()

In [11]: paper.add(sun)

In [12]: sun.setFillColor('yellow')

In [13]: sun.setRadius(50)

In [14]: sun.moveTo(700, 100)

In [15]: sunCenter = cg.Point(700, 100)

In [16]: sun2 = cg.Circle(50, sunCenter)

In [17]: sun2.serFillColor('lightYellow')
