<template>
  <div class="thumbnail-wrapper">
    <div class="thumbnail">
      <img class="thumbnail-img" src="../images/no-image.png" alt="" />
      <div class="thumbnail-footer">
        <p class="title">
          {{ book.title }}
        </p>
        <p class="caption">
          {{ book.description }}
        </p>
        <div class="tags">
          <p class="tag">{{ book.tag }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: Object
  }
};
</script>

<style lang="scss" scoped>
.thumbnail-wrapper {
  flex: 1 0 10%;
  padding: 0;
  margin: 1rem;
}

.thumbnail {
  cursor: pointer;
  background-color: $white;
  height: 100%;
  border: 1px solid rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
  font-family: "Noto Serif KR", serif;
}

.thumbnail .thumbnail-img {
  border-style: none;
  width: 180px;
  height: 270px;
  margin: 0;
  transition: opacity 150ms linear;
  user-select: none;
  justify-content: center;
  align-items: center;
}

.thumbnail .thumbnail-img:hover {
  opacity: 0.5;
}

.thumbnail .thumbnail-footer {
  padding: 0.5rem 1.2rem 0.5rem 1.2rem;
  margin: 0;
  order: 2;
  color: $black;
  line-height: 1.6;
  max-width: 100%;
  text-overflow: ellipsis;
  overflow: hidden;
}

.thumbnail .thumbnail-footer .title {
  max-width: 140px;
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.thumbnail .thumbnail-footer .caption {
  line-height: 1.5;
  max-width: 140px;
  font-size: 14px;
  color: rgba(0, 0, 0, 0.6);
  margin-bottom: 8px;
  text-overflow: ellipsis;
  overflow: hidden;

  white-space: normal;
  height: 1.4em;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.thumbnail .thumbnail-footer .tags {
  height: 1.3em;
  overflow: hidden;
}

.thumbnail .thumbnail-footer .tag {
  margin: 0;
  margin-left: 0;
  margin-bottom: 2px;
  max-width: 120px;
  font-size: 11px;
  padding: 1px 8px;
  background: $light-gray;
  color: $dark-gray;
  display: inline-block;
  position: relative;
  border-radius: 3px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
