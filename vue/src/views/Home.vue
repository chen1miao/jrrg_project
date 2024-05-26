<template>
  <div style="color: #666;font-size: 14px;">
    <div style="padding-bottom: 20px">
      <b>您好！{{ user.username }}</b>
    </div>
    <el-card>
      数据集管理
      <el-divider />
      <img src="../assets/my_logo.jpg" alt="" style="width: 100%; height: 100%">
    </el-card>

  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},

    }
  }
}
</script>
