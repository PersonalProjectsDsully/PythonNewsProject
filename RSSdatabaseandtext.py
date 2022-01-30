import time

import requests
from bs4 import *
import sqlite3
import logging

from requests import Response
#add status to check if the website is reachable before calling the function for the try and except
#add seperate function to go through all of the links this will make it so once I perfect that I can just throw it in its own file and the lines would be reduced errors and debugging would be a lot easier


def scrape(link):
    source1: Response = requests.get(link)
    soup1s = BeautifulSoup(source1.content, features='xml')
    articles = soup1s.findAll('item')
    i = 0
    for article in articles:
        link1 = article.link.text
        headline = article.title.text
        description = article.description.text
        for div in soup1s.find_all('div', {'class': 'my_class'}):
            for p in div.find('p'):
                p.string.replace_with(p.string.strip())
        date = article.pubDate.text
        date = (str(date))
        link1 = (str(link1))
        headline = (str(headline))
        description = (str(description))
        print(headline)
        i = i + 1
        insertintodatabase(link1, description, headline, date)
    return


def TextNews():
    x = 0
    logging.basicConfig(level=logging.CRITICAL)
    # links = ['https://www.theregister.com/security/headlines.rss', 'https://www.zdnet.com/news/rss.xml',
    #          'https://www.darkreading.com/rss.xml', 'https://www.eff.org/rss/updates.xml',
    #          'https://torrentfreak.com/feed/', 'https://nakedsecurity.sophos.com/feed',
    #          'http://feeds.feedburner.com/TheHackersNews?format=xml', 'https://www.cyberscoop.com/feed',
    #          'https://krebsonsecurity.com/feed/', 'https://www.hackread.com/feed/',
    #          'https://www.cyberscoop.com/feed/', 'https://seclists.org/rss/fulldisclosure.rss',
    #          'https://www.exploit-db.com/rss.xml', 'https://www.grahamcluley.com/feed/',
    #          'https://www.schneier.com/blog/atom.xml', 'https://www.bleepingcomputer.com/feed/',
    #          'https://www.welivesecurity.com/feed', 'https://threatpost.com/feed']
    links = [
        'https://www.theregister.com/security/headlines.rss', 'https://www.zdnet.com/news/rss.xml',
        'https://www.darkreading.com/rss.xml', 'https://www.eff.org/rss/updates.xml',
        'https://torrentfreak.com/feed/', 'https://nakedsecurity.sophos.com/feed',
        'http://feeds.feedburner.com/TheHackersNews?format=xml', 'https://www.cyberscoop.com/feed',
        'https://krebsonsecurity.com/feed/', 'https://www.hackread.com/feed/',
        'https://www.cyberscoop.com/feed/', 'https://seclists.org/rss/fulldisclosure.rss',
        'https://www.exploit-db.com/rss.xml', 'https://www.grahamcluley.com/feed/',
        'https://www.schneier.com/blog/atom.xml', 'https://www.bleepingcomputer.com/feed/',
        'https://www.welivesecurity.com/feed', 'https://threatpost.com/feed'
                                               'https://www.bellingcat.com/feed',
        'https://krypt3ia.wordpress.com/feed',
        'https://raffy.ch/blog/feed/rss/',
        'https://www.gironsec.com/blog/feed',
        'https://blog.kchung.co/rss/',
        'https://randywestergren.com/feed',
        # 'https://www.webroot.com/blog/feed',
        'https://blog.zsec.uk/rss/',
        # 'https://digi.ninja/rss.xml',
        'https://blog.skullsecurity.org/feed',
        'https://highon.coffee/feed',
        'https://justi.cz/feed',
        'https://tag.wonderhowto.com/rss/',
        'https://krebsonsecurity.com/feed/',
        'https://protonmail.com/blog/feed/',
        'https://isc.sans.edu/xml.html',
        # 'http://feeds.feedburner.com/oreilly/all?format=xml',
        'https://osandamalith.com/feed',
        'https://blog.codinghorror.com/rss/',
        'https://blog.codinghorror.com/rss/',
        'https://xorl.wordpress.com/feed',
        'https://blog.torproject.org/feed.xml',
        # 'https://feeds.feedburner.com/DavidLongenecker?format=xml',
        # 'https://feeds.feedburner.com/PentestTools?format=xml',
        'https://torrentfreak.com/feed',
        'https://www.schneier.com/feed/atom',
        'https://www.darknet.org.uk/feed/',
        # 'https://feeds.feedburner.com/TroyHunt?format=xml',
        'https://securelist.com/feed',
        'https://www.zdnet.com/news/rss.xml',
        'https://danielmiessler.com/feed',
        # 'feeds.feedburner.com/bmofeed?format=xml',
        'http://www.enisa.europa.eu/front-page/RSS',
        # 'https://blog.malwaremustdie.org/feeds/posts/default?alt=rss',
        'https://enigma0x3.net/feed',
        'https://wordpress.org/news/feed',
        # 'https://feedproxy.google.com/IrongeeksSecuritySite',
        'https://www.phillips321.co.uk/feed',
        'http://addxorrol.blogspot.com/feeds/posts/default',
        'https://linux-audit.com/feed/',
        'https://insights.sei.cmu.edu/blog/feeds/latest/rss/',
        'https://www.forcepoint.com/rss.xml',
        'https://cyberarms.wordpress.com/feed',
        # 'http://feeds.feedburner.com/Anti-virusRants?format=xml',
        'https://blog.shodan.io/rss/',
        'https://www.mdsec.co.uk/feed',
        # 'https://www.trustwave.com/en-us/rss/trustwave-blog/',
        'https://whitehatcheryl.com/feed',
        'https://www.jumpsec.com/feed',
        'https://dwaterson.com/feed',
        'https://dotcppfile.wordpress.com/feed',
        'https://blog.gdssecurity.com/labs/rss.xml',
        'https://holisticinfosec.blogspot.com/feeds/posts/default',
        'https://www.netresec.com/rss.ashx',
        'https://www.honeynet.org/blog/feed',
        'https://pendingtech.wordpress.com/feed/',
        'https://blog.erratasec.com/feeds/posts/default',
        'http://antukh.com/atom.xml',
        'https://luxsci.com/blog/feed',
        'https://www.ethicalhacker.net/feed',
        'https://grymoire.wordpress.com/feed',
        'https://security.stackexchange.com/feeds',
        'http://shell-storm.org/rss',
        'https://blog.0x3a.com/rss'
        'https://us-cert.cisa.gov/ncas/current-activity.xml',
        'https://www.shelliscoming.com/feeds/posts/default',
        'https://www.malwaretech.com/feed/',
        'https://www.hackingarticles.in/feed',
        'https://resources.infosecinstitute.com/feed',
        'http://blog.whitescope.io/feeds/posts/default',
        'https://blogs.cisco.com/feed',
        'https://www.imperva.com/blog/feed',
        'https://adsecurity.org/?feed=rss2',
        'https://pentest-labs.com/feed',
        'https://www.mogozobo.com/?feed=rss2',
        'https://astr0baby.wordpress.com/feed',
        'http://contagiodump.blogspot.com/feeds/posts/default',
        'https://0xdeadcode.se/feed',
        'https://javvadmalik.com/feed',
        'https://www.ericconrad.com/feeds/posts/default',
        # 'http://feeds.feedburner.com/andrewhayca?format=xml',
        'https://milo2012.wordpress.com/feed/',
        'https://leonjza.github.io/index.xml',
        'http://securosis.com/feeds/blog.rss',
        'https://jumpespjump.blogspot.com/feeds/posts/default',
        'https://www.crowdstrike.com/blog/feed/',
        'http://www.harmj0y.net/blog/feed',
        'https://www.securityartwork.es/en/feed',
        'https://www.xylibox.com/feeds/posts/default',
        'https://thepcn3rd.blogspot.com/feeds/posts/default',
        'http://securityandrisk.blogspot.com/feeds/posts/default',
        'https://myexploit.wordpress.com/feed',
        'https://www.martinvigo.com/feed/',
        'https://infosecninja.blogspot.com/feeds/posts/default',
        'https://natmchugh.blogspot.com/feeds/posts/default',
        'https://appsec-labs.com/portal/feed/',
        'https://www.podbean.com/site/podcatcher/index/blog/86g9yuLvSN0',
        # 'http://feeds.feedburner.com/GynvaelColdwindEN?format=xml',
        'https://www.fireeye.com/blog/feed',
        'https://cybersecurityventures.com/feed',
        'https://securityzap.com/feed',
        'https://securitycurrent.com/feed/',
        'http://thegreycorner.com/feed.xml',
        'https://www.doomedraven.com/feeds/posts/default',
        'https://volatility-labs.blogspot.com/feeds/posts/default',
        'https://blog.silentsignal.eu/feed',
        'http://edge-security.blogspot.com/feeds/posts/default',
        'https://blog.fox-it.com/feed',
        'http://www.labofapenetrationtester.com/feeds/posts/default',
        'https://labs.portcullis.co.uk/feed/',
        'https://www.tenable.com/blog-rss',
        'https://blog.didierstevens.com/feed',
        'https://googleonlinesecurity.blogspot.com/atom.xml',
        'https://www.yubico.com/rss',
        'https://www.scriptjunkie.us/feed',
        'https://sensepost.com/rss.xml',
        'https://sroberts.medium.com/feed',
        'https://blog.mozilla.org/en/category/privacy-security/feed',
        'https://notsosecure.com/feed',
        'https://www.bluekaizen.org/feed',
        'http://feeds.feedburner.com/SubliminalHacking?format=xml',
        'https://blog.nviso.eu/feed',
        'https://www.hackmageddon.com/feed',
        'https://zeltser.com/feed',
        'https://www.christophertruncer.com/feed',
        'https://blog.cryptographyengineering.com/feed',
        'https://googleprojectzero.blogspot.com/feeds/posts/default',
        'https://w00tsec.blogspot.com/feeds/posts/default',
        'https://icanthackit.wordpress.com/feed',
        'https://www.imperialviolet.org/posts-index.html',
        'https://sploitfun.wordpress.com/feed',
        'https://blog.netwrix.com/feed',
        'https://team-cymru.com/feed',
        'https://kb.refinepro.com/feeds/posts/default',
        'https://www.forcepoint.com/rss.xml',
        'https://us-cert.cisa.gov/ncas/current-activity.xml',
        'https://www.ehacking.net/feed',
        'http://blog.nibblesec.org/feeds/posts/default',
        'https://blog.mindedsecurity.com/feeds/posts/default',
        'https://foxglovesecurity.com/feed',
        'https://blog.mert.ninja/rss/',
        'https://www.kali.org/rss.xml',
        'http://www.weaknetlabs.com/feeds/posts/default?alt=rss',
        'https://distrowatch.com/news/dw.xml',
        'https://tails.boum.org/news/index.en.rsss',
        'https://blog.linuxmint.com/?feed=rss2',
        'https://grahamcluley.com/feed',
        'https://newsroom.trendmicro.com/news-releases?pagetemplate=rss',
        'https://grahamcluley.com/feed',
        'https://feeds.feedburner.com/TheHackersNews?format=xml',
        'https://msrc-blog.microsoft.com/feed',
        'https://iphelix.medium.com/feed',
        'https://seclists.org/rss/nmap-dev.rss',
        'https://seclists.org/rss/snort.rss',
        'https://seclists.org/rss/wireshark.rss',
        'https://seclists.org/rss/metasploit.rss',
        'https://seclists.org/rss/dataloss.rss',
        'https://seclists.org/rss/risks.rss',
        'https://seclists.org/rss/interesting-people.rss',
        'https://seclists.org/rss/nanog.rss',
        'https://seclists.org/rss/educause.rss',
        'https://seclists.org/rss/securecoding.rss',
        'https://seclists.org/rss/oss-sec.rss',
        'https://seclists.org/rss/cert.rss',
        'https://seclists.org/rss/funsec.rss',
        'https://seclists.org/rss/microsoft.rss',
        'https://seclists.org/rss/honeypots.rss',
        'https://seclists.org/rss/pauldotcom.rss',
        'https://seclists.org/rss/dailydave.rss',
        'https://seclists.org/rss/webappsec.rss',
        'https://seclists.org/rss/focus-ids.rss',
        'https://seclists.org/rss/firewall-wizards.rss',
        'https://seclists.org/rss/isn.rss',
        'https://seclists.org/rss/pen-test.rss',
        'https://seclists.org/rss/basics.rss',
        'https://seclists.org/rss/bugtraq.rss',
        'https://seclists.org/rss/fulldisclosure.rss',
        'https://seclists.org/rss/nmap-announce.rss',
        'https://seclists.org/rss/nmap-dev.rss']
    for link in links:
        print(link)
        try:
            scrape(link)
        except:
            if x ==0:
                time.sleep(5)
                scrape(link)
                #try again add check again after checking for five seconds if else just skip the next look
                print("Failed to grab link, The website is most likely the issue.")


def telegram_bot_sendtext(bot_message):
    bot_token = '2063309730:AAEZFGpeHViGtZ0dBhas7sGSuIo5qV3_0Q4'
    bot_chatID = '2038236581'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def insertintodatabase(link, description, headline, date):
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    parameters = (headline, description, date, link)
    c.execute("INSERT OR IGNORE INTO news VALUES(?,?,?,?)", parameters)
    conn.commit()
    if c.rowcount == 1:
        telegram_bot_sendtext(headline + description + date + link)
        print(c.rowcount, headline, "was inserted.")
    # else:
    #     print("duplicate Row not inserted")
    #     conn.close()
    #     return
    c.execute("SELECT * FROM news")
    conn.close()
    return


while 1 == 1:
    TextNews()
    time.sleep(60)


