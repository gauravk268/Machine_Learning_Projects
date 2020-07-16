#Using Data augmentation to increase the number of training data

# Importing necessary functions 
from keras.preprocessing.image import ImageDataGenerator,  
array_to_img, img_to_array, load_img 
   
# Initialising the ImageDataGenerator class. 
# We will pass in the augmentation parameters in the constructor. 
datagen = ImageDataGenerator( 
        rotation_range = 40, 
        shear_range = 0.2, 
        zoom_range = 0.2, 
        horizontal_flip = True, 
        brightness_range = (0.5, 1.5)) 


Path = 'D:\Practice\Git\HackerEarth-Emotion-Detection-Tom-Jerry-Cartoon\Dataset\Augmented_Image'

value = []

cols_list = ["Frame_ID", "Emotion"]
data = pd.read_csv("Copy of Train.csv", usecols=cols_list)

num_trainImage = 298
count = 298
while(num_trainImage):
    img = load_img('image.jpg')  
    x = img_to_array(img) 
    x = x.reshape((1, ) + x.shape)  
    
    i = 0
    for batch in datagen.flow(x, batch_size = 1, 
                            save_to_dir = Path,  
                            save_prefix ='frame%d' % count, save_format ='jpg'): 
        i += 1
        if i > 5:
            break

    num_trainImage -= 1