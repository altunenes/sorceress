#A collection of functions for the sorceress module that is written in python language

###############################  version: 1.8.6     ###############################
############################### Author: Enes Altun  ###############################

import cv2
import numpy as np
import colour
import glob
import os
import imageio
from matplotlib import pyplot as plt
import sys
from PIL import Image

def chromatic(img,circle=True, method="CMCCAT2000", gif=True, Gifduration=7,XYZ_w=(110, 75, 35),XYZ_wr=(200, 120, 75),L_A=2000):
    """
    This function is used to convert an image to chromatic image.
    :param img: input image with extension ("test.png")
    :param circle: a center fixation
    :param method: "CMCCAT2000" or "Von Kries"
    :param gif: export as gif
    :param Gifduration: duration of the gif (in seconds)
    :param XYZ_w, XYZ_wr, L_A: chromatic adaptation parameters (has default values)
    :return:
    """
    outputname = os.path.basename(img).split(".")[0]
    img = cv2.imread(img)
    hsize, wsize, _ = img.shape
    centery = int(hsize / 2)
    centerx = int(wsize / 2)
    Gifduration=int(Gifduration)
    pil=int(Gifduration*1000)

    XYZ = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    gry = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    L_A = int(L_A)
    XYZ_w = np.array(XYZ_w)
    XYZ_wr = np.array(XYZ_wr)
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
    if os.path.exists("chromatic") and os.path.exists("chromaticPIL"):
        sys.exit("ERROR: chromatic and chromaticPIL folder already exists, please delete them or change the name of the output folder")
    else:
        pass

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
                        duration=pil, loop=0)
    elif gif == False:
        cv2.imwrite(f'{outputname}.png', test)
        cv2.imwrite(f'{outputname}gry.png', gry)
        print("Done ", f'{outputname}.png has been added your working dir.')
        print("Your working directory: ", os.getcwd())
def dotill(dimension,hlinefreq=12,wlinefreq=12,dotcolor=(0,255,0),dotradius=5,horizontalcolor=(14, 75, 3),verticalcolor=(14, 75, 3),horizontalthickness=4,verticalthickness=4,verticallines=True,horizontallines=True):
    """
    This function is used to create a dotill image.
    :param dimension: dimension of the image (width,height)
    :param hlinefreq: horizontal line frequency
    :param wlinefreq: vertical line frequency
    :param dotcolor: color of the dot
    :param dotradius: radius of the dot
    :param horizontalcolor: horizontal line color
    :param verticalcolor: vertical line color
    :param horizontalthickness: horizontal line thickness
    :param verticalthickness: vertical line thickness
    :param verticallines: if True, vertical lines are drawn
    :param horizontallines: if True, horizontal lines are drawn
    :return:
    """
    hsize,wsize=dimension
    hsize=int(hsize)
    wsize=int(wsize)
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
        pass
    else:
        raise ValueError("neither True nor False expression has been given to the 'horizontallines=' parameter")

    for i in range(beta):
        for j in range(alpha):
            x, y = int(j * width), int(i * height)
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
    print("Done! Your working directory: ", os.getcwd())
def realtimegrid(realcolours=True):
    """ realtimegrid is a function that add grids to the gray frame.
        :param realcolours: if True, real colours (colors that correspond to the frame) are added to frame.
    :return:
    """

    def empty(a):
        pass
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('tracker')
    if realcolours == False:
        cv2.resizeWindow('tracker', 720, 640)
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
        if Wthickness == 0:
            Wthickness = Wthickness + 1
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
    


def addlines(img, linecolour1=(0,255,0), linecolour2=(0,255,255), linecolour3=(255,0,0), linecolour4=(255,255,0),alphablending=False, thickness=3, frequency=3, style='vertical', amplitude=1,period=15,midpoint=12):
    """"
    Adds lines to an image.
    Arguments:
    img: input image
    linecolours:  line colours
    alphablending: if False, line colors are much more stable against the luminance change in the background image.
    thickness: line thickness (default=3)
    frequency: line frequency (default=3)
    style: "vertical","horizontal", "diagonal","cross","zigzag","cross","checkerboard", "wave", "wave2", "circles", "rectangles"
    amplitude: wave amplitude (default=1) // only for wave and wave2
    period: wave period (default=15)    // only for wave and wave2
    midpoint: wave midpoint (default=12) // only for wave and wave2
    :return
    """
    outputname = os.path.basename(img).split(".")[0]
    rect = cv2.imread(img)
    h,w,c=rect.shape

    if alphablending == False:
        img2 = np.ones((h,w,c),dtype=np.uint8)
        if style == 'horizontal':
            if w > h or w==h:
                for i in range(0, w, frequency):
                    cv2.line(img2, (i, 0), (i, w), linecolour1, thickness)
                    cv2.line(img2, (i + 1, 0), (i + 1, (w)), linecolour2, thickness)
                    cv2.line(img2, (i + 2, 0), (i + 2, (w)), linecolour3, thickness)
                    cv2.line(img2, (i + 3, 0), (i + 3, (w)), linecolour4, thickness)
                   
            else:
                for i in range(0, h, frequency):
                    cv2.line(img2, (0, i), (h, i), linecolour1, thickness)
                    cv2.line(img2, (0, i+1), (h, (i+1)), linecolour2, thickness)
                    cv2.line(img2, (0, i+2), (h, (i+2)), linecolour3, thickness)
                    cv2.line(img2, (0, i+3), (h, (i+3)), linecolour4, thickness)
        elif style == 'vertical':
            if w > h or w==h:
                for i in range(0, h, frequency):
                    cv2.line(img2, (0, i), (w, i), linecolour1, thickness)
                    cv2.line(img2, (0, i+1), (w, (i+1)), linecolour2, thickness)
                    cv2.line(img2, (0, i+2), (w, (i+2)), linecolour3, thickness)
                    cv2.line(img2, (0, i+3), (w, (i+3)), linecolour4, thickness)
            else:
                for i in range(0, w, frequency):
                    cv2.line(img2, (i, 0), (i, h), linecolour1, thickness)
                    cv2.line(img2, (i + 1, 0), (i + 1, (h)), linecolour2, thickness)
                    cv2.line(img2, (i + 2, 0), (i + 2, (h)), linecolour3, thickness)
                    cv2.line(img2, (i + 3, 0), (i + 3, (h)), linecolour4, thickness)
                               
        elif style == 'diagonal':
            for i in range(0, h, frequency):
                cv2.line(img2, (0, i), (w, i+i), linecolour1, thickness)
                cv2.line(img2, (0, i+1), (w, (i+1+i)), linecolour2, thickness)
                cv2.line(img2, (0, i+2), (w, (i+2+i)), linecolour3, thickness)
                cv2.line(img2, (0, i+3), (w, (i+3+i)), linecolour4, thickness)

        elif style == 'cross':
            for i in range(0, h, frequency):
                cv2.line(img2, (0, i), (w, i+i), linecolour1, thickness)
                cv2.line(img2, (0, i+1), (w, (i+1+i)), linecolour2, thickness)
                cv2.line(img2, (0, i+2), (w, (i+2+i)), linecolour3, thickness)
                cv2.line(img2, (0, i+3), (w, (i+3+i)), linecolour4, thickness)
            for i in range(0, h, frequency):
                cv2.line(img2, (i, 0), (i+i, h), linecolour1, thickness)
                cv2.line(img2, (i+1, 0), ((i+1)+i, h), linecolour2, thickness)
                cv2.line(img2, (i+2, 0), ((i+2)+i, h), linecolour3, thickness)
                cv2.line(img2, (i+3, 0), ((i+3)+i, h), linecolour4, thickness)   
        elif style == 'zigzag':
            for i in range(0, h, frequency):
                cv2.line(img2, (0, i), (w, i+i), linecolour1, thickness)
                cv2.line(img2, (0, i+1), (w, (i+1+i)), linecolour2, thickness)
                cv2.line(img2, (0, i+2), (w, (i+2+i)), linecolour3, thickness)
                cv2.line(img2, (0, i+3), (w, (i+3+i)), linecolour4, thickness)
                cv2.line(img2, (w, i), (0, i+i), linecolour1, thickness)
                cv2.line(img2, (w, i+1), (0, (i+1+i)), linecolour2, thickness)
                cv2.line(img2, (w, i+2), (0, (i+2+i)), linecolour3, thickness)
                cv2.line(img2, (w, i+3), (0, (i+3+i)), linecolour4, thickness)
        
        elif style == 'checkerboard':
            for i in range(h):
                for j in range(w):
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                        cv2.line(img2, (j, i), (j+1, i), linecolour1, thickness)
                    else:
                        cv2.line(img2, (j, i), (j+1, i), linecolour2, thickness)
        
        elif style == 'wave':
            amplitude = h // 1
            midpoint = h // 12
            period = w // 15
            for i in range(h):
                x = i * frequency
                y = int(amplitude * np.sin(x * 2 * np.pi / period) + midpoint)
                cv2.line(img2, (0, i), (y, i), linecolour1, thickness)
                cv2.line(img2, (y+1, i), (w, i), linecolour2, thickness)
        elif style == 'wave2':
            amplitude = w // amplitude
            midpoint = w // midpoint
            period = h // period
    
            for i in range(w):
                x = i * frequency
                y = int(amplitude * np.sin(x * 2 * np.pi / period) + midpoint)
                cv2.line(img2, (i, 0), (i, y), linecolour1, thickness)
                cv2.line(img2, (i, y+1), (i, h), linecolour2, thickness)   
                    
                    
        elif style == 'circles':
            for i in range(frequency, h//2, frequency):
                cv2.circle(img2, (w//2, h//2), i, linecolour1, thickness)
                cv2.circle(img2, (w//2, h//2), i+1, linecolour2, thickness)
                cv2.circle(img2, (w//2, h//2), i+2, linecolour3, thickness)
                cv2.circle(img2, (w//2, h//2), i+3, linecolour4, thickness)   
        

        elif style == 'rectangles':
            for i in range(frequency, min(w, h)//2, frequency):
                cv2.rectangle(img2, (w//2-i, h//2-i), (w//2+i, h//2+i), linecolour1, thickness)
                cv2.rectangle(img2, (w//2-i-1, h//2-i-1), (w//2+i+1, h//2+i+1), linecolour2, thickness)
                cv2.rectangle(img2, (w//2-i-2, h//2-i-2), (w//2+i+2, h//2+i+2), linecolour3, thickness)
                cv2.rectangle(img2, (w//2-i-3, h//2-i-3), (w//2+i+3, h//2+i+3), linecolour4, thickness)

        
        result2 = cv2.addWeighted(rect, 0.1, img2, 77, 0)
        result3 = cv2.addWeighted(img2, 77, rect, 0.1, 77)
        result4 = cv2.addWeighted(img2, 0.5, rect, 0.5, 0)
        result5 = cv2.addWeighted(rect, 0.5, img2, 0.5, 0)
        blur = cv2.GaussianBlur(result2, (7, 7), 0)

        cv2.imwrite(f'{outputname}blur.png', blur)
        cv2.imwrite(f'{outputname}ver7.png', result2)
        cv2.imwrite(f'{outputname}ver8.png', result3)
        cv2.imwrite(f'{outputname}ver9.png', result4)
        cv2.imwrite(f'{outputname}ver10.png', result5)
        print("DONE! grids have been added to your image check your working directory:",os.getcwd())
    else:
        rect = cv2.cvtColor(rect, cv2.COLOR_BGR2BGRA)
        h, w, c = rect.shape
        img2 = rect.copy()
        if w > h or w==h:
            for i in range(0, w, frequency):
                cv2.line(img2, (i, 0), (i, w), linecolour1, thickness)
                cv2.line(img2, (i + 1, 0), (i + 1, (w)), linecolour2, thickness)
                cv2.line(img2, (i + 2, 0), (i + 2, (w)), linecolour3, thickness)
        else:
            for i in range(0, h, frequency):
                cv2.line(img2, (0, i), (h, i), linecolour1, thickness)
                cv2.line(img2, (0, i+1), (h, (i+1)), linecolour2, thickness)
                cv2.line(img2, (0, i+2), (h, (i+2)), linecolour3, thickness)
        srcBGR = img2[..., :3]
        dstBGR = rect[..., :3]
        srcA = img2[..., 3] / 255.0
        dstA = rect[..., 3] / 255.0

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

def eyecolour(img,alpha=0.8,beta=0.3,M=25,luminance=1,saturation=1,colors=(0,0,255)):
    """
    Select the iris on the image with mouse click and it returns the illusory eye colour.
    Arguments:
    :param img: input image path with extension
    :param alpha: alpha beta and M are the parameters of blending. Play with them to get the best results
    :param luminance and saturation: Don't use values greater than 1 for luminance and saturation
    :param colors: BGR values of the color you want to use for the left half of the image (default is red)
    :return:
    """
    if luminance>1 or saturation>1:
        raise ValueError("Luminance and saturation values should be between 0 and 1")

    outputname = os.path.basename(img).split(".")[0]
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    luminance=float(luminance)
    saturation=float(saturation)
    img = cv2.equalizeHist(img)
    print("select the iris (select smaller as much as possible for good results); then press to enter ")
    r = cv2.selectROI(img,fromCenter=False)

    roi_cropped = img[int((r[1])):int((r[1]) + int(r[3])), int((r[0])):int((r[0])) + int((r[2]))]

    center = int((r[0]+r[0]+r[2]) / 2), int((r[1]+r[1]+r[3]) / 2)
    redd = 255 * np.ones(roi_cropped.shape, roi_cropped.dtype)

    h, w = img.shape
    centw=int(w/2)
    mask = np.ones((h, w, 3), dtype=np.uint8)

    j = 0
    for i in range(0, centw, 20):
        mask[j:h, i:centw] = colors
        j += 20

    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    roi_cropped = cv2.cvtColor(roi_cropped, cv2.COLOR_GRAY2RGB)

    eclipse=cv2.ellipse(mask,center,(int(r[2]),int(r[3])),0,0,360,(0,0,0),-1)
    bit=cv2.bitwise_and(eclipse,mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
    mask[:, :, 2] = 200
    mask[:, :, 0] = 200

    alpha = float(alpha)
    beta =float(beta)
    M = int(M)
    result = cv2.addWeighted(img, alpha, bit, beta, M)

    output = cv2.seamlessClone(roi_cropped, result, redd, center, cv2.NORMAL_CLONE)
    blur = cv2.GaussianBlur(result, (5, 5), 0)
    # result[int((r[1])):int((r[1]) + int(r[3])), int((r[0])):int((r[0])) + int((r[2]))] = roi_cropped
    output = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
    output[:, :, 2] = np.where(output[:, :, 2] < 10, output[:,:,2]*luminance, output[:, :, 2])
    output = cv2.cvtColor(output, cv2.COLOR_HSV2BGR)

    output = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
    output[:,:,1]=np.where(output[:,:,1]<100,output[:,:,1]*saturation,output[:,:,1])
    output = cv2.cvtColor(output, cv2.COLOR_HSV2BGR)

    cv2.imwrite(f'{outputname}.png', output)
    cv2.imwrite(f'{outputname}blur.png', blur)

    print("DONE! images have been added to your working directory:")
    print("Your working directory: ", os.getcwd())

def dakinPex(outputname, dimension=800, black=(0, 0, 0), white=(255, 255, 255), bg_color=(128, 128, 128)):    
    """
    Creates an optical illusion from the Dakin and Bex, 2003 paper.
    :param outputname: output name
    :param dimension: dimension of the image
    :param black: line color1 (default is black)
    :param white: line color2 (default is white)
    :param bg_color: background color (default is gray)
    :return:
    """

    img = bg_color * np.ones((int(dimension), int(dimension), 3), dtype=np.uint8)
    h, w, _ = img.shape
    for i in range(0, h, 160):
        for j in range(0, w, 160):
            cv2.rectangle(img, (i, j), (i + 75, j + 75), black, 5)
            cv2.rectangle(img, (i + 80, j + 80), (i + 155, j + 155), black, 5)

    for i in range(0, h, 160):
        for j in range(0, w, 160):
            cv2.rectangle(img, (i + 80, j), (i + 155, j + 75), white, 2)
            cv2.rectangle(img, (i, j + 80), (i + 75, j + 155), white, 2)

    cv2.imwrite(f'{outputname}.png', img)

    print("DONE! images have been added to your working directory:")
    print("Your working directory: ", os.getcwd())


def bruno(outputname,circle=False, polycolor=(0, 255, 255), rectcolor=(255, 255, 0), circColor=(0, 0, 255)):
    """
    Creates an optical illusion from the Bruno et al. (1997).
    :param outputname: output name
    :param circle: if true, a circle is drawn instead of a rectangle
    :param polycolor: color of the polygon
    :param rectcolor: color of the rectangle
    :param circColor: color of the circle
    :return:
    """
    img = 255 * np.ones((600, 600, 3), dtype=np.uint8)
    h, w, _ = img.shape

    pts = np.array([[60, 60], [120, 30], [180, 100], [120, 180], [60, 150]])  # most left to right
    pts2 = np.array([[400, 60], [460, 30], [520, 100], [460, 180], [400, 150]])  # most left to right

    pts3 = np.array([[60, 360], [120, 330], [180, 400], [120, 480], [60, 450]])  # most left to right
    pts4 = np.array([[400, 360], [460, 330], [520, 400], [460, 480], [400, 450]])  # most left to right

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

def dolboeuf(outputname, dimension=800,bg_color=(255,255,255) ,circle1_color=(0, 0, 255), circle2_color=(0, 0, 255), radius=0.045,kill=False):
    """
    Creates an optical illusion from the Joseph Remi Leopold Delbœuf (1865).
    :param outputname: output name
    :param bgcolor: background color (default is white)
    :param circleColor1: color of the first circle
    :param circleColor2: color of the second circle
    :param kill: if true, the illusion will be destroyed by the lines
    :param dimension: dimension of the image
    :param radius: radius of the circle (default is 0.045, which is 45% of the image. It's sensitive to the dimension)

    :return:
    """
    img = bg_color * np.ones((dimension, dimension, 3), dtype=np.uint8)
    center1 = (int(dimension * 0.10), int(dimension * 0.375))
    center2 = (int(dimension * 0.75), int(dimension * 0.375))
    for i in range(35, 37, 2):
        cv2.circle(img, center1, int(dimension * radius), circle1_color, -1)
        cv2.circle(img, center1,int(dimension * radius * 1.1), (0, 0, 0), 3)
    cv2.circle(img, center2, int(dimension * radius), circle2_color, -1)
    cv2.circle(img, center2, int(dimension * radius * 2.7), (0, 0, 0), 3)
    if kill:
        cv2.line(img, (int(center1[0]), int(center1[1] + dimension * radius)), (int(center2[0]), int(center2[1] + dimension * radius)), (0, 0, 0), 2)
        cv2.line(img, (int(center1[0]), int(center1[1] - dimension * radius)), (int(center2[0]), int(center2[1] - dimension * radius)), (0, 0, 0), 2)
    cv2.imwrite(f'{outputname}.png', img)


    print("DONE! image has been added to your working directory:")
    print("Your working directory: ", os.getcwd())

def kanizsa(outputname, dims=600, circleColor=(0, 0, 255), bgcolor=(255, 255, 255)):
    """
    Creates an optical illusion from the Gaetano Kanizsa.
    :param outputname: output name
    :param dims: dimension of the image
    :param circleColor: color of the circle
    :param bgcolor: color of the background
    :return:
    """
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
    print("DONE! image has been added to your working directory:")
    print("Your working directory: ", os.getcwd())

def ponzol(outputname,kill=False,line1=(255,0,0),line2=(255,0,0),rectangle1=(0,0,255),rectangle2=(0,0,255), dimension=600, bgcolor=(255, 255, 255)):
    """
    Creates an optical illusion from Ponzo, 1912.
    :param outputname: output name
    :param kill: if true, the illusion will be destroyed by the lines
    :param line1: color of the first line
    :param line2: color of the second line
    :param rectangle1: color of the first rectangle
    :param rectangle2: color of the second rectangle
    :param dimension: dimension of the image
    :param bgcolor: color of the background
    :return:
    """
    img = bgcolor * np.ones((dimension, dimension, 3), dtype=np.uint8)
    h, w, _ = img.shape

    cv2.line(img, (int(dimension * 0.1333), int(dimension * 0.6667)), (int(dimension * 0.5), int(dimension * 0.0333)), line1, int(dimension * 0.0067))
    cv2.line(img, (int(dimension * 0.5667), int(dimension * 0.0333)), (int(dimension * 0.9333), int(dimension * 0.6667)), line2, int(dimension * 0.0067))

    cv2.rectangle(img, (int(dimension * 0.4167), int(dimension * 0.1167)), (int(dimension * 0.65), int(dimension * 0.0667)), rectangle1, -1)
    cv2.rectangle(img, (int(dimension * 0.4167), int(dimension * 0.5833)), (int(dimension * 0.65), int(dimension * 0.5333)), rectangle2, -1)

    if kill == True:
        for i in range(int(dimension * 0.1167), int(dimension * 0.5667), int(dimension * 0.05)):
            cv2.rectangle(img, (int(dimension * 0.4167), i), (int(dimension * 0.65), i + int(dimension * 0.0333)), (0, 0, 255), -1)
            cv2.line(img, (int(dimension * 0.4167), int(dimension * 0.1167)), (int(dimension * 0.4167), int(dimension * 0.5833)), (0, 0, 0), int(dimension * 0.01))
            cv2.line(img, (int(dimension * 0.65), int(dimension * 0.1167)), (int(dimension * 0.65), int(dimension * 0.5833)), (0, 0, 0), int(dimension * 0.01))

    cv2.imwrite(f'{outputname}.png', img)


    print("DONE! image has been added to your working directory:")
    print("Your working directory: ", os.getcwd())

def tAki2001(outputname, dimension=700, circlecolour=(0, 255, 255), circleradius=15, bglinecolor=(255, 128, 128),bgcolor=(255, 255, 255)):
    """
    “Coloured ray illusion ” by Akiyoshi Kitaoka (2001).
    :param outputname: output name
    :param dimension: dimension of the image
    :param circlecolour: color of the circle
    :param circleradius: radius of the circle
    :param bglinecolor: color of the background line
    :param bgcolor: color of the background
    :return:
    """
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

def cafeWall(outputname, dimension=1200, resize=False, brickcolor=(255, 255, 255), bgcolor=(0, 0, 0)):
    """
    Creates cafe wall illusion.
    :param outputname: output name
    :param dimension: dimension of the image
    :param resize: if true, the image will be adjusted to the dimension
    :param brickcolor: color of the bricks
    :param bgcolor: color of the background
    :return:
    """
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

    
def ccob(image, rms=0.5, amplitudespectrum=300, plttitle='output',figs=(0.8, 0.8)):
    """
    Creates an optical illusion about Spatial Frequency.
    :param image: input image
    :param rms: desired root mean square
    :param amplitudespectrum: amplitude spectrum
    :param plttitle: output name
    :param figs: figure size of the output (it will multiply by 1000)
    :return:
    """
    img = cv2.imread(image, 0)
    figs = float(figs[0]), float(figs[1])


    img = (img / 255.0) * 2.0 - 1.0

    rms = rms
    img = img - np.mean(img)
    img = img / np.std(img)
    img = img * rms
    img_freq = np.fft.fft2(img)
    img_amp = np.fft.fftshift(np.abs(img_freq))
    amplitudespectrum = int(amplitudespectrum)
    kerne = np.ones((amplitudespectrum, amplitudespectrum), np.float32) / amplitudespectrum
    lp_filt = cv2.filter2D(img_amp, -1, kerne)
    img_filt = np.fft.fftshift(img_freq) * lp_filt
    img_new = np.real(np.fft.ifft2(np.fft.ifftshift(img_filt)))
    img_new = img_new - np.mean(img_new)
    img_new = img_new / np.std(img_new)
    img_new = img_new * rms
    gaus = cv2.GaussianBlur(img_new, (7, 7), 7)
    laplacian = cv2.Laplacian(gaus, cv2.CV_64F, 3)
    plt.figure(figsize=(figs[0],figs[1]), dpi=1000)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.axis('off')
    plt.imshow(laplacian, cmap='gray')
    plt.savefig(f'{plttitle}', bbox_inches='tight', pad_inches=0, dpi=1000)
    print(f"DONE! image f'{plttitle} has been added to your working directory:")
    print("Your working directory: ", os.getcwd())
    plt.show()

def ebbinghaus(output, bgcolor=(255, 255, 255), lcradius=22, rcradius=22, lcradius2=25, rcradius2=45, randcirclecolors=True, dimensions=(400, 800)):
    """
    Creates ebbinghaus illision .
    :param output: output name
    :param bgcolor: background color
    :param lcradius: left center circle radius
    :param rcradius:  right center circle radius
    :param lcradius2:  left circles radius
    :param rcradius2:  right circles radius
    :param randcirclecolors: circles  have random colors (recommended)
    :param dimensions: dimensions of the image (be sure you entered a rectangular image otherwise it will be distorted it's highly experimental default is (400,800)
    :return:
    """
    img = 255 * np.ones((dimensions[0], dimensions[1], 3), np.uint8)
    img[:, :, :] = bgcolor

    lcradius = int(lcradius * dimensions[0] / 400)
    rcradius = int(rcradius * dimensions[0] / 400)
    lcradius2 = int(lcradius2 * dimensions[0] / 400)
    rcradius2 = int(rcradius2 * dimensions[0] / 400)

    lccenter = (int(dimensions[1] * 180 / 800), int(dimensions[0] * 180 / 400))
    rccenter = (int(dimensions[1] * 620 / 800), int(dimensions[0] * 180 / 400))

    b = np.random.randint(0, 255) if randcirclecolors else 0
    g = np.random.randint(0, 255) if randcirclecolors else 0
    r = np.random.randint(0, 255) if randcirclecolors else 0
    cv2.circle(img, lccenter, lcradius, (b, g, r), -1)

    for i in range(0, 8):
        center = (int(lccenter[0] + (dimensions[1] / 800) * 65 * np.sin(i * np.pi / 4)), int(lccenter[1] + (dimensions[0] / 400) * 65 * np.cos(i * np.pi / 4)))
        b = np.random.randint(0, 255) if randcirclecolors else 0
        g = np.random.randint(0, 255) if randcirclecolors else 0
        r = np.random.randint(0, 255) if randcirclecolors else 0
        cv2.circle(img, center, lcradius2, (b, g, r), -1)

    b = np.random.randint(0, 255) if randcirclecolors else 0
    g = np.random.randint(0, 255) if randcirclecolors else 0
    r = np.random.randint(0, 255) if randcirclecolors else 0
    cv2.circle(img, rccenter, rcradius, (b, g, r), -1)

    for i in range(0, 8):
        center = (int(rccenter[0] + (dimensions[1] / 800) * 130
                        * np.sin(i * np.pi / 4)), int(rccenter[1] + (dimensions[0] / 400) * 130 * np.cos(i * np.pi / 4)))
        b = np.random.randint(0, 255) if randcirclecolors else 0
        g = np.random.randint(0, 255) if randcirclecolors else 0
        r = np.random.randint(0, 255) if randcirclecolors else 0

        cv2.circle(img, center, rcradius2, (b, g, r), -1)

    cv2.imwrite(f'{output}.png', img)
    print(f"DONE! image f'{output} has been added to your working directory:")
    print("Your working directory: ", os.getcwd())

def whiteill(dimension=600, version2=False, rect1=(255, 255, 255), rect2=(0, 0, 0), bgrec1=(128, 128, 128),
             bgrec2=(128, 128, 128), bg1=(0, 0, 0), bg2=(255, 255, 255), outputname="output"):
    """
    Optiacal illusion that has been described by White (1979).
    :param dimension: dimension of the image (note, in version 2 if you enter smallar dimension than 600 it will be distorted)
    :param version2: if True, the second version of the illusion is created
    :param rect1: color of the first rectangle
    :param rect2: color of the second rectangle
    :param bgrec1: background color of the first rectangle, this also works on version2. Gray is default.
    :param bgrec2: background color of the second rectangle
    :param bg1: background color of the first image
    :param bg2: background color of the second image
    :param outputname: output name
    """
    dimension = int(dimension)
    if version2:
        img = np.zeros((dimension, dimension, 3), dtype=np.uint8)
        for i in range(0, dimension, 40):
            cv2.line(img, (0, i), (dimension, i), (255, 255, 255), 15)
        for i in range(160, int(dimension / 2), 40):
            cv2.line(img, (80, i + 40), (240, i + 40), bgrec1, 15)
        for i in range(140, int(dimension / 2), 40):
            cv2.line(img, (400, i + 40), (560, i + 40), bgrec1, 15)
        cv2.imwrite(f'{outputname}vers1.png', img)
    else:
        img = np.ones((dimension, dimension, 3), dtype=np.uint8)
        img[:, :, :] = bg1
        h, w, _ = img.shape
        cnt1 = int(h / 2)
        cv2.rectangle(img, (cnt1 - 75, cnt1 - 75), (cnt1 + 60, cnt1 + 70), bgrec1, -1)
        for i in range(0, h, 75):
            for j in range(20, h, 75):
                cv2.rectangle(img, (i + 5, j), (i + 45, j + 40), rect1, -1)
        img2 = 255 * np.ones((dimension, dimension, 3), dtype=np.uint8)
        img2[:, :, :] = bg2
        h, w, _ = img2.shape
        cnt1 = int(h / 2)
        cv2.rectangle(img2, (cnt1 - 75, cnt1 - 75), (cnt1 + 60, cnt1 + 70), bgrec2, -1)
        for i in range(0, h, 75):
            for j in range(20, h, 75):
                cv2.rectangle(img2, (i + 5, j), (i + 45, j + 40), rect2, -1)
        img = np.concatenate((img, img2), axis=1)
        cv2.imwrite(f'{outputname}.png', img)
    print(f"DONE! image f'{outputname} has been added to your working directory:")
    print("Your working directory: ", os.getcwd())

        
def enigma(dimension=512, linecolors=(255,255,255), bgcolor=(1, 1, 1), circle1=(76, 0, 153), circle2=(102, 0, 204),
           centercircle=(0,255,255),outputname="enigma",gif=True):
    """
    based on the a paper from the Zeki et al (1993).
    :param linecolors: color of the lines
    :param bgcolor:  background color of the image
    :param circle1: outer circle color
    :param circle2: inner circle color
    :param centercircle: central circle color
    :param outputname: output name
    :param gif: if True, the gif version of the illusion for the another illusion!Fix your gaze on the center than see what happens!
    :return:
    """
    x = int(dimension)
    y = int(dimension)
    img = np.ones((x, y, 3), np.uint8)
    img[:, :, :] = bgcolor
    h, w, _c = img.shape
    for i in range(0, h, int(h / 43)):
        cv2.line(img, (i, 0), (h - i, h), linecolors, int(h / dimension))
        cv2.line(img, (0, i), (h, h - i), linecolors, int(h / dimension))
    for i in range(0, h, int(h / 43)):
        cv2.line(img, (i + 1, 0), ((h - 1) - i, h), linecolors, int(h / dimension))
        cv2.line(img, (0, i + 1), (h, (h - 1) - i), linecolors, int(h / dimension))

    for i in range(0, h, int(h / 43)):
        cv2.line(img, (i + 2, 0), ((h - 2) - i, h), linecolors, int(h / dimension))
        cv2.line(img, (0, i + 2), (h, (h - 2) - i), linecolors, int(h / dimension))

    for i in range(int(h / 4), int(h / 2), int(h / 8)):
        cv2.circle(img, (int(h / 2), int(h / 2)), i - 10, circle1, int(h / 26))
        cv2.circle(img, (int(h / 2), int(h / 2)), i - 12, circle2, int(h / 45))

    cv2.circle(img, (int(h / 2), int(h / 2)), 200, circle1, int(h / 25))

    cv2.circle(img, (int(h / 2), int(h / 2)), 45, centercircle, -1)
    cv2.circle(img, (int(h / 2), int(h / 2)), 4, (0, 0, 255), -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if gif == True:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images = [img, gray]
        imageio.mimsave(outputname + '.gif', images, duration = 5)
        pass
    img=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f'{outputname}gray.png', gray)
    cv2.imwrite(f'{outputname}.png', img)



def blackhole(outputname="blackhole",dimensions=(800,800),circle_size=10, circle_color=(0, 0, 0),kill=False):
    """"
    Illusorily Expanding Holes.
    dimensions: dimensions of the image
    circle_size: size of the circles (center ellipse is adjusted with this ratio)
    circle_color: color of the circles
    kill: if True, circles are not drawn
    """

    height = dimensions[0]
    width = dimensions[1]
    img = 255*np.ones((height, width, 3), np.uint8)

    b = circle_color[0]
    g = circle_color[1]
    r = circle_color[2]
    center = (width // 2, height // 2)

    for i in range(255,0,-2):
        cv2.ellipse(img, center, (circle_size * 22+i, circle_size * 11+i), 0, 0, 360, (b+i, g+i, r+i), -1)

    if kill==False:
        if height >= width:
            for i in range(0, height, circle_size * 3):
                for j in range(0, height, circle_size *3):
                    cv2.circle(img, (i, j), circle_size, (b, g, r), -1)
        elif width > height:
            for i in range(0, width, circle_size * 3):
                for j in range(0, width, circle_size *3):
                    cv2.circle(img, (i, j), circle_size, (b, g, r), -1)
    cv2.imwrite(f'{outputname}.png', img)


def colorgrids(img,style="vertical",width=4,frequency=12,saturation=0):
    """
    This function applies Color assimilation Grid Illusion.
    :param img: input image
    :param style: style of mask, "vertical","horizontal","gaussian","grids"
    :param width: width of lines
    :param frequency: frequency of lines
    :param saturation: saturation of lines increasing this value will increase the saturation of lines but it will distort the image if it is too high
    :return:
    """
    outputname=os.path.splitext(img)[0]
    img=cv2.imread(img)
    width=int(width)
    frequency=int(frequency)
    s=int(saturation)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    mask=np.ones(img.shape, np.uint8) * 255
    if style=="vertical":
        for i in range(0,mask.shape[1],frequency):
            cv2.line(mask ,(i,0),(i,mask.shape[0]),(0,0,0),width)
    elif style=='horizontal':
        for i in range(0,mask.shape[0],frequency):
            cv2.line(mask ,(0,i),(mask.shape[1],i),(0,0,0),width)
    elif style=='gaussian':
        for i in range(0,mask.shape[0],frequency):
            for j in range(0,mask.shape[1],frequency):
                if np.random.randint(0,2)==1:
                    cv2.circle(mask ,(j+4,i+4),width,(0,0,0),-1)
    elif style=='grids':
        for i in range(0,mask.shape[1],frequency):
             for j in range(0,mask.shape[0],frequency):
                cv2.line(mask ,(i,0),(i,mask.shape[0]),(0,0,0),width)
                cv2.line(mask ,(0,j),(mask.shape[1],j),(0,0,0),width)
    else:
        print('mask type not supported')
    masked_bw=cv2.bitwise_not(mask)
    masked_bw=masked_bw[:,:,0]
    final=img.copy()
    for i in range(0,mask.shape[0]):
        for j in range(0,mask.shape[1]):
            if masked_bw[i,j] == 0:
                final[i,j,0] = img_gray[i,j]
                final[i,j,1] = img_gray[i,j]
                final[i,j,2] = img_gray[i,j]
    hsv=cv2.cvtColor(final,cv2.COLOR_BGR2HSV)
    hsv[:,:,1]=np.where(hsv[:,:,1]>100,hsv[:,:,1],hsv[:,:,1]+s)
    final=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    cv2.imwrite(outputname+"gridillusion.png",final)


def munker(dimensions=(1200,1200), linefrequency=100, rad_ratio=0.05, thickness=6, saturation=1,bgcolor=(255,255,255)):
    """
    Creates an image of the Munker illusion.
    Parameters
    ----------
    dimensions : tuple of ints (width, height) of the image. If you change this you also need to change the thickness and linefrequency. 
    linefrequency : This is the ratio of the horizontal lines to the width of the image, this value is used to calculate the distance between the lines. The default ratio is dimensions[0]/120
    rad_ratio :radius ratio of the circles.
    thickness :thickness of the lines. If you change the dimensions of the image, you may need to change this value as well. Default ratio is dimensions[0]/200
    saturation : saturation of the colors. 1 is full saturation, 0 is no saturation. 
    bgcolor : background color of the image. Default is white. This also will determines of the colors of the all circles
    """ 
    img = np.ones((dimensions[0],dimensions[1],3), np.uint8)
    img[:,:,:] = bgcolor

    alpha = linefrequency
    alpha = int(dimensions[0]/alpha)
    b,g,r = cv2.split(img)
    mask_b = np.zeros(dimensions, np.uint8)
    mask_g = np.zeros(dimensions, np.uint8)
    mask_r = np.zeros(dimensions, np.uint8)
    thickness = int(thickness)
    rad = int(min(dimensions[0], dimensions[1]) * rad_ratio)
    circle_ratio_height = int(dimensions[0]/2)
    circle_ratio_width = int(dimensions[1]/12)
    for i in range(0, int(dimensions[0]), int(dimensions[0]/5)):
        cv2.circle(mask_b, (i, i), rad, (255), -1)
        cv2.circle(mask_r, (i, i), rad, (255), -1)

    for i in range(0, int(dimensions[0]), int(dimensions[0]/5)):
        cv2.circle(mask_b, (i+circle_ratio_height, i+circle_ratio_width), rad, (255), -1)
        cv2.circle(mask_g, (i+circle_ratio_height, i+circle_ratio_width), rad, (255), -1)        
    for i in range(0, int(dimensions[0]), int(dimensions[0]/5)):
        cv2.circle(mask_g, (i, i+circle_ratio_width+int(dimensions[0]/3)), rad, (255), -1)
        cv2.circle(mask_r, (i, i+circle_ratio_width+int(dimensions[0]/3)), rad, (255), -1)
    for i in range(0, dimensions[0], alpha):
        cv2.line(mask_b, (0, i), (dimensions[0], i), (255), thickness)
        cv2.line(mask_g, (0, i+5), (dimensions[0], i+5), (255), thickness)
        cv2.line(mask_r, (0, i+8), (dimensions[0], i+8), (255), thickness)
    b=cv2.bitwise_and(b,b,mask=mask_b)
    g=cv2.bitwise_and(g,g,mask=mask_g)
    r=cv2.bitwise_and(r,r,mask=mask_r)
    img=cv2.merge((b,g,r))
    img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img[:,:,1]=img[:,:,1]*saturation
    img=cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imwrite('munker'+str(dimensions[0])+'x'+str(dimensions[1])+'.png',img)

def pareidolia(dimensions=(700,700),bg=(255,255,255),emotion="happy"):
    """
    With gabor filter coefficients, creates an image of a face with a pareidolic effect :) 
    Parameters
    dimensions : tuple of ints (width, height) of the image. This version is optimized for square images.
    bg : tuple of ints (r,g,b) of the background color. Default is white.
    emotion : string of the emotion of the face. Options are happy an sad. Default is happy.
    """
    img = 255*np.ones((dimensions[0],dimensions[1],3), np.uint8)
    img[:,:,:] = bg
    h,w,_ = img.shape
    center = (h / 2, w / 2)
    if emotion=="happy":
        for i in range(0, h,15):
            cv2.line(img, (w-1-i, 0), (w-1, i), (0, 0, 0), 5)   
    
        for i in range(0, h,12):
            cv2.line(img, (0, h-1-i), (i, h-1), (0, 0, 0), 5)
        for i in range(0, h,24):
            cv2.circle(img, (i, i), 15, (0, 255, 255), -1)

    elif emotion=="sad":
        for i in range(0, h,15):
            cv2.line(img, (w-1-i, 0), (w-1, i), (0, 0, 0), 5)
            cv2.line(img, (0, h-1-i), (i, h-1), (0, 0, 0), 5)

    
        for i in range(0, h,12):
            cv2.line(img, (0, h-1-i), (i, h-1), (0, 0, 0), 5)
        for i in range(0, h,24):
            cv2.circle(img, (i, i), 15, (0, 255, 255), -1)
    
    gabor = cv2.getGaborKernel((21,21), 8.0, np.pi/4, 10.0, 0.5, 0, ktype=cv2.CV_32F)
    gabor = cv2.filter2D(img, cv2.CV_8UC3, gabor)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_img = cv2.warpAffine(gabor, rotation_matrix, (w, h))
    cv2.imwrite('pareidolia'+str(dimensions[0])+'x'+str(dimensions[1])+'.png',rotated_img)
    print('pareidolia'+str(dimensions[0])+'x'+str(dimensions[1])+'.png was saved')

def grids2(dimensions=(340,640),line_width=5,line_color=(128,128,128),fill_color=(255,255,255)):
    """
    Creates an image of a grids and dots pattern.
    Parameters
    dimensions : tuple of ints (width, height) of the image. This version is optimized for only 340x640 images.
    line_width : int of the width of the lines. Default is 5
    line_color : tuple of ints (r,g,b) of the line color. Default is gray.
    fill_color : tuple of ints (r,g,b) of the fill color. Default is white.
    
    """
    img = np.ones((dimensions[0],dimensions[1],3),np.uint8)*1
    height,width,_ = img.shape
    for x in range(0,28):
        cv2.line(img,(x*40-304,0),(x*40+20,height),line_color,line_width)
        cv2.line(img,(x*40,0),(x*40-324,height),line_color,line_width)
    for x in range(0,20):
        for y in range(0,9):
            cv2.circle(img,(8+x*40, y*42-9), 3, fill_color, -1)
            cv2.circle(img,(28+x*40, y*42-29), 3, fill_color, -1)
    
    cv2.imwrite('grids2'+str(dimensions[0])+'x'+str(dimensions[1])+'.png',img)
    print('grids2'+str(dimensions[0])+'x'+str(dimensions[1])+'.png was saved')

def munker2(dimensions=(900,900),ilussory_colors=(255,238,138),leftstripes=(255,0,255),rightstripes=(0,255,0),bgcolor1=(255, 0, 255),bgcolor2=(0,255,0)):
    """
    Creates an image of a rectangular munker illusion.
    Parameters
    dimensions : tuple of ints (width, height) of the image.
    ilussory_colors : tuple of ints (r,g,b) of the ilussory colors (left and right rectangles)
    leftstripes : tuple of ints (r,g,b) of the left stripes color.
    rightstripes : tuple of ints (r,g,b) of the right stripes color.
    bgcolor1 : tuple of ints (r,g,b) of the background color of the left rectangle.
    bgcolor2 : tuple of ints (r,g,b) of the background color of the right rectangle.
    """

    img = 255*np.ones((dimensions[0],dimensions[1],3), np.uint8)
    for i in range(50):
        if i % 2 == 0:
            cv2.rectangle(img, (0, int(dimensions[1]/50*i)), (dimensions[0], int(dimensions[1]/50*(i+1))), bgcolor1, -1)
        else:
            cv2.rectangle(img, (0, int(dimensions[1]/50*i)), (dimensions[0], int(dimensions[1]/50*(i+1))), bgcolor2, -1)
    for i in range(50):
        if i % 2 == 0:
            cv2.rectangle(img, (int(dimensions[0]*0.2), int(dimensions[1]/50*i)), (int(dimensions[0]*0.4), int(dimensions[1]/50*(i+1))), leftstripes, -1)
        else:
            cv2.rectangle(img, (int(dimensions[0]*0.2), int(dimensions[1]/50*i)), (int(dimensions[0]*0.4), int(dimensions[1]/50*(i+1))), ilussory_colors, -1)
    for i in range(50):
        if i % 2 == 0:
            cv2.rectangle(img, (int(dimensions[0]*0.6), int(dimensions[1]/50*i)), (int(dimensions[0]*0.8), int(dimensions[1]/50*(i+1))), ilussory_colors, -1)
        else:
            cv2.rectangle(img, (int(dimensions[0]*0.6), int(dimensions[1]/50*i)), (int(dimensions[0]*0.8), int(dimensions[1]/50*(i+1))), rightstripes, -1)

    cv2.imwrite('munker2'+str(dimensions[0])+'x'+str(dimensions[1])+'.png',img)
    print('munker2'+str(dimensions[0])+'x'+str(dimensions[1])+'.png was saved')

def spiral(m):
    #function for crazy spirals for the further use
    r = np.linalg.norm(m)*6.
    a = np.arctan2(m[1], m[0])
    v = 50.*np.sin(60.*(np.power(r,1.)-1.*a))
    return np.clip(v,0.,1.)
def spiral2(m):
    #function for spirals 
    r = np.power(np.linalg.norm(m)*40.,0.8)
    a = np.arctan2(-m[1], m[0])
    v = np.sin(r-a)*2.*0.707
    rv = np.clip(v,-1.,1.)
    return rv
def mainImage(fragCoord):
    #function for image generation
    uv = fragCoord / 512.   
    m = np.array([.9,.5])
    s2 = int(spiral2(m-uv))
    s1 = spiral(m-uv)
    uv = fragCoord / 512.
    green = np.array([0.,1.,0.])
    s2_1 = np.clip(s2,0.,1.)
    s2_2 = np.abs(np.clip(s2,-1.,0.))
    magenta = (np.array([1.,0.,1.]) * (1.-s2_1) + green * s2_1)
    orange = (np.array([1.,0.5,0.]) * (1.-s2_2) + green * s2_2)
    col = magenta * (1.-s1) + orange * s1  
    return col
def spirals(dimensions=(800,800)):
    """"
    Creates an image of a spiral illusion.
    Parameters
    dimensions : tuple of ints (width, height) of the image.
    """
    img = np.zeros((dimensions[0],dimensions[1],3))
    h,w,_ = img.shape
    for i in range(h):
        for j in range(h):
            img[i,j,:] = mainImage(np.array([i,j]))
    
    cv2.imwrite('spirals.png',img*255)
    cv2.imwrite('spirals2.png',img[:,:,::-1]*255)
    print('spirals.png and spirals2.png were saved')

def negate_image(input_file, negation_method, color_space, output_quality):
    """"
    Negates an image.
    Parameters
    input_file : string of the input file path.
    negation_method : string of the negation method ('subtract', 'bitwise_not', 'subtract_hsv')
    color_space : string of the color space. ('hsv', 'gray', 'bgr')
    output_quality : int of the output quality.
    """


    img = cv2.imread(input_file)

    if color_space == 'hsv':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif color_space == 'gray':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if negation_method == 'subtract':
        neg_img = 255 - img
    elif negation_method == 'bitwise_not':
        neg_img = cv2.bitwise_not(img)
    elif negation_method == 'subtract_hsv':
        neg_img = 255 - img
        neg_img = cv2.cvtColor(neg_img, cv2.COLOR_HSV2BGR)

    filename, file_ext = os.path.splitext(input_file)

    output_file = filename + '_neg.png'

    cv2.imwrite(output_file, neg_img, [cv2.IMWRITE_PNG_COMPRESSION, output_quality])
def colordetection(inputimage):
    img = cv2.imread(inputimage)
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x,', ',y)
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = str(x) + ', ' + str(y)
            cv2.putText(img, strXY, (x,y), font, .4, (255,255,0), 2)
            cv2.imshow('image', img)
        if event == cv2.EVENT_RBUTTONDOWN:
            blue = img[y,x,0]
            green = img[y,x,1]
            red = img[y,x,2]
            font = cv2.FONT_HERSHEY_SIMPLEX
            strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
            cv2.putText(img, strBGR, (x,y), font, .4, (0,255,255), 2)
            cv2.imshow('image', img)
        if event == cv2.EVENT_MOUSEMOVE:
            blue = img[y,x,0]
            green = img[y,x,1]
            red = img[y,x,2]
            font = cv2.FONT_HERSHEY_SIMPLEX
            strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
            print(strBGR)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
