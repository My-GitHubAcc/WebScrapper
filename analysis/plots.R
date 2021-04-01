library(plotly)
library(ggplot2)
library(scales)
library(dplyr)

# Distribution des Lunettes par Gender
data_gender = data.frame(
  Gender = levels(df$Gender),
  Counts = count(df, Gender)$n
)
data_gender$fraction = data_gender$Counts / sum(data_gender$Counts)
data_gender$ymax = cumsum(data_gender$fraction)
data_gender$ymin = c(0, head(data_gender$ymax, n=-1))

data_gender$label_position = (data_gender$ymax + data_gender$ymin) / 2
data_gender$labels = paste0(
  data_gender$Gender, "\n",
  format(round(data_gender$fraction * 100, 2), nsmall = 3), 
  "%")
lunettes_gender <- ggplot(data_gender) +
  aes(ymax=ymax, ymin=ymin, xmax=5, xmin=4, fill=Gender) +
  geom_rect()+
  geom_label(x=4.5, 
             aes(y=label_position, label=labels), 
             size=6)+
  coord_polar(theta="y") +
  xlim(c(3, 5))+
  labs(x = "Gender", title = "Distribution des Lunettes par Gender") +
  theme_void() + 
  scale_fill_brewer(palette = "Set1") +
  theme(plot.title = element_text(hjust = 0.5, size = 18),
        legend.position ="none")

# Année de sortie des lunettes
annee_lunettes<- ggplot(df) +
  aes(x = year) +
  geom_histogram(bins = 30, fill = "#008ceb") +
  ggthemes::theme_hc() +
  #scale_x_discrete(limits = unique(df$year)) +
  labs(x = "Année", y= element_blank(), title = "Année de sortie des lunettes") +
  theme(plot.title = element_text(hjust = 0.5, size = 18))

# Type de Lunettes par Marque
categorie.marque = ggplot(df) +
  aes(x = Categorie, 
      fill = Marque) +
  geom_bar(position = 'dodge') +
  geom_text(stat='count', 
            aes(label=..count..), 
            position = position_dodge(0.9),
            vjust=-1.1
  ) +
  scale_fill_hue() +
  labs(title = "Type de Lunettes par Marque") +
  theme_minimal() +
  theme(axis.title.x = element_blank(),
        axis.title.y = element_blank(),
        plot.title = element_text(hjust = 0.5, size = 18))

# Densité des Taille Lunettes et des Gender
taille.gender <- ggplot(df) +
  aes(x = Taille, fill = Gender) +
  geom_bar() +
  scale_fill_manual(values= c("#118DFF",  '#12239E', '#E66C37', '#6B007B'))+
  labs(x = "Taille", 
       y = element_blank(), 
       title = "Densité des Taille Lunettes et des Gender") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 18))

# Proportions Material par Marque
p <- ggplot(df) +
  aes(x = Marque, fill = Material.Fond) +
  geom_bar(position = "fill", 
           mapping = aes(y = (..count..)/sum(..count..))) + 
  scale_y_continuous(labels=scales::percent) +
  labs(x = element_blank(), 
       y = element_blank(),
       title = "Proportions Material par Marque") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 18))+
  scale_x_discrete(labels = wrap_format(10)) 
material.marque <- ggplotly(p)

# Catégorie par ans
p <- df %>% count(year, Categorie) %>%
  ggplot(aes(x = year, col = Categorie, y = n)) +
  geom_line() + 
  geom_point() + 
  geom_text(aes(label = n),
            vjust = 0, 
            nudge_y = 0.5) + 
  labs(x = 'Années',
    y = element_blank(),
    title = 'Catégorie par ans') +
  theme_minimal() + 
  theme(plot.title = element_text(hjust = 0.5, size = 18))
categorie.ans = ggplotly(p)



