<template>
  <div class="info-card">
    <nav>
      <div class="left-nav">
        <div class="icon-wrapper-arrow">
          <i class="fas fa-chevron-left"></i>
        </div>
        <span>Back to Homepage</span>
      </div>
      <div class="icon-wrapper-heart">
        <i class="far fa-heart"></i>
      </div>
    </nav>
    <div class="content">
      <div class="image">
        <img src="../images/no-image.png" />
      </div>
      <div class="description">
        <div class="stars">
          <span class="star-avg">{{starAvg}}</span>
          <span class="full-star fas fa-star" v-for="index in this.fullStar" :key="index"></span>
          <span class="half-star fas fa-star-half-alt" v-if="this.halfStar>0"></span>
          <span class="rest-star fas fa-star" v-for="index in this.restStar" :key="index"></span>
        </div>
        <h1>This is a title</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nam hic, suscipit eos eum quam labore numquam nobis itaque at porro excepturi dolore accusamus iste pariatur repellat, sint vel ducimus! Quidem!</p>
        <div class="btn-wrapper">
          <button>후기 작성하기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: Object
  },
  data() {
    return {
      realAvg: 2.66,
      starAvg: 0,
      fullStar: 0,
      halfStar: 0,
      restStar: 0
    };
  },
  methods: {
    onCreateStar() {
      this.starAvg = Math.round(this.realAvg / 0.5) * 0.5;
      this.fullStar = Math.floor(this.starAvg);
      this.halfStar = this.starAvg % this.fullStar;
      this.restStar = 5 - Math.ceil(this.starAvg);
    }
  },
  created() {
    this.onCreateStar();
  }
};
</script>

<style lang="scss" scoped>
.info-card {
  width: 1080px;
  height: fit-content;
  position: relative;
  background-color: $white;
  margin: 10px auto;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
}

/*[nav]********************************************************************************************************************************/

nav {
  width: 100%;
  height: 60px;
  color: $dark-gray;
  padding: 20px;
  border-bottom: 2px solid $light-gray;
  font-size: 16px;
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
}

.left-nav {
  cursor: pointer;
  width: fit-content;
}

.icon-wrapper-arrow {
  font-family: IconSolid;
  float: left;
  margin-right: 10px;
}

.fa-chevron-left::before {
  content: "\f053";
}

.icon-wrapper-heart {
  font-family: IconRegular;
  cursor: pointer;
}

.fa-heart::before {
  content: "\f004";
}

/*[image]********************************************************************************************************************************/

.content {
  position: relative;
  display: flex;
}

/*[image]********************************************************************************************************************************/

.image {
  box-sizing: border-box;
  padding: 30px;
  width: 30%;
  text-align: center;
  float: left;
  border-right: 2px solid $light-gray;
  border-bottom: 2px solid $light-gray;
}

.image img {
  width: 100%;
}

/*[description]********************************************************************************************************************************/

.description {
  box-sizing: border-box;
  padding: 0px 30px 30px 30px;
  float: left;
  width: 70%;
  height: 100%;
  font-family: "Noto Serif KR", serif;
  display: flex;
  flex-direction: column;
}

.description .stars {
  box-sizing: border-box;
  line-height: 40px;
  text-align: right;
  font-family: "Noto Serif KR", serif;
  display: flex;
  justify-content: flex-end;
}

.star-avg {
  margin: 0 5px;
}

.full-star,
.half-star {
  font-family: IconSolid;
}

.rest-star {
  font-family: IconRegular;
}

.fa-star::before {
  content: "\f005";
}

.fa-star-half-alt::before {
  content: "\f5c0";
}

.description h1 {
  color: $black;
  font-size: 30px;
  font-weight: 300;
}

.description p {
  color: $dark-gray;
  font-size: 12px;
  margin: 10px 0;
}

.description .btn-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}

.description .btn-wrapper button {
  outline: none;
  border: 2px solid $light-gray;
  background: none;
  padding: 8px 0px;
  margin: 10px;
  width: 300px;
  color: $dark-gray;
  cursor: pointer;
  transition: all 0.3s ease;
}

.description .btn-wrapper button:hover {
  outline: none;
  border: 2px solid $dark-gray;
  color: $black;
}
</style>