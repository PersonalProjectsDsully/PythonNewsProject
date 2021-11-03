import requests

links = ['https://redteams.net/',
         'http://blog.uncommonsensesecurity.com/',
         'https://blog.team-cymru.org',
         'http://silendo.org',
         'https://www.osint.fail',
         'https://cyberstrategies.wordpress.com',
         'https://redteams.net/digitalops',
         'http://www.automatingosint.com/blog',
         'https://www.bellingcat.com',
         'https://redteams.net/blog/',
         'https://jesterscourt.cc',
         'https://krypt3ia.wordpress.com',
         'https://raffy.ch/blog',
         'http://blog.uncommonsensesecurity.com ',
         'https://redteams.net/digitalops/',
         'https://blog.fortinet.com/feeds/latest.rss',
         'https://www.cybrary.it',
         'https://www.gironsec.com/blog',
         'https://blog.kchung.co/',
         'https://randywestergren.com',
         'https://www.cyberguerrilla.org/blog',
         'https://www.evilsocket.net/',
         'https://www.webroot.com/blog',
         'http://marcoramilli.blogspot.com/',
         'http://shell-storm.org',
         'https://hacktips.it',
         'https://blog.zsec.uk/',
         'https://digi.ninja/rss.xml',
         'https://blog.skullsecurity.org',
         'https://l.avala.mp',
         'https://highon.coffee/',
         'https://justi.cz/',
         'https://null-byte.wonderhowto.com/',
         'https://krebsonsecurity.com',
         'http://breakdev.org/',
         'https://www.eff.org/rss/updates.xml',
         'https://protonmail.com/blog',
         'https://isc.sans.edu',
         'https://www.oreilly.com',
         'https://blog.netspi.com',
         'http://0x00sec.org/top/monthly',
         'https://owasp.blogspot.com',
         'http://blogs.bromium.com',
         'https://osandamalith.com',
         'https://blog.codinghorror.com',
         'http://www.veracode.com/blog-bkup-not-in-us',
         'http://blog.airbuscybersecurity.com',
         'https://xorl.wordpress.com',
         'http://doar-e.github.io/',
         'https://blog.torproject.org/blog/feed',
         'http://blog.thinkst.com/',
         'http://www.securityforrealpeople.com/',
         'https://blog.zsec.uk',
         'https://blog.codinghorror.com/',
         'http://blog.airbuscybersecurity.com/',
         'http://www.toolswatch.org',
         'http://seclist.us"',
         'http://www.kitploit.com/',
         'http://n0where.net',
         'http://seclist.us',
         'https://torrentfreak.com',
         'https://www.schneier.com/blog/',
         'https://www.darknet.org.uk',
         'https://www.troyhunt.com/',
         'http://www.alex-ionescu.com',
         'https://securelist.com',
         'http://malware.dontneedcoffee.com/',
         'http://www.zdnet.com/',
         'https://danielmiessler.com',
         'https://blog.malwarebytes.com',
         'https://www.blackmoreops.com',
         'https://www.enisa.europa.eu/front-page',
         'https://blogs.technet.microsoft.com/srd',
         'https://haveibeenpwned.com/',
         'http://blog.malwaremustdie.org/',
         'https://enigma0x3.net',
         'https://wordpress.org/news',
         'https://www.enisa.europa.eu/front-page"',
         'http://securityweekly.com/',
         'http://www.securitytube.net',
         'http://www.irongeek.com/',
         'https://www.phillips321.co.uk',
         'http://addxorrol.blogspot.com/',
         'https://intercepter-ng.blogspot.com/',
         'http://www.malwaredomainlist.com/mdl.php',
         'http://securityblog.gr',
         'http://0x27.me/',
         'http://blog.exploitlab.net/',
         'https://linux-audit.com',
         'https://insights.sei.cmu.edu/cert/',
         'http://securesql.info/',
         'https://blogs.forcepoint.com/',
         'http://blog.wh1t3rabbit.net/',
         'https://www.zscaler.com/',
         'http://thesprawl.org/feed/',
         'https://cyberarms.wordpress.com',
         'https://blog.zenmate.io/',
         'https://www.lookingglasscyber.com',
         'https://cofense.com',
         'http://anti-virus-rants.blogspot.com/',
         'http://www.hackw0rm.net/',
         'https://www.trustwave.com/rss.aspx?type=slb',
         'https://cybersyndicates.com/index.xml',
         'https://averagesecurityguy.github.io/',
         'http://blog.shodan.io/',
         'https://ctfcrew.org',
         'http://blog.mdsec.co.uk/',
         'https://www.trustedsec.com',
         'https://whitehatcheryl.wordpress.com',
         'http://securingthehuman.sans.org/blog',
         'https://www.jumpsec.com',
         'https://dwaterson.com',
         'https://www.darkoperator.com/',
         'https://dotcppfile.wordpress.com',
         'http://www.4n6k.com/',
         'https://binaryforay.blogspot.com/',
         'http://blog.gdssecurity.com/labs/',
         'https://holisticinfosec.blogspot.com/',
         'https://www.secureworks.com/blog',
         'http://www.netresec.com/?page=Blog',
         'http://www.honeynet.org/blog',
         'https://pendingtech.wordpress.com',
         'https://blog.erratasec.com/',
         'http://blog.shadowserver.org',
         'https://threatmatrix.cylance.com/',
         'https://access.redhat.com/blogs/766093/post',
         'http://antukh.com/',
         'https://luxsci.com/blog',
         'https://www.invincea.com',
         'https://www.ethicalhacker.net',
         'https://grymoire.wordpress.com',
         'http://ly0n.me',
         'https://security.stackexchange.com/',
         'https://www.sans.org/reading-room/',
         'https://blog.rootshell.be',
         'https://blog.0x3a.com/',
         'https://www.us-cert.gov/ncas/alerts.xml',
         'https://blog.cobaltstrike.com',
         'https://blog.rapid7.com/',
         'http://www.shelliscoming.com/',
         'https://www.lastline.com',
         'http://maltego.blogspot.com/',
         'https://www.malwaretech.com',
         'http://www.hackingarticles.in',
         'https://cloudblogs.microsoft.com/microsofts',
         'http://resources.infosecinstitute.com',
         'http://blog.whitescope.io/',
         'https://blogs.cisco.com',
         'http://blog.unmaskparasites.com',
         'https://www.imperva.com/blog',
         'https://blog.hboeck.de/',
         'https://www.checkmarx.com',
         'https://adsecurity.org',
         'https://www.stopbadware.org/blog',
         'https://azeria-labs.com',
         'http://pentestmag.com',
         'http://decentsecurity.com/blog/',
         'https://www.mogozobo.com',
         'https://blog.cloudpassage.com',
         'https://astr0baby.wordpress.com',
         'https://hakin9.org',
         'http://seclists.org/#pen-test',
         'http://contagiodump.blogspot.com',
         'https://www.social-engineer.org',
         'https://www.whitehatsec.com',
         'http://0xdeadcode.se',
         'https://www.j4vv4d.com',
         'http://www.ericconrad.com/',
         'https://www.andrewhay.ca',
         'https://milo2012.wordpress.com',
         'https://leonjza.github.io/',
         'http://securosis.com/blog',
         'http://www.kahusecurity.com',
         'https://jumpespjump.blogspot.com/',
         'http://carnal0wnage.attackresearch.com/',
         'https://www.crowdstrike.com/blog',
         'https://www.codeandsec.com',
         'http://www.harmj0y.net/blog',
         'http://www.seculert.com/blogs',
         'http://mosaicsecurity.com',
         'http://deviating.net/words',
         'http://blog.sucuri.net',
         'https://www.dearbytes.com',
         'https://www.securityartwork.es',
         'http://www.xylibox.com/',
         'https://sakurity.com/blog/',
         'https://thepcn3rd.blogspot.com/',
         'https://www.symantec.com/connect/item-feeds',
         'http://www.juniper.net',
         'http://www.kioptrix.com/blog',
         'http://securityandrisk.blogspot.com/',
         'https://www.proofpoint.com',
         'https://blog.qualys.com',
         'https://myexploit.wordpress.com',
         'https://www.martinvigo.com',
         'https://unlogic.co.uk/',
         'https://www.commonexploits.com',
         'https://www.rebootuser.com',
         'http://pen-testing.sans.org/blog',
         'https://quequero.org',
         'https://www.f-secure.com/en/web/labs_global',
         'http://www.top-hat-sec.com/r4v3ns-blog',
         'https://www.corelan.be',
         'http://infosecninja.blogspot.com/',
         'https://natmchugh.blogspot.com/',
         'https://appsec-labs.com/portal',
         'http://theloopcast.podbean.com',
         'http://gynvael.coldwind.pl/',
         'https://www.infosecisland.com',
         'https://blindseeker.com/blahg',
         'https://www.sans.org/tip-of-the-day/rss',
         'http://www.fireeye.com/blog/',
         'https://cybersecurityventures.com',
         'https://www.forensicfocus.com/',
         'https://taosecurity.blogspot.com/',
         'http://www.securitytut.com',
         'https://securityzap.com',
         'https://wiremask.eu',
         'https://securitycurrent.com',
         'http://www.thegreycorner.com/',
         'http://www.doomedraven.com/',
         'https://www.edgis-security.org/blog',
         'http://www.hecfblog.com/',
         'https://volatility-labs.blogspot.com/',
         'http://securityspread.com',
         'http://seclists.org/#basics',
         'https://blog.silentsignal.eu',
         'https://blog.sucuri.net',
         'http://edge-security.blogspot.com/',
         'https://blog.fox-it.com',
         'http://www.labofapenetrationtester.com/',
         'https://www.f-secure.com/weblog',
         'http://lifeofpentester.blogspot.com/',
         'https://www.virusbulletin.com/rss',
         'https://labs.portcullis.co.uk',
         'http://www.tenable.com/blog-2016',
         'https://blog.didierstevens.com',
         'http://security.googleblog.com/',
         'https://www.exposedbotnets.com/',
         'https://www.yubico.com',
         'https://www.scriptjunkie.us',
         'https://www.pwnieexpress.com/blog',
         'https://sensepost.com/rss.xml',
         'https://medium.com/@sroberts?source=rss-62a',
         'https://blog.mozilla.org/security',
         'https://www.notsosecure.com',
         'http://www.cerias.purdue.edu/',
         'http://www.ehacking.net/',
         'http://www.bluekaizen.org',
         'https://www.securitysift.com',
         'https://www.trendmicro.com/vinfo/us/security/news/',
         'http://www.subliminalhacking.net',
         'https://blog.nviso.be',
         'https://www.hackmageddon.com',
         'https://zeltser.com',
         'https://tails.boum.org/security/index.en.ht',
         'http://www.primalsecurity.net',
         'https://www.christophertruncer.com',
         'https://blog.cryptographyengineering.com',
         'https://googleprojectzero.blogspot.com/',
         'https://w00tsec.blogspot.com/',
         'https://icanthackit.wordpress.com',
         'http://www.imperialviolet.org/',
         'https://sploitfun.wordpress.com',
         'https://blog.netwrix.com',
         'http://www.team-cymru.org',
         'http://kb.refinepro.com/',
         'https://khr0x40sh.wordpress.com',
         'https://cybersecurity.att.com/',
         'https://www.forcepoint.com/blog/audience/cxo-cybersecurity-perspectives',
         'http://www.hackw0rm.net',
         'https://www.trustwave.com/en-us/resources/blogs/trustwave-blog/',
         'https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/',
         'http://contagiodump.blogspot.com/',
         'https://www.us-cert.gov/ncas/current-activity',
         'http://edge-security.blogspot.com ',
         'http://delimitry.blogspot.com/',
         'https://www.coalfire.com/Solutions/Coalfire',
         'http://www.ehacking.net',
         'https://www.trendmicro.com/vinfo/us/',
         'http://blog.nibblesec.org/',
         'http://blog.mindedsecurity.com/',
         'https://bugbountypoc.com',
         'http://blog.bugcrowd.com',
         'https://gerbenjavado.com/',
         'https://c0rni3sm.blogspot.com/',
         'https://buer.hausi',
         'https://foxglovesecurity.com',
         'https://whwriteups.blogspot.com/',
         'https://bugbountyforum.com/blogs',
         'http://www.wisec.it/sectou.php',
         'http://c0d3g33k.blogspot.com/',
         'https://blog.mert.ninja/',
         'http://blog.kotowicz.net/',
         'https://blog.it-securityguard.com',
         'https://c0rni3sm.blogspot.com',
         'https://buer.haus',
         'https://blog.it-securityguard.com" ',
         'https://backbox.org/portal/blog',
         'https://www.kali.org',
         'http://www.weaknetlabs.com/',
         'http://distrowatch.com/',
         'https://www.whonix.org/blog ',
         'https://tails.boum.org/news/index.en.html',
         'https://blog.linuxmint.com',
         'https://www.whonix.org/blog',
         'https://tails.boum.org/news/index.en.html',
         'https://www.grahamcluley.com',
         'https://thehackernews.com/',
         'https://securityaffairs.co/wordpress',
         'https://blog.trendmicro.com',
         'https://www.theregister.co.uk/security/',
         'https://researchcenter.paloaltonetworks.com',
         'https://www.instapaper.com/',
         'http://threatpost.com',
         'http://digital-forensics.sans.org/blog',
         'https://www.darkreading.com',
         'https://latesthackingnews.com/feed/',
         'https://securityweekly.com/feed/',
         'http://feeds.feedblitz.com/securityledgerpodcasts',
         'https://feeds.feedburner.com/TheHackersNews',
         'https://radar.securitywizardry.com/',
         'https://security.didici.cc/',
         'https://threatpost.com/feed']

for link in links:
    try:
        r = requests.get(link)
        if r.status_code == 200:
            print(link)
    except:
        print("Failed")