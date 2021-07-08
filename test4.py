from datetime import datetime

s1 = '2.21.71.143 S 1620158680.102 0 1 10 4001 10 22 1701 23.73.138.134 GET 612 1135586 e087512ad0c32643.mediapackage.eu-west-1.amazonaws.com 200 - ijspzZSPJV - - D 87 1561 0 - 1049 - - - sL8 out/v1/bac5ea7d5e06476598d34ba48b3f1bd1/index_4.m3u8 - f1prodlive.akamaized.net ^ - Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_14)%20AppleWebKit/605.1.15%20(KHTML,%20like%20Gecko-Akamai-CloudTest)%20Version/12.0%20Safari/605.1.15 - 2343fd.133824e - - - PP=0:TA:N:0:1: ^ - - ^ - - ^ - ^ - - mtse=tl|4293989793|;dev=EDC_NO_MATCH|3;aid=673586;cert=RSA-SHA256;pin=JLm|amd;aidv=50;fp=988;pgma=33536;mle=14812 - - ^ 612.ch2p 13254:61197:8762:10900 L1:L1:s:::s - - - ^ - - 174 116 1688 10086 1005 - -'
s2 = '2.21.71.143 S 1620158680.102 0 1 10 4001 10 22 1701 23.73.138.134 GET 612 1135586 e087512ad0c32643.mediapackage.eu-west-1.amazonaws.com 200 - ijspzZSPJV - - D 87 1561 0 - 1049 - - - sL8 out/v1/bac5ea7d5e06476598d34ba48b3f1bd1/index_4.m3u8 - f1prodlive.akamaized.net ^ - Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_14)%20AppleWebKit/605.1.15%20(KHTML,%20like%20Gecko-Akamai-CloudTest)%20Version/12.0%20Safari/605.1.15 - 2343fd.133824e - - - PP=0:TA:N:0:1: ^ - - ^ - - ^ - ^ - - mtse=tl|4293989793|;dev=EDC_NO_MATCH|3;aid=673586;cert=RSA-SHA256;pin=JLm|amd;aidv=50;fp=988;pgma=33536;mle=14812 - - ^ 612.ch2p 13254:61197:8762:10900 L1:L1:s:::s - - - ^ - - 174 116 1688 10086 1005 - -'
s11 = s1.split(" ")
s22 = s2.split(" ")
print(s11)
val1 = s11[0]
print(val1)

datetime_str=s11[2]
datetime.strftime(datetime_str, '%Y-%m-%d')
