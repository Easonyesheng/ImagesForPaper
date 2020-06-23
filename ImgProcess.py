"""
A Toolbox to perform Images process for paper-writing
Personal use only
"""

import cv2
import PIL
from PIL import Image, ImageDraw, ImageFont
import os

class PaperImages:
    '''
        Process Images for papers-writing
        $ Principle of Processing:
            . Process Images in specific folder

        * Functions:
            1. Paste Images
                .imgs_paste()
            2. Add txt on Images
                .draw_txt

    '''
    def __init__(self, SavePath, SavePrefix):
        '''Init
            Images Save Path - SavePath
            Images Save Name - SavePrefix
        '''
        self.SavePath = SavePath
        self.SavePrefix = SavePrefix

    def load_imgs_folder(self, FolderPath):
        '''Load current folder

        '''
        self.ImgFolderPath = FolderPath
    def __is_image(self, filename):
        '''judge image file
        '''
        if filename.split('.')[-1] == 'jpg' or filename.split('.')[-1] == 'png':
            return True
        else:
            return False

    def imgs_paste(self, target_w_img_nums, target_h_img_nums):
        '''Paste images to a single target image
            $ principle
                . Images named as 'i.jpg' as i in range(N)
                . Paste Images from 0.jpg to N.jpg
                . Paste left to right, up to down
            :Para:
                target image has i imgs on width
                target image has j imgs on height
            Return:
                save image in savepath as saveprefix.jpg
        '''
        # get Img List
        ImgList = []
        print('Images paste order: ')
        file_list = os.listdir(self.ImgFolderPath)
        file_list.sort(key=lambda x: x.split('.')[0])
        for filename in file_list:
            if self.__is_image(filename):
                print(filename)
                ImgList.append(os.path.join(self.ImgFolderPath,filename))
        
        if len(ImgList) != target_h_img_nums*target_w_img_nums:
            print('Image Numbers Error')
            return -1

        img = Image.open(ImgList[0])
        (w,h) = img.size
        Target = Image.new('RGB', (w*target_w_img_nums, h*target_h_img_nums))
        index = 0
        for j in range(target_h_img_nums):
            for i in range(target_w_img_nums):
                img = Image.open(ImgList[index])

                loc = (int(i%target_w_img_nums*w),int(j%target_h_img_nums*h))
                Target.paste(img,loc)
                index += 1
        
        Target.save(os.path.join(self.SavePath,self.SavePrefix+'_Paste.jpg'))


    def draw_txt(self, image_name, txt, location, color, font_size, fontpath):
        '''Draw txt on image at location
            :para:
                image name
                txt
                location - [w_loc(%), h_loc(%)] as percentage of length
               [ori]----------w--|
                |                |
                |                |
                |                h
                |----------------|
                color - black : (0,0,0)
                font_size -
                fontpath - path for font file /Download : http://www.fonts.net.cn/

            return:
                save image in savepath as saveprefix.jpg
        '''
        img = Image.open(os.path.join(self.ImgFolderPath, image_name))
        (w,h) = img.size
        w_loc = int(location[0]*w)
        h_loc = int(location[1]*h)
        draw = ImageDraw.Draw(img)
        ft = ImageFont.truetype(font=fontpath,size=font_size)
        draw.text((w_loc,h_loc), txt, font=ft ,fill=color)
        img.save(os.path.join(self.SavePath,self.SavePrefix+image_name))



if __name__ == "__main__":
    save_path = '/Users/zhangyesheng/Desktop/Research/GraduationDesign/StereoVision/ManualDataset/Res/KITTI'
    save_prefix = 'txt'
    filefolder = '/Users/zhangyesheng/Desktop/Research/GraduationDesign/StereoVision/ManualDataset/Res/KITTI'
    image_name = '5.jpg'
    fp = '/Users/zhangyesheng/Documents/GitHub/ImgProcess/font21727/AuxinDemiBold.otf'


    IP = PaperImages(save_path,save_prefix)
    IP.load_imgs_folder(filefolder)
    IP.imgs_paste(2,3)
    # IP.draw_txt(image_name, 'GT', [0.8,0.05], (255,255,255), 40, fp)
