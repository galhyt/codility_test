"""
Question:  Given a dictionary(list of words) , start word and end word
Find out the smallest number of similar words to transform start word to end word

Example:
start_word = "hit"
end_word = "cog"
dictionary = ["hot","dot","dog","lot","log","cog”]
Output: 5
Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"
"""

"""
map - 0:
        h: [hot]
        d: [dot, dog]
        ...
      1:
        o: [hot, dot, dog] 
"""