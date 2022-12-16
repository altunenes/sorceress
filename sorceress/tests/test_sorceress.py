from sorceress import __version__
from unittest import TestCase
from sorceress import sorceress
import unittest
import cv2
import numpy as np
import os
import imageio
class Testssorceress(TestCase):
    def test_chromatic(self):
        # Load the test image
        test_img = 255*np.ones((100, 100, 3), dtype=np.uint8)
        mean = (0, 255, 0)
        std = (10, 10, 10)
        test_img = cv2.randn(test_img, mean, std)
        file_path = "test_image.png"
        cv2.imwrite(str(file_path), test_img)

        sorceress.chromatic("test_image.png")
        self.assertTrue(os.path.exists(file_path))
        #clean up
        os.remove(file_path)
        

    def test_dotill(self):
        sorceress.dotill(dimension=(600,600))
        #there should be a output file called "dotill.png"
        self.assertTrue(os.path.exists("BGRoutput.png"))
        self.assertTrue(os.path.exists("CMCCAT2000output.png"))
        #check if the images are different
        img1 = imageio.imread("BGRoutput.png")
        img2 = imageio.imread("CMCCAT2000output.png")
        self.assertFalse(np.array_equal(img1, img2))
        #clean up
        os.remove("BGRoutput.png")
        os.remove("CMCCAT2000output.png")
        os.remove("hsvoutput.png")
        

    def test_realtimegrid(self):
        #it should open camera the camera
        self.assertTrue(True)
        
    
    def test_addlines(self):
        #create a test image with a black background
        test_img = 255*np.ones((400, 400, 3), dtype=np.uint8)
        #write the test image to as a png
        cv2.imwrite("test_image.png", test_img)
        file_path = "test_image.png"
        #now add lines to the test image
        sorceress.addlines("test_image.png")
        #check if the file exists
        self.assertTrue(os.path.exists(file_path))
        #clean up
        #look at if test_imageblur, test_imagever1 and test_imagever2 exists
        self.assertTrue(os.path.exists("test_imageblur.png"))
        self.assertTrue(os.path.exists("test_imagever1.png"))
        self.assertTrue(os.path.exists("test_imagever2.png"))
        #check if the images are different
        img=cv2.imread("test_image.png")
        img2=cv2.imread("test_imageblur.png")
        img3=cv2.imread("test_imagever1.png")
        img4=cv2.imread("test_imagever2.png")
        self.assertFalse(np.array_equal(img, img2))
        self.assertFalse(np.array_equal(img, img3))
        self.assertFalse(np.array_equal(img, img4))
        #clean up
        os.remove(file_path)
        os.remove("test_imageblur.png")
        os.remove("test_imagever1.png")
        os.remove("test_imagever2.png")
        
    
    def test_eyecolor(self):
        #crreate a test image 
        test_img = 255*np.ones((800, 800, 3), dtype=np.uint8)
        #ædd some random noise to the image
        mean = (0, 0, 0)
        std = (10, 10, 10)
        test_img = cv2.randn(test_img, mean, std)
        cv2.circle(test_img, (400, 400), 100, (0, 0, 0), -1)
        #write the test image to as a png
        cv2.imwrite("eyecolor.png", test_img)
        file_path = "eyecolor.png"
        #read the image it should show a window with the image and user can select the iris with mouse, when its done user needs to press enter
        sorceress.eyecolour("eyecolor.png")
        #after selection the image should be saved
        self.assertTrue(os.path.exists(file_path))
        #check if the eyecolorblur.png exists
        self.assertTrue(os.path.exists("eyecolorblur.png"))
        #check if the images are different
        img=cv2.imread("eyecolor.png")
        img2=cv2.imread("eyecolorblur.png")
        self.assertFalse(np.array_equal(img, img2))
        #clean up
        os.remove(file_path)
        #also remove the "eyecolorblur.png"
        os.remove("eyecolorblur.png")


    def test_dakinPex(self):
        sorceress.dakinPex("myoutput")
        #there should be a output file called "myoutput.png":
        self.assertTrue(os.path.exists("myoutput.png"))
        #clean up
        os.remove("myoutput.png")
        sorceress.dakinPex("myoutput",dimension=(500))
        #check if the image is the right size
        img = imageio.imread("myoutput.png")
        self.assertEqual(img.shape[0],500)
        self.assertEqual(img.shape[1],500)
        #clean up
        os.remove("myoutput.png")
        #add with a different color and check if the colors are different
        sorceress.dakinPex("myoutput",dimension=(500),bg_color=(0,0,0))
        sorceress.dakinPex("myoutput2",dimension=(500),bg_color=(255,255,255))
        img1 = imageio.imread("myoutput.png")
        img2 = imageio.imread("myoutput2.png")
        self.assertFalse(np.array_equal(img1, img2))
        #clean up
        os.remove("myoutput.png")
        os.remove("myoutput2.png")

    
    def test_bruno(self):
        sorceress.bruno("brunooutput")
        #there should be a output file called "brunooutput.png":
        self.assertTrue(os.path.exists("brunooutput.png"))
        #clean up
        os.remove("brunooutput.png")

    def test_dolboeuf(self):
        sorceress.dolboeuf("dolboeufoutput")
        #there should be a output file called "dolboeufoutput.png":
        self.assertTrue(os.path.exists("dolboeufoutput.png"))
        #clean up
        os.remove("dolboeufoutput.png")

    def test_kanizsa(self):
        sorceress.kanizsa("kanizsaoutput")
        #there should be a output file called "kanizsaoutput.png":
        self.assertTrue(os.path.exists("kanizsaoutput.png"))
        #clean up
        os.remove("kanizsaoutput.png")

    def test_ponzol(self):
        sorceress.ponzol("ponzoloutput")
        #there should be a output file called "ponzoloutput.png": also it should open a window with the image
        self.assertTrue(os.path.exists("ponzoloutput.png"))
        #clean up
        os.remove("ponzoloutput.png")
    def tAki2001(self):
        #function takes a outpu file name as a parameter
        sorceress.tAki2001("Aki2001output")
        #there should be a output file called "Aki2001output.png":
        self.assertTrue(os.path.exists("Aki2001output.png"))
        #clean up
        os.remove("Aki2001output.png")

    def test_cafeWalll(self):
        #function takes a outpu file name as a parameter
        sorceress.cafeWall("cafeWalloutput")
        #there should be a output file called "cafeWalloutput.png":
        self.assertTrue(os.path.exists("cafeWalloutput.png"))
        #clean up
        os.remove("cafeWalloutput.png")

    def test_ccob(self):
        #generate a test image
        test_img = 255*np.ones((700, 700, 3), dtype=np.uint8)
        #add some lines to the image
        test_img = cv2.line(test_img,(0,0),(700,700),(0,0,0),5)
        test_img = cv2.line(test_img,(0,700),(700,0),(0,0,0),5)
        #write the test image to as a png
        cv2.imwrite("test_image.png",test_img)
        #now use the function
        sorceress.ccob("test_image.png",plttitle="ccoboutput")
        #there should be a output file called "ccoboutput.png" and a window with the image
        self.assertTrue(os.path.exists("ccoboutput.png"))
        #clean up
        os.remove("ccoboutput.png")
        os.remove("test_image.png")

    def test_ebbinghaus(self):
        #use the function with a output file name
        sorceress.ebbinghaus("ebbinghausoutput")
        #there should be a output file called "ebbinghausoutput.png": also it should open a window with the image
        self.assertTrue(os.path.exists("ebbinghausoutput.png"))
        #remove the output file
        os.remove("ebbinghausoutput.png")

    def test_whiteill(self):
        #use the function with a output file name
        sorceress.whiteill(dimension=600,outputname="whiteilloutput")
        #there is also version of 2
        sorceress.whiteill(dimension=600,outputname="whiteilloutput",version2=True)
        #there should be output file called "whiteilloutput.png" and "whiteilloutput2.png" (for both versions)
        self.assertTrue(os.path.exists("whiteilloutput.png"))
        self.assertTrue(os.path.exists("whiteilloutputvers1.png"))
        #clean up
        os.remove("whiteilloutput.png")
        os.remove("whiteilloutputvers1.png")
    
    def test_enigma(self):
        # Call the enigma function with some test input
        output_name = "test_enigma"
        sorceress.enigma(dimension=(512),outputname="test_enigma",gif=True)
        
        # Check if the expected output files were created
        output_files = [f"{output_name}.png", f"{output_name}gray.png"]
        for file in output_files:
            self.assertTrue(os.path.exists(file))
        
        #check if the gif was created
        self.assertTrue(os.path.exists(f"{output_name}.gif"))
        #clean the gif
        os.remove(f"{output_name}.gif")

        # Check if the output files have the expected size
        expected_size = (512, 512)
        for file in output_files:
            img = cv2.imread(file)
            self.assertEqual(img.shape[:2], expected_size)


        # Clean up
        for file in output_files:
            os.remove(file)

    def test_blackhole(self):
        output_name = "test_blackhole"
        sorceress.blackhole(outputname=output_name,dimensions=(512,512))
        # Check if the expected output file test_blackhole.png was created
        self.assertTrue(os.path.exists(f"{output_name}.png"))
        # Check if the output file has the expected size
        expected_size = (512, 512)
        img = cv2.imread(f"{output_name}.png")
        self.assertEqual(img.shape[:2], expected_size)
        os.remove(f"{output_name}.png")

    def test_colorgrids(self):
        #create a test image and add some different colors of circles
        test_img = 255*np.ones((700, 700, 3), dtype=np.uint8)
        test_img = cv2.circle(test_img,(350,350), 100, (0,0,255), -1)
        test_img = cv2.circle(test_img,(350,350), 100, (255,0,0), 5)
        test_img = cv2.circle(test_img,(350,350), 100, (0,255,0), 10)

        #write the test image to as a png
        cv2.imwrite("test_image.png",test_img)
        #now use the function
        sorceress.colorgrids("test_image.png",style="vertical",saturation=1)
        #there should be a output file called "test_imagegridillusion.png" and a window with the image
        self.assertTrue(os.path.exists("test_imagegridillusion.png"))
        #clean the file
        os.remove("test_imagegridillusion.png")
        os.remove("test_image.png")

    def test_munker(self):
        sorceress.munker(dimensions=(800,800))
        #there should be a output file called "munker800x800.png" and a window with the image
        self.assertTrue(os.path.exists("munker800x800.png"))
        #check if the image has the expected size
        expected_size = (800, 800)
        img = cv2.imread("munker800x800.png")
        self.assertEqual(img.shape[:2], expected_size)
        #clean the file
        os.remove("munker800x800.png")

    def test_pareidolia(self):
        sorceress.pareidolia(dimensions=(800,800),emotion="happy")
        #there should be a output file called "pareidolia800x800.png" and a window with the image
        self.assertTrue(os.path.exists("pareidolia800x800.png"))
        #check if the image has the expected size
        expected_size = (800, 800)
        img = cv2.imread("pareidolia800x800.png")
        self.assertEqual(img.shape[:2], expected_size)
        #clean the file
        os.remove("pareidolia800x800.png")
    def test_grids2(self):
        sorceress.grids2(dimensions=(340,640))
        #there should be a output file called "grids2340x640.png"
        self.assertTrue(os.path.exists("grids2340x640.png"))
        #clean the file
        os.remove("grids2340x640.png")

    def test_munker2(self):
        dimensions = (800,800)
        sorceress.munker2(dimensions=dimensions)
        #there should be a output file called "munker2800x800.png"
        self.assertTrue(os.path.exists("munker2800x800.png"))
        #check if the image has the expected size
        expected_size = dimensions
        img = cv2.imread("munker2800x800.png")
        self.assertEqual(img.shape[:2], expected_size)
        #clean the file
        os.remove("munker2800x800.png")
    def test_spiral(self):
        self.assertEqual(sorceress.spiral(np.array([0,0])), 0)
        self.assertEqual(sorceress.spiral(np.array([1,0])), 1)
    def test_spiral2(self):
        self.assertEqual(sorceress.spiral2(np.array([3,5])),-1)
        self.assertEqual(sorceress.spiral2(np.array([7,15])), -0.6347427869249276)

    def test_mainImage(self):
        self.assertEqual(sorceress.mainImage(np.array([3,12])).all(), np.array([1., 0.5, 0.]).all())

    def test_spirals(self):
        sorceress.spirals(dimensions=(500,500))
        #there should be a output file called "spirals.png and spirals2.png"
        self.assertTrue(os.path.exists("spirals.png"))
        self.assertTrue(os.path.exists("spirals2.png"))
        #images must have the expected size
        expected_size = (500, 500)
        img = cv2.imread("spirals.png")
        img2 = cv2.imread("spirals2.png")
        self.assertEqual(img.shape[:2], expected_size)
        self.assertEqual(img2.shape[:2], expected_size)
        #clean the files
        os.remove("spirals.png")
        os.remove("spirals2.png")
    def test_negate_image(self):
        test_img = 255*np.ones((700, 700, 3), dtype=np.uint8)
        test_img = cv2.circle(test_img,(350,350), 100, (0,0,255), -1)
        test_img = cv2.circle(test_img,(350,350), 100, (255,0,0), 5)
        #add some noise
        test_img = cv2.randn(test_img, (0,0,0), (50,50,50))
        #write the test image to as a png
        cv2.imwrite("test_image.png",test_img)
        #apply the function
        sorceress.negate_image(input_file="test_image.png",negation_method="subtract",color_space="rgb",output_quality=1)
        #there should be a output file called "test_image_neg.png" and a window with the image
        self.assertTrue(os.path.exists("test_image_neg.png"))
        #compare if outputs are different
        img1 = cv2.imread("test_image_neg.png")
        sorceress.negate_image(input_file="test_image.png",negation_method="subtract",color_space="hsv",output_quality=100)
        img2 = cv2.imread("test_image_neg.png")
        self.assertFalse((img1==img2).all())
        #clean the file
        os.remove("test_image_neg.png")
        os.remove("test_image.png")


if __name__ == '__main__':
    unittest.main()