Acest proiect consta in testarea a catorva features de pe site-ul eMag.

  #Add to cart 
  Scenario: I want to add an item to cart
  In acest scenariu se doreste adaugarea unui obiect/element in cosul de cumparaturi prin deschiderea paginii elementului 
  si prin apasarea butonului "Adauga in cos"

  #Add to favourites
  Scenario: I want to add an item to favourite
  In acest scenariu se doreste adaugarea unui element de pe o pagina cu o lista de elemente

  Scenario: I want to add an item to favourites after I open item's page
  Item-ul s-a adaugat la sectiunea favorite dupa ce s-a navigat in pagina elementului

  #filter results
  Scenario: I want to reach mobile phones screen
  User-ul a navigat spre pagina de telefoane mobile.

  Scenario: I want to filter the results after pret crescator
  Dupa ce user-ul a ajuns pe pagina cu telefoane mobile, user-ul filtreaza crescator rezultatele, iar mai apoi verifica 
  daca sunt sortate crescator

  #Search
  Scenario: I search for an item
  De pe pagina principala, user-ul cauta "smartwatch" in field-ul de cautare dupa care verifica daca search-ul e corect

  #Sign in
  Scenario: Enter valid email address and password
  User-ul se logheaza

  #Sign up
  Scenario Outline: Enter wrong email address and verify the error
  User-ul incearca sa isi creeze cont cu un email gresit
  
  Scenario: Check error message when input invalid name into "Numele si prenumele" field
  User-ul verifica eroarea care apare in urma inserarii unui nume invalid in field-ul de nume
  
  Scenario: Check error message when leave empty the fields
  User-ul verifica eroarea care apare cand field-utile sunt empty 