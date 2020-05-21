import pandas as pd
import os
import matplotlib.pyplot as plt
import random

data_dir = "." + os.sep + "stellar_spectra" + os.sep # get spectrum directory

def spectrum_draw_and_choose():
    spectrum = random.choice(os.listdir(data_dir))  # choose spectrum
    answer = spectrum[2]  # take spectrum class from file name
    df = pd.read_csv(data_dir + spectrum, sep="\s+", skiprows=3, usecols=[0,1], names=['wavelength','flux']) # import spectrum file
#    print(df) # use to check if its importing correctly
    df.plot(kind='line', x='wavelength', y='flux')  # scatter plot
    plt.ylabel("flux")
    plt.show()
    choice = input("What kind of spectrum do you think this is? [o/b/a/f/g/k/m] ")  # take player input
    if choice == answer:
        again = input("Congratulations! Would you like to play again? [y/n] ")  # success
        if again == "y":
            game()
        elif again == "n":
            goodbye()
        else:
            invalid()
            game()
    else:
        play = input("Sorry! That wasn't right, the answer was " + answer + ". Would you like to play again? [y/n] ")  # fail
        if play == "y":
            game()
        elif play == "n":
            goodbye()
        else:
            invalid()
            game()

play = input("Would you like to play Spectrum Guesser? [y/n] ") # receive input
def game(): # run the game or not
    if play == "y":
        spectrum_draw_and_choose()
    elif play == "n":
        goodbye()
    else:
        invalid()

def invalid():
    print("Invalid input. Please type in y to play or n to quit.")

def goodbye(): # end game
    print("Thank you for playing!")

game() # call game function
