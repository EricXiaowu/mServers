# Tornado实现的微服务
## 1、基本使用
## 2. requests库测试
### 2.1 get
  resp = requests.get(url, params={ 
      'wd': 'disen' 
  }) 
  print(resp.text)

### 2.2 post
  resp = requests.post(url, data={ 
      'wd': 'jack' 
  }) 
  print(resp.text)
