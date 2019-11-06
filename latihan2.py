lst = []
nilai = 1
while nilai > 0 :
        
        numbers = int(input('Masukan bilangan : '))
        lst.append(numbers)
        if numbers ==0:
            break
print("Nilai terbesarnya adalah:",max(lst))
