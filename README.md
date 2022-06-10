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
- APIListView : 채용 공고 목록 / 채용 공고 검색 기능
- APICreateView : 채용 공고 등록 기능
- APIPersonalView : 채용 공고 리스트 조회, 수정, 삭제 기능

<hr>

## ✔ Dev Note
#### 2022.06.10
1. REST API를 구성하고 처음에는 CRUD를 모두 나누어서 진행.

#### 2022.06.11
1. APIPersonalView 라는 C를 제외한 RUD를 이 클래스에서 담당하도록 함.
2. django-filter 패키지를 설치해서 APIListView 항목에 적용.
3. APIPersonalView의 Update 부분은 PATCH 메소드를 사용(부분적인 수정도 가능하기 때문).
4. 현재 채용 상세 페이지에서 회사가 올린 다른 채용 공고 필드를 못받았음.

-- last update: 2022.06.11