URL = "https://auto.ru/-/ajax/desktop/listing/"

URL_AUTO = "https://auto.ru/moskva/cars/"

header = {
    "headers": {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "same-origin",
        "sec-fetch-site": "same-origin",
        "x-client-app-version": "390.0.11647738",
        "x-client-date": "1686134988897",
        "x-csrf-token": "8df7913143334c8d59ddef4613968de2cd706a989aef9bfa",
        "x-page-request-id": "490b73898b70ab4305878e47a4f44815",
        "x-requested-with": "XMLHttpRequest",
        "x-retpath-y": "https://auto.ru/cars/kia/optima/all/?year_from=2020&km_age_to=1000000",
        "x-yafp": "{\"a1\":\"XwnAMuyvqZc3QA==;0\",\"a2\":\"BoDN3W/j++CE7Vm9ZbW+i/7NsxWdoA==;1\",\"a3\":\"dL9wbi5tS2XdEduhaCktSQ==;2\",\"a4\":\"A/RFe0lBT5XeWgGp6HsOoEpTmCyNs+PBDqS2833enUN4JQ==;3\",\"a5\":\"c0JiO3zedj1/qg==;4\",\"a6\":\"WPk=;5\",\"a7\":\"AVnss62vXGsv9A==;6\",\"a8\":\"qXmRGe0GT5I=;7\",\"a9\":\"khPF8ccQjL7ekQ==;8\",\"b1\":\"P2EYMEJ2awM=;9\",\"b2\":\"lPmL4hwHjsNSsg==;10\",\"b3\":\"HtfqUaXTcCB3zg==;11\",\"b4\":\"A6oOaQvZmD0=;12\",\"b5\":\"K5xb1C/I9yjJaQ==;13\",\"b6\":\"b7q/6p0q6ggpgw==;14\",\"b7\":\"81izD9szms0a9w==;15\",\"b8\":\"wkBcQCJm2uQQkw==;16\",\"b9\":\"w38FgiqN+q33mQ==;17\",\"c1\":\"ig4Ruw==;18\",\"c2\":\"pzm0KQZjsZxEzgOYHG2xhcSW;19\",\"c3\":\"/+XPEAf3XLB6Q9nhTspb3dIu;20\",\"c4\":\"LPMIuxcBNpc=;21\",\"c5\":\"NxgSwZajqpA=;22\",\"c6\":\"9qRtqg==;23\",\"c7\":\"cWko9nt77cM=;24\",\"c8\":\"DqY=;25\",\"c9\":\"bk5zd+Bwitg=;26\",\"d1\":\"iseq9EnsBns=;27\",\"d2\":\"YMc=;28\",\"d3\":\"dc0To3x6srSOsw==;29\",\"d4\":\"tuPPZuso1gY=;30\",\"d5\":\"ANvEYv9WtoM=;31\",\"d7\":\"FU/dAyPF8O4=;32\",\"d8\":\"X1W6BC05d0v8LIAvWVibMllfMCibeQcilWw=;33\",\"d9\":\"8yvmUjBLU68=;34\",\"e1\":\"yolEZnAAi4+40A==;35\",\"e2\":\"q/qgUw85r44=;36\",\"e3\":\"4sJvVSiRv28=;37\",\"e4\":\"ZQ7GbWwqHvo=;38\",\"e5\":\"6eDzcwwA3CI1Qw==;39\",\"e6\":\"BDIRaCckejk=;40\",\"e7\":\"lip2P49ggDPrcg==;41\",\"e8\":\"FhboQx4mKLU=;42\",\"e9\":\"ObGZ3wxB0Bg=;43\",\"f1\":\"7nhjMzcB8lRdew==;44\",\"f2\":\"OwdWTEJDOtc=;45\",\"f3\":\"XTlgWr6h2oZXnQ==;46\",\"f4\":\"K79wTVVNGXw=;47\",\"f5\":\"9ucwXIVZiEktHw==;48\",\"f6\":\"hFtwbQRdkH55hQ==;49\",\"f7\":\"lrLmNe8eKAtlUQ==;50\",\"f8\":\"kCjaK2caf3DZfQ==;51\",\"f9\":\"3c7qW3XEG24=;52\",\"g1\":\"oAvIe1BqGey2ow==;53\",\"g2\":\"GjIJiA7Js/ONsQ==;54\",\"g3\":\"lY3dR6qaryU=;55\",\"g4\":\"Yqy4JUNZHxR24Q==;56\",\"g5\":\"qgwtVphWMgA=;57\",\"g6\":\"0Uz6LNwM5JM=;58\",\"g7\":\"oi01pvzCaTw=;59\",\"g8\":\"BrogjpAo7cE=;60\",\"g9\":\"B5bDaufi698=;61\",\"h1\":\"+5yOlQ3Z/8f+4w==;62\",\"h2\":\"YKt8clLEwcZOow==;63\",\"h3\":\"hWk8r9JMsJpUcw==;64\",\"h4\":\"VngnTJKC5BhSgw==;65\",\"h5\":\"h3ZDCWYVScE=;66\",\"h6\":\"2wwke2xYdrnCHQ==;67\",\"h7\":\"x0073HVYbHqo2+5MyODb21N7TCubWo6W1yMEm+nkafV96OYW;68\",\"h8\":\"GZBxfpSfleCkJQ==;69\",\"h9\":\"zR2dUhTsfyWXVg==;70\",\"i1\":\"xeCrdVCueZM=;71\",\"i2\":\"knWiDZS5sfbSGw==;72\",\"i3\":\"4sATLtK2oX207w==;73\",\"i4\":\"BzYu61DdKUl+aw==;74\",\"i5\":\"Rnp0ynvmkuXNag==;75\",\"z1\":\"CawH8CZuoZaQ/w4XtC3qrREEqoMSXuItYYdsZa1BDIHdWEjb2+29z9QD9Jfx7sgvOZhvqT5VxouhTa8p2Us3pw==;76\",\"z2\":\"EAh0zqaQ3W/9Mi1xWNMwxXkwxBQS7nwNwR+qf0PwhO/8yjB5XbkQziDKPYBvnHfP/yZmRHrMWHB1oMhm7om9lQ==;77\",\"y2\":\"6g8bD9Wosjg2bw==;78\",\"y3\":\"PE9+xce75PYEFA==;79\",\"y6\":\"MkCL1o/1xOJfNg==;80\",\"y8\":\"6oTdWu8dtYILtw==;81\",\"x4\":\"/CBkuWhkrW8gew==;82\",\"z5\":\"/jbNQE3QuKU=;83\",\"z4\":\"GPKi/j8yBU0+/Q==;84\",\"z6\":\"3AC6iZO09V9N5GDl;85\",\"z7\":\"0PWGb5ZQI4fd/xpe;86\",\"z8\":\"AHH/FAGQygekPr/XwR4=;87\",\"z9\":\"7s3f5659b/E0dpQm;88\",\"y1\":\"7HwBpSaMgExhcT6t;89\",\"y4\":\"1DawvmsJipATTZK1;90\",\"y5\":\"L2v0XKcJgQRxKM0l2UE=;91\",\"y7\":\"eWQjY1AtYdwYn7VE;92\",\"y9\":\"WmjvCPsfht0w/147W2M=;93\",\"y10\":\"lEl5odiro2/NnDC940k=;94\",\"x1\":\"Cj2qJLmbYWBRaWez;95\",\"x2\":\"FbpxFXYOSAopq3oZFlM=;96\",\"x3\":\"ff1IgzTaXqZ8Jik0;97\",\"x5\":\"XE7nCt6O90ZDDExS;98\",\"z3\":\"JqA4VKsfB9FI0JYM2D/yuF6gc/gI15Qob5lgEyIhhG8=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"E4TryaSE5RkcA6gzk2yBSOg5I/M=;100\",\"pgrd\":\"KeQiP3P7V2oKguGyVlNcTBRUVAlhbHMD02EwJ8UCCVXSGMWWMbGBRPijMfbXe3bQxIx8s+P3KBPiF12ZivFVV4y8gesz0Ak5Szp4ekTyQFh0qsPCTgKAnrO1oTTgoV4kSrmsS1NUNBP4Ljsc6WnjvuNP3FMhZgbxvzxvqaWWOVcrLY7Ox0JqfsFTUlQrrRcXqmKReJzr+aEqj3ha7r4Q3voUJ+U=\"}",
        "cookie": "suid=1d1e07593e816dbfbcd5bcf3c4ab8204.64b3bf5eaba8e0c229d4066efdc461e2; autoruuid=g64784f2921g83r10pfqsur99g5tq7se.52187da12f298e7fca21454c85f1ce19; counter_ga_all7=1; yuidlt=1; yandexuid=4908027581685536657; _ym_uid=1685606089801705161; yandex_login=; i=bkGXi+Kzc0LiXzk4+ksinhUpq0Oxgwk4O1jP5p8PPqVmYeJLZ/Up5jJdNRKyAICdjMJScGo0N03cpA11dXtskz0epsg=; autoru-visits-count=1; popups-rover-msk-shown-count=1; _csrf_token=8df7913143334c8d59ddef4613968de2cd706a989aef9bfa; gdpr=0; mindboxDeviceUUID=bb335f60-8b06-4221-a7d6-d264961eed5a; directCrm-session=%7B%22deviceGuid%22%3A%22bb335f60-8b06-4221-a7d6-d264961eed5a%22%7D; autoru_sid=a%3Ag64784f2921g83r10pfqsur99g5tq7se.52187da12f298e7fca21454c85f1ce19%7C1686210985485.604800.1glZSrOuaORAcL5ZT3mnWQ.aYwCRR9Q2Ns1xXIYtj2hPLPannUq4cD1PWxA-KC1xNc; yaPassportTryAutologin=1; _ym_isad=2; from=direct; _yasc=JoIASX3o9JQygPHI3k7k++Z/6xko9KWtyaocL/T8VO7dAs/03lYSmI/cZx53tGM=; Session_id=noauth:1686134368; sessar=1.99.CiA0CWGQJIgbWMK4eOGGxMklH-zfZAGnmcdmeznbgK8aMQ.JJ7W1SfkQPHZ8ptJpvk_8V-j1o6Ev7OIYLDJ6cBWfjs; ys=c_chck.744667217; mda2_beacon=1686134368684; sso_status=sso.passport.yandex.ru:synchronized; gradius=0; layout-config={\"screen_height\":1080,\"screen_width\":1920,\"win_width\":1105,\"win_height\":969}; gids=; cycada=iJSEo+PCIYNC1Lj9emAzVszcAKSt/2mt2o5277MQQ50=; _ym_d=1686134560; count-visits=3; from_lifetime=1686135062462",
        "Referer": "https://auto.ru/cars/kia/optima/all/?year_from=2020&km_age_to=1000000",
        "Referrer-Policy": "no-referrer-when-downgrade"
    },
    "body": "{\"year_to\":2023,\"km_age_from\":10,\"km_age_to\":20000,\"catalog_filter\":[{\"mark\":\"AUDI\",\"model\":\"A6\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\",\"geo_id\":[1]}",
    "method": "POST"
}

