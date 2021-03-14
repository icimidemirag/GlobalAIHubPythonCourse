#Write a knowledge competition program.
#It should consist of 10 questions in total.
#Each question will have only one answer.
#Adjust the answers of the questions according to case sensivity.
#Each question should be worth 10 points.
#If User answers 5 or fewer questions, it will be considered unsuccessful.
#If the user answers more than 5 questions correctly, it will be considered successful.

#Extras: The chance to play as much as you want was added.

questions = {"Türkiye'nin başkenti neresidir?":"ankara",
             "Facebook hangi dille yazılmıştır?":"php",
             "Corona hangi yıl çıkmıştır?":"2019",
             "Cumhuriyetin ilanı hangi yıl olmuştur?":"1923",
             "İlk cumhurbaşkanımızın adı nedir?":"mustafa kemal",
             "Halifelik kaç yılında kaldırılmıştır?":"1924",
             "Zorunlu eğitim kaç yıldır?":"12",
             "Rusya hangi yarım kürededir?":"kuzey",
             "Scooby Doo adlı çizgi filmde İskoçya'da yakaladıkları canavarın adı nedir?":"loch ness",
             "Python kursumuz ne zaman başladı?":"8 mart"}

scores = 0

while True:
    for i,j in questions.items():
        print(i)
        answer = input()
        if (j == answer.lower()):
            print("\nTebrikler! 10 puan kazandınız!\n")
            scores += 10
        else:
            print(f'\nÜzgünüm! Doğru cevap {j.title()} olacaktı.\n')
        
    if(scores > 50):
        print(f'\nYarışmayı başarıyla tamamladınız. Toplam {scores} puan kazandınız!')
    else:
        print(f'\nYarışmayı başarıyla tamamlayamadınız. Toplam {scores} puan kazandınız!')
    
    if(scores == 100):
        break
    else:
        isFinish = input("\nTekrar oynamak için 'Devam' yazmanız yeterlidir.\nÇıkmak için entera basmanız yeterlidir.\n")
        if(isFinish.lower() != "devam"):
            break
