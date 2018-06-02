import spacy
import spacy.symbols as symbols
nlp = spacy.load('en')


news = u'''NEW YORK (Reuters) - It took China just 11 hours to retaliate against the United States for proposing tariffs on some 1,300 Chinese products, but Chinese officials are holding back on taking aim at their largest American import: government debt.

A U.S. Dollar note is seen in this June 22, 2017 illustration photo. REUTERS/Thomas White/Illustration/File Photo
In a tit-for-tat response to the Trump administration’s plan for 25 percent duties on $50 billion of Chinese imports, China hit back with its own list of similar duties on key American imports including soybeans, planes, cars, beef and chemicals. But officials signaled no interest for now in bringing their vast holdings of U.S. Treasuries to the fight.

China held around $1.17 trillion of Treasuries as of the end of January, making it the largest of America’s foreign creditors and the No. 2 overall owner of U.S. government bonds after the Federal Reserve. Any move by China to chop its Treasury portfolio could inflict significant harm on U.S. finances and global investors, driving bond yields higher and making it more costly to finance the federal government.

Jeffrey Gundlach, the chief executive of DoubleLine Capital LP, said China can use its Treasury holdings as leverage, but only if they keep holding them.

“It is more effective as a threat. If they sell, they have no threat,” said Gundlach, known as Wall Street’s Bond King.

“It would only escalate the situation and eliminate their leverage.”

Prices on benchmark 10-year U.S. Treasury notes slipped on Wednesday, giving back earlier gains on the trade news. Their yield edged up to about 2.81 percent Wednesday afternoon.

China’s Treasury holdings have dipped in recent months, declining by about $30 billion from $1.20 trillion last August, and they are down about 11 percent from their record high above $1.3 trillion in late 2013, according to U.S government data. In all, foreign governments own $4 trillion, or more than a quarter, of the $14.7 trillion in Treasury securities outstanding.


Asked by a reporter on Wednesday if China would reduce its U.S. Treasury holdings in retaliation, Vice Finance Minister Zhu Guangyao reiterated China’s long-standing policy regarding its foreign exchange reserves, saying it is a responsible investor and that it will safeguard their value.

China’s foreign exchange reserves, the world’s largest, stood at about $3.13 trillion at the end of February, with roughly a third of it held in Treasuries.

“If they wanted to pull the nuclear switch, if they committed to dumping Treasuries, it would have an immediate and temporary impact on money markets in the United States,” said Jeff Klingelhofer, a portfolio manager who oversees more than $6 billion at Thornburg Investment Management Inc. “But I think it is a bigger hit to the sustainability of what they’re trying to accomplish.”

Brad Setser, senior fellow for international economics at the Council on Foreign Relations in New York, said China can sell Treasuries and buy lower-yielding European or Japanese debt.

But the effect would likely be to strengthen the yuan against the dollar, weakening the relative desirability of its exports, analysts said. The sale could also tank the value of the Treasuries China retains, with nothing to show for the aggression.

More likely, if China wanted to turn up the heat it would let the yuan depreciate against the U.S. dollar, according to CFR’s Setser, a move that could kneecap the Trump administration’s goal of jump-starting U.S. manufacturing. The yuan weakened by about 0.25 percent on Wednesday but remains near its strongest in two and a half years.

Even if the likelihood of a change in Chinese policy regarding its Treasuries portfolio remains low, investors are sensitive to the risk any big shift would pose to world financial markets, where Treasuries are a global benchmark asset.

A January report that China might halt its purchases of Treasuries forced yields higher, but China disputed the news and said it was only diversifying its foreign exchange reserves to safeguard their value.

Reporting by Kate Duguid and Trevor Hunnicutt; Additional reporting by Jennifer Ablan; Editing by Dan Burns and James Dalgleish'''


news2 = '''MOSCOW (Reuters) - Finland has approved the construction of the Nord Stream 2 gas pipeline through Finland’s economic zone, the Finnish government and Russian gas exporter Gazprom said on Thursday.

The pipeline between Russia and Germany, which would run for around 375 kilometers across Finland’s economic zone through the Baltic Sea, still requires a construction permit from local Finnish authorities.



The pipeline’s operator Nord Stream 2 AG said it expected the second permit “within the next weeks”.

Nord Stream 2, planned to run from Russia across the bed of the Baltic Sea to Germany, would double the existing Nord Stream pipeline’s current annual capacity of 55 billion cubic meters.

Eastern European and Baltic states fear the pipeline could increase reliance on Russian gas and undermine Ukraine’s role as a gas transit route, but Germany and other beneficiaries in northern Europe back the project.

Germany has approved the pipeline and the project is currently collecting permits from Russia, Sweden and Denmark.

Late last year, Denmark passed a law that could allow it to ban the pipeline from going through its waters.'''


news3 = '''New oil and gas projects to be sanctioned this year will likely have a 15-percent lower breakeven level than last year’s, at US$44 per barrel of oil equivalent, Wood Mackenzie analysts said in a fresh report on short-term developments in the upstream sector.

The consultancy sees as many as 30 new projects coming on stream this year, but notes that most of these will be small-scale ones, signaling the lingering wariness among oil and gas players of major investments.

This is a continuation of a trend started after the 2014 price crash, which saw last year’s average capex per major project—deposits with commercial reserves of 50 million boe or more—drop to US$2.7 billion from US$5.5 billion on average for the last 10 years.

Besides this new frugality, Wood Mac’s analysts note, the oil and gas industry has paid much more attention to brownfield developments and production expansion projects, with offshore operators increasingly turning to subsea tie-ins instead of tapping new fields.


Again, this is a sign of the new cost discipline that oilfield operators have been forced to apply amid the price crisis from the last three years. This trend will continue this year as well, with a focus on gas projects, plus several large expansion plans in Iran, Norway, and Oman.
Related: Oil Prices Head Higher On Large Crude Draw

Wood Mac analysts point out, however, that this leaner-and-meaner approach cannot be a long-term strategy, and mentions several megaprojects in the LNG segment, all set for a final investment decision this year. These include production expansions in Qatar and Papua New Guinea, as well as Mozambique LNG, involving Anadarko, Mitsui, and three large Indian companies, and LNG Canada, which features participants such as Shell, PetroChina, Kogas, and Mitsui.

The consultancy expects some of these projects to delay their final investment decision until later this year to avoid “all rushing through that door at the same time and then see costs blow-out.” More generally, this year’s final investment decisions will show whether the industry has learned its lesson from the latest crisis or if it will be back to the boom-and-busts cycles we all know so well, Wood Mac says.'''


news4 = '''Although oil has caught up, it was originally natural gas that ignited the U.S. shale revolution that began about a decade ago.

Looking forward now, the upside to gas prices seems as small as it has ever been: our Energy Information Administration's National Energy Modeling System projects that U.S. gas production will increasingly outpace demand.

That's mostly because the amount of gas that we have at our disposal is really without end. We probably have the largest lowest cost gas resource in the world, and our proven reserves alone were up 5% last year to 341 trillion cubic feet - a 60% leap since 2006.

More short-term, EIA has gas production outpacing domestic demand over each of the next two years by about 3 Bcf/d. Most of our new demand potential, however, is in the export market, which isn't factored into that. As the wildcard in our gas market, exports to Mexico and LNG will account for 70-80% of new demand for at least the next five years. According to EIA, LNG exports alone will increase by ~5.5 Bcf/d by the end of 2019 to nearly 9 Bcf/d. So, production will need to rise to the mid-80s Bcf/d level to support this structural increase in consumption.


Data source: EIA
Incremental gains in U.S. gas production could be double the increases in demand.
But ultimately, I would be very careful about underestimating new gas domestic demand in the U.S. It's not commonly reported as such, but be sure to see the U.S. as a "still developing nation:" each year we add 3 million people and $300-400 billion in real GDP. Unlike most of our OECD partners, we face both a population and economic explosion in the years ahead.

Gas will continue to make headway in the power and industrial sectors, which respectively account for 34% and 30% of our total gas usage.

In fact, gas is now almost 45% of U.S. power generation capacity, and climbing toward 50%. From 2017-2020, we will be installing 80,000 megawatts of new gas capacity, or almost a 20% increase in just a few years with even more coming. The entire country is turning to gas, and new regulations to cut greenhouse gas emissions favor natural gas. The ability of wind and solar power, augmented by battery storage, to displace, not supplement, natural gas, is typically overstated.

Additionally, the push for electric vehicles could be the primary factor that reserves our decade long trend of flat power demand. And don't forget that the more gas we produce, the more attractive it becomes to use to generate power.

Data source: EIA
Natural gas is even the favored source of power for those areas that don't produce any: like New York and New England.
In fact, more manufacturing itself could increase our gas demand via more power and obviously more industrial demand. "Manufacturing in U.S. Expands at Fastest Pace Since May 2004." At 21.7 Bcf/d, U.S. industrial gas demand in 2017 was the highest it has been since 2000, when consumption was assumed to have peaked.

Industrial growth could be 60% in the decades ahead. My Forbes colleague Ken Silverstein reports: "As of December 2017, the American Chemistry Council said that 317 projects are either in up-and-running, getting built or on the drawing board and collectively, they are valued at $185 billion."

The ongoing pipeline build-out will be strong enough to outweigh new demand and exports, and limit the price increase of rising gas-on-gas competition, particularly important at various hub price points across the country. This year, there are 3,000 miles of gas pipeline coming in the U.S, or about a quarter of the world’s total and more than four times what the U.S. laid in 2012.

Production wise, shale gas is now over 60% of all U.S. gas output and will be the source of essentially all new production.'''


news5 = '''Bahrain officials have revealed that the tiny gulf kingdom has discovered some 80 billion barrels of shale (otherwise known as tight) oil - the kingdom's largest oil and gas find ever. The field also discovered 14 trillion cubic feet of natural gas beneath an existing field.

Oil Minister Sheikh Mohammed bin Khalifa Al Khalifa said the kingdom has not yet determined how much of the oil can be easily extracted, according to the Associated Press.

Bahrain

The oil fields were discovered in the offshore Khalij al-Bahrain Basin, which covers some 770 square miles in the shallow waters off Bahrain's west coast.

The underwater shale would dwarf the country's existing reserves.

According to figures from the US Energy Administration, Bahrain currently pumps about 45,000 barrels a day from its Bahrain Field. It also shares income from a deposit with Saudi Arabia that produces about 300,000 barrels a day.



"Initial analysis demonstrates the find is at substantial levels, capable of supporting the long-term extraction of tight oil and deep gas," the Sheikh said.

He added during the news conference, which was held in Manama on Wednesday, that Bahrain's National Oil and Gas Authority hoped to lure foreign oil and gas firms to develop the field where the reserves were found, per the BBC.

Map

Bahrain has been pumping oil since 1932 and was among the first Arab Gulf states to extract oil.

According to the Guardian, industry consultants DeGolyer and MacNaughton (Demac) have worked with Bahrain to evaluate the newfound reserves. 

"Demac evaluated the reservoir and test data, evaluated volumetric and recovery potential, and provided reports documenting both prospective and contingent resources. This is a project which breaks new ground for the industry," a spokesperson said.

The country has not historically been a major oil producer - but the new field, which officials said could come online within five years, has the potential to dramatically change that. According to the initial estimates, the oil deposits are roughly the size of Russia's oil deposits.

It could also help bolster the sagging Bahrainian economy, which has suffered from low oil prices and unrest among the majority Shia population. The country, like most of its neighbors, is run by a Sunni monarchy, and low oil prices have forced it to cut back on popular government handouts, leading to a some unrest.'''


news6 = '''It started with a $105 billion blunder, and then it got worse.

Someone at Samsung Securities Co., one of South Korea’s largest brokerages, was trying to pay employees 1,000 won (93 U.S. cents) per share in dividends under a company compensation plan. Somehow, they gave them 1,000 Samsung Securities shares instead. In total, the company distributed 2.83 billion shares, worth -- on paper -- about 112.6 trillion won. That was more than 30 times the company’s market value.

The fact that the shares didn’t exist didn’t stop 16 employees from selling them. And that spurred a rout in Samsung Securities’ stock. It plunged as much as 12 percent in the space of minutes on April 6, the biggest decline since the global financial crisis. Many retail investors got burned.

Then the recriminations started. People are angry with Samsung Securities. They’re angry with the employees who sold the phantom shares. And they’re angry with the government and regulators for the system that allowed people to dump stock they didn’t own -- and wasn’t even real.

“Nobody expected to see something like this,” said Hwang Seiwoon, a Seoul-based research fellow with the capital markets division of Korea Capital Market Institute Co., a research company. “An employee selling a million company shares during business hours? Now, that’s weird.”

Ghost Stock

The fiasco has been dubbed the “ghost stock” incident by major local news media outlets. Regulators are reviewing Samsung Securities’ internal controls. On Monday, South Korea’s giant pension fund stopped using Samsung Securities brokerage services. The brokerage says it will sternly punish staff who sold the shares, and repay shareholders who lost money when the stock tanked.

“We are going to compensate investors who suffered losses in the widest possible way,” Koo Sung-hoon, the chief executive officer of Samsung Securities, was quoted as saying in a company statement.

In another perhaps surprising consequence, the mood in the country has turned against short selling. In an attempt to prevent recurrence of what happened at Samsung Securities, more than 200,000 people have signed a petition to the Blue House, South Korea’s presidential office, as of Thursday, asking the government to ban such trading. Because the petition has that many signatories, the Blue House must respond.

Naked Shorting

What happened at Samsung Securities, while different, has one parallel with a practice called “naked shorting,” where investors sell shares they don’t own and haven’t borrowed in the hope of buying them back later at a lower price. The Samsung employees weren’t selling their shares to profit from declines, but they did sell shares they didn’t possess.

“This doesn’t make sense at all,” the petition on the Blue House website cited one person, who wasn’t identified, as saying. “Employees sold shares even though they knew it was wrong. This is worst case of moral hazard. Overall inspection on brokerages is needed.”'''

def find_root_token(token):
    if token.pos_ == 'VERB':
        return token
    return find_root_token(token.head)


def prune_token_tree_for_digits(token, digit_tokens, qualified_tokens):
    if token.i in qualified_tokens:
        return True
    is_qualified = False
    for child in token.children:
        if prune_token_tree_for_digits(child, digit_tokens, qualified_tokens):
            is_qualified = True
            # break
    if not is_qualified:
        is_qualified = token.i in digit_tokens
    if is_qualified:
        qualified_tokens.add(token.i)
    return is_qualified


def prune_token_tree_for_subject(token, is_left, iroot, qualified_tokens):
    if token.dep == symbols.nsubj:
        if (is_left and token.i < iroot) or (token.i > iroot and not is_left):
            append_subtree(token, qualified_tokens)
            return True
    has_subject = False
    for child in token.children:
        if prune_token_tree_for_subject(child, is_left, iroot, qualified_tokens):
            has_subject = True
            break
    return has_subject


def append_subtree(token, qualified_tokens):
    for c in token.children:
        append_subtree(c, qualified_tokens)
    qualified_tokens.add(token.i)


def get_tokens(doc, token_ids):
    token_ids.sort()
    return [doc[i] for i in token_ids]


def sentence_from_tokens(tokens):
    if tokens is None:
        return None
    return ' '.join([t.text for t in tokens])


def process_sentence(stext):
    sdoc = nlp(stext)

    # Only process sentences where money or percent entities are available
    has_numbers = False
    for ent in sdoc.ents:
        # print(ent.text, ent.label_)
        if ent.label_ in ['MONEY', 'PERCENT', 'QUANTITY']:
            has_numbers = True
            break
    if not has_numbers:
        return None, None

    digit_tokens = set()
    for ent in sdoc.ents:
        if ent.label_ in ['MONEY', 'PERCENT', 'QUANTITY']:
            # print(ent.text, ent.label_)
            for token in ent:
                digit_tokens.add(token.i)

    # First find the root token, which is the nearest verb parent of the digit tokens
    for token in sdoc:
        # print(token.text, token.dep_, token.pos_, token.head.text, 'Children:', [c for c in token.children])
        if token.i in digit_tokens:
            root_token = find_root_token(token)
            if root_token:
                break

    # Starting from root token, include tokens which are related to the subtree which contains digit tokens
    tokens = set()
    prune_token_tree_for_digits(root_token, digit_tokens, tokens)
    if len(tokens) == 0:
        raise RuntimeError('Failed to find digit tokens!')

    # Try to find out subject tokens on the other side of root token
    iroot = root_token.i
    if iroot == min(tokens):
        is_left = True
    elif iroot == max(tokens):
        is_left = False
    else:
        raise RuntimeError('Root is neither at left side not at right side!')
    subject_tokens = set()
    prune_token_tree_for_subject(root_token, is_left, iroot, subject_tokens)
    if len(subject_tokens) == 0:
        all_subs = [token for token in sdoc if token.dep_ == 'nsubj']
        distances = [abs(token.i - root_token.i) for token in all_subs]
        min_distance = min(distances)
        sub_token = all_subs[distances.index(min_distance)]
        append_subtree(sub_token, subject_tokens)

    tokens = tokens.union(subject_tokens)

    # Add advs that's attached to the verb
    for child in root_token.children:
        if child.pos_ == 'PART':
            tokens.add(child.i)

    # Add preps that's attached to the digits
    for token in sdoc:
        if token.i in tokens and token.i in digit_tokens:
            for child in token.children:
                if child.dep_ == 'prep' and child.pos_ == 'ADP':
                    append_subtree(child, tokens)

    # Remove approximating digit tokens
    for token in sdoc:
        if token.i in tokens:
            if token.dep_ == 'quantmod' and token.pos_ == 'ADV':
                tokens.remove(token.i)
            elif token.dep_ == 'punct' and token.pos_ == 'PUNCT':
                tokens.remove(token.i)

    # Construct the sentence
    words = []
    itoken = 0
    for token in sdoc:
        if token.i in tokens:
            words.append(token.text)
            if token.i == root_token.i:
                root_i = itoken
            itoken += 1
    sentence = ' '.join(words)
    sentence = sentence.replace('$ ', '$').replace(' %', '%')
    return sentence, root_i


def analyze_short_sentence_structure(sentence, root_i):
    subject_tokens = []
    object_tokens = []
    verb_to_first_number_tokens = []
    verb_to_second_number_tokens = []
    first_number_tokens = []
    second_number_tokens = []
    digit_tokens = set()

    sdoc = nlp(sentence)
    root_token = sdoc[root_i]
    if root_token.pos_ != 'VERB':
        print('WARNING: Root token "' + root_token.text + '" is not a verb!')
        sentence = sentence[:root_token.idx] + root_token.text + 'ed' + sentence[root_token.idx + len(root_token.text):]
        sdoc = nlp(sentence)
        root_token = sdoc[root_i]
        if root_token.pos_ != 'VERB':
            raise RuntimeError('Root token "' + root_token.text + '" is not a verb after attempt of fix!')

    root_tokens = {root_token.i}
    # change root token to the advmod if there is one, e.g. move up, root token is up
    for token in root_token.children:
        if token.i > root_token.i:
            if token.dep_ == 'advmod' or (token.dep_ == 'prt' and token.pos_ == 'PART'):
                root_token = token
                root_tokens.add(token.i)
    verb_tokens = list(root_tokens)

    # add prep ADP to root tokens. e.g. move up to, to add is a root token
    for token_id in verb_tokens:
        token = sdoc[token_id]
        for sub_token in token.children:
            if sub_token.i > root_token.i and sub_token.dep_ == 'prep' and sub_token.pos_ == 'ADP':
                root_tokens.add(sub_token.i)

    for token in sdoc:
        if token.i < root_token.i and token.i not in root_tokens:
            subject_tokens.append(token.i)
        if token.i > root_token.i and token.pos_ == 'NUM' and token.i not in digit_tokens:
            digit_root_token = token
            while digit_root_token.head.i not in root_tokens:
                digit_root_token = digit_root_token.head
            digit_tokens = set()
            append_subtree(digit_root_token, digit_tokens)

            bridge_tokens = set()
            bridge_token = digit_root_token.head
            while bridge_token.i not in verb_tokens:
                bridge_tokens.add(bridge_token.i)
                bridge_token = bridge_token.head

            if len(first_number_tokens) == 0:
                first_number_tokens = list(digit_tokens)
                verb_to_first_number_tokens = list(bridge_tokens)
            else:
                second_number_tokens = list(digit_tokens)
                verb_to_second_number_tokens = list(bridge_tokens)
    subject_tokens = get_tokens(sdoc, subject_tokens)
    verb_tokens = get_tokens(sdoc, verb_tokens)
    verb_to_first_number_tokens = get_tokens(sdoc, verb_to_first_number_tokens)
    first_number_tokens = get_tokens(sdoc, first_number_tokens)
    verb_to_second_number_tokens = get_tokens(sdoc, verb_to_second_number_tokens)
    second_number_tokens = get_tokens(sdoc, second_number_tokens)
    return subject_tokens, verb_tokens, verb_to_first_number_tokens, first_number_tokens, verb_to_second_number_tokens, second_number_tokens


def get_tokens_from_ids(all_tokens, token_ids):
    token_map = dict(zip([t.i for t in all_tokens], all_tokens))
    return [token_map[i] for i in token_ids]


def analyze_number_group_structure(tokens):
    if len(tokens) == 0:
        return {}

    prep_token = None
    noun_tokens = set()
    unit_tokens = set()
    number_tokens = set()
    modifier_tokens = set()
    other_tokens = set()

    all_token_ids = set([token.i for token in tokens])
    root_token = tokens[0]
    # TODO: is there only one root?
    while root_token.head.i in all_token_ids:
        root_token = root_token.head

    if root_token.pos_ == 'NUM':
        root_number_tokens = {root_token.i}
    else:
        root_number_tokens = set()
    processed_token_ids = set()
    for token in tokens:
    # for token in root_token.children:
        if token.i in processed_token_ids:
            continue
        if token.dep_ == 'prep' and token.pos_ == 'ADP':
            processed_token_ids.add(token.i)
            if token.text.lower() == 'per':
                append_subtree(token, unit_tokens)
                for sub_token_id in unit_tokens:
                    processed_token_ids.add(sub_token_id)
            else:
                prep_token = token
                for sub_token in token.children:
                    append_subtree(sub_token, noun_tokens)
                for sub_token_id in noun_tokens:
                    processed_token_ids.add(sub_token_id)
    if len(root_number_tokens) == 0:
        for token in tokens:
            if token.i in processed_token_ids:
                continue
            if token.pos_ == 'NUM':
                root_number_token = token
                while root_number_token.head.pos_ == 'NUM':
                    root_number_token = root_number_token.head
                root_number_tokens.add(root_number_token.i)
                unit_token = root_number_token
                while unit_token != root_token:
                    unit_token = unit_token.head
                    unit_tokens.add(unit_token.i)
                    processed_token_ids.add(unit_token.i)
    if len(root_number_tokens) == 0:
        raise RuntimeError('Failed to find root number token!')
    number_group_tokens = set()
    root_number_tokens = get_tokens_from_ids(tokens, root_number_tokens)
    for root_number_token in root_number_tokens:
        append_subtree(root_number_token, number_group_tokens)
    number_group_tokens = get_tokens_from_ids(tokens, number_group_tokens)
    for token in number_group_tokens:
        if token.i in processed_token_ids:
            continue
        if token.dep_ == 'quantmod' and token.pos_ == 'SYM':
            unit_tokens.add(token.i)
            processed_token_ids.add(token.i)
        elif token.pos_ == 'NUM' or token.text == '-':
            number_tokens.add(token.i)
            processed_token_ids.add(token.i)

    for token in tokens:
        if token.i in processed_token_ids:
            continue
        if token.pos_ == 'ADJ' and token.dep_ == 'amod' and token.head.i in unit_tokens:
            unit_tokens.add(token.i)
        elif token.pos_ in ['ADJ', 'ADV', 'ADP'] and token.head.pos_ == 'NUM':
            modifier_tokens.add(token.i)
        elif token.text.lower() == 'some' and (token.head.i in number_tokens or token.head == root_token):
            modifier_tokens.add(token.i)
        else:
            other_tokens.add(token.i)
        processed_token_ids.add(token.i)

    def _get_tokens(ids):
        ids = list(ids)
        ids.sort()
        return get_tokens_from_ids(tokens, ids)

    noun_tokens = _get_tokens(noun_tokens)
    unit_tokens = _get_tokens(unit_tokens)
    number_tokens = _get_tokens(number_tokens)
    modifier_tokens = _get_tokens(modifier_tokens)
    other_tokens = _get_tokens(other_tokens)
    prep_tokens = [] if prep_token is None else [prep_token]
    if len(noun_tokens) > 0:
        noun_sentence = nlp(sentence_from_tokens(noun_tokens))
        for ent in noun_sentence.ents:
            if ent.label_ in ['MONEY', 'PERCENT', 'QUANTITY']:
                noun_tokens = analyze_number_group_structure(noun_tokens)
                break
    return {
        'unit': unit_tokens,
        'number': number_tokens,
        'prep': prep_tokens,
        'modifier': modifier_tokens,
        'subject': noun_tokens,
        'other': other_tokens
    }


def print_token_structure(tokens, prefix=''):
    for tag in tokens:
        value = tokens[tag]
        if type(value) is dict:
            sub_prefix = '\t' + prefix
            print(prefix + str(tag) + ':')
            print_token_structure(value, prefix=sub_prefix)
        else:
            print(prefix + str(tag) + ':', sentence_from_tokens(value))


from spacy import displacy

# Remove ’s so that the processing is more accurate
doc = nlp(news6.replace("’s", ""))
for s in doc.sents:
    stext = str(s)
    # displacy.serve(nlp(stext), style='dep')
    try:
        sentence, root_i = process_sentence(stext)
    except RuntimeError as e:
        if 'Failed to find' in str(e):
            if stext[-1] == '.':
                stext = stext[:-1]
            sinfos = stext.split(',')
            if len(sinfos) == 0:
                raise e
            sinfos = [s.strip() for s in sinfos]
            permutations = itertools.permutations(sinfos)
            sentence = None
            for permutation in permutations:
                newstext = ', '.join(permutation) + '.'
                try:
                    sentence, root_i = process_sentence(newstext)
                    break
                except RuntimeError:
                    continue
        else:
            print(e)
            continue
            # raise e
    if sentence is not None:
        print(stext)
        print('--------------------------------------------------------------')
        print(sentence)
        sdoc = nlp(sentence)
        # for ent in sdoc.ents:
        #     print(ent.text, ent.label_)
        # print('--------------------------------------------------------------')
        # for chunk in sdoc.noun_chunks:
        #     print(chunk.text, chunk.root.dep_, chunk.root.head.text)
        # print('--------------------------------------------------------------')
        # for token in sdoc:
        #     print(token.text, token.dep_, token.pos_, token.head.text, 'Children:', [c for c in token.children])
        # # # print(stext)
        print('--------------------------------------------------------------')
        subject, verb, verb_to_1, number_1, verb_to_2, number_2 = analyze_short_sentence_structure(sentence, root_i)
        number_1 = analyze_number_group_structure(number_1)
        number_2 = analyze_number_group_structure(number_2)
        print('Subject:', sentence_from_tokens(subject))
        print('Verb:', sentence_from_tokens(verb))
        print('First Prep:', sentence_from_tokens(verb_to_1))
        print('First Number Group:')
        print_token_structure(number_1, prefix='\t')
        print('Second Prep:', sentence_from_tokens(verb_to_2))
        print('Second Number Group:')
        print_token_structure(number_2, prefix='\t')

        print('\n')
