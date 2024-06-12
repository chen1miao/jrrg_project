<template>
  <el-container style="height: 800px; border: 1px solid #eee">
<el-aside width="200px" style="background-color: rgb(238, 241, 246)">
  <el-menu router :default-openeds="['1','2','3', '3-2']" :default-active="this.$router.path">
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
        <el-menu-item index="/trade2">卖出股票</el-menu-item>
        
        <el-submenu index="3-2">
          <template slot="title">交易策略</template>
          <el-menu-item index="/strategy1" class="current-page" >双均线策略</el-menu-item>
          <el-menu-item index="/strategy2">均值回归交易策略</el-menu-item>
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
    <span>{{ this.user.user }}</span>
    <span>，欢迎使用 GooseGains 量化交易平台</span>
    
  </el-header>
  
  <el-main style="position: relative; background-image: url('https://tse2-mm.cn.bing.net/th/id/OIP-C.z0pyMS3Ek3ggzNiOIaZBxgHaDt?w=315&h=175&c=7&r=0&o=5&dpr=1.5&pid=1.7'); background-size: cover; background-position: center; background-color: rgba(255, 255, 255, 0.6); padding: 20px;">
    <div style="position: relative;">
    <!-- 调整黑框位置 -->
    <div style="position: absolute; top: 5px; left: 20px; width: calc(100% - 40px); padding: 20px; background-color: rgba(0, 0, 0, 0.5); border-radius: 10px;">
      <!-- 添加标题 -->
      <h1 style="color: white; font-size: 27px; margin-top:5px;margin-bottom: 10px;">策略一：双均线策略</h1>
      <!-- 添加文字内容 -->
       
      <div style="color: white; line-height: 1.8;">
        <p style="font-weight: bold;font-size: 20px;">双均线策略-原理介绍：</p>

<div style="background-color: rgba(0, 0, 0, 0.5); margin-top:10px;padding: 10px;border-radius: 10px;">
  <p style="text-indent:15px;font-size: 18px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); color: white;">1.当短期均线（5日）上穿长期均线（60日）时，出现了所谓的“金叉”，代表买入信号;</p>
  <p style="text-indent:15px;font-size: 18px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">2.当短期均线（5日）下穿长期均线（60日）时，出现了所谓的“死叉”，代表卖出信号;</p>
  <p style="text-indent:15px;font-size: 18px;">当出现金叉的时候，意味着市场处于乐观的情绪，投资者倾向于看好后市，这种集体看涨的情绪会快速推动价格上涨。相反如果出现死叉，则代表市场出于悲观的情绪，大家都看空未来的价格，纷纷卖出股票，进而推动股票价格下跌.</p>
</div>
<p style="font-size: 24px;font-weight: bold;margin-top:16px;">策略推荐</p>
<div style="background-color: rgba(0, 0, 0, 25); margin-top:10px;padding: 10px;border-radius: 10px;">
<p style="font-size: 18px;font-weight: bold;margin-top:2px;">根据双均线策略，我们目前推荐买入的股票为：{{ buy_name }}</p>
<p style="font-size: 18px;font-weight: bold;margin-top:20px;">根据双均线策略，我们目前推荐卖出的股票为：{{ sell_name }}</p></div>
<p style="font-size: 18px;font-weight: bold;margin-top:20px;">优化策略，设置止损（10%）和止盈（20%）</p>
<div style="background-color: rgba(0, 0, 0, 25); margin-top:10px;padding: 10px;border-radius: 10px;">
<p style="font-size: 18px;font-weight: bold;margin-top:2px;">根据止损，推荐卖出：{{ stop1 }}</p>
<p style="font-size: 18px;font-weight: bold;margin-top:20px;">根据止盈，推荐卖出：{{ stop2 }}</p></div>
<p style="font-size: 24px;font-weight: bold;margin-top:16px;">查看策略回测结果：</p>
<el-input style="margin-top:10px;margin-bottom:15px; " v-model="back_name" placeholder="请输入希望查询的股票回测代码(使用小写字母)"></el-input>
  <el-button type="primary" round @click="call_back">查看回测反馈图</el-button>
  
    </div>
  </div>
</div>
</el-main>
</el-container>
</el-container>
</template>

<script>
export default{
name:"Strategy1",
data() {
  return {
    user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
    buy_name:'',//推荐买的
    sell_name:'',
    back_name:'',//回测名
    stop1:'',
    stop2:''
  }
},
mounted(){
  this.request.post("strategy1_buy").then(res => {
    if(res.code===200){
      this.buy_name=res.data.buy_name
    }
    else{
      this.buy_name="空"
    }
      })
  this.request.post("strategy1_sell").then(res => {
    if(res.code===200){
      this.sell_name=res.data.sell_name
    }
    else{
      this.sell_name="空"
    }
      })
  
    this.request.post("risk1",this.user).then(res => {
    console.log(res)
    if(res.code===200){
      this.stop1=res.data.stop1
    }
    else{
      this.stop1="空"
    }
    })

  this.request.post("risk2",this.user).then(res => {
    console.log(res)
    if(res.code===200){
      this.stop2=res.data.stop2
    }
    else{
      this.stop2="空"
    }
    })
},
methods: {
  call_back() {//跳转到回测的图展示界面
      if(this.back_name!=='600000.sh'&&this.back_name!=='600004.sh'&&this.back_name!=='600007.sh'&&this.back_name!=='600056.sh'&&this.back_name!=='600064.sh'&&this.back_name!=='600031.sh'&&this.back_name!=='600089.sh'&&this.back_name!=='688046.sh'&&this.back_name!=='688113.sh'&&this.back_name!=='688131.sh'&&this.back_name!=='000001.sz'&&this.back_name!=='000002.sz'&&this.back_name!=='000008.sz'&&this.back_name!=='000009.sz'&&this.back_name!=='000019.sz'&&this.back_name!=='000027.sz'&&this.back_name!=='000028.sz'&&this.back_name!=='000069.sz'&&this.back_name!=='000155.sz'&&this.back_name!=='000428.sz'){
              this.$message.error("您输入的股票代码不存在")
              return
          }
      localStorage.setItem("name", JSON.stringify(this.back_name))  //存想查询的回测股票名称
      this.$router.push('/strategy_show1')
      this.$message.success("查询成功")
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