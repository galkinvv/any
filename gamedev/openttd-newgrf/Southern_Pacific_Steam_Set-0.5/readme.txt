Locomotives implemented so far:
	Governor Stanford 4-4-0 1863 Saturated Mixed
	A-3		4-4-2	1904	Saturated	Passenger
	A-3s	4-4-2	1920	Superheated	Passenger
	A-6		4-4-2	1927	Superheated	Passenger
	C-3		2-8-0	1899	Saturated	Freight
	C-9		2-8-0	1905	Saturated	Freight
	C-9s	2-8-0	1922	Superheated	Freight
	E-23	4-4-0	1899	Saturated	Passenger
	E-23s	4-4-0	1916	Superheated	Passenger
	GS-1	4-8-4	1930	Superheated	Mixed
	M-4		2-6-0	1899	Saturated	Freight
	M-4s	2-6-0	1920	Superheated	Freight
	MC-2	2-8-8-2	1909	Reheated	Freight
	Mt-1	4-8-2	1924	Superheated	Mixed
	P-8		4-6-2	1921	Superheated	Passenger
	SP-1	4-10-2	1925	Superheated	Freight
	T-1		4-6-0	1895	Saturated	Mixed
	T-32	4-6-0	1913	Superheated	Mixed
	TW-1	4-8-0	1892	Saturated	Freight

    
Cars implemented so far:
	Harriman 60' Baggage
	Harriman 60' Coach
	Harriman 40' RPO
	Harriman 60' RPO
	79-CB-1 Daylight chair-baggage car
	66-ACW-2 + 66-ACM-2 Daylight articulated chair car
	70-AD-4+70-AD-2+70-AD-3 Daylight triple unit diner car
	79-C-2 Daylight chair car
	79-T-1 Daylight tavern car
	79-PR-1 Daylight parlor car
	79-PR-2 Daylight parlor-observation car
	B-40-6 boxcar
	B-50-11 boxcar
	B-50-15 express boxcar
	B-50-16 overnight boxcar
	B-50-18 boxcar
	C-30-1 Caboose
	R-30-1 PFE Refrigerator
	R-30-12 PFE Refrigerator
	R-30-9 PFE Refrigerator
	R-40-2 PFE Refrigerator
	R-40-10 PFE Refrigerator
	R-40-23 PFE Refrigerator
	S-40-2 Stock car
	S-40-12 Stock car
    
Features implemented so far:
    * Locomotives will cost 5% of their normal running cost when stopped
    * Locomotives can be repainted using a custom refit cargo
    * Cargo ages at different rates depending on the car you haul it in. Reefers keep food fresh for longer.
    * Passenger decay can be slowed down by adding service cars to your train. Service cars include dining cars, coffee shops, taverns, and observation cars.
    * Consists containing freight cars cannot be started without a caboose or passenger car at the end of the train.
    * Locomotives can receive fancy paint jobs until 1935, at which point you can ony refit to black. Existing engines will not change color, however.
    
Planned features:
	* Be able to set the default colors to either SP or CC with a grf parameter
	* Randomized tenders
	* Smokebox doors are graphite until 1945 or shortly before.
	* Some locomotives will have the option to be repainted into Daylight colors after a certain date.
	
WHY I CHOSE THE CLASSES I DID

The SP rostered over 5,000 steam locomotives over its life, many of them unique. It would be impossible to represent them all. However, since drawing with pixels is imprecise anyway, and the method I use to estimate horsepower is ridiculously unreliable, I've chosen some representative classes with the goal that any steam locomotive can be stood in for by one of the available options.

For example, the Central Pacific owned hundreds of 4-4-0 locomotives in its early days. Almost every single one was unique, but there were many similarities. Boiler pressure, wheel and cylinder dimensions, and overall weight all hovered around the same values. Therefore, I've chosen Cloverdale, later classed E-10, to be my representative for all the light 4-4-0s built in the 1880s. Jupiter represents the 1870s, Nevada the 1860s, and class E-8 represents the 90s. E-23 represents all the heavier 4-4-0s built after the turn of the century. With these five classes, any of the roads hundreds of 4-4-0s can be at least approximately represented.

In a few cases, there are a lot of options. In the 1880s and 90s the CP experimented with coumpound expansion and the 4-8-0 wheel arrangement, leadng to no fewere than three variations of the TW class in the 1890s alone. Many of these were later simpled and/or superheated, leading to even more classes later in the 1900s. As a result, almost every TW class has been represented, many multiple times, with the only missing ones being the TW-2, which was almost an exact copy of the TW-3 built the following year for another SP line, and the TW-6 and -7, which were very similar to the TW-4 and only comprised a total of 6 engines.

I've mostly left out locomotives that were built by another railroad and acquired by SP at a later date. This is mainly because of confusion about introduction dates. For example, the SP's B-1, the only class of 2-8-4s on the road, were built for the Boston & Maine in 1928, but not acquired by SP until 1945 to help with the war effort. I could introduce them in 1928, but that would be wrong because SP had no berkshires in 1928. I could introduce them in 1945, but by that time there's not a huge need for an engine from 1928. I still may introduce this class because it was unique.

I have included locomotives that were built be SP predecessors and not acquired by SP until later, however. So locomotives owned by the Central Pacific, Northwestern Pacific, El Paso & Southwestern, San Diego and Arizona Eastern, and others are included. This includes the Pr-1 and the D-1, because they were unique. However, I have left out Cotton Belt locomotives, so the GS-7 and -8 will not be included. I have also not included some of the EP&SW's 4-6-2s, 2-8-2s, and 4-8-2s because they were in many cases very similar to engines delivered to the SP lines.


For freight and passenger cars, I simply chose classes that had similar gameplay stats and grouped them by the earliest class. For example, the SP had  14 classes of 50 ton tank cars in the 1900s, but there were really only three types: 12,000 gallon riveted tanks, classes O-50-1 - O-50-11; 12,000 gallon welded tanks, classes O-50-12 - O-50-13; and 8,000 gallon welded tanks, class O-50-14. All these cars were 37'-41' long, and can be represented with a small group of sprites and stats, which also avoids cluttering up the purchase menu. All the information on these comes from http://www.railgoat.railfan.net/spcars/byclass/index.htm, which has been an invaluable resource for putting this pack together.
	
LOCOMOTIVE LIVERIES

Locomotive color is a complicated topic, especially since most photos of steam locomotives are in black and white. As far as I've been able to tell, there were a few major paint schemes.

In the early days, locomotives were painted colorfully and often decorated with brass or painted wood. There's very little information on this time.

In the early 1900s, locomotives were primarily black, with the words "Southern Pacific" on the cab and the locomotive number on the tender.

In 1916, the locomotive number was moved to the cab and the tenders were lettered "Southern Pacific Lines." As far as I can tell, this is around the time that they began painting the boiler jackets in different colors. There is evidence that Baldwin painted locomotives with light grey boilers and brownish-red cab roofs from the factory. Additionally, many early black and white photos clearly show the boiler in a lighter color than the rest of the locomotive. Finally, it is known that some of the road's 0-6-0 switchers that were assigned to passenger terminals wore a fancier green and red paint scheme into the 40s, and a number of restored SP passenger engines have also had green layers of paint discovered beneath many coats of black during restoration.

In the mid-1930s, the railroad went back to black for all engines.

In 1946 the word "lines" was dropped from all lettering, and smokebox fronts were painted aluminum for visibility.

Due to these factors, as well as the scant photographic evidence I can find, I've decided that freight engines will be painted grey and red from 1916-1934, passenger engines will be painted green and red, and both will be black from 1935 onward. Smokeboxes will be graphite until 1945, at which time the door will change to aluminum.

The grey-and-red paint scheme will also be available in dual company colors, with the boiler being the primary color and the cab roof being the secondary. This scheme will be available regardless of the date.

If you have any information for me, please contact me and tell me about it.

LICENSING

I've used a restrictive license for now, since I'm still in
the early stages of the project. I plan to eventually release
it with a more permissive license when it's more complete, and
I'm also open to collaboration if anyone is interested. Contact
ruiluth on Reddit or the TT forums.

Sources:	
		Southern Pacific Company Diagrams of Locomotives and Tenders, edited by Richard K Wright, 1973.
		https://www.steamlocomotive.com/
		https://spdaylight.net/Engines.html
		http://modelingthesp.blogspot.com
		http://www.railgoat.railfan.net/spcars/byclass/
		https://spdaylight.net/Consist.html
		http://utahrails.net/russian-iron.php

Changelog:
	v0.1:
		*	Initial release
		*	NEW:	Repaint cargo
		*	NEW:	A-3 4-4-2 in black, CC, and four colors of Russia iron.
		*	NEW:	100-C tender
		
	v0.2:
		*	NEW:	C-30-1 caboose in Brown and CC.
		*	NEW:	60 ft Harriman coach, baggage, and RPO, and 40 ft Harriman RPO in Dark Olive.
		*	NEW:	M-4 2-6-0 in black and CC.
	
	v0.3:
		*	NEW:	E-23 in black, CC, and Russia iron
		*	NEW:	E-23 Rebuild in black and CC
		*	NEW:	A-3 Rebuilt in black, CC, and Russia iron
		*	NEW:	MC-2 in black and CC
		*	NEW:	C-3 in black and CC
		*	NEW:	C-9 in black and CC
		*	NEW:	C-9 Rebuild in black and CC
		*	NEW:	T-1 in black, CC, and Russia iron
		*	NEW:	TW-1 in black and CC
		*	NEW:	36 ft double sheathed wooden boxcar
		*	CHANGE:	Harriman cars available in CC
		*	CHANGE:	Harriman cars now display cargo aging information
		*	CHANGE:	Expansion and heating info for locomotives
		*	CHANGE:	Locomotives refit using passengers
		*	REMOVED:Repaint
		
	v0.4:
		*	NEW:	120-SC tender
		*	NEW:	120-SC-2 tender
		*	NEW:	T-32 4-6-0 in black, CC, and four colors of Russia iron.
		*	NEW:	Six classes of PFE reefer in seven paint schemes that update according to year
		*	NEW:	40ft Single seathed wooden boxcar
		*	CHANGE:	More letterng on the 40' RPO
		*	CHANGE:	Adjusted all engines' maximum speed to match that shown in the diagram book.
		*	CHANGE:	Painted the roofwalk on the 36ft boxcar to match the roof color
		*	FIX:	C3 and C9 cylinder cover color
	
	v0.5
	Oh boy, big update.
		*	NEW:	B-40-15 Express boxcar in dark olive and CC
		*	NEW:	B-40-16 Express boxcar in Overnight and CC Overnight, both prewar and postwar variants of both.
		*	NEW:	B-40-18 Boxcar
		*	NEW:	G-50-3 Drop-bottom gondola. Load textures are planned for the future.
		*	NEW:	S-40-2 Stock car
		*	NEW:	S-40-12 Stock car
		*	NEW:	C-40-1 steel cupola caboose. The texture for the C-30-1 has been updated to appear more wooden.
		*	NEW:	CA wooden caboose. I couldn't find any pictures of this at all, so I used the same sprite as the C-30-1 following the tendency of post-harriman designs to follow Common Standard designs when possible. If you have any information on this, please contact me.
		*	NEW:	A-6 in daylight and CC.
		*	NEW:	GS-1 in black, CC, and passenger schemes.
		*	NEW:	SP-1 in black, CC, and freight schemes.
		*	NEW:	235-R tender (not cuurently attached to any engine)
		*	NEW:	The entire 1941 Coast Daylight consist, including the 79-CB-1 chair-baggage car, articulated chair car, three-unit diner, 79-C-2 chair car, 79-T-1 tavern car, 79-PR-1 parlor car, and 79-PRO-2 parlor-observation.
		*	NEW:	Placeholders for 2 boxcars, 11 flat cars, 5 gondolas, 5 hoppers, and 3 tank cars. They are hidden by default, but can be enaled through a parameter if you want to use them in an untextured state. This will allow you to play the game from about 1910-1950.
		*	NEW:	Placeholders for 39 locomotives that I plan to include eventually, mainly for my own organizational purposes. They don't do anything yet.
		*	NEW:	Some flavor text for the more interesting locomotives.
		*	CHANGE:	the 36ft double sheathed wooden boxcar is now the B-40-6 class
		*	CHANGE:	the 40ft single sheathed wooden boxcar is now the B-50-11 class
		*	CHANGE:	Any train headed by a locomotive from this set with at least one freight car attached must have a caboose or passenger car from this set on the end before it can leave the depot.
		*	CHANGE:	All coaches will age cargo at the same rate. Sleepers take double the time for cargo to age in transit. These times can be doubled by adding a diner, observation, coffee shop, or tavern to the train.
		*	CHANGE:	Reworked colored boilers to be more prototypical. Red and blue boilers are gone, and grey and green colors are referred to as "freight" and "passenger" styles, respectively, based on my observations of historical photos and the scant information I've been able to find online. Locomotives are now available with one or the other or both, depending on their typical roles. You can choose between black, cc, and color until 1934, but from 1935 on, you can only choose black or cc.
		*	CHANGE:	changed the color scheme for company colors. The secondary color is now applied to the cab roof rather than the injectors and cylinder covers.
		*	FIX:	Boxcars can carry goods.
		*	FIX:	Added missing booster to Mt-1.
		*	FIX:	Redid all the sprites using a modular image format. All misalignments should be fixed.
