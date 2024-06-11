<template>
  <el-container style="height: 800px; border: 1px solid #eee">
<el-aside width="200px" style="background-color: rgb(238, 241, 246)">
  <el-menu router :default-openeds="['1','2','3']" :default-active="this.$router.path">
   
    <el-submenu index="1">
      <template slot="title"><i class="el-icon-message"></i>个人信息</template>
      <el-menu-item-group>
        <el-menu-item index="/changepassword">修改密码</el-menu-item>
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
        <el-menu-item index="/trade2"  class="current-page">卖出股票</el-menu-item>
      
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
        <el-dropdown-item command="logout">退出登录</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <span>{{ this.user.user }}</span>
    <span>，欢迎使用 GooseGains 量化交易平台</span>
    
  </el-header>


  <el-main>
  <div style="display: flex; align-items: center;">
        <div style="margin: 150px 0px 110px 260px; background-color: rgb(55, 128, 224,0.2); width: 400px; height: 320px; padding: 20px; border-radius: 15px;">
            <div style="margin: 20px 0; margin-bottom: 30px; text-align: center; font-size: 24px;"><b>卖出股票</b></div>            
            <el-form>
                <el-form-item>
                  <el-button disabled class="extra-large-tag_price">当前股票价格：{{ price }}</el-button>
                </el-form-item>
                <el-form-item>
                  <el-button disabled class="extra-large-tag_num">计划卖出手数：{{ number }}(实际为{{ number*100 }}支)</el-button>
                </el-form-item>
                <el-form-item>
                  <el-button disabled class="extra-large-trade_totalcost">当前该笔收入：{{ number*100*price }}</el-button>
                </el-form-item>
                <el-form-item style="margin: 5px 5px; text-align: right">
                  <el-button @click="Click_property()" type="primary" round>确认交易</el-button> 
                  <el-button @click="Click_home()"  type="primary" round>取消交易</el-button>
                </el-form-item>
            </el-form>
        </div>
</div>
</el-main> 

</el-container>
  </el-container>
</template>

<script>
export default{
name:"Trade11",
data() {
  return {
      user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},//当前用户
      price: localStorage.getItem("price") ? JSON.parse(localStorage.getItem("price")) : {},//当前股票价格
      number:localStorage.getItem("number") ? JSON.parse(localStorage.getItem("number")) : {},//当前计划买入手数
      code:localStorage.getItem("code") ? JSON.parse(localStorage.getItem("code")) : {},
      sell_para:{}
  };
  
},
mounted() {
  const storedUser = localStorage.getItem("user");
  if (storedUser) {
    // 如果存在存储的用户信息，则解析并更新 user 数据
    this.user = JSON.parse(storedUser);
    console.log("用户信息：", this.user)
  }
},
methods: {
    Click_property()//如果点确定交易，
    {
      this.sell_para.id=this.user.id
      this.sell_para.username=this.user.user
      this.sell_para.stock_code=this.code
      this.sell_para.price=this.price
      this.sell_para.amount_out=this.number*100
      console.log(this.sell_para)
      

      this.request.post("transaction_out", this.sell_para).then(res => {
        if(res.code === 200) {
            this.$router.push("/property")
            this.$message.success("卖出成功")
          } else {
            this.$message.error(res.msg)
          }
        })
      
    },
    Click_home()//如果点取消交易，
    {  
      this.$router.push('/trade2')
      this.$message.error("交易取消")
    },
    handleCommand(command) {
      if (command==='logout'){
        this.$router.push('/login');
      }
      if (command==='home'){
        this.$router.push('/home')
      }
        
    }
  }
}
</script>
<style>
.el-header {
  background-color: #8694a7;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

</style>