import cv2
def main():
  path="C:\\Users\\hp\\OneDrive\\open cv\\misc\\4.1.03.tiff"
  img=cv2.imread(path)
  output_path="C:\\Users\\hp\\OneDrive\\open cv\\output\\4.1.03.jpg"
  cv2.namedWindow('image',img)
  cv2.imshow('image',img)
  cv2.imwrite(output_path,img)
  cv2.waitKey(0)
  cv2.destroyWindow('image')
if __name__ == "__main__":
  main()
    
