import random
import cv2
import math
class KmeansSegmentation:

    def segmentation_grey(self, image, k = 2):
        cluster = [0] * k
        oldcluster = [0] * k

        tempCLuster = [[0 for x in range(image.shape[1])] for y in range(image.shape[0])]

        for i in range(k):
            cluster[i] = random.randint(0,255) #choosing random intensity values as cluster centers

        flag = True

        while flag: #runs the loop till all the cluster centers converges 

            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    for c in range(len(cluster)):
                        oldcluster[c] = cluster[c]
                        distance = abs(cluster[c] - image[i][j])
                        if c == 0: #finding the shortest distance
                            minDist = distance
                            closest = c
                        else:
                            if minDist > distance:
                                minDist = distance
                                closest = c
                    tempCLuster[i][j] = closest
            '''for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    image[i][j] = cluster[tempCLuster[i][j]]'''

            for c in range(0, len(cluster)-1):
                sum = 0
                numPoints = 0
                for i in range(image.shape[0]):
                    for j in range(image.shape[1]):
                        if tempCLuster[i][j] == c:
                            sum = sum + image[i][j]
                            numPoints = numPoints + 1

                if numPoints != 0 and c < len(cluster)-1:
                    cluster[c] = round(sum / numPoints)
                else: #removing the cluster if no pixel belong to that
                    cluster.pop(c)
                    c = c + 1

            count = 0
            for c in range(len(cluster)):
                if cluster[c] == oldcluster[c]:
                    count = count + 1

            if count == len(cluster): #checking if the convergences matches or not
                flag = False

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i][j] = cluster[tempCLuster[i][j]]

        return image


    def segmentation_rgb(self, image, k=2):

        cluster = [[0 for x in range(3)] for y in range(k)]
        oldcluster = [[0 for x in range(3)] for y in range(k)]
        tempCluster = [[0 for x in range(image.shape[1])] for y in range(image.shape[0])]

        for i in range(k): #choosing random pixels as cluster centers
            cluster[i] = image[random.randint(0, image.shape[0]-1)][random.randint(0, image.shape[1]-1)]

        flag = True
        iter = 0
        while flag and iter < 10: #runs the loop till all the cluster centers converges

            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    for c in range(k):

                        oldcluster[c][0] = cluster[c][0]
                        oldcluster[c][1] = cluster[c][1]
                        oldcluster[c][2] = cluster[c][2]
                        distance = math.sqrt((image[i][j][0] - cluster[c][0]) ** 2 +
                                             (image[i][j][1] - cluster[c][1]) ** 2 +
                                             (image[i][j][2] - cluster[c][2]) ** 2)

                        if c == 0:  #finding the shortest distance
                            minDist = distance
                            closest = c
                        else:
                            if minDist > distance:
                                minDist = distance
                                closest = c

                    tempCluster[i][j] = closest

            for c in range(k):
                redSum = 0
                greenSum = 0
                blueSum = 0
                numOfPoints = 0
                for i in range(image.shape[0]):
                    for j in range(image.shape[1]):
                        if tempCluster[i][j] == c:
                            redSum = redSum + image[i][j][0]
                            greenSum = greenSum + image[i][j][1]
                            blueSum = blueSum + image[i][j][2]
                            numOfPoints = numOfPoints + 1

                if numOfPoints != 0:
                    cluster[c][0] = round(redSum / numOfPoints)
                    cluster[c][1] = round(greenSum / numOfPoints)
                    cluster[c][2] = round(blueSum / numOfPoints)

            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    image[i][j][0] = cluster[tempCluster[i][j]][0]
                    image[i][j][1] = cluster[tempCluster[i][j]][1]
                    image[i][j][2] = cluster[tempCluster[i][j]][2]

            count = 0
            for c in range(k):
                if cluster[c][0] == oldcluster[c][0] and cluster[c][1] == oldcluster[c][1] and cluster[c][2] == oldcluster[c][2]:
                    count = count + 1

            if count == k:  #checking if the convergences matches or not
                flag = False
            iter = iter + 1
            print(iter)
        '''for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i][j][0] = cluster[tempCluster[i][j]][0]
                image[i][j][1] = cluster[tempCluster[i][j]][1]
                image[i][j][2] = cluster[tempCluster[i][j]][2]'''

        return image
