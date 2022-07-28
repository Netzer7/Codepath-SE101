def count_by_state(locations, states, state):
  stateCount = {}
  for city in locations.values():
    for city2, state2 in states.items():
      if city == city2:
        if state2 in stateCount:
          stateCount[state2] += 1
          break
        else:
          stateCount[state2] = 1
          break
  for state1, count in stateCount.items():
    if state1 == state:
      return count
  return 0    #Returns 0 if the user given state is not present in the stateCount dict.
  
# Test Cases
locations = {"Bob": "San Francisco", "Anna": "Los Angeles", "Charlie": "Detroit"}
states = {"San Francisco": "California", "Los Angeles": "California", "Ann Arbor": "Michigan", "Detroit": "Michigan"}

state = "California"
print("Input")
print("\tlocations = ", locations)
print("\tstates = ", states)
print("\tstate = ", state)
print("Output: ", count_by_state(locations, states, state)) #2

state = "Michigan"
print("\nInput")
print("\tlocations = ", locations)
print("\tstates = ", states)
print("\tstate = ", state)
print("Output: ", count_by_state(locations, states, state)) #1

state = "Texas"
print("\nInput")
print("\tlocations = ", locations)
print("\tstates = ", states)
print("\tstate = ", state)
print("Output: ", count_by_state(locations, states, state)) #0