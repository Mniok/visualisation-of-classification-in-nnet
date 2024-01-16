def createPredictionDataArray(startX, endX, startY=None, endY=None, width=1000, height=None):
    if startY is None: startY = startX
    if endY is None: endY = endX
    if height is None: height = width
    if startX==endX or startY==endY or width==0 or height==0:
        raise Exception('Invalid parameters for prediction data') # would lead to division by 0

    if(startX > endX):
        [startX, endX] = [endX, startX]
    if(startY > endY):
        [startY, endY] = [endY, startY]

    stepWidthwise = (endX-startX)/width
    stepHeightwise = (endY-startY)/height

    xRange = range(int(startX/stepWidthwise), int(endX/stepWidthwise + 1))
    yRange = range(int(startY/stepHeightwise), int(endY/stepHeightwise + 1))
    return [[i*stepWidthwise, j*stepHeightwise] for i in xRange for j in yRange]
