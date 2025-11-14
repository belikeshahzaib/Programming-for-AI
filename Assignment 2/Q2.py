import json, numpy as np 
csvData = []
with open("sensor_data.csv", 'r') as CSVData:
    row = []
    for line in CSVData:
        val = line.strip().split(',')
        csvData.append(val)
print(csvData)
npArray = np.array(csvData)
print("Sample of original data:")
print(npArray[:1][:2])
npArrayFloat = npArray.astype(float)

npArrayFloat[npArrayFloat == -999] = np.nan
npArrayFloat[npArrayFloat < 0] = np.nan
npArrayFloat[npArrayFloat > 100] = np.nan
np.set_printoptions(precision=2)

colMean = np.nanmean(npArrayFloat, axis=0)
print(f"Average Mositure of Each Sensor: {colMean[:2]}")
rowMean = np.nanmean(npArrayFloat, axis=1)
print(f"Average Mositure for Each Hour: {rowMean[:2]}")

invalidReading = np.sum(np.isnan(npArrayFloat), axis =0)
worstSensor = np.argmax(invalidReading)

print(f"Worst col reading: {worstSensor}")
minData = np.nanmin(npArrayFloat)
maxData = np.nanmax(npArrayFloat)

normalize = (npArrayFloat - minData) / (maxData - minData)

np.savetxt('sensorDataNormalized.csv', normalize, fmt= '%.3f')
print("File saved")