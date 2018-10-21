    #Données train.csv

library("FactoMineR")
library("factoextra")
data0 <- read.csv(file.choose(), quote= "\"", dec = ".", header = TRUE)
data<-data0[,c(1,2,3,5,6,7,8,10,12,12)]
head(data)
#Mettre les variables qualitatives sous forme binaire
data$Sex<-ifelse(data$Sex=="male", yes = 1, no = 0)
data$Embarked<-ifelse(data$Embarked=="S", yes = 1, no = 0)
data$Embarked.S<-data$Embarked
data$Embarked.1<-ifelse(data$Embarked.1=="C", yes = 1, no = 0)
data$Embarked.C<-data$Embarked.1
data<-data[,-c(9,10)]
head(data)
dat<-log(data+1)
head(dat)
library(VIM)
dat.kNN=kNN(dat, k=6, imp_var=FALSE)
head(dat.kNN)
head(exp(dat.kNN)-1)
dat.kNN<-exp(dat.kNN)-1
dat.kNN$Age<-round(dat.kNN$Age,digits=2)
head(dat.kNN)
is.data.frame(dat.kNN)

write.csv(dat.kNN,file='train01.csv',row.names=F)


    #Données test.csv
library("FactoMineR")
library("factoextra")
data0 <- read.csv(file.choose(), quote= "\"", dec = ".", header = TRUE)
data<-data0[,c(1,2,4,5,6,7,9,11,11)]
head(data)
#Mettre les variables qualitatives sous forme binaire
data$Sex<-ifelse(data$Sex=="male", yes = 1, no = 0)
data$Embarked<-ifelse(data$Embarked=="S", yes = 1, no = 0)
data$Embarked.S<-data$Embarked
data$Embarked.1<-ifelse(data$Embarked.1=="C", yes = 1, no = 0)
data$Embarked.C<-data$Embarked.1
data<-data[,-c(8,9)]
head(data)
dat<-log(data+1)
head(dat)
library(VIM)
dat.kNN=kNN(dat, k=6, imp_var=FALSE)
head(dat.kNN)
head(exp(dat.kNN)-1)
dat.kNN<-exp(dat.kNN)-1
dat.kNN$Age<-round(dat.kNN$Age,digits=2)
head(dat.kNN)
is.data.frame(dat.kNN)

write.csv(dat.kNN,file='test01.csv',row.names=F)



