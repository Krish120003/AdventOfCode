import math
import collections
from collections import Counter
import re
from tqdm import tqdm


TEST = """
2333133121414131402
"""

PROD = """
2847796712879033433718603712718817354736281243964888223682694953479950792417879182187383805728208021969669819725574153728544608865468619788443786228879041777294508133256267708489825197157576995557114914777260466750629195935891235828221856509474654017546089994652235862211759249849175492377084661971734055948923317412805147549454262167624990989160957780697726661657713798189894156137528180563284441320838047593273446917256875106326605484438418913671297682662857438259566850291311753053609689229370673867533154103252382636858239164230929633449292696972321383671691568269341220449010333026141189122168855183149088419217906369755878248595144621597181837551146556589948423431952881911374379658777357386092599849231699674351243711506018568345911615642069768546956559334456402299252040878711727531791191967432828881692751802089458761682668134125291776284412358295884263579064628811349085332924379792476544325144695130868586157757256196897980147971662114172447148342827580877964607039991939583490311055435543382963415463439847507810681021105914724867729157928393465940597134953791764511139883886573685719106116149339573511964595876568331535628987109458744466104496335414804443101068774655637886902819154313671385476218573116541236814742953078353741166015573075225355611547787235504882694399407812423639646573936342848314217219246757481831608769185062223781456046462342281795674215952165432372337253468299131421916540337687912285247311198736387073405657934091689627112937905383913277968216555148703844793530513679521172186164616587515217908911488549647616603779405429646866186835584253693723128175438182193318253849502390154334394634421131208276523190113299966480551291213675963657329137616760456056829023712546864330498857949759727945224322257634882373858942659415749233111218408722131259731382184918405558436412243589982056413311399038414572994130981056206819134757353897205756609759464730701741581372339645483927135491316726546030268439604098277438107391341397999513739926447877506440825484861667646063289095206379713658127343837822782596391585718560971739833875967053954385575037339912446939791410664939417860238576498246242880757078876547312573303995608385189028127994875423875877607487204339141317729689655331665689223894815571938898513923154945524070275183443791423389754774692696123075334513199599903419216452982675738276576987604452681614931030117080425543158932813636913357311123805954872867459483837643979975481241854363844394736749832437225021425316161318495285258493544170763229776642993666241422572428395668405750848971893663467583531554757769518222495116966533458639578730634080811999593730756314916486946811186636358598572010831546681980759927226149882817742284981325302260594778608844423969721150403984594088963023872952322892687530475076187288661854764381246394292058671451253770961995151841308528417955204245944520633920888544508028563278606767894685363818456273577356558324281510671866959289984840674977401036499084442582729456295019675251442378495652369640944510206582166377327798495365178926878758163435636061907311359262239027188390547473941930248154694391596744454161442813607617308964918788178870419960833381222313263354421293962152952837766181357495771533843420614843821618149270494432761787698060483083151739123612127394951710694131852532382451162155353177351462515143529914934032724417532313262358687331829319683651714947876854692483876721267881491257611927849999827030485818452293476124858916444681446547138021952625415738209568237352837293159020844074274776482287452186484925608218151828516498759462246752117077829992597937862594332958544392237460815191221214641793389255959966697210768699906927236561851469738987523717928790131644813533231241825452912166608525757290694928285442742788385158585237944131168333155189764463497787319771798875613559306548347872973672192381131332139236991943788983334278973116475523354932177371944967958247535155668160133629939732748620245698344793585746333147806757331590104186187739731759321651411196181875294610144146118643289936885668428520654386381954445068722469644369708177578573435378196834827776754592828176244144924272181480354266586798498411823719884570509667557485819046158761276468888445198399871864645949134770735684786746206620283340179464364347467479657914879461509220432265765589658278465147992747578278958092307477493573981655906019555310869954166717751678642644924993151252565992581811695774163793763963786090823742605288105277991287337081497861744819156555824773507435743652864897197371583883413213466935593040936071918351526740998240544569808531645690538860742245307076928583323198272658319547468452966785466047316780964857994093829476373428925886443429697124937076445472844484668554704037738568664566723156993431645047969815393422974756756347545067774735463642272090803236589931398272413688583756902145183248123772578541802248974856868438805546521933154341557115353128725256479782827229755367953397492239312137906134297882737993841385924839436555878585453667135365539881829925735036381070712488441821153270145262372475745233816374593247304823261744103362572318858467263364865788166096857069127262101094847583841141834648853127305554307567846957208267651012889913143854104645414960124887263279356153925118723334546144787168119793934661151746609767225848363118265652134071247185317830824518409865231592395777104829942227928033964966915014259345263757862820323631228642855943809445206458972456112881872210883270177631337382778367111373351665637245948237214462932128279622254573301950793045112182393736931356145980719773624867544760652311904482125930376293534311964344491074807541214263162210332179458092934267869541949084912093673236277491212988138595762614537612512985229630642138632187667873571840684590184646769636655420883651319480617954588532562762204867599677833122809478686678792245342121205720519173912522879297684148229814815013488417714578976291936793317819192716456216743197417858921717468189441811244453124311399682241270697255561434377781529634943975895822925210534790273038342211476684513848526314409766768894781096655479436278688343431451192229809584482837131512758642997218411183593862328963471699549317333091891314985994354833995356726320843088442051816592106123636922402727225739138119829088281835368560739267388212633629379890624153797037994453871588326123421935353489987878191729201921637148473319195933927538496168665654308255931789878216743532761157128344725324344018492531282167314011963327468895361489224186959867212177229716941128915566584626483086816388514366716180621384725732742166553251388292401539992266758994525533525933897257492333699980908817866047611134668837535595814159306525712432306416169736296052895332785832576326464095384287673028468695336217668557691655138571442697294782995863458082694737799838821419626010309740754739105860456192364162698159586180726639177417299198216675917877968192394872716613882368632344975845936180181647392689592969346887112040535147765724849983519388617363257638177546783521513883294271187616573112794185519325552782896313675831835332199299518881666981644117445297599720344154269262352366902084575972712899251178275877616351583437356179109322723764256259551964929390408894751865515732564971939177452539985596341138439194663678804582784690931743461340508317509057723483407465968344218634758763331021814684187654223943238270172211284355814251648059287424757894657590296291621669938472974986507841135686139249533099977998819841205421327660207882122437126118269285243438211253665612951315352767897433672455265653623658301276402467427029107463307939822534109563194957859528476024325654478094183516987750102626371793989138911934326335625599869923356794413361787828765325611031164858548295862538718127892946377843798791458585659363554115393078568558465976946828492289855529824354733331233697623654816453667358487717212592847718837161561485201949958720322812533916362231804795157790892139276124675173754738485028376454254557693956803223359824551073943631958343264484149368446558453689675729717644309987653560111972161564266966676136163479356533838340723586498410809689679768966927751054275381457481521584652158689320514278718023741733903170902085739052432547568382222489832369435833281565295957337468682250658061574572145273474876349222618519925221955492559071644486467716767950444557393128911017691433775686268259876196842663276344814071382066268278949162999239305519109714101189963211392968567864804498898325793173964240857930611579758319219213697543803278345821583811555128381684146561409143461736756845705355772616926448478152331296916915917479507617923140152860571045632037115719598453598983654442579920506788492148865231255696922440204449323297335981982014614748327747365244527745332864193987724611533312949332751393331997557010698714261536106223182727617916613814671061773349255356798847833855886264515860148563697970636946776180844045281295558080724070223875427459171330723752372484907975217348692314734196983735989384554688624037112191415643767337304728887221245248686440822951293882532210928090749859755050246485353260304011763823899912354034411310879767953896383095997695362664353832699320323551976585942747508627338323843473553975819074306340593611762271264528712915865155337861129928761728127133841295231992276927639371676262375457858413136037471052441976823559564957581067408434889344632925611541678683486014736120673256325691643352579293566812764085698254817016792355379977309945229944382286256052228898187949464192974442345874162817659794662587115451157599993574253287324947322787622144236490572082494817857764183593409885141361197470762133762814556614294728682029542588783340838785695840593968609855126919898832653650863682348182469423978395705730295319572971469976742658524765765423886940291322351423207725813793845912194132985799887574794039546522273523106014457522872056148098818881341472751143861938831290938923164580185974694459434031999180109132416957669214603160703767643524601452937549256623552057665410182516325169902093363476588162799086541720453061672656866124734499627731796128772176591159494576357183495236261113764049882937952932514682738635471510415581958157694189898454926946581370805664321851629168225379273390728143184151549097502453822845273593908889214663203544377948604427388068388387207947581692719516543128552382154475369657865861189632662756783080887846395266379246738370258726931862994196731944171672984575728169526236768389503227317316285732622095547388357492467249947834324681799745691398413935761163171069371751935092147275263340867340873513629689698396647327748572697349847230576560678364686911506937244752577833811049167064282620823731731566377757635716627495301185166097234164354631805924931112907191844967267973725092155314475954924133424528961489948371331196915247343866831344116793279337604755939863652513458014206980726348465185525571111688858391751661373892271046693392678586544842244973298245506149918743443396725277954598869966733746587391957998239271572412859040292535576680366778761591798729669412561664347769645911132945305395168343148992123827802025229489759987928027107773131365349773826748507676123358635673404079135661609055482010944446977993549385999718195110859141263553546359321572615546513121525114288824679831776233574982381393108045299097906277336623148413906385194596296737397646633744868141761091226072206936213590747914901996412457264264287010351758399930843017765624933883273664626873562936845310564875207418764435478570986572445972409922757487958389714519519484477990558935395225449527674968959985162843324867737730298316966443565043493078991755909629382987744944897288872483505063491914871134184841188154753872293390362635435044809497427899256345308362632213296573857897219563755776102731558874497252655224291239824232964342654847215348689470586865102150374089398776232316151370178170652176422566588268894533544231566041236792747245277674331369992170415517857845678148706650865998347614355767369780108723149446335117159395288314469858997623886567607152331870708626917667521777801082441267323339833817478825917072538290246816488815591380501769881861756655927412471525567318109268874744685425184124243483619684301871382840672467539592865037278844573867518566159258931939417817443155447440513474265223706481759043931631411491826263129773246762441264509988827367969169751139116435175999377315694138832641498434135222996072879613269153522157976928671681914899421184898549481125676528605120106942732823865451719844743016382968324131216431835082855247158128575743711167752035907187324219906036541643334321698715766211615822251441415995625341224368235470239627438590371953977619716185949569199039641794145278393187387041755821675450111492528393138959622921536180251670912824664643807839293177797884644068749098925312359695782391454989212957708455897897238274938776448433211879579436877213614770397916499777121474376349216093638078227218671214794520694088553154359964307858996784781568885064418585146812406313934594884582532846546473747256426234693268349269977782627192821930781870823995659551551551402976159979792233409942403151715485609192779347599346715948915516289634908750262389591756845497667778686928501119226713668132234040228794468183632816674863949714786267263135759853474772268041932987708670216117258429347562651054341160978363399241831419413932492255342888512256135424868673447436202763355825436411208631593487356493238780333745583510461848281997965513702439227987221620771615201798327065598911226355785411507833433137819019853224416993791229643855279480745013341844362772675594308471139055935012809258772447197953575790253531123318273942657478786959816036788743774323256956376371477577762326253319686219189262451511664055754790492294517747714976257476399326228943707299872775118238105596412454733129976598376268523768761656596885163427929137223077233194855386198777848268997991401677462630975710322977409826233455627470982676416091112726128327969659973965699842888975122444662128198086279232386985448812515537719083133714392536232215272045485461174117567094658097738922613769395678709088477360274233189896415569676463965143362457785632161890868156578164183393521645991821167399833868988851251274471629933913607454544520651762554455624591886071834839149330743090574482124994859218945123288330302257982767708230354180797168585938559826287854131519703293271617306475527929693125772921251031554443524011852121803434397934474475439270875429469272357250909514528385832241694821326850804688137348135893653199886696951786201561701283962520452264372638973934286570667958613443625075648470241510433197174066941756172458902450174517821241278078893397422162675657963017322372859153987093162715716397257413398134549062129812574617726046254788986346475171531831727469214866795972374799635065335260829350511350335075975415392837133941515244952751736380141592536895261722269967732682336368723662262194295018583277187218888242781584933786787921375971271749196617929763932792657212391629113232853910517745828156595072657526204563124526597067904378607962821650321755848726303292184910265118159775406859406260249414458032324072948674158880864138694876407596544440468341279111702241865924453326369252174088378837782840631850171935918149891078737537509872673445446472747384781880239190106634255718712198843898971465609864744128853461218542705135319648533085185718246432534610918182825911269479182747599396725782839234806546369612583458542278423581687595968435413279302776318085261312298013885753234852902679111845509533481760719445411228969982157751224111461843576742759211761433565183337122602543651460905423663521278953686370619416371664783192123459325388886948239272285130197416496657111314859843216123239367343218167559283763447649677668415613278217458479821566684282883578606569916572236750157683333752922014951931905011152554371225303255754155255672464465911010852820739256172611345457526542451599232714956073488284303087146777208542176492588379771650111536541326398746259868727062758884119849884879118156989613428076873962645482718729473485916233406092941064344478182565983066335724441033521483943544209015297111882624926851129740794682931323482472654274906836542870143465344475394790902175115777562276941465441763269998783367524712636970573265447319367716104425615761437530456391142251679353314886784053821631875261881471156973882931494659448157979442841252145745555889358819266651459365108248501629474957916041403473783089624551708884206544185996821549955632714152248088726828665877994560699474613515397386667962512755808241893132859867682448889730648295703184236347773834339456979624667216904116984959302534533318184938707693927093359437512662342234199947614491856694551761184763659594292399431317475170757587709356564542975586262842242093669421896856804773938195638433136936725877827034968816143022496825431817839514517424229555118434171630141634316437238881572931376050459556393533188716348057445929881624241892507218939376945111833223543867214887596828186391433418538811352872239083103551714359492113532912791938876357644736819436474314196545209074635472231197307420359637225538389233521788944390295375978655226344371113315124303141125650805833302637306643171732179361265234795047512367239120797145458620274321701892686644918723992422306676744218647580916053448415288591456119243828173568645134672468937665344267351674469978174667144227165188283484513087905368333189584671901365358170898142767498541732913941842782462772334442432622556593942639178991332258142712493289691977147447903684179246774179515268901429812969804581387235329717506630417961562156438315436643191228887373702593933624291932407510684157286288236219101955819785849695827480919919543698841817145368826063363999169310271124969850382269824249564021657876305388874459268391732087872637903549354952618246716988612580742265477125104152296334806450254862553647327283476974374249245625374296599148505455794538119630245983642456642084323670849986749755806682135644126311586715462849841561755651669293675433646498233378844828119337497058772449125970851721797371201984337532479917365677349663902321357935885463571581766472892646431278576229239499943993683146579674701476395154513897392689441646716887702954896157866062291310323717513212229968901933609430454444571685348060187574836224712175838764523974655999754346951682926583238091223081979416162032171995398312428520354250306970371026647367292029913774737595559791765620677624855237639389914470875223938157655095513959446814583143653872852913665716766950546549471077194248538712186987957790954383683289122991454412378335618466859694954183993149587098815317856959711761954121755460525820364911813162252448898872772832487968538025492173418237458984671711465234788311179881418297811087747039407927757692872413571951415111947845656982968319941414491414522815707552267929259450765242557597358177875287866227411755644077323974261880538660589480752231419510273184925079372376821218594857125270592085753237204395998915724968311515528391687851612570994797709057273320626091462196307882548496168964107543362197409786251421444954479463687925977564337776701319798227969036854468956417742682893327664452535673354150594345849853503419588450883353136279502471191992337128394060676089859575998345689054245174243450308052472389784881807668158842567531986054896492716637776354777735852753796711513950946682119569533128475499228557761578549015412816151239342411945833223566911485724955372041275620692555329970714983953046802687381727451821937370131878478574135421277096829956125792381610415765611779557377197898948333408996819041559425307928682447943095775415944711193030941623587581675054601082484271379394792385819368575395122644707695588554559446992361237983417560721453959933251187585749987967758069729220852820949125646126608699781019382579704298129532278547151416683575794794383949587446514219304582597193627436787762306886141474795931997427475426375896191673753554211366188938195567856855741048213490984984854756579822584832434664184034509874609971415099211187815179131385146775842494186135536928158520595670226565859981667362555925561672643285341340998291173748124579236069405116141557468768453224655827308551405930828836768094337413646966136888709275789584641974614075658660293230393540503036254494261
"""

with open("in.txt") as f:
    PROD = f.read()


# TEST = "11" * 11

x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
grid = [list(line) for line in lines]

result = 0


s = []
i = 0
j = 0
while i < len(text):
    file, space = text[i], text[i + 1] if i + 1 < len(text) else 0
    s.extend([str(j)] * int(file))
    s.extend(["."] * int(space))
    # s "." * int(space)
    i += 2
    j += 1

print(s)
files = dict(Counter(s))
del files["."]


for key in sorted(files, key=lambda x: -int(x)):
    # find the first .
    print("Moving", key)
    start = s.index(".")
    while start + space < len(s):
        space = 1
        while start + space < len(s) and s[start + space] == ".":
            space += 1

        if space >= files[key] and start < s.index(
            key
        ):  # if we have more space than the space required for this file
            s[s.index(key) : s.index(key) + files[key]] = ["."] * files[key]
            s[start : start + files[key]] = [key] * files[key]
            break

        start = s.index(".", start + 1)

    # print("".join(s))


# print("".join(s))
# print(s)


checksum = 0
for i in range(len(s)):
    if s[i] == ".":
        continue
    checksum += i * int(s[i])

print(checksum)

# 90008815667
