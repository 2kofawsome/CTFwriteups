
e = 65537
n = 50630448182626893495464810670525602771527685838257974610483435332349728792396826591558947027657819590790590829841808151825744184405725893984330719835572507419517069974612006826542638447886105625739026433810851259760829112944769101557865474935245672310638931107468523492780934936765177674292815155262435831801499197874311121773797041186075024766460977392150443756520782067581277504082923534736776769428755807994035936082391356053079235986552374148782993815118221184577434597115748782910244569004818550079464590913826457003648367784164127206743005342001738754989548942975587267990706541155643222851974488533666334645686774107285018775831028090338485586011974337654011592698463713316522811656340001557779270632991105803230612916547576906583473846558419296181503108603192226769399675726201078322763163049259981181392937623116600712403297821389573627700886912737873588300406211047759637045071918185425658854059386338495534747471846997768166929630988406668430381834420429162324755162023168406793544828390933856260762963763336528787421503582319435368755435181752783296341241853932276334886271511786779019664786845658323166852266264286516275919963650402345264649287569303300048733672208950281055894539145902913252578285197293
c = 15640629897212089539145769625632189125456455778939633021487666539864477884226491831177051620671080345905237001384943044362508550274499601386018436774667054082051013986880044122234840762034425906802733285008515019104201964058459074727958015931524254616901569333808897189148422139163755426336008738228206905929505993240834181441728434782721945966055987934053102520300610949003828413057299830995512963516437591775582556040505553674525293788223483574494286570201177694289787659662521910225641898762643794474678297891552856073420478752076393386273627970575228665003851968484998550564390747988844710818619836079384152470450659391941581654509659766292902961171668168368723759124230712832393447719252348647172524453163783833358048230752476923663730556409340711188698221222770394308685941050292404627088273158846156984693358388590950279445736394513497524120008211955634017212917792675498853686681402944487402749561864649175474956913910853930952329280207751998559039169086898605565528308806524495500398924972480453453358088625940892246551961178561037313833306804342494449584581485895266308393917067830433039476096285467849735814999851855709235986958845331235439845410800486470278105793922000390078444089105955677711315740050638

primes = [2293226687, 2444333767, 2602521199, 2695978183, 2724658201, 2753147143, 2772696307, 2824169389, 2841115943, 2944751701, 2949007619, 2959325459,
     3056689019, 3057815377, 3228764447, 3238771411, 3417563069, 3638373857, 3716991893, 3986329331, 4140261491, 4152726959, 4218138251, 2436598001,
     2525697263, 2647129697, 2661720221, 2672301743, 2944722127, 3278196319, 3335574511, 3380851417, 3625437121, 3941016503, 2365186141, 2746638019,
     2963383867, 3013564231, 3464370241, 3646337561, 3760232953, 3978832967, 4006267823, 4235456317, 2223202649, 2278427881, 2388797093, 2682518317,
     2858807113, 3130133681, 3589083991, 3684423151, 3991834969, 2322142411, 2510750149, 2575495753, 2657405087, 2854321391, 3012495907, 3174322859,
     3177943303, 3200434847, 3303691121, 3319529377, 3346647649, 3453863503, 3487902133, 3648309311, 3789253133, 3789746923, 3861767519, 3865448239,
     3943871257, 4045323871, 4198942673, 4227099257, 2733527227, 4270521797, 2371079143, 2424270803, 2572542211, 2636069911, 2752963847, 3083881387,
     3488338697, 3721186793, 3833706949, 4056085883, 2148630611, 2216411683, 2707095227, 3279018511, 3522596999, 3623581037, 3833824031, 3854175641,
     4091945483, 4135004413, 4141964923, 4276173893, 2157385673, 2240170147, 2459187103, 2491570349, 2719924183, 3961738709, 4073647147, 4098491081,
     4205028467, 4252196909, 2230630973, 2703629041, 2710524571, 2932152359, 3035438359, 3180301633, 3285444073, 3291377941, 3359249393, 3398567593,
     3411506629, 3539958743, 3686523713, 3811207403, 3860554891, 3923208001, 3959814431, 3994425601]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

ts = []
xs = []
ds = []

for i in range(len(primes)):
	ds.append(modinv(e, primes[i]-1))

m = primes[0]

for i in range(1, len(primes)):
	ts.append(modinv(m, primes[i]))
	m = m * primes[i]

for i in range(len(primes)):
	xs.append(pow((c%primes[i]), ds[i], primes[i]))

x = xs[0]
m = primes[0]

for i in range(1, len(primes)):
	x = x + m * ((xs[i] - x % primes[i]) * (ts[i-1] % primes[i]))
	m = m * primes[i]

print (x%n)
