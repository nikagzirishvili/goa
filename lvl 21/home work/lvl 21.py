#დავალება 2) ააგეთ პროგრამა, რომელიც მოსთხოვს მომხმარებელს, რომ შეიყვანეს რიცხვი 1 - 100 მდე.
#პროგრამის დანიშნულება არის ის, რომგამოიცნოს მომხმარებლის მიერ შემოტანილი რიცხვი, იმდენჯერ მიეცეს გამოცნობის შესაძლებლობა სანამ საბოლოოდ არ გამოიცნობს. 
# y =int((input('Guess the number from 1 to 100: '))) 
# while y < 5 and y < 100:
#     y =int((input('it is incorect: ')))
# print('its corect')


#დავალება 3) შექმენით პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 100-მდე. თუმცა 3-ის ჯერადებისთვის რიცხვის ნაცვლად დაბეჭდეთ „Fizz“, ხოლო 5-ის ჯერადებისთვის დაბეჭდეთ „Buzz“. 3-ისა და 5-ის ჯერადი რიცხვებისთვის დაბეჭდეთ "FizzBuzz".  მოთხოვნები: გამოიყენეთ მარყუჟი 1-დან 100-მდე რიცხვების გასამეორებლად.
#გამოიყენეთ პირობითი განცხადებები, რათა შეამოწმოთ რიცხვი იყოფა 3-ზე, 5-ზე ან ორივეზე. დაბეჭდეთ შესაბამისი სიტყვა ("Fizz", "Buzz" ან "FizzBuzz") ან ნომერი. 
# for i in range(1, 100):
#     if i % 5 == 0 and i % 3 == 0 : 
#         print ('fizzbuzz')
#     elif i % 3 == 0 :
#         print('Fizz')
#     elif i % 5 == 0 :
#         print('buzz')
#     else :
#         print(i)





#დავალება 4) დაწერეთ პროგრამა სადაც შეამოწმეთ, სტუდენტმა ჩააბარა თუ არა ჩააბარა კურსი მათი გამოცდის ქულების მიხედვით. სთხოვეთ მომხმარებელს შეიყვანოს ქულები შუალედური გამოცდისთვის,
# დასკვნითი გამოცდისთვის და პროექტისთვის. დარწმუნდით, რომ მომხმარებელმა შეიყვანოს სწორი ქულები (პოზიტიური რიცხვები 0-დან 100-მდე) თითოეული კომპონენტისთვის.
#გამოიყენეთ შემდეგი შეფასების კრიტერიუმები: თუ საშუალო ქულა (20% შუალედური კურსისთვის, 40% საბოლოო და 40% პროექტისთვის) არის 70 ან მეტი, სტუდენტი გაივლის კურსს. 
#თუ საშუალო ქულა 70-ზე დაბალია, სტუდენტი ვერ ახერხებს კურსის ჩაბარებას. აჩვენეთ მომხმარებლისთვის შეტყობინება, რომელშიც მითითებულია მისი გავლის/ჩავარდნის სტატუსი და 
#გამოთვლილი საშუალო ქულა.

# num = int(input('enter your first score: '))
# num1 = int(input('enter your second score: '))
# num2= int(input('enter your third score: '))

# if (num + num1 + num2) // 3 >= 70  :
#     print ('You have passed')
# else :
#     print('you failed')




#დავალება 5) დაწერეთ პროგრამა სადაც შეამოწმებთ, აქვს თუ არა ადამიანს მართვის მოწმობის აღების უფლება მისი ასაკისა და მართვის გამოცდილებიდან გამომდინარე. დარწმუნდით, რომ მომხმარებელი 
# შეიყვანს თავისი ასაკს და წლების რაოდენობა, რომელსაც მანქანას მართავდა.მომხმარებელმა უნდა შეიყვანოს დადებითი მთელი რიცხვები ასაკისა და მართვის გამოცდილებისთვის. (დაგნა მოხდეს ოპერაციები)
#გამოიყენეთ შემდეგი საკვალიფიკაციო კრიტერიუმები: პირი უნდა იყოს მინიმუმ 18 წლის მართვის მოწმობის მისაღებად. თუ პირი 18 წლამდეა, მას არ შეეძლება მართვის მოწმობის აღება. თუ პირი არის
#  18 წლის ან მეტი, მას უნდა ჰქონდეს მინიმუმ 1 წლიანი მართვის გამოცდილება, რომ დაშვებული იყოს მართვის მოწმობის აღებისთვის.მომხმარებლისთვის აჩვენეთ შეტყობინება, რომელშიც მითითებულია 
# მართვის მოწმობის მიღების უფლება.


age = int(input('enter your age: '))
x = None
if age < 18:
    print('you cant take drive licens')
else:
    x = int(input('How many years of experience do you have: '))
    if age >= 18 and x >= 1:
        print('you can take drive licens')



