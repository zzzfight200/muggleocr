import time
import muggle_ocr
import os
import shutil


if __name__ == '__main__':
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
    SampleDir = os.getcwd()+'\\CAPTCHA'
    RenameDir = os.getcwd()+'\\Rename'
    for i in os.listdir(SampleDir):
        n = os.path.join(SampleDir, i)
        with open(n, "rb") as f:
            b = f.read()
        st = time.time()
        text = sdk.predict(image_bytes=b)
        SpendTime = time.time() - st
        # 打印验证码内容及识别时间
        print(text, SpendTime)
        # 将验证码样本复制到另一个文件夹，并以识别出的验证码内容重命名
        try:
            shutil.copyfile(n, RenameDir + '\\' + i + '.png')
            os.rename(RenameDir + '\\' + i + '.png',RenameDir + '\\' + text + '.png')
        except Exception as e:
            print(e)
            print('复制或重命名时出错，识别出的验证码内容为：',text)