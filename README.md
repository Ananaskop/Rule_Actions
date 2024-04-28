# 自动合并自用规则
做了一些常用规则的自动合并，使配置文件更加精简
## Surge 使用
```
[Proxy Group]
PROXY = select, policy-path=你的订阅地址, update-interval=0, no-alert=0, hidden=0, include-all-proxies=0
STREAMING = select, HK, SG, TW, no-alert=0, hidden=0, include-all-proxies=0
FINAL = select, DIRECT, PROXY, no-alert=0, hidden=0, include-all-proxies=0
HK = fallback, update-interval=0, policy-regex-filter=(?=.*(港|香港|HK|(?i)Hong))^((?!(手游|游戏|game|Game)).)*$, no-alert=1, hidden=1, include-all-proxies=0, include-other-group=PROXY
SG = fallback, update-interval=0, policy-regex-filter=(?=.*(新加坡|狮城|SG|(?i)Singapore))^((?!(手游|游戏|game|Game)).)*$, no-alert=1, hidden=1, include-all-proxies=0, include-other-group=PROXY
TW = fallback, update-interval=0, policy-regex-filter=(?=.*(台湾|台灣|TW|(?i)Taiwan))^((?!(手游|游戏|game|Game)).)*$, no-alert=1, hidden=1, include-all-proxies=0, include-other-group=PROXY
US = fallback, update-interval=0, policy-regex-filter=(?=.*(美国|美國|US|(?i)States|American))^((?!(手游|游戏|game|Game)).)*$, no-alert=1, hidden=1, include-all-proxies=0, include-other-group=PROXY

[Rule]
# CorrectionRule 规则修正
RULE-SET,https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Surge/CorrectionRule/CorrectionRule.list,DIRECT,no-resolve
# RejectRule 
RULE-SET,https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Surge/RejectRule/RejectRule.list,REJECT,no-resolve
# StreamingRule
RULE-SET,https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Surge/StreamingRule/StreamingRule.list,STREAMING,no-resolve
# USRule
RULE-SET,https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Surge/USRule/USRule.list,US,no-resolve
# DirectRule
RULE-SET,https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Surge/DirectRule/DirectRule.list,DIRECT,no-resolve
# ProxyRule
RULE-SET,https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Surge/ProxyRule/ProxyRule.list,PROXY,no-resolve
```
## Quantumult X 使用
```
[policy]
static=STREAMING, HK, SG, TW, img-url=https://raw.gitmirror.com/Koolson/Qure/master/IconSet/Color/ForeignMedia.png
static=FINAL, direct, proxy, img-url=https://raw.gitmirror.com/Koolson/Qure/master/IconSet/Color/Final.png
available=HK, server-tag-regex=(?=.*(港|香港|HK|(?i)Hong))^((?!(手游|游戏|game|Game)).)*$, img-url=https://raw.gitmirror.com/Koolson/Qure/master/IconSet/Color/HK.png
available=SG, server-tag-regex=(?=.*(新加坡|狮城|SG|(?i)Singapore))^((?!(手游|游戏|game|Game)).)*$, img-url=https://raw.gitmirror.com/Koolson/Qure/master/IconSet/Color/SG.png
available=TW, server-tag-regex=(?=.*(台湾|台灣|TW|(?i)Taiwan))^((?!(手游|游戏|game|Game)).)*$, img-url=https://raw.gitmirror.com/Koolson/Qure/master/IconSet/Color/TW.png
available=US, server-tag-regex=(?=.*(美国|美國|US|(?i)States|American))^((?!(手游|游戏|game|Game)).)*$, img-url=https://raw.gitmirror.com/Koolson/Qure/master/IconSet/Color/US.png

[filter_remote]
https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/QuantumultX/CorrectionRule/CorrectionRule.list, tag=CorrectionRule, force-policy=direct, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/QuantumultX/RejectRule/RejectRule.list, tag=RejectRule, force-policy=reject, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/QuantumultX/StreamingRule/StreamingRule.list, tag=StreamingRule, force-policy=STREAMING, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/QuantumultX/USRule/USRule.list, tag=USRule, force-policy=US, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/QuantumultX/DirectRule/DirectRule.list, tag=DirectRule, force-policy=direct, update-interval=86400, opt-parser=true, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/QuantumultX/ProxyRule/ProxyRule.list, tag=ProxyRule, force-policy=proxy, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
```
## Stash 使用
```
rule-providers:
  CorrectionRule: {!!merge <<: *c, path: ./rule_provider/CorrectionRule.yaml, url: 'https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Clash/CorrectionRule/CorrectionRule.yaml'}
  RejectRule: {!!merge <<: *c, path: ./rule_provider/RejectRule.yaml, url: 'https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Clash/RejectRule/RejectRule.yaml'}
  StreamingRule: {!!merge <<: *c, path: ./rule_provider/StreamingRule.yaml, url: 'https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Clash/StreamingRule/StreamingRule.yaml'}
  USRule: {!!merge <<: *c, path: ./rule_provider/USRule.yaml, url: 'https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Clash/USRule/USRule.yaml'}  
  ProxyRule: {!!merge <<: *c, path: ./rule_provider/ProxyRule.yaml, url: 'https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Clash/ProxyRule/ProxyRule.yaml'}
  DirectRule: {!!merge <<: *c, path: ./rule_provider/DirectRule.yaml, url: 'https://raw.githubusercontent.com/Ananaskop/Rule_Actions/main/Clash/DirectRule/DirectRule.yaml'}
```
