library(ggplot2)

#naive bubble sort average
avgNBubble=(datosImagen2$V2+datosImagen2$V2)/2
#improved bubble sort average
avgIBubble=(datosImagen2$V3+datosImagen2$V3)/2  
#Insertion sort average
avgInsertion=(datosImagen2$V4+datosImagen2$V4)/2  

df <- data.frame(avgNBubble,avgIBubble,avgInsertion)