<template>
  <div class="wrapper">
    <div class="card-wrapper">
      <div class="card">
        <div class="card-details">
          <div class="detail-wrapper"></div>
        </div>
        <div class="card-image">
          <flipping-book></flipping-book>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FlippingBook from "./FlippingBook";

export default {
  components: { FlippingBook }
};
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px 0 40px;
  position: relative;
}

.card-wrapper {
  justify-content: center;
  width: 1080px;
  position: relative;
}

.card {
  box-shadow: 0 15px 30px 1px rgba(128, 128, 128, 0.31);
  text-align: center;
  border-radius: 5px;
  height: 220px;
  width: 340px;
  margin: 1rem;
  display: flex;
  align-items: center;
  position: relative;
}

.card-details {
  position: relative;
  text-align: left;
  overflow: hidden;
  height: 100%;
  float: left;
  width: 50%;
}

.card-image {
  position: relative;
  height: 100%;
  width: 50%;
  justify-content: center;
  float: right;
}
</style>
