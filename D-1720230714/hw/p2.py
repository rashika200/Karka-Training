names=[{"name":"Virat Kohli",
        "centuries":74,
        "half_centuries":45,
        "wickets":4,
        "hat-trick wickets":5,
        "top batting scores":[254,122,183,160,145]},
        {"name":"Glenn Maxwell",
         "centuries":6,
         "half_centuries":33,
         "wickets":3,
         "hat-trick wickets":6,
         "top batting scores":[145,113,105,130,99]},
        {"name":"AB de Villiers",
         "centuries":25,
         "half_centuries":40,
         "wickets":11,
         "hat-trick wickets":3,
         "top batting scores":[278,180,143,166,240]},
        {"name":"Ben Stokes",
         "centuries":15,
         "half_centuries":30,
         "wickets":12,
         "hat-trick wickets":8,
         "top batting scores":[258,190,135,178,205]},
        {"name":"Chris Gayle",
         "centuries":25,
         "half_centuries":54,
         "wickets":8,
         "hat-trick wickets":4,
         "top batting scores":[175,138,114,156,103]}]
 
def name(names):
      centuries=0
      hat_trick_wickets=[]
      top_batting_scores=[]
      for i in names:
            if(i["centuries"])>10:
                   centuries=centuries+1

            if (i["hat-trick wickets"])>5:
                   hat_trick_wickets.append(i["name"])


            top_score=i["name"],max(i["top batting scores"])
            top_batting_scores.append(top_score)

      print("\nnumber of players scored more than 10 centuries",centuries)
      print("\nnumber of players taken more than 5 hat-trick wickets",hat_trick_wickets)
      print("\ntop batting scores:\n",top_batting_scores)


name(names)


 

        

