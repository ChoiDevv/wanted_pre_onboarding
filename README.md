# 🕒 wanted_pre_onboarding
### Make recruitment web site by using DRF

<hr>

## 💡 Service
> 1. 본 서비스는 기업의 채용을 위한 웹 서비스 입니다. 
> 2. 회사는 채용공고를 생성하고, 이에 사용자는 지원합니다.

<hr>

## 🔨 Skill
<img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/DRF-092E20?style=flat&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat&logo=SQLite&logoColor=white"/>

<hr>

## 🕒 Schedule
Start - 2022.06.10

<hr>

## ✔ API 아키텍처
- CompanyListView : 회사가 올린 공고 조회 기능
- RecruitCreateView : 회사가 올리는 채용 공고 추가 기능
- RecruitDetailView : 회사가 올린 채용 공고 수정, 삭제 기능(id 값을 pk로 받음)
- CompanyCreateView : 회사 등록 기능

<hr>

## ✔ Dev Note
#### 2022.06.10
1. REST API를 구성하고 처음에는 CRUD를 모두 나누어서 진행.

#### 2022.06.11
1. APIPersonalView 라는 C를 제외한 RUD를 이 클래스에서 담당하도록 함.
2. django-filter 패키지를 설치해서 APIListView 항목에 적용.
3. APIPersonalView의 Update 부분은 PATCH 메소드를 사용(부분적인 수정도 가능하기 때문).
4. 현재 채용 상세 페이지에서 회사가 올린 다른 채용 공고 필드를 못받았음.
5. 모델 설계부터 잘못되었음을 인지하고 수정.
6. url 및 뷰 이름 수정 - 조금 더 인식하기 쉽게 네이밍 변경 / serializer 안에 모델 두 개를 어떻게 넣어야할지 고민해야함.

#### 2022.06.13
1. Nested Serializer 방식을 통해 Recruit, Company 모델에 각 serializer에 담아 전송할 계획.
2. 원래대로라면 회사가 채용공고를 등록할 때 자신들이 가입한 정보로 등록하기에 그 정보까지 보여지는 것을 뜻하는 것 같다고 생각.
3. Nested Serializer를 활용해서 구성해보려고 했으나 채용공고 id 값만으로는 띄울 수가 없었음. 내 생각엔 모델 부분을 수정해야할 것 같은데 이번에 부족하다는 걸 느낌.

#### 2022.06.14
1. 모델 부분이 틀렸음을 인지하고 Company 테이블을 참조하도록 Recruit 테이블에서 외래키로 설정했음.
2. 지속해서 NOT NULL constraint failed 에러가 발생해서 고민해본 결과, 로그인을 했다고 착각한 문제였다.
3. 채용 공고에서 회사 정보를 가져올 수 있도록 조정하기 위해 시리얼라이저 및 뷰 수정.

-- last update: 2022.06.14