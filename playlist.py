import pygame
pygame.init()
print("Here are few songs you can add to your playlist\nSelect the songs in any order and play")
songs=["1. Lover","2. Mombattiye","3. Laal Peeli Akhiyaan","4. GOAT","5. Hum nahi sudhrenge","6. Tera yaar hun main","7. jaane kyun"]

for i  in range(len(songs)):
    print(songs[i])

Songs_path = {
    1: "songs\\128-GOAT - GOAT 128 Kbps.mp3",
    2: "songs\\128-Laal Peeli Akhiyaan - Teri Baaton Mein Aisa Uljha Jiya 128 Kbps.mp3",
    3: "songs\\128-Mombattiye - Diljit Dosanjh 128 Kbps.mp3",
    4: "songs\\hum nahi Sudhrenge.mp3",
    5: "songs\\Jaane Kyun.mp3",
    6: "songs\\Lover.mp3",
    7: "songs\\tera yaar hoon main.mp3"
    }
c=[]
j = int(input("You can choose the number of songs you want to play: "))
for i in range(j):
    value=int(input(f"Enter song number {i+1}: "))
    if value in Songs_path:
        c.append(Songs_path[value])
    else:
        print("Invalid Input")
current_index=0
while current_index < len(c):
    pygame.mixer.music.load(c[current_index])
    print("\nNow Playing:", c[current_index].split("\\")[-1])
    pygame.mixer.music.play()

    while True:
            print("----Baba apna number daba orr krna h krle----\n")
            print("1. Play")
            print("2. Pause")
            print("3. Resume")
            print("4. Next")
            print("5. Stop")
            print("6. Play in loop")
            print("7. Exit")
            choice=int(input("Enter your choice between 1 to 7: "))

            if choice==1:
                pygame.mixer.music.play()
                print("Playing...")
            
            elif choice==2:
                pygame.mixer.music.pause()
                print("Paused...")
            
            elif choice==3:
                pygame.mixer.music.unpause()
                print("Resumed...")
            
            elif choice==4:
                pygame.mixer.music.stop()
                current_index += 1
                break 

            elif choice==5:
                pygame.mixer.music.stop()
                print("Stopped...")

            elif choice==6:
                pygame.mixer.music.play(loops=-1)
                print("Looping...")

            elif choice==7:
                print("Exiting player...")
                break

            else:
                print("Invalid choice. Try again.")

