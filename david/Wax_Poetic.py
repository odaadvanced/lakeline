from random import  choice


nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adj = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prep = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adv = ["curiously", "extravagantly", "tantalizingly", "furiously", "senuously"]

noun1 = choice(nouns)
noun2 = choice(nouns)
noun3 = choice(nouns)

verb1 = choice(verbs)
verb2 = choice(verbs)
verb3 = choice(verbs)

adj1 = choice(adj)
adj2 = choice(adj)
adj3 = choice(adj)

prep1 = choice(prep)
prep2 = choice(prep)

adv1 = choice(adv)

if adj1[0].lower() in "aeiou":
    A_An = "An"
else:
    A_An = "A"


print(
    f"""{A_An} {adj1} {noun1}
    
    {A_An} {adj1} {noun1} {prep1} the {adj2} {noun2}
    {adv1}, the {noun1} {verb2}
    the {noun2} {verb3} {prep2} a {adj3} {noun3}
    """
)
