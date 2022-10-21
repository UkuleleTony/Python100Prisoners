# Simulation of the solution to the 100 Prisoners problem -
# There are 100 prisoners (numbered 1 to 100).
# Each one goes into a room where there are 100 boxes, in the boxes are 100 numbers (1 to 100).
# The prisoner is allowed to open a maximum of 50 boxes.
# If the prisoner finds his own number in one of the boxes he 'wins' and can leave the room and the next prisoner can enter.
# If ALL prisoners 'win' then they are all released.
# If ANY prisoner loses then all prisoners are executed.
# What's the best strategy?
# This simulation shows the 'loop' strategy which gives a 30%(ish) success rate

import random
import time 

fltStartTime = time.time()                                              # Make a note of the start time (going to time how long it takes)

SIMULATION_LENGTH = int(1000)                                           # We'll run the simulation this many times
NO_OF_PRISONERS = int(100)                                              # There will be this many prisoners in each run
NO_OF_ATTEMPTS = int(50)                                                # Each prisoner will have this many attmpts to find his own number

intBoxes = [0]                                                          # This array represents the boxes and will be populated with random numbers
intSuccess = int(0)                                                     # Used to keep count of the successes
intFailure = int(0)                                                     # Used to keep count of the failures
intAttempt = int(0)                                                     # Used to keep count of the number of attempts each prisoner has had
intBoxToOpen = int(0)                                                   # The next box to look in
blnFound = bool(True)                                                   # Did the current prisoner find his own number?
intPrisoner = int(0)                                                    # For looping through the prisoners
intSim = int(0)                                                         # For repeating the simulation

for intSim in range(0, SIMULATION_LENGTH):                              # Repeat the simulation the requisite number of times
                                                                        # Regenerate the boxes for each simulation
    intBoxes = [0] + random.sample(list(range(1, NO_OF_PRISONERS + 1, 1)), NO_OF_PRISONERS)                

    blnFound = True                                                     # Assume that this run will be successful
   
    for intPrisoner in range(1, NO_OF_PRISONERS):                       # For each prisoner

        intAttempt = 1                                                  # Reset the attempt count
       
        intBoxToOpen = intPrisoner                                      # First box to open is one with this prisoner's number on it
                                                                        # While we haven't found the prisoners number AND we haven't exceeded the number of attempts
        while (intBoxes[intBoxToOpen] != intPrisoner and intAttempt < NO_OF_ATTEMPTS):
            intAttempt += 1                                             # Keep count of the number of attempts
            intBoxToOpen = intBoxes[intBoxToOpen]                       # Move on to the next box
       
        if intBoxes[intBoxToOpen] != intPrisoner:                       # If the prisoner did NOT find his own number
            blnFound = False                                            # Then we failed and all the prisoners are gonna die
            break                                                       # So there's no point continuing

    if blnFound == True:                                                # If ALL the prisoners found there own number
        intSuccess += 1                                                 # Then it's a successful simulation
    else:                                                               # Otherwise
        intFailure += 1                                                 # It's a failure


# That's the simulation finished, output the results
print ("Looping Strategy----------------------------------------------")
print ("Simulation run length = " + str(SIMULATION_LENGTH))
print ("Number of prisoners = " + str(NO_OF_PRISONERS))
print ("Number of attempts for each prisoner = " + str(NO_OF_ATTEMPTS))
print ("Success=" + str(intSuccess) +", Failure=" + str(intFailure) + " (success rate = " + str(intSuccess * 100 / SIMULATION_LENGTH) + "%)")
print ("In " + str(time.time() - fltStartTime) + " seconds")            
