<template>
  <div class="header">
    <div class="header-container">
      <div class="left-menu">
        <button class="left-menu-btn">
          <i class="left-menu-btn-icon fas fa-book fa-book-open"></i>
          <span class="left-menu-btn-tag">책 추천하기</span>
        </button>
      </div>
      <div class="center-menu">
        <a href="/" class="button-link">
          <div class="logo">GOODREADS</div>
        </a>
      </div>
      <div class="right-menu">
        <button class="search-btn fa-search"></button>
        <a href="" class="right-menu-btn">
          <span class="right-menu-btn-tag">로그인 / 회원가입</span>
          <span class="profile">
            <span class="profile-image"></span>
          </span>
        </a>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Noto+Serif+KR&display=swap");

.header {
  position: fixed;
  display: flex;
  align-items: center;
  -webkit-box-pack: justify;
  justify-content: space-between;
  font-size: 16px;
  width: 100%;
  height: 60px;
  background: #ffffff;
  z-index: 999;
  margin: 0 auto;
  padding: 0;
  box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
  color: $black;
  // font-family: NanumMyeongjo;
  font-family: "Noto Serif KR", serif;
}

.header .header-container {
  width: 1080px;
  margin: 0 auto;
  position: relative;
  padding: 0;
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: justify;
  justify-content: space-between;
}

.header .header-container .left-menu {
  flex: 1 0 25%;
  text-align: center;
  display: flex;
}

.left-menu .left-menu-btn {
  border: none;
  background: transparent;
  outline: none;
  color: $black;
  font-weight: bold;
  cursor: pointer;
  padding: 0 1rem;
}

.left-menu .left-menu-btn .left-menu-btn-tag {
  font-size: 15px;
  // font-family: NanumMyeongjo;
  font-family: "Noto Serif KR", serif;
  cursor: pointer;
  line-height: 60px;
}

.left-menu .left-menu-btn .left-menu-btn-icon {
  display: inline-block;
  opacity: 1;
  margin: 0 0.25rem 0 0;
  width: 1.2em;
  height: 1em;
  font-family: Icons;
  font-style: normal;
  font-weight: 400;
  text-decoration: inherit;
  text-align: center;
}

.fa-book::before {
  content: "\f02d";
}

.header .header-container .center-menu {
  width: 10rem;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: 0 auto;
  padding: 0 1rem;
  cursor: pointer;
  display: flex;
  -webkit-box-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  align-items: center;
}

.center-menu .logo {
  color: $black;
  // font-family: NanumMyeongjo;
  font-family: "Noto Serif KR", serif;
  font-size: 16px;
}

.header .header-container .right-menu {
  flex: 1 0 25%;
  text-align: right;
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: end;
  justify-content: flex-end;
}

.right-menu .search-btn {
  cursor: pointer;
  display: inline-block;
  min-height: 1em;
  border: none;
  vertical-align: baseline;
  font-family: Icons;
  background: transparent;
  text-align: center;
  font-size: 18px;
}

.fa-search::before {
  content: "\f002";
}

.right-menu .right-menu-btn {
  display: inline-flex;
  -webkit-box-align: center;
  align-items: center;
  color: $black;
  font-weight: bold;
  cursor: pointer;
  line-height: 60px;
  padding: 0 0.6rem;
}

.right-menu .right-menu-btn .right-menu-btn-tag {
  font-size: 15px;
  // font-family: NanumMyeongjo;
  font-family: "Noto Serif KR", serif;
  cursor: pointer;
  line-height: 60px;
}

.right-menu .right-menu-btn .profile {
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  position: relative;
  margin-left: 0.75rem;
}

.right-menu .right-menu-btn .profile .profile-image {
  width: 38px;
  height: 38px;
  display: inline-block;
  background-image: url(../images/profile.png);
  background-size: contain;
}

a,
a:hover {
  text-decoration: none;
}
</style>
