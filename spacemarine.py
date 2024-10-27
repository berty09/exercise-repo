print(r'''                            .---.--.       .--.   
                          ,(     ),.`.   .'.--.`. 
                          ; \   / : \ ;.'.'    \ ;
\                         ; _; :_ :""-/ /-.     ;:
 \                        ;'-;":-':"-/ /-._^.   ;:
\ \                       :  : ;  ; / /  / \ \  ;:
\\ \                      :\  V  / : :  :   ; ;-';
 \\ \                     ; ;._.':,' ;  ;   : :-' 
\ \\ \                   : : ; : ;o /-._;   : :   
 \ \\ \                 _;o; : ; '-'.'.-"`. :-^,  
  \ \\ \            .-.;:_"  _..--"/ /  _  ;y  ;  
   \ \\ \         .' / '-,; ::    : :  (o) ;   :  
    \ \\ "-.     /  :    ;: ;;    ; ;     /    :  
bug  : \\   \   :   ;    :: ;;  .' ;._..+:     ;  
     :  \\   \  :  _:    ;: :: /   ; ;  ; ;(o):   
"-.   \  \\   \/ Y' '.  // ^ \Y   / /  :  '._.;   
\  \   \  ;"-. ;/     7"" / \ :.-'.' .';  /  /    
\\  \   \ :   ":_    :"\ ;..-^'--" .' /  /  /     
 \\  \   "+.;-"" )._..^-""        /  / .' .'      
  ;"+.;_.-" :--=<___)    __..__  /  :-" .'        
\ :/_. ;  .-" \ _____.--""__..--""   ;.-"         
 ":  '+'  __..-\/\  """"T__..___..-":             
  :   :\."      \/;     ;: () ;  .-" ;            
   "--q/\        "      :;    :-"    :            
       \/;              ;:    ;   ..-(            
        "               :-\__/-+""-. .^.          
                         ; \  (     \;  `.        
                        /`. `-/\ ,=. '.   `.      
                       : \ \ :"-:/ .`. \    \     
                       ;  ; ;;"-;\/ .'`."-.  ;    
                      :   : ;"-.: \/ .' j  "-:    
                      ;   : :"-.;  `: ,' ;    \   
                     :    : :"-:     "..':     ;  
                     ;    ; ;"-;       `=;  ;  :
*******************************************************************************
''')
print("Welcome to Avarax, brother...")
print("You\'re a space marine and was tasked to find capture a xenos(termagant) that escaped prison.")
choice = input('Do you want to proceed on the mission? '
                'Type "yes" or "no".\n').lower()
if choice == "yes":
    choice2 = input('Landed via Thunderhawk and you see two paths, were do you want to go? '
                    'Type "left" or "right".\n').lower()
    if choice2 == "left":
        choice3 = input('You walked and saw footprints of the termagant, do you want to continue walking?'
                        ' Type "yes" or "no".\n').lower()
        if choice3 == "yes":
            choice4 = input("You found three doors. "
                            "One on the left. "
                            "One in the middle. "
                            "and one one the right. "
                            "Which door do you want to open? ").lower()
            if choice4 == "left":
                print("You triggered a trap and you were killed. Mission Failed.")
            elif choice4 == "middle":
                print("You found nothing and the xenos escaped! Mission Failed.")
            elif choice4 == "right":
                choice5 = input("You found the xenos! Do you want to kill or capture the xenos?").lower()
                if choice5 == "capture":
                    print("You captured it and brought it back to the headquarters, objective complete!")
                else:
                    print("You killed the xenos! Mission Failed.")
            else:
                print("You didn't open any door. The xenos escaped.")
        else:
            print("You went back and attacked by Carnifex. Mission Failed.")
    else:
        print("You found a bunch of Carnifex charging towards you and killed you. Mission Failed.")
else:
    print("Mission Failed.")