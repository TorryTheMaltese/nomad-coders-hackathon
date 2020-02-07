<template>
  <div class="card-carousel-wrapper">
    <div class="nav-left" @click="moveCarousel(-1)" :disabled="atHeadOfList"></div>
    <div class="card-carousel">
      <div class="card-carousel-title">Stories of William Shakespeare</div>
      <div class="overflow-container">
        <div class="cards" :style="{ transform: 'translateX' + '(' + currentOffset + 'px' + ')' }">
          <thumbnail-card v-for="book in books" :key="book.id" :book="book"></thumbnail-card>
        </div>
      </div>
    </div>
    <div class="nav-right" @click="moveCarousel(1)" :disabled="atEndOfList"></div>
  </div>
</template>

<script>
import ThumbnailCard from "./ThumbnailCard";
import axios from "axios";

export default {
  data() {
    return {
      currentOffset: 0,
      windowsize: 5,
      paginationFactor: 214,
      books: []
    };
  },
  components: {
    ThumbnailCard
  },
  computed: {
    atEndOfList() {
      return (
        this.currentOffset <=
        this.paginationFactor * -1 * (this.books.length - this.windowsize)
      );
    },
    atHeadOfList() {
      return this.currentOffset === 0;
    }
  },
  methods: {
    moveCarousel(direction) {
      if (direction === 1 && !this.atEndOfList) {
        this.currentOffset -= this.paginationFactor;
      } else if (direction === -1 && !this.atHeadOfList) {
        this.currentOffset += this.paginationFactor;
      }
    },
    getBooks() {
      const path = "http://localhost:5000/";
      axios
        .get(path)
        .then(res => {
          this.books = res.data.books;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  created() {
    this.getBooks();
  }
};
</script>

<style lang="scss" scoped>
.card-carousel-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px 0 40px;
  position: relative;
}

.nav-left {
  transform: rotate(-135deg);
}

.nav-right {
  transform: rotate(45deg);
}

.nav-left,
.nav-right {
  display: inline-block;
  width: 15px;
  height: 15px;
  padding: 10px;
  box-sizing: border-box;
  border-top: 2px solid $black;
  border-right: 2px solid $black;
  cursor: pointer;
  margin: 0 20px;
  transition: transform 150ms linear;
}

.nav-left[disabled],
.nav-right[disabled] {
  opacity: 0.2;
}

.card-carousel {
  justify-content: center;
  width: 1080px;
  position: relative;
}

.card-carousel .card-carousel-title {
  display: flex;
  -webkit-box-pack: justify;
  margin-left: 20px;
  font-size: 1.5em;
  font-weight: bold;
  text-align: left;
  font-family: "Noto Serif KR", serif;
  cursor: pointer;
  color: $black;
  position: relative;
  width: fit-content;
}

.card-carousel .overflow-container {
  overflow: hidden;
  position: relative;
}

.card-carousel .overflow-container .cards {
  display: flex;
  transition: transform 150ms ease-out;
  float: left;
}
</style>
