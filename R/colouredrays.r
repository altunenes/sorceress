library(tidyverse)
grids<-function(x,y,z)
{
  ggplot(data.frame(x=c(1,1),y=c(1,1)),aes(x=x,y=y))+
    geom_hline(yintercept=seq(1,x,z),color="#89b1d1",size=1)+
    geom_vline(xintercept=seq(1,y,z),color="#89b1d1",size=1)+theme_void()+
    theme(panel.background = element_rect(fill = "#ffffff",colour = NA))+ 
geom_point(data=expand.grid(seq(1,x,z),seq(1,y,z)),aes(x=Var1,y=Var2),color="yellow",size=3) +
geom_segment(data=expand.grid(seq(1,x,z),seq(1,y,z)),
             aes(x=Var1,y=Var2,xend=Var1-z,yend=Var2-z),color="black",size=1.5)}
a<-plot(grids(100,100,10))
ggsave("grid.png",a,width=10,height=10,units="cm",dpi=300)
