import doctest
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(20, 8), dpi = 90)

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR, 
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2


# column numbers of data within input csv file
INPUT_SID        = 0
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10

def create_date(date: str) -> Date:
    '''
    This is a helper function!
    This function returns a date tuple. 

    >>> create_date('15-Nov-19')
    (2019, 11, 15)

    >>> create_date('06-Sep-18')
    (2018, 9, 6)

    >>> create_date('05-Sep-18')
    (2018, 9, 5)
    '''
    list_date = date.split('-')
    dd, mm, yy = list_date

    if mm == 'Jan':
        mm = 1
    elif mm == 'Feb':
        mm = 2
    elif mm == 'Mar':
        mm = 3
    elif mm == 'Apr':
        mm = 4
    elif mm == 'May':
        mm = 5
    elif mm == "Jun":
        mm = 6
    elif mm == "Jul":
        mm = 7
    elif mm == "Aug":
        mm = 8
    elif mm == "Sep":
        mm = 9
    elif mm == "Oct":
        mm = 10
    elif mm == "Nov":
        mm = 11
    else:
        mm = 12
    
    year = '20' + str(yy)

    return (int(year), mm, int(dd))

def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]],
                                 dict[str, str]): # type: ignore
    """
    Populates and returns a tuple with the following 4 dictionaries
    with data from valid filename.
    
    4 dictionaries returned as a tuple:
    - dict[show id: date added to Netflix]
    - dict[show id: list of unique actor names]
    - dict[category: list of unique show ids]
    - dict[show id: show title]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show id: list of unique actor names]

    The list of actors for each key in
      dict[show id: list of unique actor names]
      should be in the order they appear on the line in the input file.
      If the line has duplicated actor names, the unique actor name 
      is added once for the first time it occurs in the line.
    
    Precondition: file is csv with data in expected columns 
        and contains a header row with column titles
        Show ids within the file are unique.
        
    >>> read_file('data_analysis_project/project/assignment9/0lines_data.csv')
    ({}, {}, {}, {})
    
    >>> read_file('data_analysis_project/project/assignment9/11lines_data.csv')  # doctest: +NORMALIZE_WHITESPACE
    ({'81217749': (2019, 11, 15),
      '70303496': (2018, 9, 6),
      '70142798': (2018, 9, 5),
      '80999063': (2018, 10, 5),
      '80190843': (2018, 9, 7),
      '80119349': (2017, 9, 29),
      '70062814': (2018, 9, 5),
      '80182115': (2017, 9, 29),
      '80187722': (2018, 10, 12),
      '70213237': (2018, 10, 2),
      '70121522': (2019, 8, 1)},
     {'81217749': ['Naseeruddin Shah'],
      '70303496': ['Aamir Khan',
                   'Anuskha Sharma',
                   'Sanjay Dutt',
                   'Saurabh Shukla',
                   'Parikshat Sahni',
                   'Sushant Singh Rajput',
                   'Boman Irani',
                   'Rukhsar'],
      '70142798': ['Jirayu La-ongmanee',
                   'Charlie Trairat',
                   'Worrawech Danuwong',
                   'Marsha Wattanapanich',
                   'Nicole Theriault',
                   'Chumphorn Thepphithak',
                   'Gacha Plienwithi',
                   'Suteerush Channukool',
                   'Peeratchai Roompol',
                   'Nattapong Chartpong'],
      '80999063': ['Elyse Maloway',
                   'Vincent Tong',
                   'Erin Matthews',
                   'Andrea Libman',
                   'Alessandro Juliani',
                   'Nicole Anthony',
                   'Diana Kaarina',
                   'Ian James Corlett',
                   'Britt McKillip',
                   'Kathleen Barr'],
      '70062814': ['Ananda Everingham',
                   'Natthaweeranuch Thongmee',
                   'Achita Sikamana',
                   'Unnop Chanpaibool',
                   'Titikarn Tongprasearth',
                   'Sivagorn Muttamara',
                   'Chachchaya Chalemphol',
                   'Kachormsak Naruepatr'],
      '80187722': ['Frank Grillo'],
      '70213237': ['Graham Chapman',
                   'Eric Idle',
                   'John Cleese',
                   'Michael Palin',
                   'Terry Gilliam',
                   'Terry Jones'],
      '70121522': ['Aamir Khan',
                   'Kareena Kapoor',
                   'Madhavan',
                   'Sharman Joshi',
                   'Omi Vaidya',
                   'Boman Irani',
                   'Mona Singh',
                   'Javed Jaffrey']},
     {'Documentaries': ['81217749', '80119349', '80182115'],
      'International Movies': ['81217749',
                               '70303496',
                               '70142798',
                               '80119349',
                               '70062814',
                               '70121522'],
      'Comedies': ['70303496', '70121522'],
      'Dramas': ['70303496', '70121522'],
      'Horror Movies': ['70142798', '70062814'],
      'Children & Family Movies': ['80999063'],
      'Docuseries': ['80190843', '80187722', '70213237'],
      'British TV Shows': ['70213237']},
     {'81217749': 'SunGanges',
      '70303496': 'PK',
      '70142798': 'Phobia 2',
      '80999063': 'Super Monsters Save Halloween',
      '80190843': 'First and Last',
      '80119349': 'Out of Thin Air',
      '70062814': 'Shutter',
      '80182115': 'Long Shot',
      '80187722': 'FIGHTWORLD',
      '70213237': "Monty Python's Almost the Truth",
      '70121522': '3 Idiots'})
    """
    # TODO: complete this function according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    id_date = {}
    id_name = {}
    category_id = {}
    id_title = {}
    file_handle = open(filename, 'r')
    file_handle.readline()
    for line in file_handle:
        contents = line.strip().split(',')
        sid = contents[INPUT_SID]
        date = create_date(contents[INPUT_DATE])
        id_date[sid] = date

        name_temp = []
        name = []
        if contents[INPUT_CAST] != '':
            name_temp = contents[INPUT_CAST].split(':')
        if name_temp:
            for temp in name_temp:
                if temp not in name:
                    name.append(temp)
            id_name[sid] = name

        category_temp = []
        category = []
        if contents[INPUT_CATEGORIES] != '':
            category_temp = contents[INPUT_CATEGORIES].split(':')
        for temp in category_temp:
            if temp not in category:
                category.append(temp)
        for cate in category:
            if cate not in category_id:
                category_id[cate] = [sid]
            else:
                category_id[cate].append(sid)

        id_title[sid] = contents[INPUT_TITLE]
    
    return (id_date, id_name, category_id, id_title)

def drawPic(filename: str):
    id_date, id_name, category_id, id_title = read_file(filename)
    id_li = []
    date_li = []
    for key in id_date:
        id_li.append(key)
        date_li.append(id_date[key])
    plt.xlabel("id")
    plt.ylabel("date")
    plt.plot(id_li,date_li)
    plt.show()

drawPic("data_analysis_project/project/assignment9/11lines_data.csv")


def is_before_date(date: Date, given_date: Date) -> bool:
    '''
    This is a helper function!
    This function can tell if the date is before the given date.

    >>> is_before_date((2021, 1, 1), (2024, 1, 1))
    True

    >>> is_before_date((2024, 1, 1), (2021, 1, 1))
    False

    >>> is_before_date((2024, 11, 11), (2024, 11, 12))
    True
    '''
    year, month, day = given_date
    yy, mm, dd = date
    is_before = None
    if yy < year:
        is_before = True
    elif yy > year:
        is_before = False
    else:
        if yy == year:
            if mm < month:
                is_before = True
            elif mm > month:
                is_before = False
            elif mm == month:
                if dd < day:
                    is_before = True
                else:
                    is_before = False

    return is_before

def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[tuple[str, str]]:
    """
    returns a list of sorted tuples containing (show title, show id) pairs 
    of only those shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
      If no actors are specified (empty list), all actors in library are valid;
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('data_analysis_project/project/assignment9/0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('data_analysis_project/project/assignment9/11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('data_analysis_project/project/assignment9/11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    [('3 Idiots', '70121522'), ('PK', '70303496')]
        
    >>> query('data_analysis_project/project/assignment9/11lines_data.csv', 'Comedies', (2019, 9, 5), ['Sanjay Dutt'])
    [('PK', '70303496')]
    
    >>> query('data_analysis_project/project/assignment9/11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('3 Idiots', '70121522'), ('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('data_analysis_project/project/assignment9/11lines_data.csv', 'International Movies', (2019, 8, 1), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('data_analysis_project/project/assignment9/11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either'])
    []
    
    >>> query('data_analysis_project/project/assignment9/11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'not found', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('data_analysis_project/project/assignment9/11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'Aamir Khan', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('data_analysis_project/project/assignment9/11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either', 'Aamir Khan']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('data_analysis_project/project/assignment9/large_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('PK', '70303496')]
    
    >>> query('data_analysis_project/project/assignment9/large_data.csv', 'Comedies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'),
     ('PK', '70303496'), ('Zed Plus', '81213884')]
    
    >>> query('data_analysis_project/project/assignment9/large_data.csv', 'International Movies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'), 
     ('Dangal', '80166185'), ('Dhobi Ghat (Mumbai Diaries)', '70144331'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'), 
     ('Lagaan', '60020906'), ('Madness in the Desert', '80229953'),
     ('PK', '70303496'), ('Raja Hindustani', '17457962'), 
     ('Rang De Basanti', '70047320'), ('Secret Superstar', '80245408'), 
     ('Shutter', '70062814'), ('Taare Zameen Par', '70087087'),
     ('Talaash', '70262614'), ('Zed Plus', '81213884')]

    >>> query('data_analysis_project/project/assignment9/input.csv', 'stick insect category', (2017, 9, 28), ['Connie Blum', 'Dada Berardi', 'Bob Koenig', 'Kanta MacAoidh','Uchenna MacAoidh'])
    []
    >>> query('data_analysis_project/project/assignment9/input3.csv', 'International Movies', (2019, 7, 28), [])
    [('Out of Thin Air', '80119349'), ('PK', '70303496'), ('Phobia 2', '70142798'), ('Shutter', '70062814')]

    >>> query('data_analysis_project/project/assignment9/large_data.csv', 'Documentaries', (2018, 7, 13), [])
    [('"Behind ""The Cove"": The Quiet Japanese Speak Out"', '80132127'), ('#Rucker50', '80147908'), ('(T)ERROR', '80039644'), ('100 Days Of Solitude', '81001804'), ("100 Years: One Woman's Fight for Justice", '80144983'), ('13TH', '80091741'), ('27: Gone Too Soon', '80213148'), ('42 Grams', '80205451'), ('A Family Affair', '80089199'), ('A Grand Night In: The Story of Aardman', '80144358'), ('A Gray State', '80190840'), ('A Murder in the Park', '80044562'), ('A Week in Watts', '80223123'), ('A new Capitalism', '80994442'), ('APEX: The Story of the Hypercar', '80109260'), ('Ai Weiwei: Never Sorry', '70229921'), ('Alias JJ:la celebridad del mal', '80203742'), ('Alien Contact: Outer Space', '80213403'), ('Alive and Kicking', '80105356'), ('AlphaGo', '80190844'), ('Amanda Knox', '80081155'), ('Amelia: A Tale of Two Sisters', '80158580'), ('American Anarchist', '80143794'), ('American Experience: Ruby Ridge', '80172000'), ('An American in Madras', '80158376'), ("Asperger's Are Us", '80104420'), ('At All Costs', '80104182'), ('Attacking the Devil: Harold Evans and the Last Nazi War Crime', '80104330'), ('Audrie & Daisy', '80097321'), ('Bachelor Girls', '80236167'), ('Bad Rap', '80134952'), ('Barbecue', '80182274'), ('Be Here Now', '80061160'), ('Beak & Brain: Genius Birds From Down Under', '80135631'), ('Beary Tales', '80135586'), ('Beauties of the Night', '80141787'), ('Before the Flood', '80141928'), ('Behind the Curtain: Todrick Hall', '80185032'), ('Being AP', '80078761'), ("Being Elmo: A Puppeteer's Journey", '70166234'), ('Belief: The Possession of Janet Moses', '80126016'), ('Best Worst Thing That Ever Could Have Happened', '80132964'), ('Betting on Zero', '80108609'), ('Beyond All Boundaries', '80172938'), ('Big Time', '80226076'), ('Bill Nye: Science Guy', '80182411'), ('Black Man White Skin', '80104041'), ('Blackfish', '70267802'), ('Blurred Lines: Inside the Art World', '80190585'), ('Bobbi Jene', '80190515'), ('Bobby Sands: 66 Days', '80126507'), ('Bombshell: The Hedy Lamarr Story', '80189827'), ('Born Strong', '80210716'), ('Born to Be Free', '80131414'), ('Breaking Free', '80220783'), ('Bugs', '80108610'), ('Burlesque: Heart of the Glitter Tribe', '80173267'), ('Casablancas: The Man Who Loved Women', '80137087'), ('Casting JonBenet', '80142316'), ('Catching the Sun', '80061161'), ('Celluloid Man', '80170612'), ('Chandani: The Daughter of the Elephant Whisperer', '70175127'), ('Chasing Coral', '80168188'), ('Chasing Trane', '80147403'), ('Children of God', '80106144'), ('Chris Brown: Welcome to My Life', '80196216'), ('City of God: 10 Years Later', '80116761'), ('Coffee for All', '80232894'), ('Command and Control', '80107656'), ('Concrete Football', '80184974'), ('Conor McGregor: Notorious', '80164752'), ('Cop Watchers', '80185723'), ('Countdown to Death: Pablo Escobar', '80175405'), ('Counterpunch', '80049873'), ('Covered: Alive in Asia', '80097423'), ('Cowspiracy: The Sustainability Secret', '80033772'), ('Cuba and the Cameraman', '80126449'), ('Cutie and the Boxer', '70267830'), ('Danny Says', '80095806'), ("Defying the Nazis: The Sharps' War", '80103430'), ('Democrats', '80052683'), ('Diana: 7 Days That Shook the World', '80195835'), ('Diana: In Her Own Words', '80221317'), ('Discovering Bigfoot', '80210182'), ("Don't Look Down", '80141261'), ('Down The Fence', '80216543'), ('Dream Big: Engineering Our World', '80217136'), ('Dream Boat', '80178882'), ('Dries', '80197427'), ('E-Team', '70299286'), ('Eddie - Strongman', '80142450'), ('El Che', '80193423'), ('El Viaje: Márama y Rombai', '80208635'), ('El fin de ETA', '80160972'), ('Elizabeth at 90: A Family Tribute', '80131167'), ('Elles ont toutes une histoire', '80144691'), ('Elles étaient en guerre (1914-1918)', '80230465'), ('Elles étaient en guerre 1939-1945', '80230555'), ('Elstree 1976', '80095641'), ('Empire of Scents', '80192627'), ('End Game', '80210691'), ('Enlighten Us', '80133139'), ("Eve's Apple", '80202713'), ('Exit Afghanistan', '80114498'), ('Expedition China', '80224924'), ('Expedition Happiness', '80224476'), ('Extremis', '80106307'), ('Famous in Ahmedabad', '80139507'), ('Feel Rich', '80128689'), ('Figures of Speech', '80132411'), ('Fire at Sea', '80100945'), ('Fire in the Blood', '70268209'), ('Fishpeople', '80196139'), ('Food on the Go', '80233511'), ('Footprints: The Path of Your Life', '80127764'), ('For Grace', '80058979'), ('For the Love of Spock', '80115102'), ('Forbidden Games: The Justin Fashanu Story', '80191930'), ('Forever Pure', '80148223'), ('Franca: Chaos and Creation', '80147971'), ('Frank and Cindy', '80085438'), ('Freeway: Crack in the System', '80018252'), ('From One Second to the Next', '70302184'), ('Functional Fitness', '80196217'), ('GLOW: The Story of the Gorgeous Ladies of Wrestling', '70296765'), ('Gaga: Five Foot Two', '80196586'), ('Gender Revolution: A Journey with Katie Couric', '80186731'), ('Generation Iron 2', '80172937'), ('Get Me Roger Stone', '80114666'), ('Ghost of the Mountains', '80198046'), ('Gringo: The Dangerous Life of John McAfee', '80148180'), ('Growing Up Coy', '80128657'), ('Growing Up Wild', '80158772'), ('Gun Runners', '80124947'), ('Harry Benson: Shoot First', '80095094'), ('Harry and Snowman', '80105342'), ('Haunters: The Art of the Scare', '80213401'), ('He Named Me Malala', '80048218'), ('Heroin(e)', '80192445'), ('Highly Strung', '80134682'), ('Hiroshima: The Real History', '80131168'), ('Hitler - A Career', '80106791'), ("Hitler's Olympics", '80107987'), ("Hitler's Steel Beast", '80208211'), ('Holy Hell', '80097438'), ('Hostage to the Devil', '80119140'), ('Hostages', '80208468'), ('Hot Girls Wanted', '80038162'), ('House of Z', '80200744'), ('How the Beatles Changed the World', '80195654'), ('How to Change the World', '80036832'), ('How to Stage a Coup', '80158769'), ('How to Win the US Presidency', '80108147'), ('I Am Bolt', '80135360'), ('I Am Jane Doe', '80167459'), ('I Am Sun Mu', '80154179'), ('I Called Him Morgan', '80147988'), ("I'll Sleep When I'm Dead", '80118930'), ('Icarus', '80168079'), ('Ice Guardians', '80150246'), ('Incorruptible', '80061314'), ('Influx', '80225907'), ('Interview with a Serial Killer', '80108996'), ('Into the Inferno', '80066073'), ('Iverson', '80011846'), ('JFK: The Making of a President', '80158588'), ('Jackie: A Tale of Two Sisters', '80158579'), ('Jeremiah Tower: The Last Magnificent', '80107030'), ("Jeremy Scott: The People's Designer", '80064521'), ('Jerry Seinfeld: Comedian', '60024976'), ("Jewel's Catch One", '80990829'), ('Jim & Andy: The Great Beyond - Featuring a Very Special:Contractually Obligated Mention of Tony Clifton', '80209608'), ('Joan Didion: The Center Will Not Hold', '80117454'), ('Joe Cocker: Mad Dog with Soul', '80164112'), ('John & Jane', '80115844'), ('John Mellencamp: Plain Spoken', '80227121'), ('Joshua: Teenager vs. Superpower', '80169348'), ('Justin Bieber: Never Say Never', '70169918'), ('Keith Richards: Under the Influence', '80066798'), ('Kingdom of Us', '80158844'), ('Know Your Enemy - Japan', '80119190'), ('Koko: The Gorilla Who Talks', '80172471'), ('LA 92', '80184131'), ('LEGO House - Home of the Brick', '81002885'), ('Ladies First', '80219143'), ('Laerte-se', '80142223'), ('Le K Benzema', '80241876'), ('Les Bleus - Une autre histoire de France:1996-2016', '80164075'), ('Let It Fall: Los Angeles 1982-1992', '80183783'), ('Let There Be Light', '80119187'), ('Liberated: The New Sexual Revolution', '80222248'), ('Life 2.0', '70129457'), ('Lo and Behold: Reveries of the Connected World', '80097363'), ('Long Shot', '80182115'), ('Long Time Running', '80205085'), ('Los Niños Héroes de Chapultepec', '80219340'), ('Losing Sight of Shore', '80169548'), ('LoveTrue', '80108613'), ('Maddman: The Steve Madden Story', '80197301'), ('Madness in the Desert', '80229953'), ('Magnus', '80118004'), ('Manolo: The Boy Who Made Shoes for Lizards', '80189955'), ('Martin Luther: The Idea that Changed the World', '80217436'), ('Martyrs of Marriage', '80239988'), ('Marvel & ESPN Films Present: 1 of 1: Genesis', '80023794'), ('Maya Angelou: And Still I Rise', '80097361'), ('Meet the Trumps: From Immigrant to President', '80219941'), ('Mercury 13', '80174436'), ('Michael Lost and Found', '80186862'), ('Miss Representation', '70167128'), ('Miss Sharon Jones!', '80079428'), ('Mission Blue', '70308278'), ('Mission Control: The Unsung Heroes of Apollo', '80175483'), ('Mitt', '70296733'), ('Mortified Nation', '70251218'), ('Mostly Sunny', '80132961'), ('Mr. Gaga: A True Story of Love and Dance', '80104706'), ('My Beautiful Broken Brain', '80049951'), ('My Own Man', '80011848'), ('My Scientology Movie', '80148179'), ('My Way', '80148275'), ('Naga The Eternal Yogi', '80168052'), ("Naledi: A Baby Elephant's Tale", '80135296'), ('National Bird', '80106754'), ('National Parks Adventure', '80217040'), ('Nature: Raising the Dinosaur Giant', '80172468'), ('Nazi Concentration Camps', '80119192'), ('Newtown', '80097466'), ('Nobody Speak: Trials of the Free Press', '80168227'), ('Norman Lear: Just Another Version of You', '80097360'), ('Not Alone', '80196138'), ('Notes on Blindness', '80098842'), ('Now More Than Ever: The History of Chicago', '80138615'), ('Numbered', '80208084'), ('Numero Zero. The Roots of Italian Rap', '80992231'), ('Oklahoma City', '80169778'), ('On Yoga The Architecture of Peace', '80187188'), ('One Heart: The A.R. Rahman Concert Film', '80216270'), ('One More Shot', '80195807'), ('One in a Billion', '80142615'), ('One of Us', '80118101'), ('Out of Thin Air', '80119349'), ('Pablo Escobar: Angel or Demon?', '70204282'), ('Pacificum: Return to the Ocean', '80991025'), ('Palio', '80052790'), ('Paris Is Burning', '60036691'), ('Patient Seventeen', '80214582'), ('Pedal the World', '80245626'), ('Perú: Tesoro escondido', '80217495'), ('Peter and the Farm', '80107737'), ('Prelude to War', '60027945'), ('Prescription Thugs', '80058247'), ('Print the Legend', '80005444'), ('Radical: the Controversial Saga of Dada Figueiredo', '80164207'), ('Raiders!: The Story of the Greatest Fan Film Ever Made', '80045805'), ('Ram Dass:Going Home', '80209895'), ('Rats', '80136440'), ('Real Crime: Diamond Geezers', '80109248'), ('Real Crime: Supermarket Heist (Tesco Bomber)', '80108998'), ('Recovery Boys', '80177782'), ('Red Trees', '80206758'), ('Refugee', '80160127'), ('Reincarnated', '70261178'), ('Residente', '80184547'), ('Restless Creature: Wendy Whelan', '80173625'), ('Resurface', '80184055'), ('Roberto Saviano: Writing Under Police Protection', '80245268'), ('Rocco', '80160358'), ('Rolling Papers', '80046727'), ('Roots', '80216268'), ('Rush: Beyond the Lighted Stage', '70137744'), ('S Is for Stanley', '80172284'), ('SHOT! The Psycho-Spiritual Mantra of Rock', '80168033'), ('Sacro GRA', '70293820'), ('Saeed Mirza: The Leftist Sufi', '80182105'), ('Sample This', '70290909'), ('San Pietro', '80119188'), ('Saudi Arabia Uncovered', '80118888'), ('Saving Capitalism', '80127558'), ('Secrets of Althorp - The Spencers', '80003150'), ('Secrets of Chatsworth', '80003151'), ("Secrets of Henry VIII's Palace: Hampton Court", '80003152'), ("Secrets of Her Majesty's Secret Service", '80012477'), ('Secrets of Highclere Castle', '80003153'), ('Secrets of Scotland Yard', '70296578'), ('Secrets of Selfridges', '70296574'), ('Secrets of Underground London', '70309257'), ('Secrets of Westminster', '80012520'), ('Secrets of the Tower of London', '70296573'), ('Seeing Allred', '80174367'), ('Silicon Cowboys', '80104318'), ('Sky Ladder: The Art of Cai Guo-Qiang', '80097472'), ('Skydancers', '80994807'), ('Smash: Motorized Mayhem', '80128688'), ('Sons of Ben', '80132410'), ('Sour Grapes', '80029708'), ('Star Men', '80167667'), ('Stealing History', '80114700'), ('Stop at Nothing: The Lance Armstrong Story', '80007215'), ('Strike a Pose', '80118918'), ('Strong Island', '80168230'), ('Survivors Guide to Prison', '80220758'), ('Sustainable', '80134814'), ('Take Your Pills', '80117831'), ('Teach Us All', '80198423'), ('Team Foxcatcher', '80044093'), ('Terra', '80102305'), ("The B-Side: Elsa Dorfman's Portrait Photography", '80145699'), ('The Bad Kids', '80097468'), ('The Battered Bastards of Baseball', '70299904'), ('The Battle of Midway', '60027942'), ('The Bomb', '80080106'), ('The C Word', '80126485'), ('The Carter Effect', '80223149'), ('The Death and Life of Marsha P. Johnson', '80189623'), ('The Fear of 13', '80099305'), ('The Force', '80168198'), ('The Free Man', '80162195'), ('The House on Coco Road', '80190144'), ('The Human Factor: The Untold Story of the Bombay Film Orchestras', '80171439'), ('The Hurt Business', '80152745'), ('The Ivory Game', '80117533'), ('The Jack King Affair', '80208083'), ('The Land of the Enlightened', '80097375'), ('The Last Man on the Moon', '80087933'), ('The Last Shaman', '80121855'), ('The Legend of 420', '80173271'), ('The Look of Silence', '80016401'), ('The Lovers and the Despot', '80097376'), ('The Magic Pill', '80238655'), ('The Man Who Would Be Polka King', '70120182'), ('The Mars Generation', '80117263'), ('The Memphis Belle: A Story of a Flying Fortress', '80119194'), ('The Mitfords: A Tale of Two Sisters', '80158581'), ('The NSU-Complex', '80136332'), ('The Negro Soldier', '80119191'), ('The Other One: The Long Strange Trip of Bob Weir', '80011852'), ('The Rachel Divide', '80149821'), ('The Rat Race', '80145085'), ('The Real Miyagi', '80094358'), ('The Redeemed and the Dominant: Fittest on Earth', '80176064'), ('The Reservoir Game', '80226236'), ('The Russian Revolution', '80158770'), ('The Search for Life in Space', '80217041'), ('The Secret', '70063484'), ('The Seven Five', '80035467'), ('The Short Game', '70290567'), ('The Square', '70268449'), ('The Sunshine Makers', '80098305'), ('The Trader (Sovdagari)', '80209006'), ('The Truth About Alcohol', '80185861'), ('The White Helmets', '80101827'), ('The Women Who Kill Lions', '80185722'), ('Theater of Life', '80154884'), ('Theo Who Lived', '80101609'), ('This Was Tomorrow', '80092409'), ('Thunderbolt', '80119193'), ('Tig', '80028208'), ('To Be a Miss', '80144141'), ('Todo Sobre El Asado', '80190990'), ('Tokyo Idols', '80163353'), ('Tony Robbins: I Am Not Your Guru', '80102204'), ('Treasures from the Wreck of the Unbelievable', '80217857'), ('Tree Man', '80128692'), ('Trophy', '80168084'), ('Tunisian Victory', '80119189'), ('Twice', '80208212'), ('Tyke Elephant Outlaw', '80066806'), ('Unacknowledged', '80171742'), ('Unchained: The Untold Story of Freestyle Motocross', '80109089'), ('Undefeated', '70177633'), ('Under an Arctic Sky', '80216662'), ('Undercover: How to Operate Behind Enemy Lines', '80119186'), ('Unrest', '80168300'), ('Vegas Baby', '80195243'), ('Vikings Unearthed', '80172469'), ('Virunga', '80009431'), ('Virunga: Gorillas in Peril', '80038290'), ('Voyeur', '80176212'), ('WWII: Report from the Aleutians', '70022548'), ('Walk with Me', '80182034'), ('Water & Power: A California Heist', '80168231'), ('We:the Marines', '80217135'), ('What Happened:Miss Simone?', '70308063'), ('What We Started', '80217120'), ('What the Health', '80174177'), ('When Hari Got Married', '80145086'), ('When Two Worlds Collide', '80097475'), ('Who the F**k Is That Guy?', '80173269'), ('Why Knot', '80211540'), ('Why We Fight: The Battle of Russia', '70013050'), ('Williams', '80196135'), ('Winnie', '80170119'), ("Winter on Fire: Ukraine's Fight for Freedom", '80031666'), ('Without Gorky', '80176144')]
    """
    # TODO: complete this function according to the documentation
    id_date, id_name, category_id, id_title = read_file(filename)
    given_category_id = []
    actor_in_actors_id = []
    is_before_date_id = []
    ans_id = []
    ans = []
    for cate in category_id:
        if cate == category:
            given_category_id += category_id[cate]

    if actors == []:
        for id in given_category_id:
            actor_in_actors_id.append(id)
    else:
        for id in id_name:
            for actor in actors:
                if actor in id_name[id]:
                    actor_in_actors_id.append(id)
    
    for id in id_date:
        if is_before_date(id_date[id], date):
            is_before_date_id.append(id)
    
    for item in given_category_id:
        if item in actor_in_actors_id and item in is_before_date_id:
            ans_id.append(item)
    
    for id in id_title:
        if id in ans_id:
            ans.append((id_title[id], id))
    
    ans.sort()
    return ans

print(doctest.testmod())