#CV application
#Create 5 dictionaries. Each dictionary should represent a CV.
#Create a CV containing the information of the 5 created people.
#Print the information on CVs created on the screen.

#Question 1

#her bir kişi için cv yaratır
cv1 = {"Ad":"İçimi", "Soyad":"Demirağ", "Yaş":20, "Meslek":"Bilgisayar Mühendisi", "Yetenekler":["Python","C","C#"]}
cv2 = {"Ad":"Ayşe", "Soyad":"Demir", "Yaş":25, "Meslek":"Endüstri Mühendisi", "Yetenekler":["Programlama","Liderlik","Organizasyon"]}
cv3 = {"Ad":"Fatma", "Soyad":"Yılmaz", "Yaş":22, "Meslek":"Makine Mühendisi", "Yetenekler":["Makine","AutoCad","Tasarım"]}
cv4 = {"Ad":"Ali", "Soyad":"Kaya", "Yaş":26, "Meslek":"Kimya Mühendisi", "Yetenekler":["Laboratuvar","GMP-GLP","Pilates"]}
cv5 = {"Ad":"Mehmet", "Soyad":"Küçük", "Yaş":24, "Meslek":"Elektrik Mühendisi", "Yetenekler":["Devreler","Aurdino","Programlama"]}


#tüm cvleri ekrana bastırır
for i,j in cv1.items():
  print(i, ":", j)

print("\n")
  
for i,j in cv2.items():
  print(i, ":", j)

print("\n")
  
for i,j in cv3.items():
  print(i, ":", j)

print("\n")
  
for i,j in cv4.items():
  print(i, ":", j)

print("\n")
  
for i,j in cv5.items():
  print(i, ":", j)
