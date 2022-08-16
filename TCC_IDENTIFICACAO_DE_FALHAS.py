from deslab import *
syms('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 f1 f2 f3 f4 f5 a b c d e f g h i j k l m n o p q r s t w')
table=[(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),
       (11,'11'),(12,'12'),(13,'13'),(14,'14'),(15,'15'),(16,'16'),(17,'17'),(18,'18'),(19,'19'),(20,'20'),
       (21,'21'),(22,'22'),(23,'23'),(24,'24'),(25,'25'),(26,'26'),(27,'27'),(28,'28'),(29,'29'),(30,'30'),
       (31,'31'),(32,'32'),(33,'33'),(34,'34'),(35,'35'),(36,'36'),(37,'37'),(38,'38'),(39,'39'),(40,'40'),
       (a,'a'),(b,'b'),(c,'c'),(d,'d'),(e,'e'),(f,'f'),(g,'g'),(h,'h'),(i,'i'),
       (j,'j'),(k,'k'),(l,'l'),(m,'m'),(n,'n'),(o,'o'),(p,'p'),(q,'q'),(r,'r'),(s,'s'),(t,'t'),(w,'w'),
       (f1,'f1'),(f2,'f2'),(f3,'f3'),(f4,'f4'),(f5,'f5')]


################################################################################

#Abordagem 1 - Autômato completo com todos os estados de falhas considerando as falhas como uma só

#Definindo o autômato
X=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
Sigma=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,w]
X0=[0]
Xm=[1]
obs=[a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
T=[
    #Normal
    (0,s,1),(1,a,2),(2,b,3),(3,c,4),(4,d,5),(5,g,6),(6,h,7),(7,i,8),(8,j,9),
    (9,k,10),(10,l,11),(11,m,12),(12,n,1),(4,e,13),(13,o,14),(14,h,15),(15,i,16),
    (16,j,17),(17,p,18),(18,q,19),(19,r,20),(20,t,1),

    #Falha f1
    (4,f,21),(21,e,13),

    #Falha f2
    (4,f,24),(24,j,25),(25,w,25),

    #Falha f3
    (4,f,22),(22,j,23),(23,w,23),

    #Falha f4
    (4,f,26),(26,j,27),(27,w,27),

    #Falha f5
    (2,f,28),(28,d,29),(29,j,31),(31,w,31),(28,e,30),(30,j,31)    
    ]


G=fsa(X,Sigma,T,X0,Xm,table,Sigobs=obs,name='$G$')
#draw(G,'figure')

print('Abordagem 1 - Modelo considerando todas as falhas como uma só (f), é diagnosticável?')

#Definindo o diagnosticador
Gd=diagnoser(G,f,'GD')
Gl=diagnoser(G,f,'GL')
#draw(Gd,'figure')
Gscc=Gd//Gl
Gscc.setgraphic(style='verifier')
#draw(Gscc,'figure')
#draw(GL,'figure')
print('Falha f - ',is_diagnosable(G,'f',obs,'Gscc'))

################################################################################
################################################################################

#Abordagem 2 - Autômato completo com todos os estados de falhas separando as falhas

#Definindo o autômato
X1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
Sigma1=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,w,f1,f2,f3,f4,f5]
X01=[0]
Xm1=[1]
obs1=[a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
T1=[
    #Normal
    (0,s,1),(1,a,2),(2,b,3),(3,c,4),(4,d,5),(5,g,6),(6,h,7),(7,i,8),(8,j,9),
    (9,k,10),(10,l,11),(11,m,12),(12,n,1),(4,e,13),(13,o,14),(14,h,15),(15,i,16),
    (16,j,17),(17,p,18),(18,q,19),(19,r,20),(20,t,1),

    #Falha f1
    (4,f1,21),(21,e,13),

    #Falha f2
    (4,f2,24),(24,j,25),(25,w,25),

    #Falha f3
    (4,f3,22),(22,j,23),(23,w,23),

    #Falha f4
    (4,f4,26),(26,j,27),(27,w,27),

    #Falha f5
    (2,f5,28),(28,d,29),(29,j,31),(31,w,31),(28,e,30),(30,j,31)
    ]

G1=fsa(X1,Sigma1,T1,X01,Xm1,table,Sigobs=obs1,name='$G1$')
#draw(G1,'figure')


print()
print('Abordagem 2 - Modelo considerando falhas distintas utilizando um diagnosticador para cada falha, é diagnosticável?')

#Definindo os diagnosticadores

#Falha 1
Gd1=diagnoser(G1,f1,'GD')
Gl1=diagnoser(G1,f1,'GL')
#draw(Gd1,'figure')
Gscc1=Gd1//Gl1
Gscc1.setgraphic(style='verifier')
#draw(Gscc1,'figure')
#draw(Gd1,'figure')
print('Falha 1 - ',is_diagnosable(G1,'f1',obs1,'Gscc'))

#Falha 2
Gd2=diagnoser(G1,f2,'GD')
Gl2=diagnoser(G1,f2,'GL')
Gscc2=Gd2//Gl2
Gscc2.setgraphic(style='verifier')
#draw(Gscc2,'figure')
#draw(Gd2,'figure')
print('Falha 2 - ',is_diagnosable(G1,'f2',obs1,'Gscc'))

#Falha 3
Gd3=diagnoser(G1,f3,'GD')
Gl3=diagnoser(G1,f3,'GL')
Gscc3=Gd3//Gl3
Gscc3.setgraphic(style='verifier')
#draw(Gscc3,'figurecolor')
#draw(Gd3,'figure')
print('Falha 3 - ',is_diagnosable(G1,'f3',obs1,'Gscc'))

#Falha 4
Gd4=diagnoser(G1,f4,'GD')
Gl4=diagnoser(G1,f4,'GL')
Gscc4=Gd4//Gl4
Gscc4.setgraphic(style='verifier')
#draw(Gscc4,'figure')
#draw(Gd4,'figure')
print('Falha 4 - ',is_diagnosable(G1,'f4',obs1,'Gscc'))

#Falha 5
Gd5=diagnoser(G1,f5,'GD')
Gl5=diagnoser(G1,f5,'GL')
Gscc5=Gd5//Gl5
Gscc5.setgraphic(style='verifier')
#draw(Gscc5,'figure')
#draw(Gd5,'figure')
print('Falha 5 - ',is_diagnosable(G1,'f5',obs1,'Gscc'))


################################################################################
################################################################################

#Abordagem 3 - Autômato com uma falha por vez

#Definindo o autômato - Falha 1
Xf1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
Sigmaf1=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,w,f1]
X0f1=[0]
Xmf1=[1]
obsf1=[a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
Tf1=[
    #Normal
    (0,s,1),(1,a,2),(2,b,3),(3,c,4),(4,d,5),(5,g,6),(6,h,7),(7,i,8),(8,j,9),
    (9,k,10),(10,l,11),(11,m,12),(12,n,1),(4,e,13),(13,o,14),(14,h,15),(15,i,16),
    (16,j,17),(17,p,18),(18,q,19),(19,r,20),(20,t,1),

    #Falha f1
    (4,f1,21),(21,e,13)]

Gf1=fsa(Xf1,Sigmaf1,Tf1,X0f1,Xmf1,table,Sigobs=obsf1,name='$G_f1$')
#draw(Gf1,'figure')


print()
print('Abordagem 3 - Modelo considerando falhas distintas em autômatos separados, utilizando um diagnosticador para cada falha, é diagnosticável?')

#Definindo o diagnosticador - Falha 1
Gdf1=diagnoser(Gf1,f1,'GD')
Glf1=diagnoser(Gf1,f1,'GL')
Gsccf1=Gdf1//Glf1
Gsccf1.setgraphic(style='verifier')
#draw(Gsccf1,'figure')
#draw(Gdf1,'figure')
print('Falha 1 - ',is_diagnosable(Gf1,'f1',obsf1,'Gscc'))

################################################################################

#Definindo o autômato - Falha 2
Xf2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,24,25]
Sigmaf2=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,w,f2]
X0f2=[0]
Xmf2=[1]
obsf2=[a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
Tf2=[
    #Normal
    (0,s,1),(1,a,2),(2,b,3),(3,c,4),(4,d,5),(5,g,6),(6,h,7),(7,i,8),(8,j,9),
    (9,k,10),(10,l,11),(11,m,12),(12,n,1),(4,e,13),(13,o,14),(14,h,15),(15,i,16),
    (16,j,17),(17,p,18),(18,q,19),(19,r,20),(20,t,1),

    #Falha f2
    (4,f2,24),(24,j,25),(25,w,25) 
    ]


Gf2=fsa(Xf2,Sigmaf2,Tf2,X0f2,Xmf2,table,Sigobs=obsf2,name='$G_f2$')
draw(Gf2,'figure')

#Definindo o diagnosticador - Falha 2
Gdf2=diagnoser(Gf2,f2,'GD')
Glf2=diagnoser(Gf2,f2,'GL')
Gsccf2=Gdf2//Glf2
Gsccf2.setgraphic(style='verifier')
#draw(Gsccf2,'figure')
#draw(Gdf2,'figure')
print('Falha 2 - ',is_diagnosable(Gf2,'f2',obsf2,'Gscc'))

################################################################################

#Definindo o autômato - Falha 3
Xf3=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23]
Sigmaf3=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,w,f3]
X0f3=[0]
Xmf3=[1]
obsf3=[a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
Tf3=[
    #Normal
    (0,s,1),(1,a,2),(2,b,3),(3,c,4),(4,d,5),(5,g,6),(6,h,7),(7,i,8),(8,j,9),
    (9,k,10),(10,l,11),(11,m,12),(12,n,1),(4,e,13),(13,o,14),(14,h,15),(15,i,16),
    (16,j,17),(17,p,18),(18,q,19),(19,r,20),(20,t,1),

    #Falha f3
    (4,f3,22),(22,j,23),(23,w,23)    
    ]


Gf3=fsa(Xf3,Sigmaf3,Tf3,X0f3,Xmf3,table,Sigobs=obsf3,name='$G_f3$')
draw(Gf3,'figure')

#Definindo o diagnosticador - Falha 3
Gdf3=diagnoser(Gf3,f3,'GD')
Glf3=diagnoser(Gf3,f3,'GL')
Gsccf3=Gdf3//Glf3
Gsccf3.setgraphic(style='verifier')
#draw(Gsccf3,'figure')
#draw(Gdf3,'figure')
print('Falha 3 - ',is_diagnosable(Gf3,'f3',obsf3,'Gscc'))

################################################################################

#Definindo o autômato - Falha 4
Xf4=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,26,27]
Sigmaf4=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,w,f4]
X0f4=[0]
Xmf4=[1]
obsf4=[a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
Tf4=[
    #Normal
    (0,s,1),(1,a,2),(2,b,3),(3,c,4),(4,d,5),(5,g,6),(6,h,7),(7,i,8),(8,j,9),
    (9,k,10),(10,l,11),(11,m,12),(12,n,1),(4,e,13),(13,o,14),(14,h,15),(15,i,16),
    (16,j,17),(17,p,18),(18,q,19),(19,r,20),(20,t,1),

    #Falha f4
    (4,f4,26),(26,j,27),(27,w,27)
    ]


Gf4=fsa(Xf4,Sigmaf4,Tf4,X0f4,Xmf4,table,Sigobs=obsf4,name='$G_f4$')
draw(Gf4,'figure')

#Definindo o diagnosticador - Falha 4
Gdf4=diagnoser(Gf4,f4,'GD')
Glf4=diagnoser(Gf4,f4,'GL')
Gsccf4=Gdf4//Glf4
Gsccf4.setgraphic(style='verifier')
#draw(Gsccf4,'figure')
#draw(Gdf4,'figure')
print('Falha 4 - ',is_diagnosable(Gf4,'f4',obsf4,'Gscc'))

################################################################################

#Definindo o autômato - Falha 5
Xf5=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,28,29,30,31]
Sigmaf5=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,w,f5]
X0f5=[0]
Xmf5=[1]
obsf5=[a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
Tf5=[
    #Normal
    (0,s,1),(1,a,2),(2,b,3),(3,c,4),(4,d,5),(5,g,6),(6,h,7),(7,i,8),(8,j,9),
    (9,k,10),(10,l,11),(11,m,12),(12,n,1),(4,e,13),(13,o,14),(14,h,15),(15,i,16),
    (16,j,17),(17,p,18),(18,q,19),(19,r,20),(20,t,1),

    #Falha f5
    (2,f5,28),(28,d,29),(29,j,31),(31,w,31),(28,e,30),(30,j,31)
    ]

Gf5=fsa(Xf5,Sigmaf5,Tf5,X0f5,Xmf5,table,Sigobs=obsf5,name='$G_f5$')
draw(Gf5,'figure')

#Definindo o diagnosticador - Falha 5
Gdf5=diagnoser(Gf5,f5,'GD')
Glf5=diagnoser(Gf5,f5,'GL')
Gsccf5=Gdf5//Glf5
Gsccf5.setgraphic(style='verifier')
#draw(Gsccf5,'figure')
#draw(Gdf5,'figure')
print('Falha 5 - ',is_diagnosable(Gf5,'f5',obsf5,'Gscc'))


################################################################################




