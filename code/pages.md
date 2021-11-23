================================================================================
# Homepage App

```
1. Players
2. Tournament

Q. Exit
```


================================================================================

================================================================================
# Homepage players

```
Players list :

  ------------------------------------------------------------------------------
  [  Id     Name                            Birth date        Sex     Ranking  ]
  ------------------------------------------------------------------------------
  [  1      DUPOND Jacques                  12/05/1998         M       1103    ]
  [  2      CHEVALIER Julie                 27/11/1983         F       1547    ]
  ------------------------------------------------------------------------------

1. New Player
2. Edit Player
    [Enter Player Id]
3. Delete Player
    [Enter Player Id, "C" to Cancel]

H. Homepage
Q. Exit
```


# New Player

```
Enter id:
Enter lastname:
Enter firstname:
Enter birthdate:
Enter sex:
Enter ranking:
```


# Edit Player

```
Edit :

1. id: 1
2. lastname: DUPOND
3. firstname: Jacques
4. birthdate: 12/05/1998
5. sex: M
6. ranking: 1103

H. Homepage
```


================================================================================

================================================================================
# Homepage Tournament 

```
1. New tournament
2. Tournaments in progress
3. Ended tournaments

H. Homepage
Q. Exit
```


================================================================================

================================================================================
# New Tournament 

```
Enter tournament ID:
Enter tournament name:
Enter tournament location:
Enter tournament date:
Enter number of turns (default is 4):
Enter time mode (Bullet, Blitz or Quick_it):
Enter description of the tournament:
```


```
  ------------------------------------------------------------------------------
  [  Id     Name                            Birth date        Sex     Ranking  ]
  ------------------------------------------------------------------------------
  [  1      DUPOND Jacques                  12/05/1998         M       1103    ]
  [  2      CHEVALIER Julie                 27/11/1983         F       1547    ]
  ------------------------------------------------------------------------------

Enter player 1 ID:
Enter player 2 ID:
Enter player 3 ID:
Enter player 4 ID:
Enter player 5 ID:
Enter player 6 ID:
Enter player 7 ID:
Enter player 8 ID:
```
--> Tournament recap


# Tournament recap

```
Players :
  -------------------------------------------------------------------------------
  [  Id     Name                            Birth date        Sex     Ranking   ]
  -------------------------------------------------------------------------------
  [  1      CHEVALIER Julie                 27/11/1983         F       2547     ]
  [  2      DUPOND Jacques                  12/03/1998         M       2205     ]
  [  3      MICHELLE Paul                   24/12/1983         M       2142     ]
  [  4      POULIN Sarah                    12/07/1998         F       1903     ]
  [  5      SMITH Jack                      27/11/1983         M       1548     ]
  [  6      PELLETIER Cecile                22/04/1998         F       1104     ]
  [  7      ROUGET Emma                     17/10/1983         F        549     ]
  [  8      POULIN Victor                   12/05/1998         M        101     ]
  -------------------------------------------------------------------------------

1. Start tournament

H. Homepage
Q. Exit
```


# Start Tournament 

```
First round :
  -------------------------------------------------------------------------------
  [ Game:   Player Id and Name:        VS       Player Id and Name:             ]
  -------------------------------------------------------------------------------
  [                                                                             ]
  [  (A)     1 CHEVALIER Julie         /         3 MICHELLE Paul                ]
  [  (B)     2 DUPOND Jacques          /         4 POULIN Sarah                 ]
  [  (C)     5 SMITH Jack              /         7 ROUGET Emma                  ]
  [  (D)     6 PELLETIER Cecile        /         8 POULIN Victor                ]
  [                                                                             ]
  -------------------------------------------------------------------------------

1. Start first round

H. Homepage
Q. Exit
```


# Start first round 

```
First round :
  -------------------------------------------------------------------------------
  [ Game:   Player Id and Name:        VS       Player Id and Name:             ]
  -------------------------------------------------------------------------------
  [                                                                             ]
  [  (A)     1 CHEVALIER Julie         /         3 MICHELLE Paul                ]
  [  (B)     2 DUPOND Jacques          /         4 POULIN Sarah                 ]
  [  (C)     5 SMITH Jack              /         7 ROUGET Emma                  ]
  [  (D)     6 PELLETIER Cecile        /         8 POULIN Victor                ]
  [                                                                             ]
  -------------------------------------------------------------------------------
Enter winner ID (enter NULL for draw):

1. Game (A)     -->     1 CHEVALIER Julie (+1)
2. Game (B)
3. Game (C)     -->     7 ROUGET Emma (+0,5)  /  5 SMITH Jack (+0,5)
4. Game (D)

N. Next round
    //available only once all the result are in

H. Homepage
Q. Exit
```


# Tournaments Result 

```
Tournament results :
  -------------------------------------------------------------------------------
  [  Place:        Player Id and Name:                           Points:        ]
  -------------------------------------------------------------------------------
  [                                                                             ]
  [     1st         1 CHEVALIER Julie                               5           ]
  [     2nd         2 DUPOND Jacques                                4,5         ]
  [     3rd         3 MICHELLE Paul                                 4           ]
  [     4th         4 POULIN Sarah                                  3,5         ]
  [     5th         5 SMITH Jack                                    3           ]
  [     6th         6 PELLETIER Cecile                              2           ]
  [     7th         7 ROUGET Emma                                   1           ]
  [     8th         8 POULIN Victor                                 0           ]
  [                                                                             ]
  -------------------------------------------------------------------------------

H. Homepage
Q. Exit
```


================================================================================

================================================================================
# Tournaments in Progress 

```
Tournaments in progress :
  -------------------------------------------------------------------------------
  [  Tournament Id:        Tournament name:                     Started on:     ]
  -------------------------------------------------------------------------------
  [                                                                             ]
  [      12                "Jack's tour 6"                       31/10/2021     ]
  [     236                "Night test"                          30/10/2021     ]
  [                                                                             ]
  -------------------------------------------------------------------------------

1. Resume tournament
    [Enter tournament Id, "C" to Cancel]

H. Homepage
Q. Exit
```


================================================================================

================================================================================
# Ended Tournaments 

```
Ended tournament list :
  -------------------------------------------------------------------------------
  [  Tournament Id:        Tournament name:            Started on:    Ended on: ]
  -------------------------------------------------------------------------------
  [                                                                             ]
  [      14                "Jack's tour 5"             31/10/2021 : 31/10/2021  ]
  [     228                "Night test 34"             30/10/2021 : 31/10/2021  ]
  [                                                                             ]
  -------------------------------------------------------------------------------

1. View tournament details
    [Enter tournament Id]

H. Homepage
Q. Exit
```


# Tournaments Details

```
Tournament detail:

    Tournament name: Night test 6
    Tournament location: France
    Tournament date: 31/10/2021
    Number of turns: 4
    Time mode: Bullet
    Description of the tournament: Test

Tournament players:
    -------------------------------------------------------------------------------
    [  Id     Name                            Birth date        Sex     Ranking   ]
    -------------------------------------------------------------------------------
    [  1      CHEVALIER Julie                 27/11/1983         F       2547     ]
    [  2      DUPOND Jacques                  12/03/1998         M       2205     ]
    [  3      MICHELLE Paul                   24/12/1983         M       2142     ]
    [  4      POULIN Sarah                    12/07/1998         F       1903     ]
    [  5      SMITH Jack                      27/11/1983         M       1548     ]
    [  6      PELLETIER Cecile                22/04/1998         F       1104     ]
    [  7      ROUGET Emma                     17/10/1983         F        549     ]
    [  8      POULIN Victor                   12/05/1998         M        101     ]
    -------------------------------------------------------------------------------

First round :
    -------------------------------------------------------------------------------
    [ Game:   Player Id and Name:        VS       Player Id and Name:             ]
    -------------------------------------------------------------------------------
    [                                                                             ]
    [  (A)     1 CHEVALIER Julie         /         3 MICHELLE Paul                ]
    [  (B)     2 DUPOND Jacques          /         4 POULIN Sarah                 ]
    [  (C)     5 SMITH Jack              /         7 ROUGET Emma                  ]
    [  (D)     6 PELLETIER Cecile        /         8 POULIN Victor                ]
    [                                                                             ]
    -------------------------------------------------------------------------------
Enter winnier ID:

    1. Game (A)     -->     1 CHEVALIER Julie (+1)
    2. Game (B)     -->     2 DUPOND Jacques (+1)
    3. Game (C)     -->     7 ROUGET Emma (+0,5)  /  5 SMITH Jack (+0,5)
    4. Game (D)     -->     PELLETIER Cecile (+1)

Second round :
    //

Third round :
    //

Fourth round :
    //

Final round :
    //
    
Tournament results :
    -------------------------------------------------------------------------------
    [  Place:        Player Id and Name:                           Points:        ]
    -------------------------------------------------------------------------------
    [                                                                             ]
    [     1st         1 CHEVALIER Julie                               5           ]
    [     2nd         2 DUPOND Jacques                                4,5         ]
    [     3rd         3 MICHELLE Paul                                 4           ]
    [     4th         4 POULIN Sarah                                  3,5         ]
    [     5th         5 SMITH Jack                                    3           ]
    [     6th         6 PELLETIER Cecile                              2           ]
    [     7th         7 ROUGET Emma                                   1           ]
    [     8th         8 POULIN Victor                                 0           ]
    [                                                                             ]
    -------------------------------------------------------------------------------

1. Return to Ended tournament

H. Homepage
Q. Exit
```


================================================================================
