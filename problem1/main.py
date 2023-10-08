# input
student_score = 80

# Process: Your Solution Code Here
def hitung_nilai_huruf(nilai):
    if nilai >= 80 and nilai <= 100:
        return 'A'
    elif nilai >= 65 and nilai < 80:
        return 'B+'
    elif nilai >= 50 and nilai < 65:
        return 'B'
    elif nilai >= 35 and nilai < 50:
        return 'C'
    else:
        return 'D'




nilai_huruf = hitung_nilai_huruf(student_score)


print(f"Nilai huruf: {nilai_huruf}")


# Output "Nilai A"