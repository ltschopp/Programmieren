# Der Benutzer gibt sein Gewicht ein, dies braucht es um sein BMI auszurechnen.
Gewicht=input("Gibt dein Gewicht in kg ein: ")
Gewicht=float(Gewicht)

# Der Benutzer gibt sein Gewicht ein, dies braucht es um dein BMI auszurechnen.
Grösse=input("Gib deine Grösse in m ein: ")
Grösse=float(Grösse)

# Die Grösse wird mit sich selber multipliziert.
Grösse1=float(Grösse*Grösse)
# Das Gewicht wird durch die Grösse, welche mit sich selber multipliziert wurde, geteilt.
BMI=Gewicht/Grösse1

# Der Datentyp vom BMI wird von einem Integer in ein String umgewandelt.
BMI=str(BMI)

# Dein BMI beträgt: wird ausgegeben, danach kommt der bereits ausgerechnete BMI.
print("Dein BMI beträgt: " +BMI)


