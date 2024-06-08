<template>
  <el-container style="height: 800px; border: 1px solid #eee">
<el-aside width="200px" style="background-color: rgb(238, 241, 246)">
  <el-menu router :default-openeds="['1','2','3']" :default-active="this.$router.path">
    <el-submenu index="1">
      <template slot="title"><i class="el-icon-message"></i>个人信息</template>
      <el-menu-item-group>
        <el-menu-item index="/changepassword"  class="current-page" >修改密码</el-menu-item>
        <el-menu-item index="/property">当前资产</el-menu-item>
     
      </el-menu-item-group>
      
    </el-submenu>
    <el-submenu index="2">
      <template slot="title"><i class="el-icon-menu"></i>市场数据</template>
      <el-menu-item-group>
          <el-menu-item index="/today">今日大盘</el-menu-item>
          <el-menu-item index="/stock1">上交所</el-menu-item>
          <el-menu-item index="/stock2">深交所</el-menu-item>
        </el-menu-item-group>
        
      </el-submenu>
      <el-submenu index="3">
        <template slot="title"><i class="el-icon-setting"></i>量化交易</template>
        
        <el-menu-item index="/trade1">买入股票</el-menu-item>
        <el-menu-item index="/trade2">卖出股票</el-menu-item>
        
        <el-submenu index="3-2">
          <template slot="title">交易策略</template>
          <el-menu-item index="/strategy1">策略1</el-menu-item>
          <el-menu-item index="/strategy2">策略2</el-menu-item>
      </el-submenu>
    </el-submenu>
  </el-menu>
</el-aside>

<el-container>
  <el-header style="text-align: left; font-size: 16px">
      <el-dropdown @command="handleCommand">
        <i class="el-icon-more" style="margin-right: 20px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="home">返回主页</el-dropdown-item>
          <el-dropdown-item command="logout">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <span>{{ this.current.user }}</span>
      <span>，欢迎使用 GooseGains 量化交易平台</span>
      
    </el-header>
  
  <el-main>
    <div style="margin: 80px auto; background-color: rgb(55, 128, 224,0.2); width: 350px; height: 320px; padding: 20px; border-radius: 10px">
      <div style="margin: 20px 0; text-align: center; font-size: 24px"><b>修改密码</b></div>
      <el-form :model="user" :rules="rules" ref="userForm">
        <el-form-item prop="oldpasssword">
          <el-input placeholder="请输入旧密码" size="medium" prefix-icon="el-icon-key" show-password v-model="user.oldpassword"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input placeholder="请设置新密码" size="medium" prefix-icon="el-icon-lock" show-password v-model="user.password"></el-input>
        </el-form-item>
        <el-form-item prop="confirmPassword">
          <el-input placeholder="请确定新密码" size="medium" prefix-icon="el-icon-lock" show-password v-model="user.confirmPassword"></el-input>
        </el-form-item>
        <el-form-item style="margin: 5px 0; text-align: right">
          <el-button type="primary" size="small"  autocomplete="off" @click="change">确定</el-button>
        </el-form-item>
      </el-form>
    </div>
  </el-main>
</el-container>
</el-container>
</template>

<script>
export default{
name:"ChangePassword",
data() {
  return {
    current: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
    user: {},
      rules: {
        oldpassword: [
          { required: true, message: '请输入旧密码', trigger: 'blur' },
          { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请设置新密码', trigger: 'blur' },
          { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
        confirmPassword: [
          { required: true, message: '请确认新密码', trigger: 'blur' },
          { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
        ],
      }
  }
},

methods: {
  handleCommand(command) {
        if (command==='logout'){
          this.$router.push('/login');
        }
        if (command==='home'){
          this.$router.push('/home')
        }
          
      },
      change() {
      this.$refs['userForm'].validate((valid) => {
        if (valid) {  // 表单校验合法
          this.user.username=this.current.user
          if (this.user.password !== this.user.confirmPassword) {
            this.$message.error("两次输入的密码不一致")
            return false
          }
          if(this.user.oldpassword !== this.current.pw){
            this.$message.error("旧密码输入错误")
            return false
          }
          this.request.post("change", this.user).then(res => {
            if(res.code === 200) {
              this.$message.success("密码重置成功,请重新登录")
              // 暂停 1 秒钟
            setTimeout(() => {
              this.$router.push('/login');
            }, 1000);
              return
            } else {
              this.$message.error(res.msg)
            }
          })
        }
      });
    }
  }
}
</script>
<style>
.el-header {
  background-color: rgb(55, 128, 224,0.4);
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

.current-page {
  background-color: rgb(55, 128, 224);
  color: white; /* 设置文本颜色，以增加可读性 */
}

</style>