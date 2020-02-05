<template>
  <div class="search-header">
    <div class="search-wrapper">
      <div class="search-input-widget">
        <form class="search-form">
          <div class="search-icon fa-search"></div>
          <input type="search" placeholder="검색어를 입력해주세요." class="search-input" />
          <input type="submit" style="display:none" />
        </form>
      </div>
      <div class="search-btn-wrapper">
        <router-link to="/" tag="button" class="search-btn fa-times"></router-link>
      </div>
    </div>
    <div class="auto-complete">
      <div class="result-wrapper">
        <div class="result-container">
          <dl class="result-list">
            <dt>인기 검색어</dt>
            <dd>
              <div class="result-item-icon fa-search"></div>
              <span class="result-item">셰익스피어</span>
            </dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import router from "../routes/routes.js";
export default {
  router
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Noto+Serif+KR&display=swap");

/*[search header]***********************************************************************************************************/

.search-header {
  position: absolute;
  z-index: 9999;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
}

.search-wrapper {
  height: 60px;
  width: 1080px;
  margin: 0 auto;
  padding: 0 0 0 1rems;
  position: relative;
  left: auto;
  border: none;
  background: transparent;
  display: flex;
  z-index: 100;
}

/*[search header input]***********************************************************************************************************/

.search-input-widget {
  -webkit-box-flex: 2;
  flex-grow: 2;
  height: 100%;
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  transition: all 0.2s;
}

.search-icon {
  padding: 12px 13px 12px 8px;
  margin: 0;
  display: inline-block;
  min-height: 1em;
  outline: none;
  border: none;
  vertical-align: baseline;
  user-select: none;
  font-family: Icons;
  background: transparent;
  font-size: 1.3rem;
}

.search-form {
  width: 100%;
  position: relative;
  box-sizing: border-box;
  display: flex;
  -webkit-box-align: center;
  align-items: center;
}

.search-form .search-input {
  box-sizing: content-box;
  font-size: 1.28rem;
  width: 90%;
  padding: 0.75rem 0;
  border: none;
  font-weight: bold;
  outline: none;
  font-family: "Noto Serif KR", serif;
  -webkit-appearance: none;
}

/*[search header btn]***********************************************************************************************************/

.search-btn-wrapper {
  display: flex;
  max-width: 48px;
  margin: 0;
}

.search-btn {
  padding: 12px 13px 12px 8px;
  margin: 0;
  cursor: pointer;
  display: inline-block;
  min-height: 1em;
  outline: none;
  border: none;
  vertical-align: baseline;
  user-select: none;
  font-family: Icons;
  background: transparent;
  font-size: 1.3rem;
}

/*[Auto complete]***********************************************************************************************************/

.auto-complete {
  padding-top: 60px;
  width: 100%;
  height: 100%;
  padding: 58px 0 0;
  box-sizing: border-box;
  z-index: 99;
  left: 0;
  top: 0;
  position: fixed;
}

.auto-complete .result-wrapper {
  width: 100%;
  border-top: 1px solid $gray;
  display: flex;
  height: 100%;
  flex-direction: column;
  flex-wrap: wrap;
  background: $white;
  font-size: 1.1rem;
  font-weight: bold;
  color: $gray;
  position: relative;
}

.auto-complete .result-wrapper .result-container {
  padding: 0;
  overflow-x: hidden;
  overflow-y: auto;
}

.result-list {
  font-size: 1.14rem;
  margin: 8px auto 0;
  padding: 0 0 0 1rems;
  width: 1080px;
}

.result-list dt {
  font-size: 1rem;
  margin: 0 0 8px;
  color: $dark-gray;
  padding: 12px 0 0;
}

.result-list dd {
  font-weight: normal;
  line-height: 48px;
  height: 48px;
  padding: 0;
  margin: 0;
  display: flex;
}

.result-list dd .result-item {
  height: 48px;
  line-height: 48px;
  cursor: pointer;
  color: $dark-gray;
  position: relative;
  padding: 0 0 0 26px;
}

.result-list dd .result-item-icon {
  font-family: Icons;
}

/*[icon fonts]***********************************************************************************************************/

.fa-times::before {
  content: "\f00d";
}
.fa-search::before {
  content: "\f002";
}
</style>
