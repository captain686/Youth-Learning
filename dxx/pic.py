"""
图片处理
    拼接图片
    添加水印信息
"""

from PIL import Image, ImageDraw, ImageFont
import os
import config

class Pic(object):
    def allPath(self):
        self.imgpath = os.path.dirname(__file__)
        # self.imgpath = os.path.join(self.path,"img")
        return self.imgpath
    
    
    def getPic(self):
        """
        header大小 (375, 90)
        """
        basePath = self.allPath()
        imagePath = os.path.join(basePath,"img")
        tffPath = os.path.join(basePath,"tff")
        # pics = []
        header = os.path.join(imagePath,"header.png")
        png_1 = os.path.join(imagePath,"one.png")
        png_2 = os.path.join(imagePath,"two.png")
        new_1 = os.path.join(imagePath,"new1.png")
        new_2 = os.path.join(imagePath, "new2.png")
        new_3 = os.path.join(imagePath, "new3.png")
        endPath = os.path.join(imagePath,"end.png")
        info = config.info
        self.join(header, png_1, new_1, flag='vertical')
        os.remove(png_1)
        self.join(header, png_2, new_2, flag='vertical')
        os.remove(png_2)
        self.join(new_1, new_2, new_3, flag='horizontal')
        os.remove(new_1)
        os.remove(new_2)
        self.addInfo(tffPath,new_3,endPath,info)
        os.remove(new_3)
        
        
    # 拼接图片
    def join(self,png1, png2, path, flag='horizontal'):
        """
        :param png1: path
        :param png2: path
        :param flag: horizontal or vertical
        :return:
        """
        img1, img2 = Image.open(png1), Image.open(png2)
        size1, size2 = img1.size, img2.size
        
        # 横向拼接
        if flag == 'horizontal':
            joint = Image.new('RGB', (size1[0]+size2[0], size1[1]))
            loc1, loc2 = (0, 0), (size1[0], 0)
            joint.paste(img1, loc1)
            joint.paste(img2, loc2)
            joint.save(path)
        # 纵向拼接
        elif flag == 'vertical':
            joint = Image.new('RGB', (size1[0], size1[1]+size2[1]))
            loc1, loc2 = (0, 0), (0, size1[1])
            joint.paste(img1, loc1)
            joint.paste(img2, loc2)
            joint.save(path)


    # 添加水印信息
    def addInfo(self,tffPath,imgPath,savePath,info):
        img = Image.open(imgPath)
        draw = ImageDraw.Draw(img)
        myfont = ImageFont.truetype(tffPath+"/MI_LanTing_Regular.ttf", size=40)
        fillcolor = "#ff0000"
        width, height = img.size
        draw.text((width/2, height/2), info, font=myfont, fill=fillcolor)
        img.save(savePath)
        # img.show()


if __name__ == '__main__':
    Pic().getPic()