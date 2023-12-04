import os
import subprocess
import sys
os.environ['PATH'] += os.pathsep + os.path.join(os.path.expanduser("~"), ".local", "bin")

# create a list of names
names = [['Lección 1. Introducción a la inteligencia artificial.md','http://kunusoft.com/slides/ia1/ia101_intro/']
        ,['Lección 2. Agentes inteligentes y búsquedas.md','http://kunusoft.com/slides/ia1/ia102_agentes']
        ,['Lección 3. Otras búsquedas no informadas.md','http://kunusoft.com/slides/ia1/ia103_otras/']
        ,['Lección 4. Búsquedas informadas.md','http://kunusoft.com/slides/ia1/ia104_informadas/']
        ,['Lección 5. Búsquedas por adversario.md','http://kunusoft.com/slides/ia1/ia105_adversario/']
        ,['Lección 6. Algoritmos genéticos.md','http://kunusoft.com/slides/ia1/ia106_geneticos/']
        ,['Lección 7. Machine Learning I.md','http://kunusoft.com/slides/ia1/ia107_ml1/']
        ,['Lección 8. Machine Learning II.md','http://kunusoft.com/slides/ia1/ia108_ml2/']
        ,['Lección 9. Machine Learning III.md','http://kunusoft.com/slides/ia1/ia109_ml3/']
        ,['Lección 10. Machine Learning IV.md','http://kunusoft.com/slides/ia1/ia110_ml4/']]

# now we will open a file for each name in the list
for name in names:
    file = open(name[0], "w")
    for i in range(200):
        if i<10:
            file.write("![]("+name[1]+"Diapositiva0"+str(i)+".JPG)" + os.linesep)
        elif i>99:
            if i<110:
                file.write("![]("+name[1]+"Diapositiva"+str(i)+".JPG)" + os.linesep)
            else:
                file.write("![]("+name[1]+"Diapositiva"+str(i)+".JPG)" + os.linesep)
        else:
            file.write("![]("+name[1]+"Diapositiva"+str(i)+".JPG)" + os.linesep)

    file.close()
