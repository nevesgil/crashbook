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

##

upper_string = test_string.upper()

lower_string = test_string.lower()

title_string = test_string.title()

strip_string = test_string.strip()

replace_string = test_string.replace(" ", "")  # this remove all white spaces

print(
    " ".join(test_string.split())
)  # this is great for removing white spaces, escape characteres, etc

# import this
