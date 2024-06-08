<template>
  <div class="wrapper">
    <div style="height: 60px; line-height: 60px; font-size: 20px; padding-left: 20px; color: white;
      background-color: rgba(0,0,0,0.2)">欢迎使用 GooseGains 量化交易平台</div>
    <div style="display: flex; align-items: center;">
        <div style="margin: 150px 0px 110px 260px; background-color: #fff; width: 400px; height: 300px; padding: 20px; border-radius: 15px;">
            <div style="margin: 20px 0; margin-bottom: 30px; text-align: center; font-size: 24px;"><b>登录</b></div>            
            <el-form :model="user" :rules="rules" ref="userForm">
                <el-form-item prop="username">
                    <el-input size="medium" prefix-icon="el-icon-user" v-model="user.username"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input size="medium" prefix-icon="el-icon-lock" show-password v-model="user.password"></el-input>
                </el-form-item>
                
                <el-form-item style="margin: 35px 10px; text-align: right">
                    <el-button type="warning" size="small" autocomplete="off" @click="$router.push('/register')">前往注册</el-button>
                    <el-button type="primary" size="small" autocomplete="off" @click="login">登录</el-button>
                </el-form-item>
            </el-form>
        </div>
        <img src="../assets/my_logo.jpg" alt="" style="margin-left: 0px; width: 300px; height: 300px; border-radius: 15px; border: 2px solid rgb(55, 128, 224);margin-top: 40px;">
    </div>
</div>
</template>

<script>
import {resetRouter, setRoutes} from "@/router";

export default {
  name: "Login",
  data() {
    return {
      user: {},
      pass: {},
      code: '',
      dialogFormVisible: false,
      
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
      }
    }
  },

  mounted() {
    // 重置路由
    resetRouter()
  },
  methods: {
    login() { 
      this.$refs['userForm'].validate((valid) => {
        if (valid) {  // 表单校验合法
          this.request.post("login", this.user).then(res => {
            console.log(res.code)
            if(res.code === 200) {
              localStorage.setItem("user", JSON.stringify(res.data))  // 存储用户信息到浏览器
              this.$router.push("/home")
              this.$message.success("登录成功")
            } else {
              this.$message.error(res.msg)
            }
          })
        }
      });
    },
    
    handlePass() {
      this.dialogFormVisible = true
      this.pass = {}
    },
  }
}
</script>

<style>
.wrapper {
  height: 100vh;
  background-image: linear-gradient(to bottom right, #4169E1 , 	#87CEFA);
  overflow: hidden;
}
</style>
