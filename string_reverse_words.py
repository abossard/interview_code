#well thats a bit weird, because in C this need actual thinking whereas in Python its pretty straightforward

input = "let's reverse every word in that sentence"
parts = input.split()
parts.reverse()
reverse = " ".join(parts)

reverse_2 = " ".join(input.split()[::-1])
print reverse_2

#in C
# REVERSE the String
# REVERSE the words back!