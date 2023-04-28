
def count_a(word, loops):
    count = 0
    new_word = word * loops
    for i in new_word:
        if i == 'a':
            count += 1
    return count

word = input("Masukkan kata: ")
loop = int((input("Jumlah loop: ")))
new_word = word * loop
a_count = count_a(word, loop)
print(a_count)
print("Reason:")
print(word+' * '+str(loop)+' = '+new_word)
print(f'therefore {a_count} a is present')