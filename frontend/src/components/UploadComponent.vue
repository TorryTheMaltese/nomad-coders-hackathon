<template>
  <div class="container">
    <div class="wrapper">
      <div class="profile-wrapper">
        <img @click="ControlModal" class="avatar" />
      </div>
    </div>

    <div v-if="visible" class="modal-container">
      <div class="modal-wrapper">
        <div class="close-btn" @click="ControlModal">
          <i class="fas fa-times"></i>
        </div>

        <div v-if="!imgAdded" class="before-upload-contents">
          <div class="drop-area" @drop.prevent="addImg" @dragover.prevent>
            <div class="icon">
              <i class="fas fa-upload"></i>
            </div>
            <span class="hint">Click or Drag the image here to upload</span>
          </div>
          <div class="error-area" v-if="notImgError">
            <div class="icon">
              <i class="fas fa-times"></i>
            </div>Image Only
          </div>
          <div class="operate-area">
            <a>Cancel</a>
          </div>
        </div>

        <div v-else class="after-upload-contents">
          <div class="crop-area">
            <div class="crop-left">
              <div class="img-container">
                <img
                  :src="imgSrc"
                  draggable="false"
                  class="img"
                  style="top: 0px; left: 28px; width: 184px; height: 184px;"
                />
                <div class="img-shade shade-left" style="width: 28px; height: 184px;"></div>
                <div class="img-shade shade-right" style="width: 28px; height: 184px;"></div>
              </div>
              <div class="img-range">
                <i class="fas fa-minus"></i>
                <input type="range" step="1" min="0" max="100" value="0" class="slider" />
                <i class="fas fa-plus"></i>
              </div>
            </div>

            <div class="crop-right">
              <div class="circle-preview">
                <img :src="imgSrc" style="width:180px; height:180px" />
                <span>Preview</span>
              </div>
            </div>
          </div>
          <div class="operate-area">
            <a>Back</a>
            <a>Save</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      visible: false,
      imgAdded: false,
      notImgError: false,
      filename: "",
      imgSrc: ""
    };
  },
  methods: {
    ControlModal() {
      this.visible = !this.visible;
    },
    addImg(e) {
      const files = e.dataTransfer.files;
      if (files.length) {
        const file = files[0];
        const imgType = /image.*/;
        if (file.type.match(imgType)) {
          this.imgAdded = true;
          this.filename = file.name;

          if (typeof file === "string") {
            this.imgSrc = file;
          } else {
            const reader = new FileReader();
            reader.onload = () => {
              this.imgSrc = reader.result;
            };
            reader.readAsDataURL(file);
          }
        } else {
          this.notImgError = true;
        }
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.icon {
  font-family: IconSolid;
}

/*[user profile]********************************************************************************************************************************/

.profile-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.avatar {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  transform: scale(0.95);
  transition: all 0.5s;
  cursor: pointer;
  background-image: url(../images/profile.png);
  background-repeat: no-repeat;
  background-size: cover;
}
.avatar:hover {
  transform: scale(1);
  box-shadow: 0 37.125px 70px -12.125px rgba(0, 0, 0, 0.2);
  opacity: 0.5;
}

/*[modal]********************************************************************************************************************************/

.modal-container {
  position: fixed;
  display: block;
  box-sizing: border-box;
  z-index: 10000;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.65);
  -webkit-tap-highlight-color: transparent;
}

.modal-wrapper {
  position: fixed;
  display: block;
  box-sizing: border-box;
  z-index: 10000;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.23);
  margin: auto;
  width: 600px;
  height: 330px;
  padding: 25px;
  background-color: #fff;
  border-radius: 5px;
  animation: vicp 0.12s ease-in;
}

.close-btn {
  position: absolute;
  right: -30px;
  top: -30px;
  font-family: IconSolid;
  font-size: 25px;
  cursor: pointer;
}

.close-btn .fa-times::before {
  content: "\f00d";
  color: #fff;
}

.drop-area {
  position: relative;
  box-sizing: border-box;
  padding: 35px;
  height: 210px;
  background-color: rgba(0, 0, 0, 0.03);
  text-align: center;
  border: 1px dashed rgba(0, 0, 0, 0.08);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  cursor: pointer;
}

.drop-area:hover {
  background-color: rgba(0, 0, 0, 0.05);
  border: 1px dashed rgba(0, 0, 0, 0.1);
}

.drop-area .icon .fa-upload::before {
  content: "\f093";
  color: #999;
  display: block;
  margin: 6px auto 6px;
  font-size: 50px;
  overflow: hidden;
}

.drop-area .hint {
  font-family: "Noto Serif KR", serif;
  display: block;
  padding: 10px;
  font-size: 14px;
  color: #999;
  line-height: 30px;
}

.error-area {
  display: flex;
  font-size: 14px;
  line-height: 24px;
  height: 24px;
  color: #d10;
  text-align: center;
  justify-content: center;
  font-family: "Noto Serif KR", serif;
}

.error-area .fa-times::before {
  content: "\f00d";
  color: #d10;
  margin: 3px;
}

.operate-area {
  position: absolute;
  right: 20px;
  bottom: 20px;
}

.operate-area a {
  font-family: "Noto Serif KR", serif;
  position: relative;
  float: left;
  display: block;
  margin-left: 10px;
  width: 100px;
  height: 36px;
  line-height: 36px;
  text-align: center;
  cursor: pointer;
  font-size: 14px;
  color: gray;
  border-radius: 2px;
  overflow: hidden;
  user-select: none;
}

.operate-area a:hover {
  background-color: rgba(0, 0, 0, 0.03);
}

.crop-area {
  display: flex;
  overflow: hidden;
  justify-content: space-around;
}

.img-container {
  position: relative;
  display: block;
  width: 240px;
  height: 180px;
  background-color: #e5e5e0;
  overflow: hidden;
}

.img-container .img {
  position: absolute;
  display: block;
  cursor: move;
  user-select: none;
}

.img-shade {
  box-shadow: 0 2px 6px 0 rgba(0, 0, 0, 0.18);
  position: absolute;
  background-color: rgba(241, 242, 243, 0.8);
}

.img-shade .shade-left {
  top: 0;
  left: 0;
}

.img-shade .shade-right {
  bottom: 0;
  right: 0;
}

.img-range {
  position: relative;
  margin: 30px 0 10px 0;
  width: 240px;
  height: 18px;
  font-family: IconSolid;
  display: flex;
}

.img-range .slider {
  display: block;
  margin: auto;
  width: 180px;
  height: 5px;
  border-radius: 5px;
  background: #d3d3d3;
  -webkit-appearance: none;
  cursor: pointer;
  outline: none;
  opacity: 0.7;
  transition: opacity 0.2s;
  -webkit-transition: 0.2s;
}

.slider:hover {
  opacity: 1;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: #555;
  cursor: pointer;
}

.slider::-moz-range-thumb {
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: #555;
  cursor: pointer;
}

.fa-minus .fa-plus {
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 100%;
  border-color: rgba(0, 0, 0, 0.08);
}

.fa-minus::before {
  content: "\f068";
  display: block;
}

.fa-plus::before {
  content: "\f067";
  display: block;
}

.circle-preview {
  position: relative;
  padding: 5px;
  width: 180px;
  height: 180px;
  float: left;
}

.circle-preview img {
  position: absolute;
  display: block;
  border-radius: 100%;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  padding: 3px;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.15);
  overflow: hidden;
  user-select: none;
}

.circle-preview span {
  position: absolute;
  bottom: -30px;
  width: 100%;
  font-size: 14px;
  color: #999;
  display: block;
  text-align: center;
}
</style>