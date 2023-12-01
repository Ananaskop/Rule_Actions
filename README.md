# 自动合并自用规则
做了一些常用规则的自动合并，使配置文件更加精简
## Surge 使用
```
[Rule]
# CorrectionRule 规则修正
RULE-SET,https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Surge/CorrectionRule/CorrectionRule.list,DIRECT,no-resolve
# RejectRule 
RULE-SET,https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Surge/RejectRule/RejectRule.list,REJECT,no-resolve
# StreamingRule
RULE-SET,https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Surge/StreamingRule/StreamingRule.list,STREAMING,no-resolve
# USRule
RULE-SET,https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Surge/USRule/USRule.list,US,no-resolve
# DirectRule
RULE-SET,https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Surge/DirectRule/DirectRule.list,DIRECT,no-resolve
# ProxyRule
RULE-SET,https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Surge/ProxyRule/ProxyRule.list,PROXY,no-resolve
```
## Quantumult X 使用
```
[filter_remote]
https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/QuantumultX/CorrectionRule/CorrectionRule.list, tag=CorrectionRule, force-policy=direct, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/QuantumultX/RejectRule/RejectRule.list, tag=RejectRule, force-policy=reject, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/QuantumultX/StreamingRule/StreamingRule.list, tag=StreamingRule, force-policy=STREAMING, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/QuantumultX/USRule/USRule.list, tag=USRule, force-policy=US, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/QuantumultX/DirectRule/DirectRule.list, tag=DirectRule, force-policy=direct, update-interval=86400, opt-parser=true, inserted-resource=true, enabled=true
https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/QuantumultX/ProxyRule/ProxyRule.list, tag=ProxyRule, force-policy=proxy, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
```
## Stash 使用
```
rule-providers:
  CorrectionRule: {!!merge <<: *c, path: ./rule_provider/CorrectionRule.yaml, url: 'https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Stash/CorrectionRule/CorrectionRule.yaml'}
  RejectRule: {!!merge <<: *c, path: ./rule_provider/RejectRule.yaml, url: 'https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Stash/RejectRule/RejectRule.yaml'}
  StreamingRule: {!!merge <<: *c, path: ./rule_provider/StreamingRule.yaml, url: 'https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Stash/StreamingRule/StreamingRule.yaml'}
  USRule: {!!merge <<: *c, path: ./rule_provider/USRule.yaml, url: 'https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Stash/USRule/USRule.yaml'}  
  ProxyRule: {!!merge <<: *c, path: ./rule_provider/ProxyRule.yaml, url: 'https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Stash/ProxyRule/ProxyRule.yaml'}
  DirectRule: {!!merge <<: *c, path: ./rule_provider/DirectRule.yaml, url: 'https://raw.githubusercontent.com/GiveYou32Likes/Rule_Actions/main/Stash/DirectRule/DirectRule.yaml'}
  
rules:
  - RULE-SET,CorrectionRule,DIRECT
  - RULE-SET,RejectRule,REJECT
  - RULE-SET,StreamingRule,STREAMING
  - RULE-SET,USRule,US
  - RULE-SET,DirectRule,DIRECT
  - RULE-SET,ProxyRule,PROXY
  - GEOIP,CN,DIRECT
  - MATCH,FINAL
```
