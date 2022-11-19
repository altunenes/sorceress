#A collection of functions for the sorceress module that is written in python language

###############################  version: 1.8.1     ###############################
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

def chromatic(img,circle=True, method="CMCCAT2000", gif=True, Gifduration=7):
    """
    This function is used to convert an image to chromatic image.
    :param img: input image with extension ("test.png")
    :param circle: a center fixation
    :param method: "CMCCAT2000" or "Von Kries"
    :param gif: export as gif
    :param Gifduration: duration of the gif (in seconds)
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

def addlines(img,linecolour1=(0,255,0),linecolour2=(0,255,255),linecolour3=(255,0,0),alphablending=False):
    """"
    Adds lines to an image.
    Arguments:
    img: input image
    linecolour1: first line colour
    linecolour2: second line colour
    linecolour3: third line colour
    alphablending: if True, line colors are much more stable against the luminance change in the background image.
    :return
    """
    outputname = os.path.basename(img).split(".")[0]
    rect = cv2.imread(img)
    h,w,c=rect.shape

    if alphablending == False:
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

        print("DONE! grids have been added to your image check your working directory:",os.getcwd())
    else:
        rect = cv2.cvtColor(rect, cv2.COLOR_BGR2BGRA)
        h, w, c = rect.shape
        img2 = rect.copy()

        for i in range(0, w, 3):
            cv2.line(img2, (i, 0), (i, w), linecolour1, 12)
            cv2.line(img2, (i + 1, 0), (i + 1, (w)), linecolour2, 12)
            cv2.line(img2, (i + 2, 0), (i + 2, (w)), linecolour3, 12)
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
    #if user enter luminance and saturation values more than 1 raise error and exit
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

def dakinPex(outputname,dimension=800):
    """
    Creates an optical illusion from the Dakin and Bex, 2003 paper.
    :param outputname: output name
    :param dimension: dimension of the image
    :return:
    """


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

def dolboeuf(outputname,circleColor=(0,0,255),kill=False):
    """
    Creates an optical illusion from the Joseph Remi Leopold Delbœuf (1865).
    :param outputname: output name
    :param circleColor: color of the circle
    :param kill: if true, the illusion will be destroyed by the lines
    :return:
    """
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
    cv2.imshow("img", img)
    cv2.waitKey(0)
    print("DONE! image has been added to your working directory:")
    print("Your working directory: ", os.getcwd())

def ponzol(outputname,kill=False,line1=(255,0,0),line2=(255,0,0),rectangle1=(0,0,255),rectangle2=(0,0,255)):
    """
    Creates an optical illusion from Ponzo, 1912.
    :param outputname: output name
    :param kill: if true, the illusion will be destroyed by the lines
    :param line1: color of the first line
    :param line2: color of the second line
    :param rectangle1: color of the first rectangle
    :param rectangle2: color of the second rectangle
    :return:
    """
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
    cv2.imshow("img", img)
    cv2.waitKey(0)


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
    cv2.imshow("img", img)
    cv2.waitKey(0)

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

def ebbinghaus(output, bgcolor=(255, 255, 255), lcradius=22, rcradius=22, lcradius2=25, rcradius2=45,randcirclecolors=True):
    """
    Creates ebbinghaus illision .
    :param output: output name
    :param bgcolor: background color
    :param lcradius: left center circle radius
    :param rcradius:  right center circle radius
    :param lcradius2:  left circles radius
    :param rcradius2:  right circles radius
    :param randcirclecolors: circles  have random colors (recommended)
    :return:
    """
    img = 255 * np.ones((400, 800, 3), np.uint8)
    img[:, :, :] = bgcolor
    lcradius = int(lcradius)
    rcradius = int(rcradius)
    lcradius2 = int(lcradius2)
    rcradius2 = int(rcradius2)
    if randcirclecolors==False:
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
    else:
        cv2.circle(img, (180, 180), lcradius, (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), -1)

        for i in range(0, 8):
            center = (int(180 + 65 * np.sin(i * np.pi / 4)), int(180 + 65 * np.cos(i * np.pi / 4)))
            b = np.random.randint(0, 255)
            g = np.random.randint(0, 255)
            r = np.random.randint(0, 255)
            cv2.circle(img, center, lcradius2, (b, g, r), -1)

        cv2.circle(img, (620, 180), rcradius,(np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), -1)
        for i in range(0, 8):
            center = (int(620 + 130 * np.sin(i * np.pi / 4)), int(180 + 130 * np.cos(i * np.pi / 4)))
            b = np.random.randint(0, 255)
            g = np.random.randint(0, 255)
            r = np.random.randint(0, 255)
            cv2.circle(img, center, rcradius2, (b, g, r), -1)
        cv2.imshow("img", img)
        cv2.imwrite(f'{output}.png', img)
        print(f"DONE! image f'{output} has been added to your working directory:")
        print("Your working directory: ", os.getcwd())
        cv2.waitKey(0)

def whiteill(dimension=300, version2=False, rect1=(255, 255, 255), rect2=(0, 0, 0), bgrec1=(128, 128, 128),
             bgrec2=(128, 128, 128), bg1=(0, 0, 0), bg2=(255, 255, 255), outputname="output"):
    """
    Optiacal illusion that has been described by White (1979).
    :param dimension: dimension of the image
    :param version2: if True, the second version of the illusion is created
    :param rect1: color of the first rectangle
    :param rect2: color of the second rectangle
    :param bgrec1: background color of the first rectangle
    :param bgrec2: background color of the second rectangle
    :param bg1: background color of the first image
    :param bg2: background color of the second image
    :param outputname: output name

    """

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

def enigma(linecolors=(255,255,255), bgcolor=(1, 1, 1),circle1=(76, 0, 153),circle2=(102, 0, 204),
           centercircle=(0,255,255),
           outputname="enigma"):
    """
    based on the a paper from the Zeki et al (1993).
    :param linecolors: color of the lines
    :param bgcolor:  background color of the image
    :param circle1: outer circle color
    :param circle2: inner circle color
    :param centercircle: central circle color
    :param outputname: output name
    :return:
    """
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

def blackhole(outputname="blackhole",height=800, width=800, circle_size=10, circle_color=(0, 0, 0),kill=False):
    """"
    Illusorily Expanding Holes.
    height: height of the image
    width: width of the image
    circle_size: size of the circles (center ellipse is adjusted with this ratio)
    circle_color: color of the circles
    kill: if True, circles are not drawn
    """
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

    cv2.imshow("img", img)
    cv2.imwrite(f'{outputname}.png', img)
    cv2.waitKey(0)

def colorgrids(img,style="vertical",width=4,frequency=1,saturation=0):
    """
    This function applies Color assimilation Grid Illusion.
    :param img: input image
    :param style: style of mask, "vertical","horizontal","gaussian","grids"
    :param width: width of lines
    :param frequency: frequency of lines
    :param saturation: saturation of lines
    :return:
    """
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
    cv2.imwrite("gridillusion.png",final)
    print("image saved as gridillusion.png")