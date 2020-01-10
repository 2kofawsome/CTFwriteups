# Compute modular inverse of e
def egcd(a, gcd):
    d,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = gcd//a, gcd%a
        m, n = d-u*q, y-v*q
        gcd,a, d,y, u,v = a,r, u,v, m,n
    return gcd, d, y

60413 * 76753
#4636878989

5051846941 / 54269
#93089

p = 66347
q = 12611
(p - 1) * (q - 1)
#836623060

pt = 6357294171489311547190987615544575133581967886499484091352661406414044440475205342882841236357665973431462491355089413710392273380203038793241564304774271529108729717
n = 29129463609326322559521123136222078780585451208149138547799121083622333250646678767769126248182207478527881025116332742616201890576280859777513414460842754045651093593251726785499360828237897586278068419875517543013545369871704159718105354690802726645710699029936754265654381929650494383622583174075805797766685192325859982797796060391271817578087472948205626257717479858369754502615173773514087437504532994142632207906501079835037052797306690891600559321673928943158514646572885986881016569647357891598545880304236145548059520898133142087545369179876065657214225826997676844000054327141666320553082128424707948750331
pow(pt, 3, n)
#256931246631782714357241556582441991993437399854161372646318659020994329843524306570818293602492485385337029697819837182169818816821461486018802894936801257629375428544752970630870631166355711254848465862207765051226282541748174535990314552471546936536330397892907207943448897073772015986097770443616540466471245438117157152783246654401668267323136450122287983612851171545784168132230208726238881861407976917850248110805724300421712827401063963117423718797887144760360749619552577176382615108244813

I forget
#1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729


p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
n = 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239
ct = 10496510088274902517299178768333730065992897742235902320007578224403774318104497156738365444241089630692197311872046743787932903871738912730947374372609494115768796292859523251014066286252373901727312673573274495843410693046791979220669260953960619507971294694463164277744016559982662929754355928780542750072107333974915772701552164290866209545224671282318195750368109981112233864748602184218190031376709412641946959510225082365136919104816042391287051732486769814274336923977198360558519694173601497461543969548258699385186851539202794298787048506039770788426472823983574848966963388594389939049145642334898187112162
e = 65537
q = n // p

phi = (p - 1) * (q - 1)
gcd, d, b = egcd(e, phi)
if d < 0:
    d += phi
pt = pow(ct, d, n)

print(pt)
#14311663942709674867122208214901970650496788151239520971623411712977120527438342574810751357
