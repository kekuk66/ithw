# The problem with input() was that it does something different in
# python 2 compared to python 3. Your mac had python 2.7.5 but I added python 3.
# It might still use python 2 by default. To make sure you run python 3,
# use "python3" from the command line.
#
# I've configured your TextMate to use python3 when you invoke the menu
# Bundles -> Python -> Run Script (terminal), or hit
# Command-Shift-R. Both will open a new window and run this code
import sys

def geo_topics():
    print("")
    print("TOPICS FOR GEOGRAPHY:")
    print("1.  Water and Rivers")
    print("2.  Coasts")
    print("3.  Ecosystems - the living world")
    print("4.  Glacial Landscapes and Processes")
    print("5.  Rocks and Landscapes")
    print("6.  Natural Hazards")
    print("7.  Weather and Climate")
    print("8.  Climate change")
    print("9.  Economic change")
    print("10. Globalisation")
    print("11. Development")
    print("12. Population")
    print("13. Migration")
    print("14. Tourism")
    print("15. Urban environments")
    print("16. Rural environments")
    print("17. Energy Resources")
    print("18. Wasting Resources")
    print("19. Sustainability")
    print("20. Geographical skills ")
    choice = input("Please enter your choice:")
    if choice == "1":
        geo_water_and_rivers()
    elif choice == "2":
        geo2()
    elif choice == "3":
        geo3()
    elif choice == "4":
        geo4()
    elif choice == "5":
        geo5()
    elif choice == "6":
        geo6()
    elif choice == "7":
        geo7()
    elif choice == "8":
        geo8()
    elif choice == "9":
        geo9()
    elif choice == "10":
        geo10()
    elif choice == "11":
        geo11()
    elif choice == "12":
        geo12()
    elif choice == "13":
        geo13()
    elif choice == "14":
        geo14()
    elif choice == "15":
        geo15()
    elif choice == "16":
        geo16()
    elif choice == "17":
        geo17()
    elif choice == "18":
        geo18()
    elif choice == "19":
        geo19()
    elif choice == "20":  
        geo20()
    else:
        print("Please choose the number of your chosen topic (1-20)")
        
        
######
def geo_water_and_rivers():
    print("TOPICS FOR WATERS AND RIVERS")
    print("1.  Background to rivers")
    print("2.  River profiles")
    print("3.  River processes")
    print("4.  River landforms")
    print("5.  River flooding and management issues")
    print("6.  Water usage")
    print("7.  Too little water - drought")
    choice = input("Please enter your choice:")
    if choice == "1":
        print("all about rivers!! They so cool like!!")
    else:
        print("not yet written")

def geo2():
    print("TOPICS FOR COASTS")
    print("1.  Coastal processes")
    print("2.  Erosional landforms")
    print("3.  Depositional landforms")
    print("4.  Coastal management")
    print("5.  Coastal flooding")
    
def geo3():
    print("TOPICS FOR ECOSYSTEMS - THE LIVING WORLD")
    print("1.  Biomes")
    print("2.  Tropical rainforests")
    print("3.  Coniferous woodland")
    print("4.  Deciduous woodlands")
    print("5.  Savannah grassland")
    print("6.  Desert")
    print("7.  Tundra")
    print("8.  Human uses of rainforests")
    print("9.  Human uses of the savannah")
    print("10. Human uses of the desert")
    print("11.  Human uses of temperate deciduous woodlands.")
    
def geo4():
    print("TOPICS FOR GLACIAL LANDSCAPES AND PROCESSES")
    print("1.  Glaciation")
    print("2.  Glacial erosion landforms")
    print("3.  Glacial deposition landforms")
    print("4.  Human activity in glaciated areas")
    print("5.  Case study: conservation and management in the Lake District")
    print("6.  Avalanches")
    
def geo5():
    print("TOPICS FOR ROCKS AND LANDSCAPES")
    print("1.  Geological time")
    print("2.  Classification of Rocks")
    print("3.  Processes")
    print("4.  Rock types in the British Isles")
    print("5.  Quarrying")
    
def geo6():
    print("TOPICS FOR NATURAL HAZARDS")
    print("1.  Tectonic plates")
    print("2.  Fold mountains")
    print("3.  Earthquakes")
    print("4.  Volcanoes and volcanic eruptions")
    print("5.  Managing tectonic hazards")
    print("6.  Hurricanes")
    print("7.  Tsunamis")
    
def geo7():
    print("TOPICS FOR WEATHER AND CLIMATE")
    print("1.  Climate ")
    print("2.  Extreme weather")
    print("3.  Weather systems")
    print("4.  Weather and human activity")

def geo8():
    print("TOPICS FOR CLIMATE CHANGE")
    print("1.  Describing climatic trends")
    print("2.  Greenhouse effect")
    print("3.  Carbon footprints")
    
def geo9():
    print("TOPICS FOR ECONOMIC CHANGE")
    print("1.  Characteristics of industry")
    print("2.  Industry in MEDCs")
    print("3.  Industrial change in MEDCs")
    
def geo10():
    print("TOPICS FOR GLOBALISATION")
    print("1.  Globalisation")
    print("2.  The global food industry")

def geo11():
    print("TOPICS FOR DEVELOPMENT")
    print("1.  Contrasts in development")
    print("2.  Factors influencing development")
    print("3.  Uneven development")
    print("4.  Trade")
    print("5.  Aid")
    
def geo12():
    print("TOPICS FOR POPULATION")
    print("1.  Population distribution and density")
    print("2.  Population change and structure")
    print("3.  Managing population change")
    
def geo13():
    print("TOPICS FOR MIGRATION")
    print("1.  Migration trends")
    print("2.  Types of migration")
    
def geo14():
    print("TOPICS FOR TOURISM")
    print("1.  Tourism trends")
    print("2.  Attractions for tourists")
    print("3.  Tourism in the UK")
    print("4.  Tourism in an LEDC")
    print("5.  Ecotourism")
    
def geo15():
    print("TOPICS FOR URBAN ENVIRONMENTS")
    print("1.  Settlement characteristics")
    print("2.  Urban models in MEDCs")
    print("3.  Urban models in LEDCs")
    print("4.  Urbanization in MEDCs")
    print("5.  Urbanization in LEDCs")
    
def geo16():
    print("TOPICS FOR RURAL ENVIRONMENTS")
    print("1.  Characteristics of rural areas")
    print("2.  Changes in rural areas - MEDCs")
    print("3.  Changes in rural areas - LEDCs")
    print("4.  Farming in rural areas")
    print("5.  Managing rural areas")
    print("6.  Using tropical rural areas")
    
def geo17():
    print("TOPICS FOR ENERGY RESOURCES")
    print("1.  What are resources?")
    print("2.  Energy")
    print("3.  Sustainable energy")
    
def geo18():
    print("TOPICS FOR WASTING RESOURCES")
    print("1.  Waste and pollution")
    
def geo19():
    print("TOPICS FOR SUSTAINABILITY")
    print("1.  Sustainable tourism")
    print("2.  Sustainable resources")
    print("3.  Sustainable uses of environments")
    print("4.  Sustainable living")
    
def geo20():
   print("TOPICS FOR GEOGRAPHICAL SKILLS")
   print("1.  Map skills")
   print("2.  Graph skills")
   print("3.  Photos in geography")
   print("4.  Controlled assessment in Geography") 

def hist_topics():
    print("Courses:")
    print("1.  Modern World History")
    print("2.  Twentieth Century History")
    print("3.  Schools History project")
    choice = input("Please enter the topic number you wish to choose:")
    if choice == "1":
        hist1()
    elif choice == "2":
        hist2()
    elif choice == "3":
        hist3()
    else:
        print("bad choice")

def hist1():
    print("TOPICS FOR MODERN WORLD HISTORY:")
    print("1.  World War One and Two")
    print("2.  The Cold War")
    print("3.  Britain 1905 - 1951")
    print("4.  Germany 1918-1939")
    print("5.  Russia/USSR 1905 - 1941")
    print("6.  USA 1919 - 1941")
    print("7.  Vietnam 1954 - 1975")
    print("8.  Northern Ireland 1965 - 1985")
    # TODO: choice

def hist2():
    print("TOPICS FOR TWENTIETH CENTURY HISTORY: ")
    print("1.  The USA, A nation of contrasts, 1910 - 1929")
    print("2.  The development of the USA, 1929 - 2000")
    print("3.  Germany in transition, c.1929 - 1947")
    # TODO: choice
    
def hist3():
    print("TOPICS FOR SCHOOLS HISTORY PROJECT:")
    print("1.  Ancient Medicine")
    print("2.  Medieval and Renaissance medicine")
    print("3.  Modern medicine")
    print("4.  American West")
    print("5.  Germany 1918 - 1939")
    print("6.  British society - 1815 - 1851")
    # TODO: choice
    
def sci_topics():
    print("TOPICS FOR SCIENCE")
    print("Sciences:")
    print("1.  Biology")
    print("2.  Chemistry")
    print("3.  Physics")
    choice = input("Please enter the topic number you wish to choose:")
    if choice == "1":
        sci1()
    elif choice == "2":
        sci2()
    elif choice == "3":
        sci3()
    else:
        print("bad choice")
            
def sci1():
    print("TOPICS FOR BIOLOGY:")
    print("1.  Living Organisms")
    print("2.  Nutrition, digestion and excretion")
    print("3.  Respiration and gas exchange")
    print("4.  Transport")
    print("5.  Nerves and hormones")
    print("6.  Health and Disease")
    print("7.  Reproduction")
    print("8.  Inheritance and genetics")
    print("9.  Evolution")
    print("10. Ecosystems and Habitats ")
    print("11. Humans and the environment")
         # TODO: choice
        
def sci2():
    print("TOPICS FOR CHEMISTRY ")
    print("1.  Solids, liquids and gases")
    print("2.  Atomic structure")
    print("3.  Quantitative Chemistry ")
    print("4.  Chemical reactions and tests")
    print("5.  Metals")
    print("6.  Organic Chemistry")
    print("7.  Acids, Alkalis and Salts")
    print("8.  Energy")
    print("9.  Crude oils and fuels")
    print("10. Chemical industry")
    print("11. Earth and the environment ")
    print("12. Materials")
        # TODO: choice
        
def sci3():
    print("TOPICS FOR PHYSICS")
    print("1.  Forces and movements")
    print("2.  Electricity")
    print("3.  Waves")
    print("4.  Electromagnetism and magnetism")
    print("5.  Energy")
    print("6.  Solids, liquids and gases")
    print("7.  Space")
    print("8.  Atoms and radiation")
    print("9.  The origin of chemical elements")
    print("10. Inventions")
        # TODO: choice
def re_topics():
    print("What topic would you like to learn about??")
    print("TOPICS:")
    print("1.  Buddhism")
    print("2.  Christianity")
    print("3.  Hinduism")
    print("4.  Islam")
    print("5.  Judaism")
    print("6.  Roman Catholicism")
    print("7.  Sikhism")
    choice = input("Please enter the topic number you wish to choose:")
    if choice == "1":
        re1()
    elif choice == "2":
        re2()
    elif choice == "3":
        re3()
    elif choice == "4":
        re4()
    elif RE == "5":
        re5()
    elif choice == "6":
        re6()
    elif choice == "7":
        re7()
    else:
        print("bad choice")
def re1():
    print("TOPICS FOR BUDDHISM:")
    print("1.  Beliefs")
    print("2.  Global issues")
    print("3.  Practices and belonging")
    print("4.  Science and religion")    
        
def re2():
     print("TOPICS FOR CHRISTIANITY:")
     print("1.  Beliefs")
     print("2.  Ethics")
     print("3.  Global issues")
     print("4.  Media")
     print("5.  Practices and belonging")
     print("6.  Relationships and lifestyle")
     print("7.  Science and religion")  
      
def re3():
     print("TOPICS FOR HINDUISM")
     print("1.  Beliefs")
     print("2.  Global issues")
     print("3.  Practices and Belonging")
     print("4.  Relationships and lifestyle")
     
def re4():
    print("TOPICS FOR ISLAM")
    print("1.   Beliefs")
    print("2.   Ethics")
    print("3.   Global issues")
    print("4.   Media")
    print("5.   Practices and belonging")
    print("6.   Relationships and lifestyle")
    print("7.   Sources")
    
def re5():
    print("TOPICS FOR JUDAISM")
    print("1.   Beliefs")
    print("2.   Ethics")
    print("3.   Global issues")
    print("4.   Practices and belonging")
    print("5.   Relationships and lifestyle")
    print("6.   Source")
    
def re6():
    print("TOPICS FOR ROMAN CATHOLICISM")
    print("1.   Beliefs")
    print("2.   Global issues")
    print("3.   Media")
    
def re7():
    print("TOPICS FOR SIKHISM")
    print("1.   Beliefs")
    print("2.   Practices and belonging")
    print("3.   Relationships and lifestyle")

def ict_topics():
    print("What topic would you like to learn about??")
    print("TOPICS:")
    print("1.  ICT systems")
    print("2.  Hardware")
    print("3.  Software")
    print("4.  Data and Databases")
    print("5.  Networks and communications")
    print("6.  Measurement and control")
    print("7.  Modeling and stimulation")
    print("8.  Legal framework")
    print("9.  Risks and implications of ICT")
    print("10. Industrial and commercial applications")
    choice = input("Please enter the topic number you wish to choose:")  
    print("not yet implemented")
    
def music_topics():
    print("What topic would you like to learn about??")
    print("TOPICS:")
    print("1.  Elements and music")
    print("2.  Music in the 20th century")
    print("3.  Music for dance")
    print("4.  Performing")
    print("5.  Popular music")
    print("6.  The western classical tradition")
    print("7.  World music")
    choice = input("Please enter the topic number you wish to choose:")
    if choice == "1":
        mus1()
    elif choice == "2":
        mus2()
    elif choice == "3":
        mus3()
    elif choice == "4":
        mus4()
    elif choice == "5":
        mus5()
    elif choice == "6":
        mus6()
    elif choice == "7":
        mus7()
    else:
        print(" bad choice")
        
def mus1():
    print("TOPICS FOR ELEMENTS OF MUSIC   ")
    print("1.  Notation")
    print("2.  Instrumentation")
    print("3.  Melody")
    print("4.  Rhythm and meter")
    print("5.  Texture")
    
def mus2():
    print("TOPICS FOR MUSIC IN THE 20TH CENTURY    ")
    print("1.  Expressionism")
    print("2.  Minimalism")
    print("3.  Musical theatre")
    
def mus3():
    print("TOPICS FOR MUSIC FOR DANCE      ")
    print("1.  Group dance")
    print("2.  Improvised dance")
    print("3.  Paired dance")
def mus4():
    print("TOPICS FOR PERFORMING")
    print("Performance")

def mus5():
    print("TOPICS FOR POPULAR MUSIC        ")
    print("1.   Blues")
    print("2.   Film music")
    print("3.   Jazz")
    print("4.   Sampling")
    print("5.   Popular music of the 1960s")
    print("6.   R 'n' B, Hip-hop")
    print("7.   Rock music")
    
def mus6():
    print("TOPICS FOR THE WESTERN CLASSICAL TRADITION  ")
    print("1.   Chamber music")
    print("2.   The concerto")
    print("3.   The sonata")
    print("4.   Baroque orchestral music")
    print("5.   Mozart - Symphony No. 40: movement 1")
    print("6.   Chopin - Prelude No. 15, Op. 28")
    print("7.   Program music")
    print("8.   Music for voices")
    print("9.   Lieder")
def mus7():
    print("TOPICS FOR WORLD MUSIC ")
    print("1.   Celtic rock")
    print("2.   Gamelan music")
    print("3.   African music")
    print("4.   Music of the Caribbean")
    print("5.   Music of India") 
   
def design_technology_topics():
    print("What topic would you like to learn about??")
    print("TOPICS:")
    print("1.  Electronics")
    print("2.  Food Technology")
    print("3.  Graphics")
    print("4.  Resistant materials")
    print("5.  Systems and control")
    print("6.  Textiles")
    choice = input("Please enter the topic number you wish to choose:")
    if choice == "1":
        dt1()
    elif choice == "2":
        dt2()
    elif choice == "3":
        dt3()
    elif choice == "4":
        dt4()
    elif choice == "5":
        dt5()
    elif choice == "6":
        dt6()
    else:
        print("Please choose the number of your chosen topic (1-20)")
        
def dt1():
    print("TOPICS FOR ELECTRONICS   ")
    print("1.  Components")
    print("2.  Electronic calculations")
    print("3.  Integrated circuits")
    print("4.  Logic and micro-controllers")
    print("5.  Materials")
    print("6.  Switches, transistors and relays")
    print("7.  Design activities")
    print("8.  Environmental and social issues")
    print("9.  Manufacturing processes")
    
def dt2():
    print("TOPICS FOR FOOD TECHNOLOGY     ")
    print("1.  Nutritional properties")
    print("2.  Functional properties")
    print("3.  Acidity and temperature")
    print("4.  Food product development")
    print("5.  Food packaging and labeling")
    print("6.  Social and environmental issues")
    print("7.  Systems and practices")

def dt3():
    print("TOPICS FOR GRAPHICS      ")
    print("1.  Graphics media")
    print("2.  Materials and components")
    print("3.  Drawing 1: Sketching, enhancing, shapes and charts")
    print("4.  Drawing 2: Formal drawing technique")
    print("5.  Graphics product development, evaluation and ICT")
    print("6.  Design and market influence")
    print("7.  Systems and production methods")
    print("8.  Printing, finishing, paper and card engineering.")
    
def dt4():
    print("TOPICS FOR RESISTANT MATERIALS  ")
    print("1.   Materials")
    print("2.   Components, joints and adhesives")
    print("3.   Product analysis and design")
    print("4.   Social, moral, environment, and legal issues")
    print("5.   Health and safety")
    print("6.   Production techniques")
    print("7.   Industrial practices")
    
def dt5():
    print("TOPICS FOR SYSTEMS AND CONTROL      ")
    print("1.   Working with systems")
    print("2.   Product design and evaluation")
    print("3.   Societal and moral factors, health and safety")
    print("4.   Production techniques")
    print("5.   ICT")
    print("6.   Electronics")
    print("7.   Mechanisms")
    print("8.   Pneumatics")

def dt6():        
    print("TOPICS FOR TEXTILES    ")
    print("1.   Fibers")
    print("2.   Fabrics")
    print("3.   Product analysis and evaluation")
    print("4.   Consumers, maintenance and safety")
    print("5.   Systems and practices")
    print("6.   Production techniques")

def english_topics():    
    print(" TOPICS:")
    print("1.   Reading ")
    print("1.   Writing for different purposes ")
    print("2.   Speaking and listening skills ")
    print("3.   Critical writing ")
    print("4.   Creative writing")
    print("5.   Spoken language ")
    choice = input("choice")
    if choice == "1":
        en1()
    elif choice == "2":
        en2()
    elif choice == "3":
        en3()
    elif choice == "4":
        en4()
    elif choice == "5":
        en5()
        
def en1():
    print("TOPICS FOR READING    ")
    print("1.  What are non-fiction texts?")
    print("2.  Analyzing non-fiction text")
    
def en2():
    print("TOPICS FOR SPEAKING AND LISTENING SKILLS     ")
    print("1.  Identifying genre, audience, purpose and style")
    print("2.  Writing to advise")
    print("3.  Writing to argue")
    print("4.  Writing to inform, explain and describe")
    
def en3():
    print("TOPICS FOR CRITICAL WRITING       ")
    print("1.   Critical writing overview")
    print("2.   Themes and ideas")
    print("3.   Characterization and voice")
    print("4.   Language, form and structure")
    
def en4():
    print("TOPICS FOR CREATIVE WRITING     ")
    print("1.   An introduction to creative writing")
    print("2.   Writing a narrative")
    print("3.   Writing for print")
    print("4.   Writing for web")
    print("5.   Writing an autobiography")
    print("6.   Writing a film review")
    print("7.   Writing a voice-over")
    print("8.   Rewriting original texts")
    
def en5():
    print("TOPICS FOR SPOKEN LANGUAGE      ")
    print("1.   Analyzing speech")
    print("2.   Capturing speech")
    print("3.   Identifying and understanding different types of speech")
    print("4.   Influence of social change and technology on speech")


def literature():
    print(" TOPICS")
    print("1.   Dr Jeckyll and Mr Hyde")
    print("2.   Frankenstein")
    print("3.   Great Expectations")
    print("4.   Jane Eyre")
    print("5.   Lord of the Flies")
    print("6.   Of mice and men")
    print("7.   Pride and prejudice")
    print("8.   To kill a Mockingbird")
    print("9.   Heroes")
    print("10.  Animal Farm")
    print("11.  Wuthering Heights")
    print("12.  Touching the Void")
    print("13.  Paddy Clarke Ha Ha Ha")
    print("14.  Silas Marner")
    print("15.  Anita and Me")
    print("16.  Flight")
    print("17.  Superman and Paula Brown's New Snowsuit")
    print("18.  The end of something")
    print("19.  Your Shoes")
    print("20.  My Polish Teacher's Tie")        
    print("21.  Compass and Torch")
    print("22.  The Darkness Out There")
    print("23.  Anil")
    print("24.  Something Old, Something New")
    print("25.  The Withered Arm")
    print("26.  The Crucible")
    print("27.  A View from the bridge")
    print("28.  An Inspector Calls")
    print("29.  Blood Brothers")
    print("30.  Hamlet")
    print("31.  Macbeth")
    print("32.  Much Ado About Nothing")
    print("33.  Othello")
    print("34.  Romeo and Juliet")
    print("35.  The Merchant of Venice")
    print("36.  Julius Caesar")
    print("37.  Twelfth Night")
    print("38.  Educating Rita")
    print("39.  The History of Boys")
    print("40.  Journey's End")
    print("41.  Poetry: Character and voice")
    print("42.  AQA Poetry: Place")
    print("43.  AQA Poetry: Conflict")
    print("44.  AQA Poetry: Relationships")
    print("45.  CCEA Poetry: Love and death")
    print("46.  CCEA Poetry: Nature and war: ")
    print("47.  CCEA Poetry: Seamus Heaney and Thomas Hardy")
    print("48.  WJEC Poetry: Love")
    print("49.  WJEC Poetry: Relationships")
    print("50.  WJEC Poetry: The treatment of women")
    print("51.  WJEC Poetry: Control and power")
    print("52.  OCR Poetry: Reflections")
    
def pe_topics():
    print("TOPICS:")
    print("1.  Performing sport")
    print("2.  Popular sports")
    print("3.  The body")
    choice = input("Please enter the topic number you wish to chose:")
    if choice == "1":
        pe1()
    elif choice == "2":
        pe2()
    elif choice == "3":
       pe3()
    else:
        print("bad choice")

def pe1():
    print("TOPICS FOR PERFORMING SPORT            ")
    print("1.  Analysis and development of performance")
    print("2.  Factors affecting participation")

def pe2():
    print("TOPICS FOR POPULAR SPORTS         ")
    print("1.  Dance")

def pe3():
    print("TOPICS FOR THE BODY      ")
    print("1.  Anatomy and physiology")
    print("2.  Health, fitness and training")
    print("3.  Factors affecting performance")
    print("4.  Injuries")
    
def maths_topics():
    print("What topic would you like to learn about??")
    print("TOPICS:")
    print("1.  Algebra")
    print("2.  Geometry and measures")
    print("3.  Numbers")
    print("4.  Statistics and probability")
    print("5.  Calculus")
    print("6.  Functional maths")
    Math = input("Please enter the topic number you wish to choose:")
    if Math == "1":
        math1()
    elif Math == "2":
        math2()
    elif Math == "3":
        math3()
    elif Math == "4":
        math4()
    elif Math == "5":
        math5()
    elif Math == "6":
        math6()
    else:
        print("bad choice")
            
def math1():
    print("TOPICS FOR ALGEBRA")
    print("1.  Expressions and formulae")
    print("2.  Equations")
    print("3.  Graphs")
    print("4.  Patterns and sequences")
    print("5.  Factors")

def math2():
    print("TOPICS FOR GEOMETRY AND MEASURES")
    print("1.  Transformations")
    print("2.  Symmetry")
    print("3.  Coordinates")
    print("4.  Perimeter, Area, Volume")
    print("5.  Measurement")
    print("6.  Trigonometry")
    print("7.  Pythagoras")
    print("8.  Angles")
    print("9.  Shapes")
    print("10. Time")
    print("11. Locus ")

def math3():
    print("NUMBERS")
    print("1.  Distance, speed and time")
    print("2.  Rounding and estimating")
    print("3.  Ratio and proportion")
    print("4.  Factors, multiples and primes")
    print("5.  Powers and roots")
    print("6.  Decimals")
    print("7.  Positive and negative numbers")
    print("8.  Operations (Calculations/sums)")
    print("9.  Fractions")
    print("10. Percentages")

def math4():
    print("TOPICS FOR STATISTICS AND PROBABILITY")
    print("1.   Collecting, recording and presenting data")
    print("2.   Averages")
    print("3.   Probability")
    print("4.   Standard deviation and semi-interquartile range (Data analysis)")

def math5():
    print("TOPICS FOR CALCULUS")
    print("1.   Differentiation")

def math6():
    print("TOPICS FOR FUNCTIONAL MATHS")
    print("1.   Inequalities")
    print("2.   Equations")
    print("3.   Symmetry")
    print("4.   Perimeter, Area, Volume")
    print("5.   Measurement")
    print("6.   Angles")
    print("7.   Shapes")
    print("8.   Time")
    print("9.   Locus")
    print("10.  Distance, speed and time")
    print("11.  Rounding and estimating")
    print("12.  Ratio and proportion")
    print("13.  Powers and roots ")
    print("14.  Operations (calculations/sums) ")
    print("15.  Fractions  ")
    print("16.  Percentages ")
    print("17.  Collecting, recording and representing data ")
    print("18.  Averages")
    print("19.  Probability")

def art_design_topics():
    print("What topic would you like to learn about??")
    print("TOPICS:")
    print("1.  Course structure")
    print("2.  Assessment objectives")
    print("3.  Quick reference")
    choice = input("Please enter the topic number you wish to choose:")
    if choice == "1":
        art1()
    elif choice == "2":
        art2()
    elif choice == "3":
        art3()
    else:
        print("bad choice")
        
def art1():
    print("TOPICS FOR COURSE STRUCTURE")
    print("1.  Course structure")
    print("2.  Coursework portfolio")
    print("3.  Externally set task")

def art2():         
    print("TOPICS FOR ASSESSMENT OBJECTIVES")
    print("1.  Assessment Objective 1: Developing ideas")
    print("2.  Assessment Objective 2: Using resources, media and materials")
    print("3.  Assessment Objective 3: Recording ideas and observations")
    print("4.  Assessment Objective 4: Making a personal, informed, and meaningful response")

def art3():
    print("TOPICS FOR QUICK REFERENCE")
    print("1.   Art, craft and design")
    print("2.   Subject matter")
    print("3.   Elements of art")
    print("4.   Composing artwork")
    print("5.   Drawing")
    print("6.   Media and techniques")
    print("7.   Using ICT")
    print("8.   Using photography")
    print("9.   Analyzing an artist's work")
    print("10.  Annotating and evaluating your work")

def german_topics():
    print("What topic would you like to learn about??")
    print("TOPICS:")
    print("1.  Listening: foundation")
    print("2.  Listening: higher")
    print("3.  Reading: foundation")
    print("4.  Reading: higher")
    print("5.  Speaking: foundation")
    print("6.  Speaking: higher")
    print("7.  Writing: foundation")
    print("8.  Writing: higher")
    print("9.  Grammar")
    print("10. Exam skills")
    choice = input("Please enter the topic number you wish to choose:")
    if choice == "1":
        german1()
    elif choice == "2":
        german2()
    elif choice == "3":
        german3()
    elif choice == "4":
        german4()
    elif choice == "5":
        german5()
    elif choice == "6":
        german6()
    elif choice == "7":
        german7()
    elif choice == "8":
        german8()
    elif choice == "9":
        german9()
    elif choice == "10":
        german10()
    else:
        print("Bad choice")
        
def german1():
    print("TOPICS FOR LISTENING: FOUNDATION")
    print("1.  My family")
    print("2.  Finding your way")
    print("3.  Daily routine")
    print("4.  Holidays abroad")
    print("5.  Different jobs")
    print("6.  Technology")
    print("7.  Relationships and children")
    print("8.  Healthy and unhealthy lifestyles")
    print("9.  Free time activities")
    
def german2():
    print("TOPICS FOR LISTENING: HIGHER")
    print("1.  Traveling to Germany")
    print("2.  Mobile phones")
    print("3.  Daily routine")
    print("4.  Holidays abroad")
    print("5.  Telephone messages")
    print("6.  Being environmentally friendly")
    print("7.  Technology")
    print("8.  Relationships and children")
    print("9.  Healthy and unhealthy lifestyles")
    print("10. Free time activities")
    
def german3():
    print("TOPICS FOR READING: FOUNDATION")
    print("1.  Public signs and notices")
    print("2.  Postcards")
    print("3.  Signs and notices at work")
    print("4.  Weather")
    print("5.  Learning about people")
    print("6.  Writing about a holiday")
    print("7.  Finding and email pen-friend")
    print("8.  Being environmentally friendly")
    print("9.  Relationships with family and friends")
    
def german4():
    print("TOPICS FOR READING: HIGHER")
    print("1.   Buying from a market")
    print("2.   Describing where you live")
    print("3.   Different jobs")
    print("4.   A life story")
    print("5.   Health resort activities")
    print("6.   Problems facing the planet")
    print("7.   Social issues")
    
def german5():
    print("TOPICS FOR SPEAKING: FOUNDATION")
    print("1.   Family and pastimes")
    print("2.   Daily routine")
    print("3.   Holidays and travel")
    print("4.   The world of work")
    print("5.   Summarizing into key points")
    print("6.   Use of tenses")
    print("7.   How to answer questions")
    
def german6():
    print("TOPICS FOR SPEAKING: HIGHER")
    print("1.   Family and pastimes")
    print("2.   Home and the local area")
    print("3.   Boosting your grade")
    print("4.   How to answer questions")
    
def german7():
    print("TOPICS FOR WRITING: FOUNDATION")
    print("1.   Home town")
    print("2.   A past holiday")
    print("3.   Shopping")
    
def german8():
    print("TOPICS FOR WRITING: HIGHER")
    print("1.   Prepositions and case endings")
    print("2.   Verbs in the perfect tense")
    print("3.   Writing a letter of complaint")
    
def german9():
    print("TOPICS FOR GRAMMAR ")
    print("1.   Adjective and adjective endings")
    print("2.   Possessive adjectives")
    print("3.   Comparatives and superlatives")
    print("4.   Adverbs of time, manner and place")
    print("5.   Adjectives: foundation")
    print("6.   Adjectives: higher")
    print("7.   Adverbs: foundation")
    print("8.   Nouns, gender and plurals")
    print("9.   Definite and indefinite articles")
    print("10.  Cases")
    print("11.  Numbers, dates, time and quantities")
    print("12.  Nouns and articles")
    print("13.  Numbers ")
    print("14.  Prepositions ")
    print("15.  Conjunctions ")
    print("16.  Questions ")
    print("17.  Prepositions, clauses and conjunctions")
    print("18.  Personal")
    print("19.  Demonstrative")
    print("20.  Relative pronouns: higher ")
    print("21.  Pronouns: foundation")
    print("22.  Pronouns: higher ")
    print("23.  Overview ")
    print("24.  Present tense ")
    print("25.  Impersonal ")
    print("26.  Reflexive ")
    print("27.  Modal ")
    print("28.  Future tense ")
    print("29.  Pluperfect tense ")
    print("30.  Separable  ")
    print("31.  Perfect tense ")
    print("32.  Imperfect tense ")
    print("33.  Infinitive form: higher")
    print("34.  Conditional tense: higher ")
    print("35.  Verb placement ")
    print("36.  Verbs: foundation ")
    print("37.  Verbs - past tense: foundation ")
    print("38.  Verbs: higher")
    
def german10():
    print("TOPICS FOR EXAM SKILLS")
    print("1.   Understanding exam rubric")
    print("2.   Preparing for the listening exam")
    print("3.   Preparing for the reading exam")
    print("4.   Speaking Controlled Assessment")
    print("5.   Writing Controlled Assessment")
    print("6.   Using a dictionary")
            
def french_topics():
    print("What topic would you like to learn about??")
    print("TOPICS:")
    print("1.  Listening: foundation")
    print("2.  Listening: higher")
    print("3.  Reading: foundation")
    print("4.  Reading: higher")
    print("5.  Speaking: foundation")
    print("6.  Speaking: higher")
    print("7.  Writing: foundation")
    print("8.  Writing: higher")
    print("9.  Grammar")
    print("10. Exam skills")
    choice = input("Please enter the topic number you wish to choose:")
    if choice == "1":
        french1()
    elif choice == "2":
        french2()
    elif choice == "3":
        french3()
    elif choice == "4":
        french4()
    elif choice == "5":
        french5()
    elif choice == "6":
        french6()
    elif choice == "7":
        french7()
    elif choice == "8":
        french8()
    elif choice == "9":
        french9()
    elif choice == "10":
        french10()
    else:
        print("Bad choice")
        
def french1():
    print("TOPICS FOR LISTENING: FOUNDATION")
    print("1.  Finding the way")
    print("2.  Holidays abroad")
    print("3.  Different jobs")
    print("4.  Families")
    print("5.  School day")
    print("6.  Transport issues")
    
def french2():
    print("TOPICS FOR LISTENING: HIGHER")
    print("1.  A typical day")
    print("2.  Telephone messages")
    print("3.  Holidays")
    print("4.  Getting around")
    print("5.  The environment")
    print("6.  Employment")
    
def french3():
    print("TOPICS FOR READING: FOUNDATION")
    print("1.  At the airport")
    print("2.  Halloween")
    print("3.  Job adverts")
    print("4.  Future plans")
    print("5.  Pen-friends")
    print("6.  How 'green' are you?")
    print("7.  Small ads")
    print("8.  Television")
    
def french4():
    print("TOPICS FOR READING: HIGHER")
    print("1.   Christmas")
    print("2.   Magazines")
    print("3.   Websites")
    print("4.   Teenagers' problems")
    print("5.   Work experience abroad")
    print("6.   Lifestyle and social issues")
    
def french5():
    print("TOPICS FOR SPEAKING: FOUNDATION")
    print("1.   Conversation: Typical day")
    print("2.   Conversation: School")
    print("3.   Conversation: Holidays and travel")
    print("4.   Conversation: Work")
    print("5.   Interview: A healthy lifestyle?")
    print("6.   Interview: Leisure activities")
    print("7.   Presentation: Summarizing into key points")
    print("8.   Presentation: Using a variety of tenses")
    
def french6():
    print("TOPICS FOR SPEAKING: HIGHER")
    print("1.   Conversation: Adult life")
    print("2.   Conversation: Free time")
    print("3.   Conversation: My house")
    print("4.   Conversation: My region")
    print("5.   Presentation: Traditional celebrations")
    print("6.   Preparing for a discussion")
    
def french7():
    print("TOPICS FOR WRITING: FOUNDATION")
    print("1.   Filling in a form")
    print("2.   Health")
    print("3.   Holidays abroad")
    print("4.   Opinions")
    print("5.   School life")
    print("6.   Friendship")
    
def french8():
    print("TOPICS FOR WRITING: HIGHER")
    print("1.   Healthy lifestyle")
    print("2.   Holidays")
    print("3.   Summer jobs")
    print("4.   School life")
    print("5.   Media")
    
def french9():
    print("TOPICS FOR GRAMMAR")
    print("1.   Adjectives and adverbs - foundation")
    print("2.   Adjectives - foundation + higher")
    print("3.   Nouns and articles - foundation + higher")
    print("4.   Pronouns - foundation")
    print("5.   Pronouns - higher")
    print("6.   Verbs - foundation")
    print("7.   Verbs - higher")
    print("8.   Where, when and how much")
    
def french10():
    print("TOPICS FOR EXAM SKILLS")
    print("1.   Preparing for the listening exam")
    print("2.   Preparing for the reading exam")
    print("3.   Preparing for the speaking controlled assessment: Dialogue")
    print("4.   Preparing for the speaking controlled assessment: Presentation + discussion")
    print("5.   Preparing for the speaking exam: Role-play")
    print("6.   Preparing for the written controlled assessment")
    print("7.   Using a dictionary")
    print("8.   Understanding exam instructions / rubrics")
    print("9.   The French alphabet")
    print("10.  Checking your writing")
    
    
def spanish_topics():
    print("What topic would you like to learn about??")
    print("TOPICS:")
    print("1.  Listening: foundation")
    print("2.  Listening: higher")
    print("3.  Reading: foundation")
    print("4.  Reading: higher")
    print("5.  Speaking: foundation")
    print("6.  Speaking: higher")
    print("7.  Writing: foundation")
    print("8.  Writing: higher")
    print("9.  Grammar")
    print("10. Exam skills")
    choice = input("Please enter the topic number you wish to choose:")
    if choice == "1":
        spanish1()
    elif choice == "2":
        spanish2()
    elif choice == "3":
        spanish3()
    elif choice == "4":
        spanish4()
    elif choice == "5":
        spanish5()
    elif choice == "6":
        spanish6()
    elif choice == "7":
        spanish7()
    elif choice == "8":
        spanish8()
    elif choice == "9":
        spanish9()
    elif choice == "10":
        spanish10()
    else:
        print("Bad choice")
    
def spanish1():
    print("TOPICS FOR LISTENING: FOUNDATION")
    print("1.  School day")
    print("2.  Holidays")
    print("3.  Free time")
    print("4.  Out and about")
    print("5.  Jobs")

def spanish2():
    print("TOPICS FOR LISTENING: HIGHER")
    print("1.  School")
    print("2.  Holidays")
    print("3.  Free time")
    print("4.  My region")
    print("5.  Jobs")

def spanish3():
    print("TOPICS FOR READING: FOUNDATION")
    print("1.  The world around us: Around the town")
    print("2.  International world: Holidays")
    print("3.  Personal and social life: Interests")
    print("4.  Everyday activities: The media")
    print("5.  The world of work: Part-time jobs")

def spanish4():
    print("TOPICS FOR READING: HIGHER")
    print("1.   Personal and social life: Describing someone")
    print("2.   Everyday activities: The news")
    print("3.   The world around us: Shopping")
    print("4.   International world: A tourist brochure")
    print("5.   The world of work: Work experience")

def spanish5():
    print("TOPICS FOR SPEAKING: FOUNDATION")
    print("1.   Conversation: Free time")
    print("2.   Conversation: Daily routine")
    print("3.   Conversation: My house")
    print("4.   Conversation: My region")
    print("5.   Conversation: Jobs")
    print("6.   Role play: Shopping")
    print("7.   Role play: Feeling ill")
    print("8.   Role play: Part-time jobs")
    print("9.   Presentation structure J-Lo")

def spanish6():
    print("TOPICS FOR SPEAKING: HIGHER")
    print("1.   Conversation: School")
    print("2.   Conversation: Holidays")
    print("3.   Role play: Shopping")

def spanish7():
    print("TOPICS FOR WRITING: FOUNDATION")
    print("1.   Everyday activities: About the house")
    print("2.   The world around us: Finding the way")
    print("3.   The world of work: Part-time jobs")
    print("4.   Personal and social life: Personal details")
    print("5.   International world: Tourism")

def spanish8():
    print("TOPICS FOR WRITING: HIGHER")
    print("1.   The world around us: Festivals")
    print("2.   Personal and social life: Holidays")
    print("3.   The world of work: Job application")
    print("4.   International world: Places of interest")
    print("5.   Everyday activities: School life")

def spanish9():
    print("TOPICS FOR GRAMMAR")
    print("1.   Nouns and articles - foundation + higher")
    print("2.   Adjectives: foundation")
    print("3.   Adjectives: Higher")
    print("4.   Adverbs: foundation")
    print("5.   Adverbs: higher")
    print("6.   Pronouns: foundation")
    print("7.   Pronouns: higher")
    print("8.   Prepositions and Conjunctions")
    print("6.   Verbs: foundation")
    print("7.   Verbs: higher")

def spanish10():
    print("TOPICS FOR EXAM SKILLS")
    print("1.   Understanding exam rubric")
    print("2.   Preparing for the listening exam")
    print("3.   Preparing for the reading exam")
    print("4.   Preparing for the speaking exam: conversation")
    print("5.   Preparing for the speaking exam: Role-play")
    print("6.   Preparing the speaking exam: presentation")
    print("7.   Preparing for the written exam")
    print("8.   Checking your writing")
    print("9.   Using a dictionary")


def subjects():
    print("1   Geography. ")
    print("2.  History. ")
    print("3.  Science. ")
    print("4.  RE. ")
    print("5.  ICT. ")
    print("6.  Music. ")
    print("7.  Design and Technology. ")
    print("8.  English. ")
    print("9.  Physical Education ")
    print("10. Mathematics. ")
    print("11. Art and design")
    print("12. German")
    print("13. French")
    print("14. Spanish")
    choice = input("Please input the number of the subject you would like to learn more about:")
    if choice == "1":
        geo_topics()
    elif choice == "2":
        hist_topics()
    elif choice == "3":
        sci_topics()
    elif choice == "4":
        re_topics()
    elif choice == "5":
        ict_topics()
    elif choice == "6":
        music_topics()
    elif choice == "7":
        design_technology_topics()
    elif choice == "8":
        english_topics()
    elif choice == "9":
        pe_topics()
    elif choice == "10":
        maths_topics()
    elif choice == "11":
        art_design_topics()
    elif choice == "12":
        german_topics()
    elif choice == "13":
        french_topics()
    elif choice == "14":
        spanish_topics()
    else:
        print("not yet implemented")

subjects()