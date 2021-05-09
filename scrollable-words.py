

one="AC1222".lower()
two="BO1222".lower()
three="OU1222".lower()
four="UL1222".lower()
five="D11222".lower()
sys=__import__("sys")


if len(sys.argv)==2:
	one=str(sys.argv[1][0:6]).lower()
	two=str(sys.argv[1][6:12]).lower()
	three=str(sys.argv[1][12:18]).lower()
	four=str(sys.argv[1][18:24]).lower()
	five=str(sys.argv[1][24:30]).lower()
elif len(sys.argv)==6:
	one=str(sys.argv[1]).lower()
	two=str(sys.argv[2]).lower()
	three=str(sys.argv[3]).lower()
	four=str(sys.argv[4]).lower()
	five=str(sys.argv[5]).lower()


wordlist=[
	"about",
	"after",
	"again",
	"below",
	"could",
	"every",
	"first",
	"found",
	"great",
	"house",
	"large",
	"learn",
	"never",
	"other",
	"place",
	"plant",
	"point",
	"right",
	"small",
	"sound",
	"spell",
	"still",
	"study",
	"their",
	"there",
	"these",
	"thing",
	"think",
	"three",
	"water",
	"where",
	"which",
	"world",
	"would",
	"write",
	"testw"
]


string=one+two+three+four+five
combinations = [list(elem) for elem in list(__import__("itertools").combinations(string,5))]
print "\n"
if len(list([e for e in combinations if "".join(e) in wordlist]))!=0:print ["[WP] Found Word \""+str("".join(x))+"\"" for x in combinations if "".join(x) in wordlist][0]
else: print "[WP] No Word Found"
print "\n"
