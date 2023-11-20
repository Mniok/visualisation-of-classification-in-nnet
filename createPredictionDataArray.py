def createPredictionDataArray(startX, endX, startY=None, endY=None, width=1000, height=None):
    # if startX==endX or startY==endY or maybe width==0 or height==0 -> division by 0
    if startY is None: startY = startX
    if endY is None: endY = endX
    if height is None: height = width
    print('createPredictionDataArray', startX, endX, startY, endY, width, height)
    if(startX > endX):
        [startX, endX] = [endX, startX]
    if(startY > endY):
        [startY, endY] = [endY, startY]
    print('post enforce start<=end : ', startX, endX, startY, endY, width, height)
    stepWidthwise = (endX-startX)/width
    stepHeightwise = (endY-startY)/height
    print('steps:', stepWidthwise, stepHeightwise)
    xRange = range(int(startX/stepWidthwise), int(endX/stepWidthwise + 1))
    yRange = range(int(startY/stepHeightwise), int(endY/stepHeightwise + 1))
    print('ranges:', xRange, yRange)
    return [[i*stepWidthwise, j*stepHeightwise] for i in xRange for j in yRange]
