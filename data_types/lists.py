elements = ["val", "var", "it", 3, 0, 0.5, ["a", "b"]]

print(f"the upper 1th element of my list is {elements[0].upper()}")


##

test_string = """
Hey little girl is your daddy home
Did he go away and leave you all alone
I got a bad desire
I'm on fire
Tell me now baby is he good to you
Can he do to you the things that I do
I can take you higher
I'm on fire
Sometimes it's like someone took a knife baby
edgy and dull and cut a six-inch valley
through the middle of my soul
At night I wake up with the sheets soaking wet
and a freight train running through the
middle of my head
Only you can cool my desire
I'm on fire"""

song_list = []
for item in (" ".join(test_string.split())).split():
    song_list.append(item)

print(sorted(set(song_list)))

print(len(set(song_list)))

print(len(song_list))
