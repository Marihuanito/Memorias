import cv2
import numpy as np

title = 'Matching'
img = cv2.imread('nadal.jpg', 0) #cargamos la imagen monocromo

template = cv2.imread('pelota_nadal.png', 0) #cargamos la imagen monocromo
print('template.shape: ',template.shape) #El 'shape' no nos devuelve el nº de canales por estar
w, h = template.shape                    #la imagen en escala de grises
print('w: ',w)
print('h: ',h)



# Existen 6 métodos para match
'''
'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED'
'''
method='cv2.TM_SQDIFF'
# Apply template Matching
res = cv2.matchTemplate(img,template,eval(method)) 
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print('min_val: ',min_val)
print('max_val: ',max_val)
print('min_loc: ',min_loc)
print('max_loc: ',max_loc)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if eval(method) in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
    
print('top_left[0]: ',top_left[0])
print('top_left[1]: ',top_left[1])
bottom_right = (top_left[0] + w, top_left[1] + h)

#cv2.rectangle(img, top_left, bottom_right, 255, 4)

umbral = 0.8
loc = np.where( res >= umbral)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, top_left, bottom_right, 255, 4)

cv2.imshow(title, img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
