import datetime
import urllib.request
import urllib.parse
import json
import re
import ssl

# --- Global Data for Literary Devices and Literature Guides ---

LITERARY_DEVICES = {
    "metaphor": {
        "definition": "A direct comparison between two unrelated things without using 'like' or 'as'.",
        "example": "'Love is a battlefield' or 'The classroom was a zoo.'",
        "analysis_tip": "Look at the qualities of the comparison source and how they apply to the subject. What feelings or ideas does this comparison evoke?"
    },
    "simile": {
        "definition": "A comparison between two unrelated things using 'like' or 'as'.",
        "example": "'Her cheeks were like roses' or 'As brave as a lion.'",
        "analysis_tip": "Similes establish a connection but keep the two objects separate. Consider why the author chose to compare them using 'like' or 'as' rather than making it a direct metaphor."
    },
    "personification": {
        "definition": "Attributing human characteristics, emotions, or behaviors to non-human things or abstract ideas.",
        "example": "'The wind whispered in the night' or 'The flowers danced in the breeze.'",
        "analysis_tip": "Consider how giving human traits to the object affects the reader's empathy or helps visualize the setting and atmosphere."
    },
    "hyperbole": {
        "definition": "An extreme, deliberate exaggeration used for emphasis or effect.",
        "example": "'I've told you a million times' or 'I'm so hungry I could eat a horse.'",
        "analysis_tip": "Determine what the author is trying to highlight through exaggeration. Is it humor, frustration, urgency, or intensity?"
    },
    "understatement": {
        "definition": "The deliberate presentation of something as being smaller, worse, or less important than it actually is.",
        "example": "Describing a huge storm as 'a bit of rain' or Mercutio describing his fatal wound as 'a scratch' in Romeo and Juliet.",
        "analysis_tip": "Understatement often creates irony, humor, or emphasizes the severity of a situation by contrasting it with a casual reaction."
    },
    "alliteration": {
        "definition": "The repetition of the same consonant sound at the beginning of adjacent or closely connected words.",
        "example": "'Peter Piper picked a peck of pickled peppers.'",
        "analysis_tip": "Pay attention to the sound quality. Fast, sharp sounds (like 't' or 'p') can create tension or speed, while soft sounds (like 's' or 'm') can create a soothing or sinister mood."
    },
    "onomatopoeia": {
        "definition": "Words that mimic the natural sounds of the objects or actions they describe.",
        "example": "'Buzz', 'hiss', 'clang', 'boom', 'splat'.",
        "analysis_tip": "Onomatopoeia enhances imagery and sensory details, making the scene feel more immersive and immediate."
    },
    "foreshadowing": {
        "definition": "Hints or clues about what will happen later in the story.",
        "example": "In Romeo and Juliet, Romeo says, 'My mind misgives / Some consequence yet hanging in the stars,' before entering the Capulet party.",
        "analysis_tip": "Analyze how foreshadowing builds suspense and tension, and how it makes the eventual outcome feel inevitable or tragic."
    },
    "irony": {
        "definition": "A contrast between expectation and reality. It comes in three main forms: Verbal (saying the opposite of what is meant), Situational (an outcome contrary to expectations), and Dramatic (the audience knows something the characters do not).",
        "example": "A fire station burning down (situational); saying 'What lovely weather' during a hurricane (verbal); in Romeo and Juliet, the audience knows Juliet is asleep, but Romeo thinks she is dead (dramatic).",
        "analysis_tip": "Identify the type of irony. How does it affect the tone? In dramatic irony, how does it heighten suspense or tragedy for the audience?"
    },
    "symbolism": {
        "definition": "Using an object, person, situation, or color to represent a deeper abstract meaning beyond its literal sense.",
        "example": "The green light in The Great Gatsby representing Gatsby's hopes and dreams for the future.",
        "analysis_tip": "Trace the symbol throughout the work. Does its meaning evolve? How does it reinforce the central themes of the story?"
    },
    "imagery": {
        "definition": "Vivid descriptive language that appeals to the five senses (visual, auditory, olfactory, gustatory, tactile).",
        "example": "'The warm aroma of freshly baked bread drifted through the damp, chilly kitchen.'",
        "analysis_tip": "Identify which senses are targeted. What mood or emotional response does this sensory description elicit?"
    },
    "juxtaposition": {
        "definition": "Placing two contrasting concepts, characters, or settings side-by-side to highlight their differences.",
        "example": "Charles Dickens' opening: 'It was the best of times, it was the worst of times.'",
        "analysis_tip": "Examine the contrast. What does the comparison reveal about each element that wouldn't be obvious on its own?"
    },
    "oxymoron": {
        "definition": "A figure of speech pairing two contradictory terms.",
        "example": "'Jumbo shrimp', 'deafening silence', 'seriously funny', 'cruel kindness'.",
        "analysis_tip": "Oxymorons highlight tension, complexity, or conflicting emotions (e.g., Romeo's 'loving hate')."
    },
    "paradox": {
        "definition": "A statement that seems self-contradictory but reveals a deeper truth.",
        "example": "'I must be cruel only to be kind' (Hamlet) or 'The child is father of the man' (Wordsworth).",
        "analysis_tip": "Look past the surface contradiction to find the underlying philosophical or emotional truth the author is conveying."
    },
    "allusion": {
        "definition": "An indirect reference to a well-known person, place, event, literary work, or work of art (often mythological, biblical, or historical).",
        "example": "Describing a difficult path as 'a road to Damascus' or a person's weakness as their 'Achilles' heel.'",
        "analysis_tip": "Consider what context the alluded work brings. What associations does the reader automatically make when they recognize the reference?"
    }
}

CLASSIC_LITERATURE_GUIDES = {
    "1984": {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian Fiction, Political Fiction",
        "year": 1949,
        "summary": "Set in a totalitarian state called Oceania, the novel follows Winston Smith, a low-ranking member of the Ruling Party who secretly hates the Party and dreams of rebellion. He enters a forbidden love affair with Julia, but they are ultimately captured, tortured, and brainwashed by the Ministry of Love.",
        "characters": [
            {"name": "Winston Smith", "description": "The protagonist, a pensive citizen who works at the Ministry of Truth rewriting history. He secretly rebels against the totalitarian regime."},
            {"name": "Julia", "description": "Winston's lover, a pragmatic rebel who works in the Fiction Department. She rebels for personal pleasure rather than political ideology."},
            {"name": "O'Brien", "description": "A powerful member of the Inner Party who tricks Winston into believing he is part of a secret rebellion, only to betray and torture him."},
            {"name": "Big Brother", "description": "The perceived ruler of Oceania, whose face is on posters everywhere. He represents the omnipresence of the Party's surveillance."}
        ],
        "themes": [
            {"theme": "Totalitarianism and Surveillance", "description": "The Party maintains control through constant monitoring (telescreens), psychological manipulation, and rewriting history."},
            {"theme": "Individualism vs. Collectivism", "description": "Winston's struggle to maintain his personal identity and memory in a society that demands absolute conformity."},
            {"theme": "Language as Control (Newspeak)", "description": "The restriction of language to limit range of thought, making thoughtcrime literally impossible."}
        ],
        "quotes": [
            {"quote": "War is peace. Freedom is slavery. Ignorance is strength.", "context": "The official slogans of the Party, carved into the Ministry of Truth.", "analysis": "Demonstrates 'doublethink'—the ability to hold two contradictory beliefs simultaneously and accept both."},
            {"quote": "Big Brother is watching you.", "context": "Seen on posters throughout London.", "analysis": "A reminder of constant surveillance and the psychological control it exerts over citizens."},
            {"quote": "If you want a picture of the future, imagine a boot stamping on a human face—forever.", "context": "O'Brien speaking to Winston during his torture in Room 101.", "analysis": "The ultimate expression of the Party's motive: pure, unadulterated power."}
        ]
    },
    "the great gatsby": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Modernist Fiction, Tragedy",
        "year": 1925,
        "summary": "Narrated by Nick Carraway, the novel tells the story of Jay Gatsby, a mysterious millionaire who throws lavish parties in hope of attracting his former love, Daisy Buchanan, who is now married to the wealthy Tom Buchanan. Gatsby's romantic obsession leads to tragedy and death.",
        "characters": [
            {"name": "Jay Gatsby", "description": "A fabulously wealthy young man living in West Egg. He is famous for his lavish parties, but his sole motivation is to win back Daisy Buchanan."},
            {"name": "Nick Carraway", "description": "The narrator, a young bond salesman from the Midwest who rents a small cottage next to Gatsby's mansion and is Daisy's cousin."},
            {"name": "Daisy Buchanan", "description": "Gatsby's former love, now married to Tom Buchanan. She represents the hollow allure of old money and upper-class life."},
            {"name": "Tom Buchanan", "description": "Daisy's wealthy husband, an arrogant, hypocritical bully who comes from 'old money' and holds deeply elitist views."}
        ],
        "themes": [
            {"theme": "The Decline of the American Dream", "description": "The corruption of the American Dream, shifting from hard work and idealism to materialism, excess, and social climbing."},
            {"theme": "Class and Social Status", "description": "The unbridgeable divide between 'new money' (West Egg) and 'old money' (East Egg)."},
            {"theme": "Love and Obsession", "description": "Gatsby's inability to accept the past and his idealization of Daisy, which blinds him to reality."}
        ],
        "quotes": [
            {"quote": "So we beat on, boats against the current, borne back ceaselessly into the past.", "context": "The famous closing line of the novel.", "analysis": "Metaphor for humanity's struggle to move forward while constantly drawn back by our past dreams and memories."},
            {"quote": "I hope she'll be a fool—that's the best thing a girl can be in this world, a beautiful little fool.", "context": "Daisy describing her hopes for her infant daughter.", "analysis": "Reflects the limited options for women in the 1920s and Daisy's cynical view of her own life and marriage."},
            {"quote": "Gatsby believed in the green light, the orgastic future that year by year recedes before us.", "context": "Nick reflecting on Gatsby's dream.", "analysis": "The green light represents Gatsby's hopes, but also the general human pursuit of an elusive future."}
        ]
    },
    "to kill a mockingbird": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Southern Gothic, Bildungsroman",
        "year": 1960,
        "summary": "Set in Maycomb, Alabama during the Great Depression, the story is narrated by young Scout Finch. Her father, Atticus Finch, is a principled lawyer appointed to defend Tom Robinson, a Black man falsely accused of raping a white woman, Mayella Ewell. The novel explores themes of racial injustice and the destruction of innocence.",
        "characters": [
            {"name": "Scout Finch", "description": "The narrator and protagonist, a tomboy growing up in Maycomb, learning lessons about empathy and human nature."},
            {"name": "Atticus Finch", "description": "Scout's father, a wise, moral lawyer who defends Tom Robinson and teaches his children tolerance and integrity."},
            {"name": "Jem Finch", "description": "Scout's older brother, who is deeply affected by the injustice and prejudice he witnesses during the trial."},
            {"name": "Arthur 'Boo' Radley", "description": "A reclusive neighbor who has become the subject of local legend, but turns out to be a protector and friend to the children."}
        ],
        "themes": [
            {"theme": "Racial Injustice and Prejudice", "description": "The deep-seated racial prejudice of the Jim Crow South that overrides evidence and fairness in court."},
            {"theme": "The Coexistence of Good and Evil", "description": "The transition of Scout and Jem from childhood innocence (believing all people are good) to a mature understanding of human flaws and hatred."},
            {"theme": "Empathy and Moral Courage", "description": "Atticus's philosophy of walking in another person's shoes before judging them."}
        ],
        "quotes": [
            {"quote": "You never really understand a person until you consider things from his point of view... until you climb into his skin and walk around in it.", "context": "Atticus giving advice to Scout after her first day of school.", "analysis": "The central moral philosophy of the book: the importance of empathy and perspective."},
            {"quote": "Shoot all the bluejays you want, if you can hit 'em, but remember it's a sin to kill a mockingbird.", "context": "Atticus explaining why he doesn't want the children shooting mockingbirds.", "analysis": "The mockingbird symbolizes innocence; killing one represents destroying those who do no harm and only bring beauty to the world (like Tom Robinson and Boo Radley)."},
            {"quote": "Real courage is when you know you're licked before you begin, but you begin anyway and see it through no matter what.", "context": "Atticus explaining to Jem why Mrs. Dubose was a courageous woman.", "analysis": "Defines moral courage as standing up for what's right even when victory is impossible."}
        ]
    },
    "romeo and juliet": {
        "title": "Romeo and Juliet",
        "author": "William Shakespeare",
        "genre": "Tragedy",
        "year": 1597,
        "summary": "In Verona, Italy, two noble families, the Capulets and the Montagues, are locked in a deadly feud. Romeo Montague and Juliet Capulet fall deeply in love and marry in secret. A series of misunderstandings, fueled by violence and fate, leads to the tragic suicides of both lovers, which finally unites their grieving families.",
        "characters": [
            {"name": "Romeo Montague", "description": "A passionate, impulsive young man who falls in love with Juliet and ignores the family feud."},
            {"name": "Juliet Capulet", "description": "A young, strong-willed Capulet girl who exhibits maturity and bravery in her devotion to Romeo."},
            {"name": "Friar Laurence", "description": "A well-meaning monk who marries the couple in secret, hoping to end the feud, and devises the plan with the sleeping potion."},
            {"name": "Mercutio", "description": "Romeo's witty, cynical friend whose hot temper leads to his death at Tybalt's hands, cursing both houses."}
        ],
        "themes": [
            {"theme": "Love as an Overpowering Force", "description": "The intense, consuming nature of romantic love that overrides family, law, and self-preservation."},
            {"theme": "Fate vs. Free Will", "description": "The role of fate ('star-crossed lovers') in driving the couple to their inevitable tragic end."},
            {"theme": "Individual vs. Society", "description": "The conflict between personal desire and societal duties, expectations, and family obligations."}
        ],
        "quotes": [
            {"quote": "What's in a name? That which we call a rose / By any other name would smell as sweet.", "context": "Juliet speaking on her balcony, wishing Romeo didn't bear the Montague name.", "analysis": "Argues that names are arbitrary and do not define the essence of a person."},
            {"quote": "A plague o' both your houses!", "context": "Mercutio's dying words after being stabbed by Tybalt under Romeo's arm.", "analysis": "Marks the turning point from comedy to tragedy; his curse foreshadows the downfall of both families."},
            {"quote": "For never was a story of more woe / Than this of Juliet and her Romeo.", "context": "Prince Escalus's final lines closing the play.", "analysis": "A couplet summarizing the profound tragedy of the star-crossed lovers."}
        ]
    },
    "macbeth": {
        "title": "Macbeth",
        "author": "William Shakespeare",
        "genre": "Tragedy",
        "year": 1606,
        "summary": "Macbeth, a brave Scottish general, receives a prophecy from three witches that he will become King. Urged on by his ambitious wife, he murders King Duncan and seizes the throne. Consumed by guilt and paranoia, he becomes a tyrannical ruler, committing more murders to secure his power, leading to a civil war and his own downfall.",
        "characters": [
            {"name": "Macbeth", "description": "A Scottish general who becomes Thane of Cawdor, then King. Ambition drives him to murder, which leads to madness and tyranny."},
            {"name": "Lady Macbeth", "description": "Macbeth's ambitious wife who ruthlessly pushes him to commit regicide, but is eventually consumed by guilt and sleepwalks to her death."},
            {"name": "The Three Witches", "description": "Mysterious, supernatural beings who manipulate Macbeth with prophecies, feeding his ambition and false sense of security."},
            {"name": "Banquo", "description": "Macbeth's brave co-commander whose descendants are prophesied to rule Scotland. Macbeth murders him to protect his throne."}
        ],
        "themes": [
            {"theme": "Unchecked Ambition", "description": "How the pursuit of power corrupts moral boundaries, destroying both Macbeth and Lady Macbeth."},
            {"theme": "Fate and Prophecy", "description": "The question of whether the witches' prophecies are pre-destined fate or self-fulfilling prophecies driven by Macbeth's choices."},
            {"theme": "Guilt and Madness", "description": "The psychological toll of murder, represented by blood imagery, sleeplessness, and hallucinations (Banquo's ghost)."}
        ],
        "quotes": [
            {"quote": "Fair is foul, and foul is fair / Hover through the fog and filthy air.", "context": "The witches chanting in the opening scene.", "analysis": "Establishes the theme of moral inversion and deception—things are not always as they appear."},
            {"quote": "Out, damned spot! out, I say!", "context": "Lady Macbeth sleepwalking, hallucinating blood on her hands.", "analysis": "Demonstrates her psychological breakdown and the inescapable guilt that haunts her."},
            {"quote": "Life's but a walking shadow, a poor player / That struts and frets his hour upon the stage / And then is heard no more. It is a tale / Told by an idiot, full of sound and fury, / Signifying nothing.", "context": "Macbeth's reaction to news of Lady Macbeth's death.", "analysis": "A profound expression of nihilism; Macbeth realizes all his ambitious efforts have resulted in a meaningless, empty existence."}
        ]
    }
}

WORDINESS_PATTERNS = {
    r"\bat this point in time\b": "now",
    r"\bdue to the fact that\b": "because",
    r"\bin spite of the fact that\b": "although",
    r"\bin order to\b": "to",
    r"\bfor the purpose of\b": "to",
    r"\bwith the exception of\b": "except",
    r"\bin the near future\b": "soon",
    r"\bat the end of the day\b": "ultimately",
    r"\ba large number of\b": "many",
    r"\btake into consideration\b": "consider",
    r"\bmake an effort\b": "try",
    r"\bhas the ability to\b": "can",
    r"\bconduct an investigation\b": "investigate",
    r"\bby means of\b": "by",
    r"\bcoupled with the fact that\b": "and",
    r"\bin close proximity to\b": "near",
    r"\bin the event that\b": "if",
    r"\buntil such time as\b": "until",
}

PASSIVE_VOICE_PATTERN = re.compile(
    r"\b(am|is|are|was|were|be|been|being)\b\s+(?:[a-zA-Z]+ly\s+)?([a-zA-Z]+ed|done|seen|written|given|taken|known|made|built|chosen|eaten|broken|heard|read|understood|run|kept|left|lost|met|paid|sat|spent|stood|told|thought|won|bought|brought|caught|dealt|felt|fought|held|hurt|laid|led|meant|sent|shot|shut|sold|sung|swept|taught|torn|worn)\b",
    re.IGNORECASE
)


# --- Helper functions ---

def _count_syllables_word(word: str) -> int:
    """Estimates the number of syllables in a single English word."""
    word = word.lower().strip(".:,;!?()\"'-")
    if not word or not word.isalpha():
        return 0
    vowels = "aeiouy"
    count = 0
    prev_was_vowel = False
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel
    if word.endswith("e"):
        count -= 1
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        count += 1
    if count <= 0:
        count = 1
    return count

def _split_sentences(text: str) -> list[str]:
    """Splits text into sentences, ignoring common abbreviations."""
    abbrev_pattern = r"(?<!Mr)(?<!Mrs)(?<!Dr)(?<!Prof)(?<!Sr)(?<!Jr)(?<!Gen)(?<!Rep)(?<!Sen)(?<!St)(?<!a\.m)(?<!p\.m)(?<!e\.g)(?<!i\.e)(?<!vs)"
    sentence_endings = re.compile(abbrev_pattern + r"[.!?]\s+")
    sentences = sentence_endings.split(text)
    return [s.strip() for s in sentences if s.strip()]

def _std_dev(values: list[float]) -> float:
    """Computes the sample standard deviation of a list of numbers."""
    if len(values) <= 1:
        return 0.0
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return variance ** 0.5


# --- Exposed Tools ---

def check_readability_and_style(text: str) -> dict:
    """
    Analyzes an essay or text block for readability grade level, sentence structure, 
    clichés, wordy phrases, passive voice, and repetitive vocabulary.
    Use this tool when students ask for feedback, editing help, or proofreading on their writing.
    
    Args:
        text: The draft writing or essay content to analyze.
        
    Returns:
        A dictionary containing readability scores, structural stats, and a list of style suggestions.
    """
    if not text.strip():
        return {"status": "error", "message": "Text content is empty."}

    sentences = _split_sentences(text)
    words = re.findall(r"\b[a-zA-Z']+\b", text)
    
    num_sentences = max(len(sentences), 1)
    num_words = max(len(words), 1)
    num_chars = len(text)
    
    syllables = [_count_syllables_word(w) for w in words]
    total_syllables = sum(syllables)
    complex_words = sum(1 for s in syllables if s >= 3)
    
    # Calculate Readability Scores
    avg_sentence_len = num_words / num_sentences
    avg_syllables_per_word = total_syllables / num_words
    
    # Flesch Reading Ease
    flesch_ease = 206.835 - (1.015 * avg_sentence_len) - (84.6 * avg_syllables_per_word)
    flesch_ease = round(flesch_ease, 2)
    
    # Flesch-Kincaid Grade Level
    fk_grade = (0.39 * avg_sentence_len) + (11.8 * avg_syllables_per_word) - 15.59
    fk_grade = round(fk_grade, 2)
    
    # Gunning Fog Index
    pct_complex = (complex_words / num_words) * 100
    gunning_fog = 0.4 * (avg_sentence_len + pct_complex)
    gunning_fog = round(gunning_fog, 2)
    
    # Readability description
    if flesch_ease >= 90:
        readability_desc = "Very Easy (5th grade level)"
    elif flesch_ease >= 80:
        readability_desc = "Easy (6th grade level)"
    elif flesch_ease >= 70:
        readability_desc = "Fairly Easy (7th grade level)"
    elif flesch_ease >= 60:
        readability_desc = "Standard (8th-9th grade level)"
    elif flesch_ease >= 50:
        readability_desc = "Fairly Difficult (10th-12th grade level)"
    elif flesch_ease >= 30:
        readability_desc = "Difficult (College level)"
    else:
        readability_desc = "Very Difficult (Graduate level)"

    # Identify style suggestions
    suggestions = []
    
    # 1. Wordy and Cliché Phrases
    wordy_found = []
    for pattern, replacement in WORDINESS_PATTERNS.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            wordy_found.append({
                "phrase": matches[0],
                "replacement": replacement,
                "count": len(matches)
            })
            suggestions.append(f"Replace '{matches[0]}' with '{replacement}' to reduce wordiness.")

    # 2. Passive Voice
    passive_matches = PASSIVE_VOICE_PATTERN.findall(text)
    if passive_matches:
        for verb, participle in passive_matches:
            suggestions.append(f"Passive voice detected: '{verb} {participle}'. Consider converting to active voice for stronger writing.")

    # 3. Sentence Length Variety
    sentence_lens = []
    for s in sentences:
        s_words = re.findall(r"\b[a-zA-Z']+\b", s)
        sentence_lens.append(len(s_words))
        
    s_std = _std_dev(sentence_lens)
    variety_status = "Good variation"
    if len(sentences) >= 4:
        if s_std < 3.0:
            variety_status = "Monotonous (sentence lengths are too uniform)"
            suggestions.append("Vary your sentence lengths. Combining short sentences or splitting very long ones will create a better rhythm.")
        elif s_std > 12.0:
            variety_status = "High variation (mix of very long and very short)"
    
    # 4. Vocabulary Repetition
    stop_words = {
        "the", "a", "an", "and", "or", "but", "of", "to", "in", "is", "it", "that", "this", 
        "he", "she", "they", "we", "i", "you", "was", "were", "for", "with", "as", "at", 
        "on", "by", "for", "from", "had", "have", "his", "her", "their", "are", "be", "been"
    }
    word_counts = {}
    for w in words:
        wl = w.lower()
        if wl not in stop_words and len(wl) > 2:
            word_counts[wl] = word_counts.get(wl, 0) + 1
            
    repetitive_words = []
    for wl, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / num_words) * 100
        if count >= 4 and pct > 1.5:
            repetitive_words.append({"word": wl, "count": count, "percentage": round(pct, 2)})
            if len(repetitive_words) <= 3:  # Only suggest first few
                suggestions.append(f"The word '{wl}' is repeated {count} times. Consider using synonyms like thesaurus lookups.")

    return {
        "status": "success",
        "statistics": {
            "word_count": num_words,
            "sentence_count": num_sentences,
            "character_count": num_chars,
            "average_sentence_length": round(avg_sentence_len, 2),
            "average_syllables_per_word": round(avg_syllables_per_word, 2),
            "complex_words_count": complex_words,
            "sentence_length_variety": variety_status,
            "sentence_length_std_dev": round(s_std, 2)
        },
        "readability": {
            "flesch_reading_ease": flesch_ease,
            "flesch_kincaid_grade_level": fk_grade,
            "gunning_fog_index": gunning_fog,
            "interpretation": readability_desc
        },
        "style_analysis": {
            "passive_voice_count": len(passive_matches),
            "wordy_phrases_detected": wordy_found,
            "repetitive_content_words": repetitive_words,
            "suggestions": suggestions
        }
    }

def search_literary_devices(query: str) -> dict:
    """
    Search for a literary device (e.g. metaphor, simile, irony, personification, foreshadowing)
    to get its official definition, classroom examples, and practical analysis guidelines.
    Use this when students are identifying literary tools in their reading or writing essays.
    
    Args:
        query: The name of the literary device.
        
    Returns:
        A dictionary containing the definition, example, and analysis tip.
    """
    q = query.lower().strip()
    if q in LITERARY_DEVICES:
        return {
            "status": "success",
            "device": q.capitalize(),
            "definition": LITERARY_DEVICES[q]["definition"],
            "example": LITERARY_DEVICES[q]["example"],
            "analysis_tip": LITERARY_DEVICES[q]["analysis_tip"]
        }
    
    # Try fuzzy substring matching on keys
    matches = []
    for device, info in LITERARY_DEVICES.items():
        if q in device or device in q:
            matches.append({
                "device": device.capitalize(),
                "definition": info["definition"],
                "example": info["example"],
                "analysis_tip": info["analysis_tip"]
            })
            
    if matches:
        return {
            "status": "success",
            "message": f"Found {len(matches)} matching literary devices.",
            "results": matches
        }
        
    # Search in definitions/examples
    search_results = []
    for device, info in LITERARY_DEVICES.items():
        if q in info["definition"].lower() or q in info["example"].lower():
            search_results.append({
                "device": device.capitalize(),
                "definition": info["definition"],
                "example": info["example"],
                "analysis_tip": info["analysis_tip"]
            })
            
    if search_results:
        return {
            "status": "success",
            "message": f"Found {len(search_results)} devices mentioning '{query}' in descriptions.",
            "results": search_results
        }
        
    return {
        "status": "error",
        "message": f"No literary device found matching '{query}'. Try search terms like 'metaphor', 'simile', 'irony', 'alliteration', or 'symbolism'."
    }

def get_classic_literature_guide(title: str) -> dict:
    """
    Retrieves a study guide for classic school curriculum books (e.g. '1984', 'The Great Gatsby', 
    'To Kill a Mockingbird', 'Romeo and Juliet', 'Macbeth') containing plot summary, major characters, 
    key themes, and famous quotes with detailed literary analysis.
    Use this for literature study questions, character analyses, or theme exploration.
    
    Args:
        title: The title of the classic book.
        
    Returns:
        A dictionary containing the study guide details, or an error if the book is not in the database.
    """
    t = title.lower().strip()
    
    # Exact match
    if t in CLASSIC_LITERATURE_GUIDES:
        return {"status": "success", "guide": CLASSIC_LITERATURE_GUIDES[t]}
        
    # Substring match
    matches = []
    for book_key, guide in CLASSIC_LITERATURE_GUIDES.items():
        if t in book_key or book_key in t:
            matches.append(guide)
            
    if len(matches) == 1:
        return {"status": "success", "guide": matches[0]}
    elif len(matches) > 1:
        return {
            "status": "multiple_matches",
            "message": f"Found multiple guides matching '{title}': {[g['title'] for g in matches]}",
            "results": [g["title"] for g in matches]
        }
        
    return {
        "status": "error",
        "message": f"No study guide found for '{title}'. Currently supporting classics: {', '.join(g['title'] for g in CLASSIC_LITERATURE_GUIDES.values())}."
    }

def search_gutenberg_books(query: str) -> dict:
    """
    Searches Project Gutenberg's catalog of public domain classic books.
    Use this to look up books, find authors, retrieve subjects, and access read/download links.
    
    Args:
        query: The title, author, or keyword to search for (e.g., 'Pride and Prejudice', 'Charles Dickens').
        
    Returns:
        A dictionary containing metadata of matching classic books.
    """
    try:
        # Bypass SSL verification which frequently fails on macOS Python installations
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        # Format search query
        formatted_query = urllib.parse.quote(query)
        url = f"https://gutendex.com/books/?search={formatted_query}"
        
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'SchoolMultiAgent/1.0 (Student Project)'}
        )
        
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode('utf-8'))
            results = data.get("results", [])
            
            formatted_results = []
            for book in results[:10]: # Limit to top 10 matches
                authors = [a.get("name") for a in book.get("authors", [])]
                formats = book.get("formats", {})
                
                # Try to get HTML or Text reading link
                read_link = formats.get("text/html") or formats.get("text/html; charset=utf-8") or formats.get("text/plain; charset=utf-8") or formats.get("text/plain")
                
                formatted_results.append({
                    "id": book.get("id"),
                    "title": book.get("title"),
                    "authors": authors,
                    "subjects": book.get("subjects", [])[:3], # Limit to 3 subjects
                    "languages": book.get("languages", []),
                    "download_count": book.get("download_count"),
                    "read_link": read_link
                })
                
            return {
                "status": "success",
                "count": data.get("count", 0),
                "results": formatted_results
            }
    except Exception as e:
        return {"status": "error", "message": f"Could not query Gutenberg catalog. Error: {str(e)}."}
