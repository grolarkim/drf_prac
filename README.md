django-rest-framework 
연습용 레포지토리입니다.

## config 폴더
settings.py 가 들어있는 폴더입니다.

## userapp 폴더
사용자 계정과 관련된 앱입니다.

#### 모델
 - `User(AbstractBaseUser)`
 - `UserManager(BaseUserManager)`
 - `UserProfile`
 - `Hobby`
 - `UserProfileHobby`

#### 시리얼라이저
 - `UserSerializer`
 - `UserProfileSerializer`
 - `HobbySerializer`

#### 뷰
 - `LoginView`
 - `UserView`



## blogapp 폴더
게시글과 관련된 앱입니다.

#### 모델
 - `Article`
 - `Category`
 - `Comment`


#### 시리얼라이저
 - `ArticleSerializer`
 - `CategorySerializer`
 - `CommentSerializer`

#### 뷰




### 기타
secret.json 파일을 통해 django secretkey 등의 중요정보를 따로 보관하고 있습니다. 토이프로젝트이기에 .gitignore에서 처리하지 않았습니다.



