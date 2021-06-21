import cv2
import numpy as np
import colour
from PIL import Image
import glob
import os
class sorcerer(object):

    @classmethod
    def chromatic(self,img,outputname,circle=True,method="CMCCAT2000",gif=False,duration=10000):
        global chromatic
        img = cv2.imread(img)
        hsize, wsize, _ = img.shape
        centery = int(hsize / 2)
        centerx = int(wsize / 2)

        XYZ = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
        gry = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        XYZ_w = np.array([110, 75, 35])
        XYZ_wr = np.array([200, 120, 75])
        L_A = 2000


        if method=="CMCCAT2000":
            test = colour.chromatic_adaptation(XYZ, XYZ_w, XYZ_wr, method="CMCCAT2000", L_A1=L_A, L_A2=L_A)
        elif method=="Von Kries":
            test = colour.chromatic_adaptation(XYZ, XYZ_w, XYZ_wr, method="Von Kries")
        if circle==True:
            cv2.circle(test, (centerx, centery), 4, (0, 0, 255), -1)
        else:
            pass
        outputname = str(outputname)

        if gif==True:
            os.mkdir('chromatic')

            cv2.imwrite("chromatic/"f'{outputname}.png', test)
            cv2.imwrite("chromatic/"f'{outputname}gry.png',gry)
            frames = []
            imgs = glob.glob("chromatic/*.png")
            for i in imgs:
                new_frame = Image.open(i)
                frames.append(new_frame)

            frames[0].save('chromatic/mygif.gif', format='GIF',
                           append_images=frames[1:],
                           save_all=True,
                           duration=duration, loop=0)
        elif gif==False:
            cv2.imwrite(f'{outputname}.png', test)
            cv2.imwrite(f'{outputname}gry.png',gry)


    @classmethod
    def dotill(self,hsize,wsize,hlinefreq=12,wlinefreq=12,dotcolor=(0,255,0),dotradius=5,horizontalcolor=(14, 75, 3),verticalcolor=(14, 75, 3),horizontalthickness=4,verticalthickness=4,verticallines=True,horizontallines=True):
        global dotill
        img2 = np.ones((hsize, wsize, 3), dtype=np.uint8)
        lines = img2.copy()
        h, w, c = lines.shape
        alpha = hlinefreq
        beta = wlinefreq
        if alpha==0:
            print("lines of height can't be zero if you don't want to vertical lines use the parameter 'verticallines==False' ; 0 value has been set to 1")
            alpha=alpha+1
        if beta==0:
            print("lines of width can't be zero if you don't want to vertical lines use the parameter 'horizontallines==False' ; 0 value has been set to 1")
            beta=beta+1



        width = w / alpha
        height = h / beta
        if verticallines==True:
            for i in range(450):
                for j in range(600):
                    x, y = int(i * width), int(j * height)
                    z, t = int(i * width), int(j + height)
                    cv2.line(lines, (x, y), (z, t), verticalcolor, verticalthickness)
        elif verticallines==False:
            print("vertical lines have been removed")
            pass
        else:
            raise ValueError("neither True nor False expression has been given to the 'verticallines=' parameter")
        if horizontallines==True:
            for i in range(beta):
                for j in range(alpha):
                    x, y = int(j * width), int(i * height)
                    z, t = int((j + 1) * width), int(i * height)
                    cv2.line(lines, (x, y), (z, t), horizontalcolor, horizontalthickness)
        elif horizontallines==False:
            # print("horizontal lines have been removed")
            pass
        else:
            raise ValueError("neither True nor False expression has been given to the 'horizontallines=' parameter")

        for i in range(beta):
            for j in range(alpha):
                x, y = int(j * width), int(i * height)
                z, t = int((j + 1) * width), int(i * height)
                cv2.circle(lines, (x, y), dotradius, dotcolor, -1)

        XYZ_w = np.array([2, 12, 85])
        XYZ_wr = np.array([3, 4, 145])
        L_A = 300

        XYZ = cv2.cvtColor(lines, cv2.COLOR_RGB2XYZ)
        hsv = cv2.cvtColor(lines, cv2.COLOR_RGB2HSV)

        test = colour.chromatic_adaptation(XYZ, XYZ_w, XYZ_wr, method='CMCCAT2000', L_A1=L_A, L_A2=L_A)

        cv2.imwrite("BGRoutput.png", lines)
        cv2.imwrite("CMCCAT2000output.png", test)
        cv2.imwrite("hsvoutput.png", hsv)
        # print("all done")

    @classmethod
    def realtimegrid(self,realcolours=False):
        def empty(a):  # for our trackbar
            pass

        cap = cv2.VideoCapture(0)
        cv2.namedWindow('tracker')
        cv2.resizeWindow('tracker', 720, 640)  # resize
        cv2.createTrackbar('vertical', 'tracker', 1, 300,
                           empty)
        cv2.createTrackbar('horizontal', 'tracker', 1, 300, empty)
        cv2.createTrackbar('Hthickness', 'tracker', 1, 20, empty)
        cv2.createTrackbar('Wthickness', 'tracker', 1, 20, empty)

        if realcolours==False:
            cv2.createTrackbar('Vblue', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Vgreen', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Vred', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Hblue', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Hgreen', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Hred', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Hblue2', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Hgreen2', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Hred2', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Vblue2', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Vgreen2', 'tracker', 1, 255, empty)
            cv2.createTrackbar('Vred2', 'tracker', 1, 255, empty)
        while True:
            _, img = cap.read()
            bgr_img = cv2.cvtColor(img,
                                   cv2.COLOR_RGB2BGR)
            gry_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
            gry2bgr = cv2.cvtColor(gry_img, cv2.COLOR_GRAY2BGR)

            h, w, c = gry2bgr.shape

            vertical = cv2.getTrackbarPos('vertical', 'tracker')
            horizon = cv2.getTrackbarPos('horizontal', 'tracker')
            Wthickness = cv2.getTrackbarPos('Wthickness', 'tracker')
            Hthickness=cv2.getTrackbarPos('Hthickness', 'tracker')
            bluever=cv2.getTrackbarPos('Vblue', 'tracker')
            greenver = cv2.getTrackbarPos('Vgreen', 'tracker')
            redver= cv2.getTrackbarPos('Vred', 'tracker')
            Hblue=cv2.getTrackbarPos("Hblue",'tracker')
            Hgreen=cv2.getTrackbarPos('Hgreen', 'tracker')
            Hred=cv2.getTrackbarPos('Hred', 'tracker')
            Hblue2=cv2.getTrackbarPos("Hblue2",'tracker')
            Hgreen2=cv2.getTrackbarPos('Hgreen2', 'tracker')
            Hred2=cv2.getTrackbarPos('Hred2', 'tracker')

            width = w / (vertical + 0.0000001)
            height = h / (horizon + 0.0000001)
            if Hthickness == 0:
                Hthickness = Hthickness + 1
                # print("You can't select thickness as 0, thickness has been converted to 1")
            if Wthickness == 0:
                Wthickness = Wthickness + 1
                # print("You can't select thickness as 0, thickness has been converted to 1")
            for i in range(vertical):
                for j in range(horizon):
                    first_x, first_y = int(i * width), int(j * height)
                    last_x, last_y = int(i * width), int((j + 1) * height)
                    col_x = int(first_x + 0.4 * (last_x - first_x))
                    col_y = int(first_y + 0.4 * (last_y - first_y))
                    gridcolor = img[col_y, col_x,
                                :]
                    gridcolor = gridcolor.tolist()
                    color = gridcolor
                    if realcolours==False:
                        cv2.line(gry2bgr, (first_x, first_y), (last_x, last_y), (bluever,greenver,redver), Wthickness, 1)
                    elif realcolours==True:
                        cv2.line(gry2bgr, (first_x, first_y), (last_x, last_y), color, Wthickness, 1)
                    else:
                        raise ValueError(
                            "realcolours parameter need True or False statement")

            for i in range(horizon):
                for j in range(vertical):
                    first_x, first_y = int(j * width), int(i * height)
                    last_x, last_y = int((j + 1) * width), int(i * height)
                    # renkler
                    col_x = int(first_x + 0.4 * (last_x - first_x))
                    col_y = int(first_y + 0.4 * (last_y - first_y))
                    gridcolor = img[col_y, col_x, :]
                    gridcolor = gridcolor.tolist()
                    color = gridcolor
                    if realcolours==False:
                        cv2.line(gry2bgr, (first_x, first_y), (last_x, last_y), (Hblue,Hgreen,Hred), Hthickness, 1)

                    elif realcolours==True:
                        cv2.line(gry2bgr, (first_x, first_y), (last_x, last_y), color, Hthickness, 1)
                    else:
                        raise ValueError(
                            "realcolours parameter need True or False statement")
            if realcolours == False:
                for i in range(horizon):
                    for j in range(vertical):
                        first_x, first_y = int((j+3) * width), int((i+2) * height)
                        last_x, last_y = int((j + 1) * width), int(i * height)



                        cv2.line(gry2bgr, (first_x + 1, first_y + 1), (last_x + 1, last_y + 1),
                                     (Hblue2, Hgreen2, Hred2), Hthickness, 1)




            blur = cv2.GaussianBlur(gry2bgr, (7, 7),
                                    0)



            cv2.imshow("cam", gry2bgr)
            cv2.imshow("gausblur", blur)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()



    @classmethod
    def addlines(self,img,linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0)):

        rect = cv2.imread(img)

        h,w,c=rect.shape


        img2 = np.ones((h,w,c),dtype=np.uint8)
        if w > h or w==h:
            for i in range(0, w, 3):
                cv2.line(img2, (i, 0), (i, w), linecolour1, 3)
                cv2.line(img2, (i + 1, 0), (i + 1, (w)), linecolour2, 3)
                cv2.line(img2, (i + 2, 0), (i + 2, (w)), linecolour3, 3)
        else:
            for i in range(0, h, 3):
                cv2.line(img2, (0, i), (h, i), linecolour1, 3)
                cv2.line(img2, (0, i+1), (h, (i+1)), linecolour2, 3)
                cv2.line(img2, (0, i+2), (h, (i+2)), linecolour3, 3)


        result2 = cv2.addWeighted(rect, 0.1, img2, 77, 0)
        result3 = cv2.addWeighted(img2, 77, rect, 0.1, 77)


        blur = cv2.GaussianBlur(result2, (7, 7), 0)


        cv2.imwrite("MyGrids+GaussianBlur.png", blur)
        cv2.imwrite("MyGridsssss22.png", result3)
        cv2.imwrite("MyGridsssss2232.png", result2)

        # print("DONE! grids have been added to image")






    @classmethod
    def addlinesAlpha(self,img,linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0)):
        rect = cv2.imread(img)
        rect = cv2.cvtColor(rect, cv2.COLOR_BGR2BGRA)
        h, w, c = rect.shape
        img2 = rect.copy()

        for i in range(0, w, 3):
            cv2.line(img2, (i, 0), (i, w), linecolour1, 12)
            cv2.line(img2, (i + 1, 0), (i + 1, (w)), linecolour2, 12)
            cv2.line(img2, (i + 2, 0), (i + 2, (w)), linecolour3, 12)
        srcBGR=img2[...,:3] #re
        dstBGR=rect[...,:3]
        srcA=img2[...,3]/255.0
        dstA=rect[...,3]/255.0


        outA = srcA + dstA * (1 - srcA)
        outBGR = (srcBGR * srcA[..., np.newaxis] + dstBGR * dstA[..., np.newaxis] * (1 - srcA[..., np.newaxis])) / outA[
            ..., np.newaxis]
        outBGRA = np.dstack((outBGR, outA * 255)).astype(np.uint8)

        result2 = cv2.addWeighted(img2, 0.8, outBGRA, 0.3, 0)
        result3 = cv2.addWeighted(img2, 0.8, rect, 0.3, 0)

        blur = cv2.GaussianBlur(result2, (7, 7), 0)

        cv2.imwrite("MyGrids.png", result2)
        cv2.imwrite("MyGrids+GaussianBlur.png", blur)
        cv2.imwrite("MyGridsssss.png", outBGRA)
        cv2.imwrite("MyGridsssss22.png", result3)

        # print("DONE! grids have been added to image")
        # cv2.imshow("hsv",hsv)

    @classmethod
    def eyecolour(self,img):
        img = cv2.imread(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = cv2.equalizeHist(img)
        # print("select the iris (select smaller as much as possible for good results; then press to enter ")
        r = cv2.selectROI(img,fromCenter=False)

        roi_cropped = img[int((r[1])):int((r[1]) + int(r[3])), int((r[0])):int((r[0])) + int((r[2]))]

        center = int((r[0]+r[0]+r[2]) / 2), int((r[1]+r[1]+r[3]) / 2)
        # masking for seamless Clone
        redd = 255 * np.ones(roi_cropped.shape, roi_cropped.dtype)

        h, w = img.shape
        centh=int(h/2)
        centw=int(w/2)
        mask = np.ones((h, w, 3), dtype=np.uint8)


        j = 0
        for i in range(0, centw, 20):
            mask[0:h, i:i + 25][:, :, 2] = j + 45
            j = j + 5
            if j > 230:
                break

        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

        roi_cropped = cv2.cvtColor(roi_cropped, cv2.COLOR_GRAY2RGB)

        eclipse=cv2.ellipse(mask,center,(int(r[2]),int(r[3])),0,0,360,(0,0,0),-1)
        bit=cv2.bitwise_and(eclipse,mask)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
        mask[:, :, 2] = 200
        mask[:, :, 0] = 200

        mask = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)

        aplha = 0.8
        beta = 0.3
        M = 25
        result = cv2.addWeighted(img, aplha, bit, beta, M)

        output = cv2.seamlessClone(roi_cropped, result, redd, center, cv2.NORMAL_CLONE)
        blur = cv2.GaussianBlur(result, (5, 5), 0)
        blur2 = cv2.GaussianBlur(output, (5, 5), 0)



        result[int((r[1])):int((r[1]) + int(r[3])), int((r[0])):int((r[0])) + int((r[2]))] = roi_cropped

        cv2.imwrite("eyes.png", output)
        cv2.imwrite("eyes2.png", blur)

