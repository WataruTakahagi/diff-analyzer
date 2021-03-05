import cv2
import numpy as np
import math
import scipy.linalg as linalg
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.patches as patches
import pathlib
import os

class diff:
    def __init__(self):
        self.filename = str()
        self.img = str()
        self.seq = []
        self.opt = list()

    def read(self,filename):
        self.filename = filename
        self.img = cv2.imread(self.filename, cv2.IMREAD_COLOR)

    def onMouse(self,event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            crop_img = self.img[[y], [x]]
            print('(x, y) = (%d, %d)' % (x,y))
            self.seq.append([x,y])

    def pointing(self):
        window_name = self.filename
        cv2.namedWindow(window_name)
        cv2.imshow(window_name, self.img)
        cv2.setMouseCallback(window_name, diff.onMouse)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def LSA(self):#Least squared approximation
        point = self.seq
        A = np.zeros((3,3))
        B = np.zeros((3,1))
        for i in range(len(point)):
            x = point[i][0]
            y = point[i][1]
            A[0,0] += math.pow(x,2)
            A[0,1] += x * y
            A[0,2] += x
            A[1,0] += x * y
            A[1,1] += math.pow(y,2)
            A[1,2] += y
            A[2,0] += x
            A[2,1] += y
            A[2,2] += 1
            p = math.pow(x,2) + math.pow(y,2)
            B[0] -= x * p
            B[1] -= y *p
            B[2] -= p
        LU = linalg.lu_factor(A)
        abg = linalg.lu_solve(LU, B)
        a_opt = - abg[0,0] / 2
        b_opt = - abg[1,0] / 2
        r_opt = math.sqrt(abs(math.pow(a_opt,2) + math.pow(b_opt,2) - abg[2,0]))
        self.opt = [a_opt,b_opt,r_opt]
        #print(a_opt,b_opt,r_opt)

    def plot(self):
        img = cv2.circle(self.img,(int(self.opt[0]),int(self.opt[1])),int(self.opt[2]),(255,0,0),thickness=1, lineType=cv2.LINE_8, shift=0)
        cv2.imwrite('LSA-'+self.filename, img)

    def line_pointing(self):
        self.seq = []
        self.read('LSA-'+self.filename)
        window_name = self.filename
        cv2.namedWindow(window_name)
        cv2.imshow(window_name, self.img)
        cv2.setMouseCallback(window_name, diff.onMouse)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def line_plot(self,filename):
        self.read('LSA-'+filename)
        fig = plt.figure()
        ax = plt.subplot(111)
        plt.imshow(self.img)
        plt.scatter(self.opt[0],self.opt[1],color='red')
        for i in range(len(self.seq)):
            plt.plot([self.seq[i][0],self.opt[0]],[self.seq[i][1],self.opt[1]],color='blue')
            plt.scatter(self.seq[i][0],self.seq[i][1],color='blue')
            circle = patches.Circle([self.opt[0], self.opt[1]], radius=math.sqrt((self.seq[i][0]-self.opt[0])**2 + (self.seq[i][1]-self.opt[1])**2), fill=False)
            r = '%4d pixel' % float(math.sqrt((self.seq[i][0]-self.opt[0])**2 + (self.seq[i][1]-self.opt[1])**2))
            ax.text(self.seq[i][0], self.seq[i][1], r, size=10)
            ax.add_patch(circle)
        ax.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
        ax.tick_params(bottom=False,left=False,right=False,top=False)
        ax.set_frame_on(False)
        plt.savefig('Result-LSA-'+filename)
        plt.close()

    def summary(self):
        os.system('open '+'Result-'+self.filename)

    def center(self, filename):
        print(filename)
        self.read(filename)
        self.pointing()
        self.LSA()
        self.plot()
        self.line_pointing()
        self.line_plot(filename)
        self.summary()

diff = diff()
diff.center('carbon-1050mm1.tif')
