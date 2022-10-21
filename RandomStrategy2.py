# Simulation of the solution to the 100 Prisoners problem -
# There are 100 prisoners (numbered 1 to 100).
# Each one goes into a room where there are 100 boxes, in the boxes are 100 numbers (1 to 100).
# The prisoner is allowed to open a maximum of 50 boxes.
# If the prisoner finds his own number in one of the boxes he 'wins' and can leave the room and the next prisoner can enter.
# If ALL prisoners 'win' then they are all released.
# If ANY prisoner loses then all prisoners are executed.
# What's the best strategy?
# This simulation shows the most basic approach - each prisoner just opens 50 boxes at random (extremely low chance of success)

import random
import time 

fltStartTime = time.time()                                              # Make a note of the start time (going to time how long it takes)

SIMULATION_LENGTH = int(1000)                                           # We'll run the simulation this many times
NO_OF_PRISONERS = int(100)                                              # There will be this many prisoners in each run
NO_OF_ATTEMPTS = int(50)                                                # Each prisoner will have this many attmpts to find his own number

intSequence = [0]                                                       # This is used to hold the contents of the NUMBER_OF_ATTEMPTS random boxes (which is just a list of random numbers between 1 and NUMBER_OF_PRISONERS)
intPrisoner = int(0)                                                    # To loop through all the prisoners
blnFound = bool(False)                                                  # Did all the prisoner's find their own box?
intSim = int(0)                                                         # For looping through the simulation many times
intSuccess = int(0)                                                     # Keep count of the successes
intFailure = int(0)                                                     # Keep count of the failures

for intSim in range(0, SIMULATION_LENGTH):                              # Run the simulation the requisite number of times

    blnFound = True                                                     # Assume that we ARE going to find every prisoner's number
    
    for intPrisoner in range(1, NO_OF_PRISONERS):                       # For each prisoner
                                                                        # Generate the list of random numbers that represent the contents of the boxes to be opened
        intSequence = random.sample(list(range(1, NO_OF_PRISONERS, 1)), NO_OF_ATTEMPTS)                

        if intPrisoner not in intSequence:                              # If this prisoner's number is not in the randomly generated list
            blnFound = False                                            # Then we've failed and everybody dies
            break                                                       # So we might as well quit

    if blnFound == True:                                                # If we DID find the prisoner's number
        intSuccess = intSuccess + 1                                     # Increment the success count
    else:                                                               # Otherwise, we DIDN'T find the prisoner's number
        intFailure = intFailure + 1                                     # So increment the failure count


# That's the simulation finished, output the results
print ("Random Strategy-----------------------------------------------")
print ("Simulation run length = " + str(SIMULATION_LENGTH))
print ("Number of prisoners = " + str(NO_OF_PRISONERS))
print ("Number of attempts for each prisoner = " + str(NO_OF_ATTEMPTS))
print ("Success=" + str(intSuccess) +", Failure=" + str(intFailure) + " (success rate = " + str(intSuccess * 100 / SIMULATION_LENGTH) + "%)")
print ("In " + str(time.time() - fltStartTime) + " seconds")            
