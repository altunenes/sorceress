import cv2
import numpy as np
import colour
import glob
import os
import imageio
from matplotlib import pyplot as plt
import sys
from PIL import Image

class sorcerer(object):

    @classmethod
    def chromatic(self,img, outputname, circle=True, method="CMCCAT2000", gif=True, Gifduration=7):
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

        if method == "CMCCAT2000":
            test = colour.chromatic_adaptation(XYZ, XYZ_w, XYZ_wr, method="CMCCAT2000", L_A1=L_A, L_A2=L_A)
        elif method == "Von Kries":
            test = colour.chromatic_adaptation(XYZ, XYZ_w, XYZ_wr, method="Von Kries")
        else:
            sys.exit("no method selected")

        if circle == True:
            cv2.circle(test, (centerx, centery), 4, (0, 0, 255), -1)
        else:
            pass

        outputname = str(outputname)

        if gif == True:
            os.mkdir('chromatic')

            cv2.imwrite("chromatic/"f'{outputname}.png', test)
            cv2.imwrite("chromatic/"f'{outputname}gry.png', gry)
            frames = []
            imgs = glob.glob("chromatic/*.*")
            for i in imgs:
                new_frame = cv2.imread(i)
                frames.append(new_frame)

            with imageio.get_writer(f"chromatic/{outputname}.gif", mode="I", duration=Gifduration) as writer:
                for idx, frame in enumerate(frames):
                    print("Adding frame to GIF file: in chromatic folder ", idx + 1)
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    writer.append_data(rgb_frame)
                    print("Done")
                    print("Done ", f'{outputname}.png has been added your working dir.')
                    print("Your working directory: ", os.getcwd())

            os.mkdir('chromaticPIL')

            cv2.imwrite("chromaticPIL/"f'{outputname}.png', test)
            cv2.imwrite("chromaticPIL/"f'{outputname}gry.png', gry)
            frames2 = []
            imgs2 = glob.glob("chromaticPIL/*.png")
            for i in imgs2:
                new_frame2 = Image.open(i)
                frames2.append(new_frame2)

            frames2[0].save('chromaticPIL/mygifPIL.gif', format='GIF',
                            append_images=frames2[1:],
                            save_all=True,
                            duration=7000, loop=0)
        elif gif == False:
            cv2.imwrite(f'{outputname}.png', test)
            cv2.imwrite(f'{outputname}gry.png', gry)
            print("Done ", f'{outputname}.png has been added your working dir.')
            print("Your working directory: ", os.getcwd())

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
        print("3 images have been saved to your working directory: BGRoutput.png, CMCCAT2000output.png hsvoutput.png ")
        print("Your working directory: ", os.getcwd())

    @classmethod
    def realtimegrid(self,realcolours=True):
        def empty(a):  # for our trackbar
            pass
        cap = cv2.VideoCapture(0)
        cv2.namedWindow('tracker')
        if realcolours == False:
            cv2.resizeWindow('tracker', 720, 640)  # resize
        else:
            cv2.resizeWindow('tracker', 400, 200)
        cv2.createTrackbar('vertical', 'tracker', 1, 300,
                           empty)
        cv2.createTrackbar('horizontal', 'tracker', 1, 300, empty)
        cv2.createTrackbar('Hthickness', 'tracker', 1, 20, empty)
        cv2.createTrackbar('Wthickness', 'tracker', 1, 20, empty)

        if realcolours == False:
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
            Hthickness = cv2.getTrackbarPos('Hthickness', 'tracker')
            if realcolours == False:
                bluever = cv2.getTrackbarPos('Vblue', 'tracker')
                greenver = cv2.getTrackbarPos('Vgreen', 'tracker')
                redver = cv2.getTrackbarPos('Vred', 'tracker')
                Hblue = cv2.getTrackbarPos("Hblue", 'tracker')
                Hgreen = cv2.getTrackbarPos('Hgreen', 'tracker')
                Hred = cv2.getTrackbarPos('Hred', 'tracker')
                Hblue2 = cv2.getTrackbarPos("Hblue2", 'tracker')
                Hgreen2 = cv2.getTrackbarPos('Hgreen2', 'tracker')
                Hred2 = cv2.getTrackbarPos('Hred2', 'tracker')

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
                    if realcolours == False:
                        cv2.line(gry2bgr, (first_x, first_y), (last_x, last_y), (bluever, greenver, redver), Wthickness,
                                 1)
                    elif realcolours == True:
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
                    if realcolours == False:
                        cv2.line(gry2bgr, (first_x, first_y), (last_x, last_y), (Hblue, Hgreen, Hred), Hthickness, 1)

                    elif realcolours == True:
                        cv2.line(gry2bgr, (first_x, first_y), (last_x, last_y), color, Hthickness, 1)
                    else:
                        raise ValueError(
                            "realcolours parameter need True or False statement")
            if realcolours == False:
                for i in range(horizon):
                    for j in range(vertical):
                        first_x, first_y = int((j + 3) * width), int((i + 2) * height)
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
    def addlines(self,img,outputname,linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0)):

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

        cv2.imwrite(f'{outputname}blur.png', blur)
        cv2.imwrite(f'{outputname}ver1.png', result2)
        cv2.imwrite(f'{outputname}ver2.png', result3)

        print("DONE! grids have been added to your image check your working directory:")
        print("Your working directory: ", os.getcwd())






    @classmethod
    def addlinesAlpha(self,img,outputname,linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0)):
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



        cv2.imwrite(f'{outputname}ver1.png', result2)
        cv2.imwrite(f'{outputname}blur.png', blur)
        cv2.imwrite(f'{outputname}ver2.png', outBGRA)
        cv2.imwrite(f'{outputname}ver3.png', result3)


        print("DONE! images have been added to your working directory:")
        print("Your working directory: ", os.getcwd())


    @classmethod
    def eyecolour(self,img,outputname):
        img = cv2.imread(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = cv2.equalizeHist(img)
        print("select the iris (select smaller as much as possible for good results); then press to enter ")
        r = cv2.selectROI(img,fromCenter=False)

        roi_cropped = img[int((r[1])):int((r[1]) + int(r[3])), int((r[0])):int((r[0])) + int((r[2]))]

        center = int((r[0]+r[0]+r[2]) / 2), int((r[1]+r[1]+r[3]) / 2)
        # masking for seamless Clone
        redd = 255 * np.ones(roi_cropped.shape, roi_cropped.dtype)

        h, w = img.shape
        # centh=int(h/2)
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

        # mask = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)

        aplha = 0.8
        beta = 0.3
        M = 25
        result = cv2.addWeighted(img, aplha, bit, beta, M)

        output = cv2.seamlessClone(roi_cropped, result, redd, center, cv2.NORMAL_CLONE)
        blur = cv2.GaussianBlur(result, (5, 5), 0)
        # blur2 = cv2.GaussianBlur(output, (5, 5), 0)



        result[int((r[1])):int((r[1]) + int(r[3])), int((r[0])):int((r[0])) + int((r[2]))] = roi_cropped


        cv2.imwrite(f'{outputname}.png', output)
        cv2.imwrite(f'{outputname}blur.png', blur)


        print("DONE! images have been added to your working directory:")
        print("Your working directory: ", os.getcwd())

    @classmethod
    def dakinPex(self,outputname,dimension=800):


        img = 128 * np.ones((int(dimension), int(dimension), 3), dtype=np.uint8)
        h, w, _ = img.shape
        for i in range(0, h, 160):
            for j in range(0, w, 160):
                cv2.rectangle(img, (i, j), (i + 75, j + 75), (0, 0, 0), 5)
                cv2.rectangle(img, (i + 80, j + 80), (i + 155, j + 155), (0, 0, 0), 5)

        for i in range(0, h, 160):
            for j in range(0, w, 160):
                cv2.rectangle(img, (i + 80, j), (i + 155, j + 75), (255, 255, 255), 2)
                cv2.rectangle(img, (i, j + 80), (i + 75, j + 155), (255, 255, 255), 2)


        cv2.imwrite(f'{outputname}.png', img)


        print("DONE! images have been added to your working directory:")
        print("Your working directory: ", os.getcwd())

    @classmethod
    def bruno(self,outputname,circle=False, polycolor=(0, 255, 255), rectcolor=(255, 255, 0), circColor=(0, 0, 255)):
        img = 255 * np.ones((600, 600, 3), dtype=np.uint8)
        h, w, _ = img.shape

        pts = np.array([[60, 60], [120, 30], [180, 100], [120, 180], [60, 150]])  # most left to right
        pts2 = np.array([[400, 60], [460, 30], [520, 100], [460, 180], [400, 150]])  # most left to right

        pts3 = np.array([[60, 360], [120, 330], [180, 400], [120, 480], [60, 450]])  # most left to right
        pts4 = np.array([[400, 360], [460, 330], [520, 400], [460, 480], [400, 450]])  # most left to right

        color = (255, 0, 0)
        cv2.fillPoly(img, pts=[pts], color=polycolor)
        cv2.fillPoly(img, pts=[pts2], color=polycolor)
        cv2.fillPoly(img, pts=[pts3], color=polycolor)
        cv2.fillPoly(img, pts=[pts4], color=polycolor)

        if circle == True:

            cv2.circle(img, (480, 75), 30, circColor, -1)

            cv2.circle(img, (140, 375), 30, (255, 255, 255), -1)
            cv2.circle(img, (480, 375), 30, circColor, -1)
        else:

            cv2.rectangle(img, (470, 10), (540, 90), rectcolor, -1)  # top rights
            cv2.rectangle(img, (470, 310), (540, 390), rectcolor, -1)  # bot right
            cv2.rectangle(img, (130, 310), (200, 390), (255, 255, 255), -1)  # bot left

        cv2.putText(img, "is the shape on the left the same as the one on the right?", (40, 240),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, 55)

        cv2.line(img, (0, 250), (600, 250), (0, 0, 0), 5)

        cv2.imwrite(f'{outputname}.png', img)


        print("DONE! image has been added to your working directory:")
        print("Your working directory: ", os.getcwd())


    @classmethod
    def dolboeuf(self,outputname,circleColor=(0,0,255),kill=False):
        img = 255 * np.ones((800, 800, 3), dtype=np.uint8)
        for i in range(35, 37, 2):
            cv2.circle(img, (250, 300), 35, circleColor, -1)
            cv2.circle(img, (250, 300), i + 7, (0, 0, 0), 3)

        cv2.circle(img, (600, 300), 35, circleColor, -1)
        cv2.circle(img, (600, 300), 100, (0, 0, 0), 3)

        if kill == True:
            cv2.line(img, (250, 335), (600, 335), (0, 0, 0), 2)
            cv2.line(img, (250, 265), (600, 265), (0, 0, 0), 2)

        cv2.imwrite(f'{outputname}.png', img)


        print("DONE! image has been added to your working directory:")
        print("Your working directory: ", os.getcwd())



    @classmethod
    def kanizsa(self,outputname, dims=600, circleColor=(0, 0, 255), bgcolor=(255, 255, 255)):
        img = 255 * np.ones((dims, dims, 3), dtype=np.uint8)
        img[:, :, :] = bgcolor
        h, w, _ = img.shape
        a = int(h / 7)
        b = int(h / 3.86)
        radius = int(h / 11)
        for i in range(0, w, int(w / 4)):
            for j in range(0, w, int(w / 4)):
                cv2.circle(img, (i + a, j + a), radius, circleColor, -1)

        for i in range(0, w, int(w / 2)):
            for j in range(0, w, int(w / 2)):
                cv2.rectangle(img, (i + a, j + a), (i + a + b, j + a + b), bgcolor, -1)
        cv2.imwrite(f'{outputname}.png', img)
        cv2.imshow("img", img)
        cv2.waitKey(0)
        print("DONE! image has been added to your working directory:")
        print("Your working directory: ", os.getcwd())

    @classmethod
    def ponzol(self,outputname,kill=False,line1=(255,0,0),line2=(255,0,0),rectangle1=(0,0,255),rectangle2=(0,0,255)):
        img = 255 * np.ones((600, 600, 3), dtype=np.uint8)
        h, w, _ = img.shape

        cv2.line(img, (80, 400), (300, 20), line1, 4)
        cv2.line(img, (340, 20), (560, 400), line2, 4)

        cv2.rectangle(img, (250, 70), (390, 90), rectangle1, -1)
        cv2.rectangle(img, (250, 350), (390, 370), rectangle2, -1)
        #
        if kill == True:
            for i in range(70, (340), 30):
                cv2.rectangle(img, (250, i), (390, i + 20), (0, 0, 255), -1)
                cv2.line(img, (250, 70), (250, 370), (0, 0, 0), 4)
                cv2.line(img, (390, 70), (390, 370), (0, 0, 0), 4)

        cv2.imwrite(f'{outputname}.png', img)


        print("DONE! image has been added to your working directory:")
        print("Your working directory: ", os.getcwd())

    @classmethod
    def tAki2001(self,outputname, dimension=700, circlecolour=(0, 255, 255), circleradius=15, bglinecolor=(255, 128, 128),bgcolor=(255, 255, 255)):
        dimension = int(dimension)
        img = 255 * np.ones((dimension, dimension, 3), dtype=np.uint8)
        img[:, :, :] = bgcolor
        h, w, _ = img.shape
        for i in range(0, w - 50, 75):
            for j in range(0, h - 50, 25):
                cv2.line(img, (30, i), (h - 50, i), bglinecolor, 2)
                cv2.line(img, (i, 30), (i, h - 50), bglinecolor, 2)

        for i in range(75, h, 150):
            for j in range(75, h, 150):
                cv2.circle(img, (j, i), circleradius, circlecolour, -1)

        for i in range(145, h, 150):
            for j in range(145, h, 150):
                cv2.circle(img, (j, i), circleradius, circlecolour, -1)
        for i in range(0, w - 50, 150):
            cv2.line(img, (5, i + 5), (h - i, h), (0, 0, 0), 7)

        for i in range(150, w - 50, 150):
            cv2.line(img, (i, 0), (h, h - i), (0, 0, 0), 7)
        cv2.imwrite(f'{outputname}.png', img)

        print("DONE! image has been added to your working directory:")
        print("Your working directory: ", os.getcwd())
        cv2.imshow("img", img)
        cv2.waitKey(0)


    @classmethod
    def cafeWall(self,outputname, dimension=1200, resize=False, brickcolor=(255, 255, 255), bgcolor=(0, 0, 0)):
        dimension = int(dimension)
        img = np.zeros((dimension, dimension, 3), dtype=np.uint8)
        img[:, :, :] = bgcolor
        h, w, _ = img.shape

        for i in range(0, h, 200):
            for j in range(0, w, 160):
                cv2.rectangle(img, (i + 43, j), (i + 140, j + 77), brickcolor, -1)
                cv2.rectangle(img, (i + 100, j + 83), (i + 197, j + 157), brickcolor, -1)

        for i in range(0, h, 80):
            cv2.line(img, (0, i), (w, i), (128, 128, 128), 4)

        cv2.imwrite(f'{outputname}.png', img)
        if resize == True:
            resizedimg = cv2.resize(img, (300, 300))
            cv2.imwrite(f'{outputname}resized.png', resizedimg)
        else:
            pass

        print("DONE! image has been added to your working directory:")
        print("Your working directory: ", os.getcwd())
        cv2.imshow("img", img)
        cv2.waitKey(0)

    @classmethod
    def ccob(self,image, rms=0.5, amplitudespectrum=300, plttitle='output'):

        # loaded the image in grayscale
        img = cv2.imread(image, 0)

        #  convert image to the -1:+1 range
        img = (img / 255.0) * 2.0 - 1.0

        # desired RMS (root mean square contrast)
        rms = rms

        # make the mean to be zero
        img = img - np.mean(img)
        # make the standard deviation to be 1
        img = img / np.std(img)
        # make the standard deviation to be the desired RMS
        img = img * rms

        # convert to frequency domain
        img_freq = np.fft.fft2(img)
        rows, cols = img.shape

        # calculate amplitude spectrum
        img_amp = np.fft.fftshift(np.abs(img_freq))
        amplitudespectrum = int(amplitudespectrum)
        kerne = np.ones((amplitudespectrum, amplitudespectrum), np.float32) / amplitudespectrum

        lp_filt = cv2.filter2D(img_amp, -1, kerne)

        img_filt = np.fft.fftshift(img_freq) * lp_filt

        # convert back to an image
        img_new = np.real(np.fft.ifft2(np.fft.ifftshift(img_filt)))

        # convert to mean zero and specified RMS contrast
        img_new = img_new - np.mean(img_new)
        img_new = img_new / np.std(img_new)
        img_new = img_new * rms

        # Apply Lapplacian of Gaussian

        gaus = cv2.GaussianBlur(img_new, (7, 7), 7)
        laplacian = cv2.Laplacian(gaus, cv2.CV_64F, 3)

        plt.imshow(laplacian, cmap='gray')
        plt.title(f'{plttitle}')
        plt.savefig(f'{plttitle}')
        print(f"DONE! image f'{plttitle} has been added to your working directory:")
        print("Your working directory: ", os.getcwd())

        plt.show()

    @classmethod
    def ebbinghaus(self,output, bgcolor=(255, 255, 255), lcradius=22, rcradius=22, lcradius2=25, rcradius2=45):
        img = 255 * np.ones((400, 800, 3), np.uint8)
        img[:, :, :] = bgcolor
        lcradius = int(lcradius)
        rcradius = int(rcradius)
        lcradius2 = int(lcradius2)
        rcradius2 = int(rcradius2)

        cv2.circle(img, (180, 180), lcradius, (0, 0, 0), 3)

        for i in range(0, 8):
            center = (int(180 + 65 * np.sin(i * np.pi / 4)), int(180 + 65 * np.cos(i * np.pi / 4)))
            cv2.circle(img, center, lcradius2, (0, 0, 0), 3)

        cv2.circle(img, (620, 180), rcradius, (0, 0, 0), 3)

        for i in range(0, 8):
            center = (int(620 + 130 * np.sin(i * np.pi / 4)), int(180 + 130 * np.cos(i * np.pi / 4)))
            cv2.circle(img, center, rcradius2, (0, 0, 0), 3)

        cv2.imshow("img", img)
        cv2.imwrite(f'{output}.png', img)
        print(f"DONE! image f'{output} has been added to your working directory:")
        print("Your working directory: ", os.getcwd())
        cv2.waitKey(0)

    @classmethod
    def whiteill(self,dimension=300, version2=False, rect1=(255, 255, 255), rect2=(0, 0, 0), bgrec1=(128, 128, 128),
                 bgrec2=(128, 128, 128), bg1=(0, 0, 0), bg2=(255, 255, 255), outputname="output"):
        dimension = int(dimension)

        if version2 == False:
            img = np.ones((dimension, dimension, 3), dtype=np.uint8)
            img[:, :, :] = bg1
            h, w, _ = img.shape
            cnt1 = int(h / 2)
            cnt2 = int(w / 2)

            cv2.rectangle(img, (cnt1 - 75, cnt1 - 75), (cnt1 + 60, cnt1 + 70), bgrec1, -1)
            for i in range(0, h, 75):
                for j in range(20, h, 75):
                    cv2.rectangle(img, (i + 5, j), (i + 45, j + 40), rect1, -1)

            img2 = 255 * np.ones((dimension, dimension, 3), dtype=np.uint8)
            img2[:, :, :] = bg2
            h, w, _ = img2.shape
            cnt1 = int(h / 2)
            cnt2 = int(w / 2)
            cv2.rectangle(img2, (cnt1 - 75, cnt1 - 75), (cnt1 + 60, cnt1 + 70), bgrec2, -1)
            for i in range(0, h, 75):
                for j in range(20, h, 75):
                    cv2.rectangle(img2, (i + 5, j), (i + 45, j + 40), rect2, -1)
            cv2.imwrite(f'{outputname}.png', img)
            cv2.imwrite(f'{outputname}2.png', img2)

            cv2.imshow("img2", img2)

            cv2.imshow("img1", img)

            cv2.waitKey(0)
        else:
            img = np.ones((700, 700, 3), dtype=np.uint8)
            for i in range(0, 700, 40):
                cv2.line(img, (0, i), (700, i), (255, 255, 255), 15)
            for i in range(160, int(700 / 2), 40):
                cv2.line(img, (80, i + 40), (240, i + 40), (128, 128, 128), 15)
            for i in range(140, int(700 / 2), 40):
                cv2.line(img, (400, i + 40), (560, i + 40), (128, 128, 128), 15)
            cv2.imshow("img", img)
            cv2.imwrite(f'{outputname}vers1.png', img)

            cv2.waitKey(0)
    @classmethod
    def enigma(self,linecolors=(255,255,255), bgcolor=(1, 1, 1),circle1=(76, 0, 153),circle2=(102, 0, 204),
               centercircle=(0,255,255),
               outputname="enigma"):
        x = int(512)
        y = int(512)

        img = np.ones((x, y, 3), np.uint8)
        img[:, :, :] = bgcolor
        h, w, _c = img.shape

        for i in range(0, h, int(h / 43)):
            # cv2.line(img,(0,i),(512-i,512),(255,255,255),3)
            cv2.line(img, (i, 0), (h - i, h), linecolors, int(h / 512))
            cv2.line(img, (0, i), (h, h - i), linecolors, int(h / 512))

        for i in range(0, h, int(h / 43)):
            # cv2.line(img,(0,i),(512-i,512),(255,255,255),3)
            cv2.line(img, (i + 1, 0), ((h - 1) - i, h), linecolors, int(h / 512))
            cv2.line(img, (0, i + 1), (h, (h - 1) - i), linecolors, int(h / 512))

        for i in range(0, h, int(h / 43)):
            # cv2.line(img,(0,i),(512-i,512),(255,255,255),3)
            cv2.line(img, (i + 2, 0), ((h - 2) - i, h), linecolors, int(h / 512))
            cv2.line(img, (0, i + 2), (h, (h - 2) - i), linecolors, int(h / 512))

        for i in range(int(h / 4), int(h / 2), int(h / 8)):
            cv2.circle(img, (int(h / 2), int(h / 2)), i - 10, circle1, int(h / 26))
            cv2.circle(img, (int(h / 2), int(h / 2)), i - 12, circle2, int(h / 45))

        cv2.circle(img, (int(h / 2), int(h / 2)), 200, circle1, int(h / 25))

        cv2.circle(img, (int(h / 2), int(h / 2)), 45, centercircle, -1)
        cv2.circle(img, (int(h / 2), int(h / 2)), 4, (0, 0, 255), -1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'{outputname}gray.png', gray)
        cv2.imwrite(f'{outputname}.png', img)