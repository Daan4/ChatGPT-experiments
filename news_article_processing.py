from helpers import *

prompt = """
For each Dutch news article given below delimited by triple backticks do the following tasks:
1. Summarize the article in at most 50 words
2. Provide up to five main topics of the article
3. Determine the sentiment of the article
4. Generate a new headline for the article
5. Generate a joke based on the article

Your answer should use the English language.

Format the results as a JSON object with the keys 'Summary', 'Topics', 'Sentiment', 'Headline', 'Joke'

Article 1: ```
Brussel geeft groen licht voor uitkoop piekbelasters stikstof in veehouderij

De Europese Commissie heeft de plannen van het kabinet om de grote uitstoters van stikstof in de veehouderij aan te pakken goedgekeurd. Daardoor wordt het mogelijk om snel de zogeheten piekbelasters uit te kopen, zodat de uitstoot op korte termijn een stuk omlaag kan.

De commissie ziet de regelingen niet als ongeoorloofde staatssteun. In een verklaring noemt Brussel ze "noodzakelijk en gepast". Bovendien zijn ze in lijn met de doelen uit de Europese Green Deal. "De positieve effecten overstijgen de eventuele verstoringen van de vrije markt."

Dat Brussel nu groen licht geeft is van groot belang voor het Nederlandse stikstofbeleid. De piekbelasters zijn verantwoordelijk voor een belangrijk deel van de neerslag van stikstof in beschermde natuurgebieden. Als zij stoppen, kan de natuur zich herstellen en komt het halen van de stikstofdoelen een stuk dichterbij.

De stikstofruimte die vrijkomt, wordt bij voorrang gebruikt om boeren te helpen die buiten hun schuld zonder vergunning zitten, zogeheten PAS-melders. De rest kan worden ingezet om bouwprojecten mogelijk te maken, zoals de bouw van woningen en nieuwe wegen.

Vrijwillig stoppen
Het kabinet wil zo'n 3000 piekbelasters in de buurt van Natura 2000-gebieden een aanbod doen om vrijwillig te stoppen. Het gaat daarbij om melkveebedrijven, varkenshouderijen, vleeskalverhouderijen en pluimveebedrijven.

Ze kunnen tot 120 procent van de marktwaarde van het bedrijf krijgen, zo is het plan. Voorwaarde is wel dat de boeren echt stoppen en dat de veestapel dus kleiner wordt.

Daarnaast komt er een soortgelijke regeling voor melkvee-, varkens- en pluimveehouders die willen stoppen, maar niet onder de piekbelasters vallen. Zij kunnen tot 100 procent van de waarde van hun bedrijf krijgen. Er komt een website om te berekenen of de uitstoot van een boerderij boven de drempelwaarde komt om voor subsidie in aanmerking te komen.

Voor beide regelingen wil het kabinet in totaal 1,4 miljard euro uittrekken.

Geen staatssteun
Minister Christianne van der Wal (Natuur en Stikstof) noemde de voorgenomen regelingen eerder "woest aantrekkelijk". Wel was de toestemming van de Europese Commissie cruciaal, omdat de uitkoop mogelijk als ongeoorloofde staatssteun kon worden gezien.

Eigenlijk was het de bedoeling dat de regelingen in januari al van start zouden gaan, maar door verschillende oorzaken liep dat vertraging op. Vorige week bleek dat Van der Wal nog een aantal technische vragen van Brussel moest beantwoorden, voordat er definitief groen licht gegeven kon worden. Die vragen zijn nu kennelijk tot tevredenheid beantwoord.

Het kabinet wil de uitkoopregelingen, met de precieze voorwaarden, eind deze maand publiceren. De verwachting is dat veehouders er dan komende zomer op kunnen inschrijven.

Industrie
De nu goedgekeurde uitkoopregelingen gaan specifiek over agrarische bedrijven. Het kabinet wil ook industriële ondernemingen in de buurt van natuurgebieden aanpakken door de vergunningen aan te scherpen, waardoor ze minder stikstof mogen uitstoten.

De industrie en ook het verkeer zijn vanwege de klimaatdoelen en de verbetering van de luchtkwaliteit al verplicht om hun uitstoot de komende jaren te verminderen. Als er minder CO2 en fijnstof wordt uitgestoten, betekent dat volgens het kabinet waarschijnlijk ook minder stikstof.

Wachten op provincies
Premier Rutte zei vorige maand dat hij de stikstofaanpak wil versnellen en dat hij de piekbelastersregeling daarvoor nodig heeft. Tegelijkertijd wacht het kabinet voor veel volgende stappen in het beleid op de vorming van de nieuwe provinciebesturen.

De provincies moeten het beleid grotendeels uitvoeren, maar bij de verkiezingen van 15 maart werd de BBB van Caroline van der Plas bijna overal de grootste. Die partij heeft grote moeite met het stikstofbeleid.

Ook regeringspartij CDA trapt op de rem. Die partij wil binnenkort opnieuw onderhandelen in de coalitie over de stikstofdoelen en wanneer die bereikt moeten worden.
```

Article 2: ```
'Vakbonden wijzen nieuw loonbod Albert Heijn af'

Na ruim een week staken wil Albert Heijn de medewerkers van de eigen distributiecentra toch meer loon betalen. Maar de 10 procent die de supermarktketen gisteravond heeft geboden, is door de vakbonden FNV en CNV afgewezen, zegt een woordvoerder van Albert Heijn. Vakbonden CNV en FNV spreken tegen dat er een concreet bod ligt.

Albert Heijn zegt de bonden gisteravond een nieuw loonbod te hebben gedaan, met het "dringende" verzoek om opnieuw om de tafel te gaan. "Maar het bod is afgewezen en de bonden komen ook niet terug aan tafel. Daar zijn we heel verbaasd over", zegt de woordvoerder. Het loonbod gaat om een periode van één jaar en had op 22 mei van kracht moeten worden.

Schappen langzaam leeg
Albert Heijn wilde in eerste instantie niet verder gaan dan een loonsverhoging van 8 procent. Vakbond CNV bevestigt een brief van Albert Heijn te hebben ontvangen met daarin een verzoek om opnieuw te onderhandelen, maar stelt dat er geen bod ligt. Ook FNV ontkent een nieuw loonbod te hebben ontvangen. "Wij hebben niets afgewezen, wij hebben gevraagd om een formeel loonbod zodat we weten waar we over onderhandelen. En dat is niet gekomen", zegt een woordvoerder tegen persbureau ANP.

Ondertussen beginnen bij steeds meer filialen van Albert Heijn de schappen langzaam leeg te raken. De AH-woordvoerder benadrukt dat de impact van de staking in de distributiecentra per supermarkt verschilt, omdat dit afhankelijk is van het personeel dat in de centra nog aan het werk is.
```

Article 3: ```
Amnesty: Israël onderwerpt Palestijnen aan meer gezichtsherkenning

Israël zet steeds meer gezichtsherkenningstechnologie in om Palestijnen op de bezette Westelijke Jordaanoever en in Oost-Jeruzalem in de gaten te houden. Dat stelt Amnesty International in een nieuw rapport. Volgens de mensenrechtenorganisatie wordt de technologie onder meer gebruikt bij belangrijke checkpoints, die Palestijnen moeten passeren om zich van gebied naar gebied te verplaatsen.

In het rapport beschrijft Amnesty het gebruik van meerdere militaire bewakingssystemen, waaronder het experimentele Red Wolf. Palestijnen die voorbij een checkpoint willen, zouden te maken krijgen met gezichtsscans. Israëlische militairen krijgen vervolgens een kleurcode te zien die bepaalt of iemand doorgelaten mag worden of niet, aldus Amnesty.

Slaagt het systeem er niet in iemand te herkennen, dan worden persoonlijke gegevens door militairen handmatig ingevoerd. De database van (biometrische) gegevens zou daarmee steeds verder worden uitgebreid. "Zowel in Hebron als in het bezette Oost-Jeruzalem ondersteunt gezichtsherkenningstechnologie een afgesloten netwerk van bewakingscamera's om Palestijnen bijna constant in de gaten te houden", concludeert Amnesty.

'Apartheid in stand houden'
Volgens Amnesty wordt de technologie voornamelijk tegen Palestijnen ingezet: de organisatie spreekt daarom van "geautomatiseerde apartheid". Israël reageerde vorig jaar woest toen het door Amnesty werd beschuldigd van apartheid, het rassensegregatiesysteem dat Zuid-Afrika jarenlang hanteerde.

Cameratoezicht is volgens de Israëlische regering noodzakelijk om de veiligheid te waarborgen. Het is bijvoorbeeld bedoeld om aanslagen te voorkomen. Maar volgens het rapport wordt de bewegingsvrijheid van Palestijnen door gezichtsherkenningstechnologie in hoge mate ingeperkt. De onderzoekers baseren hun conclusies op zowel de getuigenissen van Palestijnen als die van voormalige Israëlische militairen.

"Ik word de hele tijd in de gaten gehouden", wordt de Palestijnse Neda geciteerd. "Het geeft me overal op straat een heel slecht gevoel. Telkens als ik een camera zie, voel ik me angstig. Alsof je altijd wordt behandeld alsof je een doelwit bent."

In 2021 schreef de Amerikaanse krant The Washington Post al dat Israël bouwde aan een database met daarin grote aantallen beelden van Palestijnen.

'Camera's van Nederlands bedrijf'
Verder schrijft de mensenrechtenorganisatie dat camera's afkomstig van een Nederlands bedrijf zijn 'ontdekt' in openbare ruimten en politie-infrastructuur. Het zou gaan om camera's van het bedrijf TKH Security.

In een verklaring aan de NOS laat het bedrijf weten dat het gaat om TKH Security CCTV-camera's, die via een distributeur zijn geleverd. "TKH Security heeft geen zakelijke relatie met de Israëlische veiligheidsdiensten." Het techbedrijf geeft verder aan geen toegang tot de camera's, noch tot de systemen te hebben.

Ook een Chinees bedrijf zou gezichtsherkenningscamera's hebben geleverd aan Israël. "Zij moeten stoppen met het leveren van technologieën die door de Israëlische autoriteiten worden gebruikt om illegale nederzettingen in stand te houden", roept Amnesty-chef Agnès Callamard op.

In een verklaring in de Amerikaanse krant The New York Times zegt het Israëlische leger enkel "noodzakelijke veiligheids- en inlichtingenoperaties" te hebben opgetuigd. "Terwijl we gelijktijdig zoveel mogelijk doen om de gevolgen voor de Palestijnse bevolking te beperken." Het leger gaat in de verklaring verder niet inhoudelijk in op het rapport.

De technologie wordt volgens Amnesty ingezet op de bezette Westelijke Jordaanoever, die sinds 1967 is bezet door Israël. Wat houdt die bezetting nou precies in en wat betekent het voor de Palestijnen die hier wonen? Dat zie je in deze video:
```
"""

response = get_completion_from_prompt(prompt)
print(response)
