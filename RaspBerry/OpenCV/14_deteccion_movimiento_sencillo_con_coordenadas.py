import cv2
import numpy as np  #Sirve para trabajar con matrices, vectores, etc...
                    #y asignamos un alias 'np'
    
webcam_id = 0       #Seleccionamos el id de la cámara
cap = cv2.VideoCapture(webcam_id) #creamos el objeto 'cap'
cap.set(3,520) #pixeles en horizontal de la ventana
cap.set(4,240) #pixeles en vertical

ret,prev=cap.read()
prevG=cv2.cvtColor(prev,cv2.COLOR_RGB2GRAY)
kernel=np.ones((5,5),np.uint8)
font=cv2.FONT_HERSHEY_SIMPLEX
PrevCen=np.array([0,0])

while(cap.isOpened()):
    # Capture frame-by-frame
    ret,next1 = cap.read() #si se estan recibiendo imagenes 'ret'=True.
    if ret == True:
        nextG=cv2.cvtColor(next1,cv2.COLOR_RGB2GRAY)
        flow=np.array(abs(np.array(nextG,np.float32)-np.array(prevG,np.float32)),np.uint8)
        
        #mostramos las imagenes
        cv2.imshow('flow',flow)
        rang=cv2.inRange(flow,20,255)
        cv2.imshow('rang',rang)
        opening=cv2.morphologyEx(rang,cv2.MORPH_OPEN,kernel)
        closing=cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel)
        cv2.imshow('closing',closing)

        contours,_=cv2.findContours(closing,1,2) #detecta los contornos

        M=[0,0]
        n=0
        for cnt in contours:            
            x,y,w,h=cv2.boundingRect(cnt) #extrae los valores del punto inicial(x,y) 
                                          #y el ancho 'w' y alto'h'del rectángulo que va a dibujar
            if w>15 and h>15 and w<200 and h<200: #aplicamos un filtro más y eliminamos ruido
                                                  #si el ancho y alto están entre 15 y 200
                #hallamos el centro de todos los contornos detectados
                M[0]+=x+float(w)/2  
                M[1]+=y+float(h)/2
                n+=1
        
        if M[0]!=0 and M[1]!=0:            
            M=np.array(M)
            NewCen=PrevCen+0.9*(M-PrevCen)
            cntX=int(NewCen[0]/n)
            cntY=int(NewCen[1]/n)
            cv2.circle(next1,(cntX,cntY),5,(130,50,200),-1)
            cv2.putText(next1,str(cntX)+','+str(cntY),(cntX+10,cntY+10),font,1,(130,50,200),1)
            PrevCen=NewCen
            
        prevG=nextG
        cv2.imshow('next',next1)
        
        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
