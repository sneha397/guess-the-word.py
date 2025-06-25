import time

score = 0  # Define the score at the beginning
time_limit = 10  # seconds for each stage

Stage 1: CAT

x = ["_", "a", "t"]
for i in x:
print(i, end='')

start1 = time.time()
user1 = input("\nFill first letter (10s): ")
end1 = time.time()

if end1 - start1 > time_limit:
print("⏰ Time's up for CAT! Game over.")
else:
if user1 == "c":
x[0] = "c"
word = ''.join(x)
print(word)
score += 1
print("✅ Correct! Let's go to next word.\n")

# Stage 2: APPLE  
    y = ["a", "_", "_", "l", "e"]  
    for j in y:  
        print(j, end='')  

    start2 = time.time()  
    user2 = input("\nFill missing letters (10s): ")  
    end2 = time.time()  

    if end2 - start2 > time_limit:  
        print("⏰ Time's up for APPLE! Game over.")  
    else:  
        if user2 == "pp":  
            y[1] = "p"  
            y[2] = "p"  
            word1 = ''.join(y)  
            print(word1)  
            score += 1  
            print("✅ Great! Let's go to next word.\n")  

            # Stage 3: CAMEL  
            z = ["c", "a", "_", "_", "_"]  
            for k in z:  
                print(k, end='')  

            start3 = time.time()  
            user3 = input("\nFill missing letters (10s): ")  
            end3 = time.time()  

            if end3 - start3 > time_limit:  
                print("⏰ Time's up for CAMEL! Game over.")  
            else:  
                if user3 == "mel":  
                    z[2] = "m"  
                    z[3] = "e"  
                    z[4] = "l"  
                    word2 = ''.join(z)  
                    print(word2)  
                    score += 1  
                    print("✅ Finished all stages!")  
                else:  
                    print("❌ Wrong answer for CAMEL. Game over.")  
        else:  
            print("❌ Wrong answer for APPLE. Game over.")  
else:  
    print("❌ Wrong answer for CAT. Game over.")

Final Score

print(f"\n🎯 Your final score is: {score} out of 3")
