originalPixels = [
    [10, 20, 30],
    [40, 50, 60]
]
class Image:
    def __init__(self, pixels):
        self.pixels = pixels
    
    def applyTransformation(self, transformationFunc):
        self.pixels = transformationFunc(self.pixels)
    
    def getCopy(self):
        copy = []
        for row in self.pixels:
            newRow = []
            for val in row:
                newRow.append(val)
            copy.append(newRow)
        return Image(copy)
def flipHorizontal(data):
    newdata = []
    for row in data:
        newrow = row[::-1]
        newdata.append(newrow)
    return newdata

def adjustBrightness(data, brightval):
    newdata = []
    for row in data:
        newrow = []
        for val in row:
            newval = val + brightval
            if newval < 0:
                newval = 0
            newrow.append(newval)
        newdata.append(newrow)
    return newdata

def rotateNinetyDegrees(data):
    rows = len(data)
    cols = len(data[0])
    newdata = []
    for j in range(cols):
        newrow = []
        for i in range(rows-1, -1, -1):
            newrow.append(data[i][j])
        newdata.append(newrow)
    return newdata
class AugmentationPipeline:
    def __init__(self):
        self.steps = []
    
    def addStep(self, func):
        self.steps.append(func)
    
    def processImage(self, img):
        results = []
        for step in self.steps:
            copy = img.getCopy()
            copy.applyTransformation(step)
            results.append(copy)
        return results
img = Image(originalPixels)

pipe = AugmentationPipeline()
pipe.addStep(flipHorizontal)
pipe.addStep(lambda data: adjustBrightness(data, 10))
pipe.addStep(rotateNinetyDegrees)

results = pipe.processImage(img)

print("final output:")
for i, result in enumerate(results):
    print(f"Image {i+1}:")
    for row in result.pixels:
        print(row)