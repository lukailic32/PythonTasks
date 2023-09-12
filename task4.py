
nums = [1, 5, 0, 123, 23, 0, 3, 4, 0]
for i in nums:
    if 0 in nums:
        nums.remove(0)
        nums.append(0)
print(nums)
'''
Mana ovog koda je njegova efikasnost jer ima slozenost O(n^2).
For koji za promenljivu i uzima vrednosti svakog elementa iz niza ima slozenost O(n),
kao i provera if 0 in nums koja se vrsi za svaku iteraciju for petlje. 
Zbog ugnjezdenja ukupna slozenost koja se dobija je O(n^2).
Takodje jos jedna mana bila bi ta da nije dobro menjati listu kroz koju trenutno iteriramo,
vec ako hocemo da menjamo tu listu onda iteriramo kroz njenu kopiju

Neko efikasnije resenje bi bilo da u novu listu kopiramo sve brojeve koji nisu nula,
a da nule samo prebrojimo i na kraju kada izadjemo iz petlje dodamo ih na kraj.
Slozenost ovog koda bi bila O(n) pa bi on bio efikasniji.

Primer takvog jednog koda:
'''
nums = [1, 5, 0, 123, 23, 0, 3, 4, 0]
count_zero = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[i - count_zero] = nums[i]
    else:
        count_zero += 1

for i in range(len(nums) - count_zero, len(nums)):
    nums[i] = 0

print(nums)